"""
anomaly_detector_brandon.py - Project script.

Author: Brandon Smith
Date: 2026-03-22

Purpose:
  Read global suicide rate data from a CSV file,
  detect anomalies based on unusually high suicide rates,
  save the anomaly results to a new CSV file,
  and create a chart of the top anomalies.

Run as a Module:
  uv run python -m cintel.anomaly_detector_brandon_custom
"""

import logging
from pathlib import Path
from typing import Final

import matplotlib.pyplot as plt
import polars as pl
from datafun_toolkit.logger import get_logger, log_header, log_path

LOG: logging.Logger = get_logger("P2", level="DEBUG")

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
ARTIFACTS_DIR: Final[Path] = ROOT_DIR / "artifacts"

DATA_FILE: Final[Path] = DATA_DIR / "suicide_rates_custom.csv"
OUTPUT_FILE: Final[Path] = ARTIFACTS_DIR / "suicide_rate_anomalies_brandon.csv"
CHART_FILE: Final[Path] = ARTIFACTS_DIR / "suicide_rate_anomalies_chart_custom.jpg"


def main() -> None:
    """Run the anomaly detection pipeline."""
    log_header(LOG, "CINTEL")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "DATA_FILE", DATA_FILE)
    log_path(LOG, "OUTPUT_FILE", OUTPUT_FILE)
    log_path(LOG, "CHART_FILE", CHART_FILE)

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    log_path(LOG, "ARTIFACTS_DIR", ARTIFACTS_DIR)

    # STEP 1: READ DATA
    df: pl.DataFrame = pl.read_csv(DATA_FILE)

    LOG.info(f"Loaded {df.height} records")
    LOG.info(f"Columns found: {df.columns}")

    # STEP 2: DETECT ANOMALIES
    LOG.info("Studying suicide rates to find anomalies...")

    MAX_REASONABLE_SUICIDE_RATE: Final[float] = 25.0
    LOG.info(f"MAX_REASONABLE_SUICIDE_RATE: {MAX_REASONABLE_SUICIDE_RATE}")

    anomalies_df: pl.DataFrame = df.filter(
        (pl.col("sex") == "both")
        & (pl.col("age_group") == "ALL")
        & (pl.col("suicide_rate") >= MAX_REASONABLE_SUICIDE_RATE)
    ).sort("suicide_rate", descending=True)

    LOG.info(f"Count of anomalies found: {anomalies_df.height}")

    # STEP 3: SAVE ANOMALIES CSV
    anomalies_df.write_csv(OUTPUT_FILE)
    LOG.info(f"Wrote anomalies file: {OUTPUT_FILE}")

    # STEP 4: CREATE CHART
    top_anomalies = anomalies_df.head(10)

    if top_anomalies.height > 0:
        labels = [
            f"{country} ({year})"
            for country, year in zip(
                top_anomalies["country"].to_list(),
                top_anomalies["year"].to_list(),
                strict=False,
            )
        ]
        values = top_anomalies["suicide_rate"].to_list()

        plt.figure(figsize=(12, 6))
        plt.bar(labels, values)
        plt.xticks(rotation=45, ha="right")
        plt.ylabel("Suicide Rate")
        plt.xlabel("Country and Year")
        plt.title("Top 10 Suicide Rate Anomalies")
        plt.tight_layout()
        plt.savefig(CHART_FILE)
        plt.close()

        LOG.info(f"Wrote chart file: {CHART_FILE}")
    else:
        LOG.warning("No anomalies found, so no chart was created.")

    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")
    LOG.info("END main()")


if __name__ == "__main__":
    main()
