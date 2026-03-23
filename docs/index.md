# Continuous Intelligence

This site provides documentation for this project.
Use the navigation to explore module-specific materials.

## How-To Guide

Many instructions are common to all our projects.

See
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to get these projects running on your machine.

## Project Documentation Pages (docs/)

- **Home** - this documentation landing page
- **Project Instructions** - instructions specific to this module
- **Your Files** - how to copy the example and create your version
- **Glossary** - project terms and concepts

## Additional Resources

- [Suggested Datasets](https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/)

## Custom Project

### Dataset

I used a global suicide rate dataset located in:

`data/suicide_rates_custom.csv`

The dataset includes country, year, and suicide rate information.

---

### Signals

The main signal used was the `suicide_rate` column.

I used this value to detect unusually high suicide rates.

---

### Experiments

I made the following changes:

- Changed the dataset from clinic data to suicide rate data
- Updated the logic to detect high suicide rates
- Adjusted the threshold to change how many anomalies are found
- Added a chart to show the top anomaly values

---

### Results

The pipeline created:

- A CSV file with anomaly results
- A chart showing the highest suicide rates

Changing the threshold changed how many anomalies were detected.

---

### Interpretation

The project shows that anomaly detection can find unusually high suicide rates.

The chart makes it easier to see extreme values, and the system can be adjusted to focus on more or fewer anomalies.
