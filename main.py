import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Shopping Analysis", layout="wide")

# Main Title
st.title("Customer Shopping Behavior Analysis")
st.write("In this dashboard, we analyzed customer shopping data and spending habits.")

def load_data():
    data = pd.read_csv("shopping_behavior.csv")
    return data


# Load the dataset
df = load_data()

st.sidebar.header("Filter Options")

# Filter 1: Gender
gender_list = df['Gender'].unique()
selected_gender = st.sidebar.multiselect("Select Gender", gender_list, default=gender_list)

# Filter 2: Category
category_list = df['Category'].unique()
selected_category = st.sidebar.multiselect("Select Category", category_list, default=category_list)

# Filter 3: Age Range (Slider)
min_age = int(df['Age'].min())
max_age = int(df['Age'].max())
selected_age_range = st.sidebar.slider("Select Age Range", min_age, max_age, (min_age, max_age))


filtered_df = df[
    (df['Gender'].isin(selected_gender)) &
    (df['Category'].isin(selected_category)) &
    (df['Age'] >= selected_age_range[0]) &
    (df['Age'] <= selected_age_range[1])
    ]


st.write(f"Total records found based on filters: {filtered_df.shape[0]}")

st.dataframe(filtered_df.head())

st.header("Visualizations & Insights")

# Row 1: Basic Charts
col1, col2, col3 = st.columns(3)

# CHART 1: Bar Chart (Category Counts)
with col1:
    st.subheader("1. Sales by Category")

    category_counts = filtered_df['Category'].value_counts().reset_index()
    category_counts.columns = ['Category', 'Count']

    fig1 = px.bar(category_counts, x='Category', y='Count', color='Category',
                  title="Number of Items Sold per Category")
    st.plotly_chart(fig1, width="stretch")

# CHART 2: Histogram (Age Distribution)
with col2:
    st.subheader("2. Customer Age Distribution")
    fig2 = px.histogram(filtered_df, x='Age', nbins=20, title="Age Groups Histogram",
                        color_discrete_sequence=['orange'])
    st.plotly_chart(fig2, width="stretch")

# CHART 3: Pie Chart (Gender Distribution)
with col3:
    st.subheader("3. Gender Distribution")
    fig3 = px.pie(filtered_df, names='Gender', title="Male vs Female Ratio", hole=0.3)
    st.plotly_chart(fig3, width="stretch")

col4, col5 = st.columns(2)

# CHART 4: Treemap
with col4:
    st.subheader("4. Spending Hierarchy (Treemap)")

    fig4 = px.treemap(filtered_df,
                      path=['Category', 'Item Purchased'],
                      values='Purchase Amount (USD)',
                      title="Total Spending by Category and Item")
    st.plotly_chart(fig4, width="stretch")

# CHART 5: Sunburst Chart
with col5:
    st.subheader("5. Seasonal Preferences (Sunburst)")

    fig5 = px.sunburst(filtered_df, path=['Season', 'Category'],
                       title="Category Distribution by Season")
    st.plotly_chart(fig5, width="stretch")



# Row 3: Statistical & Flow Charts
st.subheader("6. Customer Flow (Parallel Categories)")
# CHART 6: Parallel Categories

fig6 = px.parallel_categories(filtered_df, dimensions=['Gender', 'Category', 'Size'],
                              title="Flow: Gender -> Category -> Size")
st.plotly_chart(fig6, width="stretch")

col6, col7 = st.columns(2)

# CHART 7: Box Plot
with col6:
    st.subheader("7. Spending Distribution (Box Plot)")

    fig7 = px.box(filtered_df, x='Category', y='Purchase Amount (USD)', color='Category',
                  title="Purchase Amount Distribution per Category")
    st.plotly_chart(fig7, width="stretch")

# CHART 8: Violin Plot
with col7:
    st.subheader("8. Review Ratings (Violin Plot)")
    fig8 = px.violin(filtered_df, y="Review Rating", x="Category", box=True,
                     title="Density of Review Ratings by Category")
    st.plotly_chart(fig8, width="stretch")

# CHART 9: Scatter Plot
st.subheader("9. Age vs. Spending Relationship")
fig9 = px.scatter(filtered_df, x='Age', y='Purchase Amount (USD)',
                  color='Subscription Status',
                  color_discrete_sequence=['blue', 'red'],
                  title="Correlation between Age and Purchase Amount")
st.plotly_chart(fig9, width="stretch")
