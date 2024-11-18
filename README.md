# Financial Analysis of Higher Education Institutions in the UK [Click Here](https://huggingface.co/spaces/VirendraChavda/Hesa_Dashboard)
### Author: Virendrasinh Chavda

<p align="justify">
This repository contains the code and resources for analyzing the financial performance of higher education institutions (HEIs) in the UK using a dynamic and interactive dashboard. The project focuses on trends in income, expenditure, and other key financial metrics, providing visual and statistical insights for stakeholders.
</p>

## Table of Contents
1. [Overview](#Overview)
2. [Installation](#Installation)
3. [Data](#Data)
4. [Features](#Features)
5. [Methodology](#Methodology)
6. [Future Work](#Future-Work)
7. [Contributing](#Contributing)
8. [License](#License)

---

## Overview
<p align="justify">
Higher education institutions play a pivotal role in the economy and social progress. This project provides a detailed analysis of financial trends in UK universities, covering areas such as income sources, expenditures, and student statistics. The interactive dashboard enables users to explore data by country, region, and associated groups, offering valuable insights for decision-making and policy development.
</p>

<p align="justify">
The project leverages technologies like <strong>Streamlit</strong> for building the dashboard, <strong>Plotly</strong> for interactive visualizations, and <strong>Google Drive API</strong> for managing comments and feedback on the dashboard.
</p>

---

## Installation

To set up and use this project, follow these steps:

1. **Install Python**:
   - Download Python from [Python.org](https://www.python.org/downloads/) and install it.

2. **Install Anaconda**:
   - Download the Anaconda Distribution from [Anaconda](https://www.anaconda.com/download/success) and install it.

3. **Initialize the Environment**:
   - Open the project folder and run the `Initialisation.py` file to install all necessary dependencies:
     ```bash
     python Initialisation.py
     ```
   - This step may take up to 5 minutes.

4. **Launch the Dashboard**:
   - After installation, run the `HESA Dashboard.exe` file to start the dashboard in your default web browser.

For detailed instructions, refer to the [Installation Guide](./Installation%20guide.docx).

---

## Data
<p align="justify">
The dataset used in this project contains financial and operational metrics for UK higher education institutions, including:
</p>

- **Income Sources**: Tuition fees, research grants, funding body grants, and more.
- **Expenditures**: Staff costs, total expenditure, and surplus/deficit.
- **Student Statistics**: Total students, UK students, EU students, and international students.

<p align="justify">
The dataset is pre-processed and formatted in the `University Benchmarking Dashboard - Formatted.xlsx` file, enabling seamless integration with the dashboard. Filter options such as country, region, and income group are provided for exploratory analysis.
</p>

---

## Features

1. **Interactive Filters**:
   - Select data by country, region, establishment group, and other attributes.
   - Compare institutions across multiple dimensions.

2. **Dynamic Visualizations**:
   - Line charts for trends in income, expenditure, and student statistics.
   - Pie charts for visualizing income and fee distributions.

3. **Mode Selection**:
   - `Normal` mode for a single dataset analysis.
   - `Comparison` mode for side-by-side analysis of datasets.

4. **Google Drive Integration**:
   - Comments and feedback are stored and managed securely using the Google Drive API.

5. **Customizable Metrics**:
   - Users can explore percentages, absolute values, and trends.

---

## Methodology

### 1. Data Processing
- Cleaned and aggregated data from the original source into a structured format.
- Added computed columns for percentage growth and relative contributions.

### 2. Dashboard Implementation
- Developed using **Streamlit** for a responsive user interface.
- **Plotly** visualizations for interactivity and clarity.

### 3. Cloud Integration
- Integrated with Google Drive API to handle user comments and feedback.

---

## Future Work
- **Advanced Analytics**:
  - Add predictive modeling for financial metrics using machine learning.
- **Enhanced Visualizations**:
  - Include more detailed graphs and heatmaps for better insights.
- **Expanded Scope**:
  - Incorporate more datasets, such as student satisfaction scores or employment statistics.

---

## Contributing
<p align="justify">
Contributions are welcome! If you’d like to suggest improvements or add new features, please submit a pull request or open an issue in the repository.
</p>

---

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

For additional details, refer to the provided code files and documentation. If you encounter any issues, please feel free to raise an issue in this repository.
