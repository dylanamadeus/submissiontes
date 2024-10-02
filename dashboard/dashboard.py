import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_path_day_csv = os.path.join(project_folder, "data", "day.csv")
file_path_hour_csv = os.path.join(project_folder, "data", "hour.csv")

# Membaca file .csv menggunakan pandas
day_df = pd.read_csv(file_path_day_csv)
hour_df = pd.read_csv(file_path_hour_csv)

#hour_df = pd.read_csv("data/hour.csv")
#day_df = pd.read_csv("data/day.csv")

dteday_column = ["dteday"]
for column in dteday_column:
    day_df[column] = pd.to_datetime(day_df[column])
    
dteday_column = ["dteday"]
for column in dteday_column:
    hour_df[column] = pd.to_datetime(hour_df[column])

st.title("Bike Sharing Data Visualization")
st.sidebar.title("Menu")

selected_option = st.sidebar.selectbox("Select Visualization Option", ["Total and Average Count of Rentals by Season", 
                                                                      "Total and Average Count of Rentals by Weather",
                                                                      "Total and Average Count of Rentals Trend Throughout the Day"])


if selected_option == "Total and Average Count of Rentals by Season":
    st.write("You selected: Total and Average Count of Rentals by Season")
    
    total_rentals_by_season = day_df.groupby(by="season").agg({
    "instant": "nunique",
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum"
    }).sort_values(by="cnt", ascending=False)

    fig_season1, ax_season1 = plt.subplots(figsize=(8, 6))
    total_rentals_by_season.plot(kind='bar', color=['green', 'blue', 'orange', 'red'], ax=ax_season1)
    season_names = ['Spring', 'Summer', 'Fall', 'Winter']
    ax_season1.set_xlabel('Season (1:spring, 2:summer, 3:fall, 4:winter)')
    ax_season1.set_ylabel('Total Count of Rentals')
    ax_season1.set_title('Total Count of Rentals by Season')
    ax_season1.set_xticklabels(season_names, rotation=0)
    st.pyplot(fig_season1)
    
    avg_rentals_by_season = day_df.groupby(by="season").agg({
    "instant": "nunique",
    "casual": "mean",
    "registered": "mean",
    "cnt": "mean"
    }).sort_values(by="cnt", ascending=False)
    
    fig_season2, ax_season2 = plt.subplots(figsize=(8, 6))
    avg_rentals_by_season.plot(kind='bar', color=['green', 'blue', 'orange', 'red'], ax=ax_season2)
    ax_season2.set_xlabel('Season (1:spring, 2:summer, 3:fall, 4:winter)')
    ax_season2.set_ylabel('Average Count of Rentals')
    ax_season2.set_title('Average Count of Rentals by Season')
    ax_season2.set_xticklabels(season_names, rotation=0)
    st.pyplot(fig_season2)

    
elif selected_option == "Total and Average Count of Rentals by Weather":
    st.write("You selected: Total and Average Count of Rentals by Weather")
    
    total_rentals_by_weathersit = day_df.groupby(by="weathersit").agg({
    "instant": "nunique",
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum"
    }).sort_values(by="cnt", ascending=False)

    avg_rentals_by_weathersit = day_df.groupby(by="weathersit").agg({
        "instant": "nunique",
        "casual": "mean",
        "registered": "mean",
        "cnt": "mean"
    }).sort_values(by="cnt", ascending=False)
    
    fig_weather1, ax_weather1 = plt.subplots(figsize=(8, 6))
    total_rentals_by_weathersit.plot(kind='bar', color=['green', 'blue', 'orange', 'red'], ax=ax_weather1)
    ax_weather1.set_xlabel('Weather (1: Clear, 2: Mist+Cloudy, 3: Light Rain, 4: Heavy Rain)')
    ax_weather1.set_ylabel('Total Count of Rentals')
    ax_weather1.set_title('Total Count of Rentals by Weather')
    st.pyplot(fig_weather1)
    
    fig_weather2, ax_weather2 = plt.subplots(figsize=(8, 6))
    total_rentals_by_weathersit.plot(kind='bar', color=['green', 'blue', 'orange', 'red'], ax=ax_weather2)
    ax_weather2.set_xlabel('Weather (1: Clear, 2: Mist+Cloudy, 3: Light Rain, 4: Heavy Rain)')
    ax_weather2.set_ylabel('Average Count of Rentals')
    ax_weather2.set_title('Average Count of Rentals by Weather')
    st.pyplot(fig_weather2)
    
elif selected_option == "Total and Average Count of Rentals Trend Throughout the Day":
    st.write("You selected: Total and Average Count of Rentals Trend Throughout the Day")
    
    hourly_rentals_total = hour_df.groupby('hr')['cnt'].sum()
    
    hourly_rentals_avg = hour_df.groupby('hr')['cnt'].mean().round()

    fig_total_trend, ax_total_trend = plt.subplots(figsize=(10, 6))
    hourly_rentals_total.plot(kind='line', marker='o', color='blue', ax=ax_total_trend)
    ax_total_trend.set_xlabel('Hour of the Day')
    ax_total_trend.set_ylabel('Total Count of Rentals')
    ax_total_trend.set_title('Total Count of Rentals Trend Throughout the Day')
    ax_total_trend.set_xticks(hourly_rentals_total.index)
    ax_total_trend.grid(True)
    st.pyplot(fig_total_trend)

    fig_avg_trend, ax_avg_trend = plt.subplots(figsize=(10, 6))
    hourly_rentals_avg.plot(kind='line', marker='o', color='green', ax=ax_avg_trend)
    ax_avg_trend.set_xlabel('Hour of the Day')
    ax_avg_trend.set_ylabel('Average Count of Rentals (Rounded)')
    ax_avg_trend.set_title('Average Count of Rentals Trend Throughout the Day')
    ax_avg_trend.set_xticks(hourly_rentals_avg.index)
    ax_avg_trend.grid(True)
    st.pyplot(fig_avg_trend)