# Customer Shopping Behavior Analysis Report

## Project Overview
This project involves the development of an interactive data visualization dashboard using Streamlit and Plotly. The dashboard analyzes customer shopping behavior, providing insights into sales trends, customer demographics, and spending habits based on the "Shopping Behavior" dataset.

## Team Members and Contributions

The project was collaboratively developed by three team members. Below is the breakdown of responsibilities and contributions:

### 1. Seymen
*   **Role:** Interactivity & Hierarchical Visualizations
*   **Responsibilities:**
    *   Implemented sidebar filters for Gender, Category, and Age Range to make the dashboard interactive.
    *   Handled the logic for dynamic data filtering.
    *   **Visualizations Created:**
        7.  **Spending Distribution (Box Plot):** Analyzes the spread and outliers of purchase amounts across different categories.
        8.  **Review Ratings (Violin Plot):** Displays the density and distribution of review ratings for each category.
        9.  **Age vs. Spending Relationship (Scatter Plot):** Investigates the correlation between customer age and their purchase amount, colored by subscription status.

### 2. Huseyin
*   **Role:** Data Preprocessing & Basic Visualizations
*   **Responsibilities:**
    *   Loaded and cleaned the dataset (`shopping_behavior.csv`).
    *   Designed the initial layout of the Streamlit dashboard.
    *   **Visualizations Created:**
        4.  **Spending Hierarchy (Treemap):** Visualizes the total spending broken down by Category and specific Items.
        5.  **Seasonal Preferences (Sunburst):** Shows how category preferences change across different seasons.
        6.  **Customer Flow (Parallel Categories):** Traces the relationship between Gender, Category, and Size choices.

### 3. Mehmet Emin
*   **Role:** Statistical Analysis & Report Writing
*   **Responsibilities:**
    *   Conducted statistical analysis of spending and ratings.
    *   Compiled the final project report and documentation.
    *   **Visualizations Created:**
        1.  **Sales by Category (Bar Chart):** Displays the total number of items sold per category to identify popular product lines.
        2.  **Customer Age Distribution (Histogram):** Shows the frequency distribution of customer ages to understand the target demographic.
        3.  **Gender Distribution (Pie Chart):** Illustrates the ratio of male to female customers.

## Conclusion
The dashboard successfully integrates various visualization techniques to provide a comprehensive view of the shopping data. Each team member contributed to specific aspects of the pipeline, from data handling to advanced visualization and documentation, resulting in a functional and insightful analytical tool.
