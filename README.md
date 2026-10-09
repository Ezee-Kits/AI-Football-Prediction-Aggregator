# AI Football Prediction Aggregator

**A Python-powered, multi-source football prediction collection and analysis system integrating predictions from six external football prediction platforms.**

AI Football Prediction Aggregator is a Python project designed to collect, organize, and prepare football match predictions from multiple independent websites within one structured workflow.

The system integrates six prediction sources:

1. Statarea
2. BetClan
3. Forebet
4. Accumulator Generator
5. FootballSuperTips
6. Prematips

Each source has a dedicated Python module responsible for collecting its available prediction information. A shared helper module, `func.py`, provides reusable functionality for common operations, while `READ_CSV.py` supports reading and processing the resulting datasets.

The goal is to make football prediction information from different platforms easier to collect, organize, compare, and analyze without manually visiting each website and transferring predictions into spreadsheets.

---

## Overview

Football prediction websites publish estimates and recommendations for upcoming matches. Depending on the platform, these may include home-win and away-win predictions, goal-market estimates, both-teams-to-score predictions, and other football-related statistics.

However, predictions from different websites can be presented in different formats, use different field names, and cover different betting markets.

This project addresses the data collection and organization side of that problem by providing separate Python modules for multiple prediction sources and reusable utilities for managing their output.

The collected information can then be used for:

* Comparing predictions across different websites.
* Identifying matches where multiple sources agree.
* Investigating differences between prediction sources.
* Organizing predictions by match and date.
* Reviewing home-win and away-win estimates.
* Analyzing over/under and both-teams-to-score predictions where available.
* Building historical datasets for further statistical research.
* Developing future prediction consensus and evaluation tools.

## AI Integration

The project is AI-integrated through its use of prediction information published by external football prediction platforms.

Some external platforms may use machine learning, statistical models, historical match analysis, or proprietary prediction methods. This repository collects their published outputs for further processing.

**The current project should not be described as training its own AI model unless a separate training implementation is added.** Its main function is multi-source prediction collection and data aggregation.

This distinction matters because collecting predictions from AI-powered websites is different from developing, training, or deploying an independent machine-learning model.

---

## Key Features

* **Six prediction sources:** Collects football prediction data from six different platforms.
* **Dedicated scraper modules:** Keeps source-specific extraction logic in separate Python files.
* **Reusable helper functions:** Centralizes common operations in `func.py`.
* **Automated prediction collection:** Reduces the need to manually gather predictions from each website.
* **Multi-source data aggregation:** Prepares prediction information from different platforms for combined analysis.
* **Home-win and away-win estimates:** Collects these markets where provided by a source.
* **Goal-market predictions:** Supports fields such as over 2.5 goals where available.
* **Both-teams-to-score analysis:** Collects BTTS-related information where supported by the source.
* **CSV-based storage:** Saves collected information in structured CSV files.
* **Date-aware collection:** Supports selecting predictions for the current or following day, depending on the configured helper functions.
* **Duplicate management:** Supports duplicate removal through shared utilities.
* **Sorting and data organization:** Provides reusable utilities for arranging prediction datasets.
* **Extensible architecture:** Allows additional prediction sources to be integrated as separate modules.
* **Research-ready data:** Creates a foundation for prediction comparison, historical evaluation, and future consensus analysis.

The availability of each prediction market depends on the website being collected and its current page structure.

---

## Prediction Sources

The project is designed around six external football prediction platforms.

### 1. Statarea

The `statarea.py` module collects match prediction information from Statarea.

In the provided implementation, the scraper reads match entries and extracts available home-team and away-team information alongside selected prediction fields.

The current code includes fields for:

* Home team
* Away team
* Home-win prediction
* Away-win prediction
* Over 2.5 goals
* Both teams to score (BTS)
* Other teams to score (OTS)
* Source identifier

The collected data is saved in a source-specific CSV file.

### 2. BetClan

The `betclan.py` module is dedicated to collecting prediction information from BetClan.

It provides a separate location for the extraction logic needed to process that platform's page structure and prediction fields.

Its output can be used alongside predictions from the other sources once the fields are normalized into a consistent schema.

### 3. Forebet

The `forbet.py` module is dedicated to collecting football predictions from Forebet.

It separates Forebet-specific data extraction from the rest of the application, making the project easier to maintain when the source website changes.

Collected fields should be mapped into the project's common data format where possible.

### 4. Accumulator Generator

The `accumulator.py` module is dedicated to collecting prediction information from Accumulator Generator.

It allows the project to incorporate another source of football prediction recommendations into the wider collection workflow.

The precise markets and fields available depend on the source's published information and the implementation of this module.

### 5. FootballSuperTips

The `footballsupertips.py` module is dedicated to collecting football prediction information from FootballSuperTips.

Its output can contribute to cross-source comparisons, provided that the relevant matches and prediction markets can be matched consistently.

### 6. Prematips

The `prematips.py` module collects prediction information from Prematips.

The provided implementation:

