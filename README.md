# cintel-02-static-anomalies

[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](#)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project for continuous intelligence.

Continuous intelligence systems monitor data streams, detect change, and respond in real time.
This course builds those capabilities through working projects.

In the age of generative AI, durable skills are grounded in real work:
setting up a professional environment,
reading and running code,
understanding the logic,
and pushing work to a shared repository.
Each project follows the structure of professional Python projects.
We learn by doing.

## This Project

This project introduces **static anomaly detection**.

The goal is to copy this repository,
set up your environment,
run the example analysis,
and explore how anomalies are identified in static data.

You will run the example pipeline, read the code,
and make small modifications to understand how
the detection logic works.

## Data

The example pipeline reads **pediatric clinic** age and height
data from: `data/clinic_data_case.csv`.
It creates reasonable thresholds and outputs
**anomalies** (data outside the expected threshold).

You'll copy the Python file and make it your own (see docs/your-files.md),
and perform a similar analysis on `data/clinic_data_yourname.csv`
given **adult clinic** age and height data.

## Working Files

You'll work with just these areas:

- **data/** - it starts with the data
- **docs/** - tell the story
- **src/cintel/** - where the magic happens
- **pyproject.toml** - update authorship & links
- **zensical.toml** - update authorship & links

## Instructions

Follow the [step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/) to complete:

1. Phase 1. **Start & Run**
2. Phase 2. **Change Authorship**
3. Phase 3. **Read & Understand**
4. Phase 4. **Modify**
5. Phase 5. **Apply**

## Challenges

Challenges are expected.
Sometimes instructions may not quite match your operating system.
When issues occur, share screenshots, error messages, and details about what you tried.
Working through issues is part of implementing professional projects.

## Success

After completing Phase 1. **Start & Run**, you'll have your own GitHub project,
running on your machine, and running the example will print out:

```shell
========================
Pipeline executed successfully!
========================
```

And a new file named `project.log` will appear in the project folder.

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.

Follow the guide for the **full instructions**.

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

After you get a copy of this repo in your own GitHub account,
open a machine terminal in your `Repos` folder:

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/Brandon112123/cintel-02-static-anomalies

cd cintel-02-static-anomalies
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install
git add -A
uvx pre-commit run --all-files

uv run python -m cintel.anomaly_detector_brandon
uv run python -m cintel.anomaly_detector_brandon_custom

uv run ruff format .
uv run ruff check . --fix
uv run zensical build

git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.

## Professional Modification

I modified the pipeline in three ways:

1. I changed the input dataset from clinic_data_case.csv to clinic_data_brandon.csv.
2. I changed the output file from anomalies_case.csv to anomalies_brandon.csv.
3. I adjusted the anomaly detection thresholds by lowering the maximum reasonable age and height values.

## Custom Project

## Overview

This project applies anomaly detection techniques to a global suicide rate dataset.

The pipeline reads a CSV file, identifies unusually high suicide rate values, saves the results to a CSV file, and generates a chart to visualize the top anomalies.

## Dataset

The dataset includes:

- iso_code
- country
- year
- sex
- age_group
- suicide_rate

## Features

- Reads data using Polars
- Detects anomalies based on suicide rate thresholds
- Outputs anomaly results to CSV
- Generates a chart of top anomalies
- Logs execution for debugging and transparency

## Setup

```bash
uv sync
```

### Professional Modifications

1. I changed the problem from clinic age and height anomaly detection to global suicide rate anomaly detection.
2. I changed the input file to `data/suicide_rates_custom.csv`.
3. I changed the anomaly detection logic to use the `suicide_rate` column.
4. I changed the output file to `artifacts/suicide_rate_anomalies_brandon.csv`.
5. I added a chart output file: `artifacts/suicide_rate_anomalies_chart_custom.png`.
6. I customized the pipeline to better fit a real-world dataset.
