# 💼 Job Scraping & Analysis

Welcome to **Job Scraping & Analysis**! 🚀 This project automates job postings extraction from various websites and visualizes key insights such as job trends, salary distribution, and required skills. Whether you're a job seeker or data enthusiast, this project can provide valuable insights! 📊

---

## 📂 Project Structure
This repository contains:
- 📓 **Job Scraper.ipynb** - Jupyter Notebook for scraping job postings.
- 📊 **jobs.csv** / **jobs.json** - Scraped job data in structured formats.
- 📈 **Charts & Visualizations:**
  - `job_description_wordcloud.png` - A word cloud of common job descriptions.
  - `job_postings_by_site.png` - Comparison of job postings by platform.
  - `job_postings_over_time.png` - Trend analysis of job postings.
  - `job_type_distribution.png` - Breakdown of job types.
  - `salary_correlation_heatmap.png` - Correlation heatmap of salaries.
- 📝 **log.txt** - Execution logs tracking the scraping process.

---

## 🛠️ Requirements
Ensure you have the following before running the scraper:
- Python 3.9 or higher 🐍
- Jupyter Notebook (for `.ipynb` execution) 📓
- Required Python libraries: `pandas (2.2.1)`, `requests(2.32.3)`, `beautifulsoup4 (4.12.3)`, `seaborn (0.13.2)`, `matplotlib (3.8.2)`, `wordcloud (1.9.4)`
- Stable Internet Connection

---

## 💻 Installation Commands
Run these commands in your terminal to install dependencies:
```sh
python -m pip install --upgrade pip
pip install pandas requests beautifulsoup4 seaborn matplotlib wordcloud
```

---

## ⚙️ How to Use
1. Clone this repository:
   ```sh
   git clone https://github.com/vinitrshah03/OST/Web Scraping/Job Scraper.git
   cd OST/Web Scraping/Job Scraper
   ```
2. Open `Job Scraper.ipynb` in Jupyter Notebook.
3. Run all the cells to start scraping job postings.
4. The extracted data will be saved in `jobs.csv` and `jobs.json`.
5. Generated charts will be saved in the project folder.
6. Check `log.txt` for any errors or progress updates.

---

## ⚠️ Notes & Disclaimers
- **Respect website terms of service!** Scraping too frequently may result in IP bans due to rate limits. Use this script responsibly. 🚨
- This project is for **educational purposes only**. 📚
- Job website structures may change, which could break the scraper. Keep the script updated! 🔄


Happy Scraping! 💼📊