1. Creates a date-specific output directory using `save_daily_csv()`.
2. Selects the appropriate prediction page according to `match_day_date`.
3. Uses `requests_init()` to obtain and parse the page.
4. Finds links matching the platform's `/tip/` URL pattern.
5. Visits individual match pages.
6. Extracts the home and away team names.
7. Collects percentage values from the page's prediction statistics.
8. Organizes selected home-win, away-win, over 2.5, BTS, and OTS values.
9. Adds a source identifier to the record.
10. Saves the collected records and removes duplicate rows.

The current implementation writes to `prematips.csv` within the directory returned by `save_daily_csv()`.

The actual availability and meaning of these fields depend on the source page's structure.

---

## Repository Structure

```text
AI-Football-Prediction-Aggregator/
│
├── PY FILES/
│   ├── func.py
│   ├── prematips.py
│   ├── READ_CSV.py
│   ├── statarea.py
│   ├── accumulator.py
│   ├── betclan.py
│   ├── footballsupertips.py
│   └── forbet.py
│
├── CSV FILES/
│   └── Date-specific prediction datasets
│
├── requirements.txt
└── README.md
```

The `CSV FILES` directory represents the intended location for generated datasets. The exact directory structure depends on the implementation of `save_daily_csv()` in `func.py`.

---

## Python Modules

| File                   | Responsibility                                                                                               |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| `func.py`              | Shared utilities for requests, CSV saving, duplicate removal, date handling, directory creation, and sorting |
| `prematips.py`         | Collects prediction information from Prematips                                                               |
| `READ_CSV.py`          | Reads and processes collected CSV datasets                                                                   |
| `statarea.py`          | Collects prediction information from Statarea                                                                |
| `accumulator.py`       | Handles prediction collection from Accumulator Generator                                                     |
| `betclan.py`           | Handles prediction collection from BetClan                                                                   |
| `footballsupertips.py` | Handles prediction collection from FootballSuperTips                                                         |
| `forbet.py`            | Handles prediction collection from Forebet                                                                   |

The descriptions for modules whose source code was not provided are based on their filenames and stated purpose. Their exact fields, extraction methods, and output formats depend on the actual implementations.

---

## Shared Helper Module: `func.py`

The `func.py` file contains reusable functions imported by the individual scraper modules.

In the provided Prematips and Statarea examples, the shared functions include:

| Function           | Purpose                                                                                   |
| ------------------ | ----------------------------------------------------------------------------------------- |
| `requests_init()`  | Initializes a request and returns parsed page information according to its implementation |
| `saving_files()`   | Saves collected records to CSV and supports adding records to an existing dataset         |
| `drop_duplicate()` | Removes duplicate records from a dataset                                                  |
| `match_day_date`   | Configuration value used to choose the collection date                                    |
| `main_date()`      | Calculates a date from an offset                                                          |
| `save_daily_csv()` | Creates or returns the output directory for daily prediction files                        |
| `sorting_values()` | Sorts a dataset by a specified column                                                     |

Centralizing common functionality makes it easier to maintain the project, reduces repeated code, and helps individual scrapers follow a consistent data-saving workflow.

The precise behavior of each helper is defined by its implementation in `func.py`.

---

## Data Fields and Prediction Markets

The provided Prematips and Statarea implementations use several common fields.

| Field       | Description                                      |
| ----------- | ------------------------------------------------ |
| `HOME TEAM` | Name of the home team                            |
| `AWAY TEAM` | Name of the away team                            |
| `HOME WIN`  | Home-win prediction or associated value          |
| `AWAY WIN`  | Away-win prediction or associated value          |
| `OVER 2.5`  | Over 2.5 goals prediction value                  |
| `BTS`       | Both-teams-to-score prediction value             |
| `OTS`       | Other-teams-to-score field as used by the source |
| `NAME`      | Identifier for the prediction source             |

The source identifier in the provided examples uses values such as `PRE` for Prematips and `STA` for Statarea.

These fields form a starting point for normalizing data across the six platforms. Other websites may provide different markets, naming conventions, or data formats.

### Understanding prediction percentages

A percentage displayed by a prediction website is not automatically a calibrated probability of a match outcome. Its interpretation depends on how the source generates, defines, and validates that value.

Where one website supplies percentages and another supplies categorical tips, the data should be normalized carefully before making direct numerical comparisons.

---

## How the Project Works

A typical workflow is:

1. **Select a prediction source.** Choose one of the six source-specific Python modules.
2. **Request the prediction page.** The scraper retrieves relevant website content.
3. **Parse the available information.** HTML parsing extracts the match and prediction fields.
4. **Normalize the record.** The scraper organizes the extracted information into a structured format.
5. **Save the data.** Shared helper functions write records into CSV files.
6. **Clean the dataset.** Duplicate removal and sorting utilities can be applied where appropriate.
7. **Read the collected data.** `READ_CSV.py` provides the module for reading or processing the generated CSV datasets.
8. **Compare sources.** The resulting datasets can be aligned by match and market for additional analysis.

The exact execution order and automation behavior depend on how the individual scripts and `READ_CSV.py` are implemented.

---

## Installation

### Prerequisites

* Python installed on your system.
* An internet connection.
* Access to the relevant prediction websites.
* The project's Python scripts and helper module.

