# 🛒 Amazon Web Scraper

Welcome to **Amazon Web Scraper**! 🚀 This project allows you to scrape product details, prices, and ratings from Amazon best-sellers using Python. The scraped data is stored in a CSV file and can be analyzed for insights.

---

## 📂 Project Structure
This repository contains:
- 📓 **Amazon Web Scraper.ipynb** - The Jupyter Notebook with the scraping script.
- 📊 **amazon_best_sellers.csv** - The scraped product data in CSV format.
- 📝 **log.txt** - Log file to track scraping progress and errors.

---

## 🛠️ Requirements
Ensure you have the following before running the scraper:
- Python 3.9 or higher 🐍
- Jupyter Notebook (for running the `.ipynb` file) 📓
- Required Python libraries with same or higher versions: `pandas (2.2.1)`, `requests (2.32.3)`, `beautifulsoup4 (4.12.3)`, `time`
- ChromeDriver and Chrome Browser for testing 
- Stable Internet Connection
---

## 💻 Installation Commands
Run these commands in your terminal to install the necessary dependencies:
```sh
python -m pip install --upgrade pip
pip install pandas requests beautifulsoup4
```
### To download Chrome browser
1. Go to the official **Google Chrome** download page using your default browser (Edge or Safari or Firefox):  
   🔗 [Google Chrome](https://www.google.com/chrome/)
2. Click **Download Chrome** and follow the installation steps.
3. After installation, verify Chrome is installed by running the following command in your terminal/CMD prompt:  
   ```sh
   chrome --version
   ```

### To download Chrome Webdriver
1. Open Chrome browser and click on *Help* --> *About Google Chrome*
2. Check the version of your browser 133.0.XXXX.XXX
3. Visit the Chromedriver site:
   ```sh
   https://googlechromelabs.github.io/chrome-for-testing/
   ```
4. Find your exact version of browser and choose the correct file for your OS
5. Copy the URL along with your chosen driver and paste it in a new tab
6. It will automatically start downloading the driver
7. Once download is complete, you can choose where you want to save the chromedriver

---

## ⚙️ How to Use
1. Clone this repository:
   ```sh
   git clone https://github.com/vinitrshah03/OST/Web Scraping/Amazon Scraper.git
   cd OST/Web Scraping/Amazon Scraper
   ```
2. Open `Amazon Web Scraper.ipynb` in Jupyter Notebook.
3. Find *my_chromedriver_path* and write path to *chromedriver.exe* application
4. Find *my_directory_path* and write your path to save the csv and log file
5. Run all the cells to start scraping.
6. The extracted data will be saved in `amazon_best_sellers.csv`.
7. Check `log.txt` for any errors or progress updates.

---

## ⚠️ Notes & Disclaimers
- **Respect Amazon’s Terms of Service!** Scraping too frequently may result in IP bans. Use this script responsibly. 🚨
- This project is for **educational purposes only**. 📚
- Amazon’s website structure may change, which could break the scraper. Keep the script updated! 🔄

Happy Scraping! 🛍️📊
