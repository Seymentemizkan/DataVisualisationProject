# Customer Shopping Behavior Analysis Dashboard

## Overview
This project is a data visualization dashboard built with **Streamlit** and **Plotly**. It analyzes customer shopping behavior and spending habits based on a dataset. The dashboard provides interactive filters and various charts to explore sales trends, customer demographics, and spending patterns.

## Features

### Interactive Filters
The sidebar allows you to filter the data based on:
- **Gender:** Select specific genders to analyze.
- **Category:** Choose specific product categories.
- **Age Range:** Adjust the slider to focus on a specific age group.

### Visualizations
The dashboard includes the following interactive charts:
1.  **Sales by Category:** Bar chart showing the number of items sold per category.
2.  **Customer Age Distribution:** Histogram of customer age groups.
3.  **Gender Distribution:** Pie chart showing the male vs. female ratio.
4.  **Spending Hierarchy:** Treemap of total spending by category and item.
5.  **Seasonal Preferences:** Sunburst chart showing category distribution by season.
6.  **Customer Flow:** Parallel categories diagram visualizing the flow from Gender to Category to Size.
7.  **Spending Distribution:** Box plot of purchase amounts per category.
8.  **Review Ratings:** Violin plot showing the density of review ratings by category.
9.  **Age vs. Spending Relationship:** Scatter plot correlating age and purchase amount, colored by subscription status.

## Installation

1.  Clone the repository or download the project files.
2.  Ensure you have Python installed on your system.
3.  Install the required Python libraries:

    ```bash
    pip install streamlit pandas plotly
    ```

## Usage

1.  Navigate to the project directory in your terminal.
2.  Run the Streamlit application:

    ```bash
    streamlit run main.py
    ```

    *Note: If you encounter issues running the `streamlit` command directly, you can use:*
    ```bash
    python -m streamlit run main.py
    ```

3.  The dashboard will automatically open in your default web browser (usually at `http://localhost:8501`).

## File Structure

- `main.py`: The main Python script containing the Streamlit application logic and visualizations.
- `shopping_behavior.csv`: The dataset file containing customer shopping data.
- `README.md`: This documentation file.

## Dependencies

- Python 3.x
- Streamlit
- Pandas
- Plotly Express