### 1. Clone the repository

```bash
git clone https://github.com/Ezee-Kits/AI-Football-Prediction-Aggregator.git
```

### 2. Enter the project directory

```bash
cd AI-Football-Prediction-Aggregator
```

### 3. Install the dependencies

Create a `requirements.txt` file containing the third-party libraries required by your complete project. The provided snippets directly use or import the following:

```text
beautifulsoup4
pandas
requests
```

Install them with:

```bash
python -m pip install -r requirements.txt
```

The helper module or other source files may require additional dependencies. Add those to `requirements.txt` based on the imports in the complete repository.

---

## Running the Scrapers

The following commands assume that the scripts are located inside `PY FILES/` and that their imports and relative file paths are configured accordingly.

### Collect Prematips predictions

```bash
python "PY FILES/prematips.py"
```

The provided implementation calls `prematips_func()` when the script runs.

### Collect Statarea predictions

```bash
python "PY FILES/statarea.py"
```

The provided implementation calls `statarea_func()` when the script runs.

### Run the other source modules

```bash
python "PY FILES/betclan.py"
python "PY FILES/forbet.py"
python "PY FILES/accumulator.py"
python "PY FILES/footballsupertips.py"
```

These commands assume the remaining modules also execute their collection routines when run directly. Verify their actual entry points before relying on this behavior.

### Read collected CSV files

```bash
python "PY FILES/READ_CSV.py"
```

The actual behavior depends on the implementation of `READ_CSV.py`.

**Important:** Running scripts individually may be more reliable during development because it makes errors easier to isolate. Check the source-specific output paths before running the full collection workflow.

---

## Multi-Source Prediction Analysis

Once predictions have been collected, the datasets can support more advanced analysis.

### 1. Source agreement

Identify matches for which multiple websites recommend the same outcome.

For example, if several sources select a home win, that match can be marked as a home-win consensus candidate. Agreement is a feature to investigate, not proof that the prediction is correct.

### 2. Prediction disagreement

Find matches where different platforms provide conflicting recommendations.

Disagreement can help identify matches that require closer review or further statistical investigation.

### 3. Market-specific comparisons

Compare equivalent markets across the sources, such as:

* Home win
* Away win
* Over 2.5 goals
* Both teams to score

Only compare values that represent the same outcome and use compatible definitions.

### 4. Historical performance evaluation

If actual match results are added to the datasets, the collected predictions can be evaluated over a defined historical period.

Possible measures include:

* Prediction accuracy
* Market-specific accuracy
* Source-by-source performance
* Agreement rate among sources
* Calibration metrics for suitable probability forecasts
* Profit and loss under explicitly defined betting assumptions

A reliable evaluation requires independently verified outcomes and a consistent methodology. A large number of agreeing websites does not guarantee a correct result.

---

## Data Quality and Reliability

Because the project relies on third-party websites, collection reliability depends on their current availability and page structure.

Potential problems include:

* Changes to HTML elements or CSS classes.
* Missing prediction fields.
* Website request failures or timeouts.
* Different team names for the same club.
* Different formats for percentages and prediction values.
* Duplicate matches across collection runs.
* Different kickoff dates caused by timezone differences.
* Different definitions for similarly named betting markets.
* Inconsistent CSV column names across sources.

Recommended safeguards include validating required fields, handling HTTP errors, using request timeouts, normalizing team names, recording collection timestamps, and maintaining a consistent dataset schema.

Always verify that the websites permit automated access and that your usage follows their terms and applicable rules.

---

## Security and Responsible Use

The project is intended for football data collection, software development, and statistical research.

Do not commit private credentials, session cookies, API keys, or other sensitive information to a public repository. Keep configuration and secrets outside version-controlled source files.

Football predictions are uncertain. Predictions published by an external platform may be incorrect, and combining several prediction sources does not guarantee a winning selection or positive betting returns.

Treat the collected information as analytical input rather than financial certainty. Independently evaluate predictions against actual results before drawing conclusions about their usefulness.

## Contributing

Contributions that improve the reliability, maintainability, and analytical usefulness of the project are welcome.

Areas for contribution include:

* Improving website parsers.
* Adding data validation.
* Normalizing source-specific prediction fields.
* Improving error handling and logging.
* Adding tests for helper functions.
* Developing historical evaluation tools.
* Improving documentation and installation instructions.

When modifying a scraper, verify that the extracted data still matches the intended schema and that website access complies with the source's terms.

---

## License

No license has been specified for this repository yet. Add a `LICENSE` file if you intend to grant other users permission to use, modify, and distribute the project.

---

## Author

**Ezee Kits**

Electrical and Electronics Engineer | Python Developer | Automation and Data Analysis

* **Portfolio:** https://ezee-kits-portfolio.onrender.com/
* **GitHub:** https://github.com/Ezee-Kits/
* **YouTube:** https://www.youtube.com/@EzeeKits

Explore my projects and tutorials on Python programming, automation, data processing, machine learning, and software development.

---

*AI Football Prediction Aggregator — six prediction sources, one structured football data workflow.*
