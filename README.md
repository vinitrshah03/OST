COVID-19 Daily Reports Analyzer Dashboard
-----------------------------------------

This is a simple web-based Dashboard that shows analysis of daily reports recorded during the COVID-19 pandemic. Feel free to try out the code...

### 🛑 You will require 🛑 
*Ensure you meet these requirements or are using versions higher than the ones mentioned below*

- A python version 3.9 or higher
- Python libraries such as: pandas (2.2.1), numpy (1.26.3), matplotlib (3.8.2), seaborn (0.13.2), requests (2.32.3), os, multiprocessing and datetime
- An IDE that supports Python programming like: VSCode, Spyder, Jupyter, PyCharm etc.
- A Github account and a API token

### 💻 Installation Commands 💻
*Run these once in your IDE terminal before actually executing the code*

'python -m pip install --upgrade pip'
'pip install pandas seaborn matplotlib requests'

### Github API Token Creation 
1. Create an account in [Github](https://github.com/)
2. Click on your *Profile* and select *Settings*
3. Navigate to *Developer Settings* and click on *Personal access tokens*
4. Select *Tokens(classic)* and click on *Generate new token* --> *Generate new token(classic)*
5. Set "Token Permission" and select *public_repo*
6. Click *Generate token* and copy it for future use....

### ⚙️How it Works⚙️
1. Download, save and edit the csv_files_handler.py file in your python IDE.
2. Find 👉 *GITHUB_TOKEN* in the code and paste your copied Github API token in place of *"my_github_api_token"*.
3. Then, locate 👉 *GRAPHS_DIR* in the code and write the path to the folder where you want the Charts to be saved in place of *"my_directory_path"*.
4. Save the edited code file and run it..
5. You will be notified with messages like: *Processed: 01-01-2021.csv*
6. Wait for sometime as it will take from 2-5mins based on system's processing speed
7. Once all files have been processed, you can check your folder for the charts and graphs created.

*Note: CSV files used are publicly available and have been referred for analysis. Link to COVID-19 dataset👉* [COVID-19 Dataset](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data)

Results of csv_files_handler.py can be viewed freely by following the link below 👇:
Click here 👉 [Graphs](https://mega.nz/folder/37ogECJK#8OAHG-_VEW25CxV09v48Qg)
