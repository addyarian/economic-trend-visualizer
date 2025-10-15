import pandas as pd
import plotly.express as px
import streamlit as st


gdp = pd.read_csv("data/gdp.csv", skiprows=4)
gdpPc = pd.read_csv("data/gdpPc.csv", skiprows=4)
inflation = pd.read_csv("data/inflation.csv", skiprows=4)
unemployment = pd.read_csv("data/unemployment.csv", skiprows=4)
carbonEmissions = pd.read_csv("data/carbonEmissions.csv", skiprows=4)

st.title("Economic Trend Visualizer")

tab1, tab2, tab3, tab4 = st.tabs(["GDP", "Inflation", "Unemployment", "Carbon Emissions"])

with tab1:
    st.header("GDP Data")

    # Checkbox for per capita
    perCapita = st.checkbox("Show per capita GDP")

    # Country selector
    countries = st.multiselect(
        "Select up to 3 countries:",
        gdp["Country Name"].unique(),
        ["India", "United States", "China"]
    )

    # Year range selector
    years = [str(y) for y in range(1960, 2024)]
    start_year, end_year = st.select_slider(
        "Select year range:", 
        options=years, 
        value=("2000", "2023"),
        key="gdp_year_slider"  # <- unique key
    )

    # Choose which dataset to use based on checkbox
    data = gdpPc if perCapita else gdp

    # Reshape
    df = data[data["Country Name"].isin(countries)]
    df = df.melt(id_vars=["Country Name"], value_vars=years,
                 var_name="Year", value_name="GDP (in USD)")
    df = df[(df["Year"] >= start_year) & (df["Year"] <= end_year)]

    # Chart
    title = "GDP Per Capita Over Time" if perCapita else "Total GDP Over Time"
    fig = px.line(df, x="Year", y="GDP (in USD)", color="Country Name", title=title)
    st.plotly_chart(fig, use_container_width=True)



with tab2:
    st.header("Inflation Data")

    # Let the user pick up to 3 countries
    countries = st.multiselect(
        "Select up to 3 countries:",
        inflation["Country Name"].unique(),
        ["India", "United States", "China"]  # default values
    )

    # Let the user pick a year range
    years = [str(y) for y in range(1960, 2024)]
    start_year, end_year = st.select_slider(
        "Select year range:", 
        options=years, 
        value=("2000", "2023"),
        key="inflation_year_slider"  # <- unique key
    )

    # Filter the data
    filtered = inflation[inflation["Country Name"].isin(countries)]
    filtered = filtered.melt(id_vars=["Country Name"], value_vars=years, var_name="Year", value_name="Inflation Rate (in %)")
    filtered = filtered[(filtered["Year"] >= start_year) & (filtered["Year"] <= end_year)]

    # Chart
    fig = px.line(filtered, x="Year", y="Inflation Rate (in %)", color="Country Name", title="Inflation Rate Over Time")
    st.plotly_chart(fig, use_container_width=True)


with tab3:
    st.header("Unemployment Data")

    # Let the user pick up to 3 countries
    countries = st.multiselect(
        "Select up to 3 countries:",
        unemployment["Country Name"].unique(),
        ["India", "United States", "China"]  # default values
    )

    # Let the user pick a year range
    years = [str(y) for y in range(1960, 2024)]
    start_year, end_year = st.select_slider(
        "Select year range:", 
        options=years, 
        value=("2000", "2023"),
        key="unemployment_year_slider"  # <- unique key
    )

    # Filter the data
    filtered = unemployment[unemployment["Country Name"].isin(countries)]
    filtered = filtered.melt(id_vars=["Country Name"], value_vars=years, var_name="Year", value_name="Unemployment Rate (in %)")
    filtered = filtered[(filtered["Year"] >= start_year) & (filtered["Year"] <= end_year)]

    # Chart
    fig = px.line(filtered, x="Year", y="Unemployment Rate (in %)", color="Country Name", title="Unemployment Rate Over Time")
    st.plotly_chart(fig, use_container_width=True)


with tab4:
    st.header("Carbon Emissions Data")

    # Let the user pick up to 3 countries
    countries = st.multiselect(
        "Select up to 3 countries:",
        carbonEmissions["Country Name"].unique(),
        ["India", "United States", "China"]  # default values
    )

    # Let the user pick a year range
    years = [str(y) for y in range(1960, 2024)]
    start_year, end_year = st.select_slider(
        "Select year range:", 
        options=years, 
        value=("2000", "2023"),
        key="carbon_emissions_year_slider"  # <- unique key
    )

    # Filter the data
    filtered = carbonEmissions[carbonEmissions["Country Name"].isin(countries)]
    filtered = filtered.melt(id_vars=["Country Name"], value_vars=years, var_name="Year", value_name="Carbon Emissions (in Mt CO2e)")
    filtered = filtered[(filtered["Year"] >= start_year) & (filtered["Year"] <= end_year)]

    # Chart
    fig = px.line(filtered, x="Year", y="Carbon Emissions (in Mt CO2e)", color="Country Name", title="Carbon Emissions Over Time")
    st.plotly_chart(fig, use_container_width=True)

