"""
Flask Web Application for Visualizing Covid-19 Data.

This application loads Covid-19 data, processes it, and provides
visualizations such as time series trends, bar charts, and correlation matrices.
Users can access these visualizations via the web interface.

Author: Vinit Shah
Date: 25/02/2025
"""

from flask import Flask, render_template, Response
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import matplotlib.dates as mdates

app = Flask(__name__)

# Load dataset
data = pd.read_csv('covid_data.csv', sep=',')

# Ensure all columns are visible
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Extract country names from 'Combined_Key' column
data['Country'] = data['Combined_Key'].apply(
    lambda x: x.split(',')[-1].strip() if ',' in x else x)

# Remove invalid country names and drop NaN values
invalid_countries = [
    "Winter Olympics 2022",
    "Summer Olympics 2020",
    "Diamond Princess",
    "MS Zaandam"]
data = data[~data['Country'].isin(invalid_countries)]
data = data.dropna(subset=['Incident_Rate'])

# Group by country and calculate the mean Incident Rate
country_data = data.groupby('Country', as_index=False)['Incident_Rate'].mean()

# Convert 'Last_Update' to datetime format
data['Last_Update'] = pd.to_datetime(data['Last_Update'], errors='coerce')

# Group by 'Last_Update' and 'Country' to get total Active and Death cases
# per country per date
aggregated_data = data.groupby(['Last_Update', 'Country'], as_index=False).agg({
    'Active': 'sum', 'Deaths': 'sum'})

# Aggregate again by date to get the total global values per day
trend_data = aggregated_data.groupby('Last_Update', as_index=False).agg({
    'Active': 'sum', 'Deaths': 'sum'}).sort_values(by='Last_Update')


@app.route('/')
def home():
    """
    Renders the home page of the Flask web application.

    Returns:
        HTML template for the home page.
    """
    return render_template('index.html')


def generate_plot(fig):
    """
    Converts a Matplotlib figure into a PNG image response.

    Args:
        fig (matplotlib.figure.Figure): The figure to be converted.

    Returns:
        Flask Response object containing the PNG image.
    """
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    return Response(img.getvalue(), mimetype='image/png')


@app.route('/time_series')
def time_series():
    """
    Generates and returns a time series plot of Active and Death cases over time.

    Returns:
        Flask Response object containing the time series chart.
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(
        trend_data['Last_Update'],
        trend_data['Active'],
        marker='o',
        linestyle='-',
        color='orange',
        label='Active Cases')
    ax.plot(
        trend_data['Last_Update'],
        trend_data['Deaths'],
        marker='s',
        linestyle='-',
        color='red',
        label='Death Cases')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.xticks(fontsize=8)
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Cases")
    ax.set_title("Active Cases and Death Cases Trends Over Time")
    ax.legend()
    ax.grid(True)
    return generate_plot(fig)


@app.route('/bar_chart')
def bar_chart():
    """
    Generates and returns a bar chart of the average Covid-19 Incident Rate by country.

    Returns:
        Flask Response object containing the bar chart.
    """
    fig, ax = plt.subplots(figsize=(18, 6))
    global_avg = country_data['Incident_Rate'].mean()
    ax.bar(
        country_data['Country'],
        country_data['Incident_Rate'],
        color='skyblue',
        width=0.6)
    ax.axhline(
        global_avg,
        color='red',
        linestyle='--',
        linewidth=2,
        label=f'Global Avg: {global_avg:.2f}')
    exceeding_countries = country_data[country_data['Incident_Rate'] > global_avg]
    ax.set_xticks(exceeding_countries.index)
    ax.set_xticklabels(
        exceeding_countries['Country'],
        rotation=90,
        fontsize=9,
        ha='right',
        rotation_mode="anchor")
    ax.set_xlabel("Country")
    ax.set_ylabel("Average Incident Rate")
    ax.set_title("Average Covid-19 Incident Rate by Country")
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.legend()
    plt.tight_layout()
    return generate_plot(fig)


@app.route('/correlation_matrix')
def correlation_matrix():
    """
    Generates and returns a correlation matrix heatmap of Covid-19 data.

    Returns:
        Flask Response object containing the correlation matrix heatmap.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    corr_matrix = data[['Confirmed', 'Deaths', 'Recovered',
                        'Active', 'Incident_Rate', 'Case_Fatality_Ratio']].corr()
    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap='coolwarm',
        linewidths=0.5,
        fmt=".2f",
        ax=ax)
    ax.set_title("Correlation Matrix of Covid-19 Data", fontsize=14)
    ax.set_xticklabels(ax.get_xticklabels(), ha='right', rotation=20)
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
    plt.tight_layout()
    return generate_plot(fig)


if __name__ == '__main__':
    app.run(debug=True)
