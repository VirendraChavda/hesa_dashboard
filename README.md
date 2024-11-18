# Financial Analysis of Higher Education Institutions in the UK [Click Here](https://huggingface.co/spaces/VirendraChavda/Hesa_Dashboard)
### Author: Virendrasinh Chavda

<p align="justify">
This repository contains the code and resources for analyzing the financial performance of higher education institutions (HEIs) in the UK using a dynamic and interactive dashboard. The project focuses on trends in income, expenditure, and other key financial metrics, providing visual and statistical insights for stakeholders.
</p>

[Hesa Dashbord](homepage.png)

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

## Data
<p align="justify">
The dataset used in this project contains financial and operational metrics for UK higher education institutions, including:
</p>

- <strong>Income Sources</strong>: Tuition fees, research grants, funding body grants, and more.
- <strong>Expenditures</strong>: Staff costs, total expenditure, and surplus/deficit.
- <strong>Student Statistics</strong>: Total students, UK students, EU students, and international students.

<p align="justify">
The dataset is pre-processed and formatted in the `University Benchmarking Dashboard - Formatted.xlsx` file, enabling seamless integration with the dashboard. Filter options such as country, region, and income group are provided for exploratory analysis.
</p>

---

## Features

1. <strong>Interactive Filters</strong>:
   - Select data by country, region, establishment group, and other attributes.
   - Compare institutions across multiple dimensions.

2. <strong>Dynamic Visualizations</strong>:
   - Line charts for trends in income, expenditure, and student statistics.
   - Pie charts for visualizing income and fee distributions.

3. <strong>Mode Selection</strong>:
   - `Normal` mode for a single dataset analysis.
   - `Comparison` mode for side-by-side analysis of datasets.

4. <strong>Google Drive Integration</strong>:
   - Comments and feedback are stored and managed securely using the Google Drive API.

5. <strong>Customizable Metrics</strong>:
   - Users can explore percentages, absolute values, and trends.

---

## Methodology

### 1. Data Processing
- Cleaned and aggregated data from the original source into a structured format.
- Added computed columns for percentage growth and relative contributions.

### 2. Dashboard Implementation
- Developed using <strong>Streamlit</strong> for a responsive user interface.
- <strong>Plotly</strong> visualizations for interactivity and clarity.

### 3. Cloud Integration
- Integrated with Google Drive API to handle user comments and feedback.

---

## Future Work
- <strong>Advanced Analytics</strong>:
  - Add predictive modeling for financial metrics using machine learning.
- <strong>Enhanced Visualizations</strong>:
  - Include more detailed graphs and heatmaps for better insights.
- <strong>Expanded Scope</strong>:
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
