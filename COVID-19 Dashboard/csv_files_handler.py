"""
CSV File Handler for Processing Covid-19 Data.

This script downloads daily Covid-19 reports from GitHub, processes them,
and generates visualizations including time-series plots, bar charts,
and correlation matrices.

Author: Vinit Shah
Date: 25/02/2025

https://github.com/vinitrshah03/OST
"""
import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from datetime import datetime
from multiprocessing import Pool, cpu_count

# GitHub API details
GITHUB_TOKEN = "my_github_api_token"
OWNER = "CSSEGISandData"
REPO = "COVID-19"
PATH = "csse_covid_19_data/csse_covid_19_daily_reports"
GITHUB_API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{PATH}"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

# Directory to save graphs
GRAPHS_DIR = "my_direcotry_path"
os.makedirs(GRAPHS_DIR, exist_ok=True)

"""
    Fetches the list of available CSV files from the GitHub repository.

    Returns:
        List of CSV file names.
"""
# Fetch repository contents
response = requests.get(GITHUB_API_URL, headers=HEADERS)
if response.status_code == 200:
    files = response.json()
    csv_files = [file["name"]
                 for file in files if file["name"].endswith(".csv")]
else:
    print(
        f"Error: Unable to fetch repository contents. Status code {response.status_code}")
    exit()


def process_csv(file_name):
    """
    Processes a single CSV file and generates charts.

    Args:
        file_name (str): The name of the CSV file to process.
    """
    try:
        # Download CSV file
        file_url = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/master/{PATH}/{file_name}"
        df = pd.read_csv(file_url)

        # Convert 'Last_Update' column to datetime format if present
        if "Last_Update" in df.columns:
            df["Last_Update"] = pd.to_datetime(
                df["Last_Update"], errors="coerce", format="%m/%d/%y %H:%M")

        # Process country-based data if 'Combined_Key' is present
        if "Combined_Key" in df.columns:
            df["Country"] = df["Combined_Key"].apply(
                lambda x: x.split(",")[-1].strip() if isinstance(x, str) else x)
            df = df.dropna(subset=["Country"])
            invalid_countries = [
                "Winter Olympics 2022",
                "Summer Olympics 2020",
                "Diamond Princess",
                "MS Zaandam"]
            df = df[~df["Country"].isin(invalid_countries)]

        # Generate time-series chart if 'Active' and 'Deaths' are present
        if "Last_Update" in df.columns and "Active" in df.columns and "Deaths" in df.columns:
            time_series_df = df.groupby("Last_Update", as_index=False).agg({
                "Active": "sum", "Deaths": "sum"})
            time_series_df = time_series_df.sort_values(by="Last_Update")

            ax = plt.subplots(figsize=(10, 5))
            ax.plot(
                time_series_df["Last_Update"],
                time_series_df["Active"],
                marker="o",
                linestyle="-",
                color="orange",
                label="Active Cases")
            ax.plot(
                time_series_df["Last_Update"],
                time_series_df["Deaths"],
                marker="s",
                linestyle="-",
                color="red",
                label="Death Cases")
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
            ax.xaxis.set_major_locator(mdates.AutoDateLocator())
            ax.set_xlabel("Date")
            ax.set_ylabel("Total Cases")
            ax.set_title(f"Covid-19 Active & Death Cases - {file_name}")
            ax.legend()
            ax.grid(True)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(
                os.path.join(
                    GRAPHS_DIR,
                    f"time_series_{file_name}.png"))
            plt.close()

        # Generate bar chart if 'Incident_Rate' is present
        if "Country" in df.columns and "Incident_Rate" in df.columns:
            country_data = df.groupby("Country", as_index=False)[
                "Incident_Rate"].mean()
            global_avg = country_data["Incident_Rate"].mean()

            fig, ax = plt.subplots(figsize=(18, 6))
            ax.bar(
                country_data["Country"],
                country_data["Incident_Rate"],
                color="skyblue",
                width=0.6)
            ax.axhline(
                global_avg,
                color="red",
                linestyle="--",
                linewidth=2,
                label=f"Global Avg: {global_avg:.2f}")
            exceeding_countries = country_data[country_data["Incident_Rate"] > global_avg]
            ax.set_xticks(exceeding_countries.index)
            ax.set_xticklabels(
                exceeding_countries["Country"],
                rotation=90,
                fontsize=9,
                ha="right",
                rotation_mode="anchor")
            ax.set_xlabel("Country")
            ax.set_ylabel("Average Incident Rate")
            ax.set_title(f"Covid-19 Incident Rate by Country - {file_name}")
            ax.grid(axis="y", linestyle="--", alpha=0.7)
            ax.legend()
            plt.tight_layout()
            plt.savefig(os.path.join(GRAPHS_DIR, f"bar_chart_{file_name}.png"))
            plt.close()

        # Generate correlation matrix if relevant columns are available
        correlation_columns = [
            "Confirmed",
            "Deaths",
            "Recovered",
            "Active",
            "Incident_Rate",
            "Case_Fatality_Ratio"]
        available_columns = [
            col for col in correlation_columns if col in df.columns]
        if len(available_columns) > 1:
            ax = plt.subplots(figsize=(12, 6))
            corr_matrix = df[available_columns].corr()
            sns.heatmap(
                corr_matrix,
                annot=True,
                cmap="coolwarm",
                linewidths=0.5,
                fmt=".2f",
                ax=ax)
            ax.set_title(
                f"Covid-19 Correlation Matrix - {file_name}",
                fontsize=14)
            plt.tight_layout()
            plt.savefig(
                os.path.join(
                    GRAPHS_DIR,
                    f"correlation_{file_name}.png"))
            plt.close()

        print(f"Processed: {file_name}")

    except Exception as e:
        print(f"Error processing {file_name}: {e}")


if __name__ == "__main__":
    with Pool(cpu_count()) as pool:
        pool.map(process_csv, csv_files)
