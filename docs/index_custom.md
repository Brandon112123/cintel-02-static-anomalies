# Continuous Intelligence

This site provides documentation for this project.
Use the navigation to explore module-specific materials.

---

## Custom Project Overview

This project applies anomaly detection techniques to a global suicide rate dataset.

The pipeline reads a CSV file, identifies unusually high suicide rate values,
saves the results to a CSV file, and generates a chart to visualize the top anomalies.

This project demonstrates how the example anomaly detection pipeline can be adapted to a different real-world problem.

---

## Project Goal

The goal of this project is to apply the example pipeline structure to a new dataset and problem.

Instead of analyzing clinic age and height data, this project analyzes suicide rate data across countries, years, and demographic groups.

---

## How-To Guide

Many instructions are common to all our projects.

See
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to get these projects running on your machine.

---

## Project Documentation Pages (docs/)

- **Home** - this documentation landing page
- **Project Instructions** - instructions specific to this module
- **Your Files** - how to copy the example and create your version
- **Glossary** - project terms and concepts

---

## Dataset

The custom pipeline uses:

### Dataset Fields

- iso_code
- country
- year
- sex
- age_group
- suicide_rate

---

## Method

The pipeline performs the following steps:

1. Reads the dataset using Polars
2. Applies a threshold to detect unusually high suicide rate values
3. Filters anomaly records
4. Saves results to a CSV file
5. Generates a chart of the top anomaly values

---

## Output

The project generates the following files:

---

## Results

The anomaly detection process identified records with unusually high suicide rates.

The output CSV contains all anomaly records, and the chart highlights the top anomaly values for easier interpretation.

---

## Example Chart

![Anomaly Chart](../artifacts/suicide_rate_anomalies_chart_custom.png)

---

## Key Insights

- Higher suicide rates were detected in specific countries and years
- Adjusting the threshold affects how many anomalies are detected
- Visualization improves understanding of extreme values
- The pipeline can be reused for other datasets

---

## Technologies Used

- Python
- Polars
- Matplotlib
- datafun_toolkit

---

## Project Structure

---

## Additional Resources

- [Suggested Datasets](https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/)

---

## Conclusion

This project demonstrates how a reusable anomaly detection pipeline can be adapted to a new dataset and problem.

By modifying the input data, updating the detection logic, and adding visualization,
the pipeline was successfully applied to a real-world dataset and produced meaningful results.
