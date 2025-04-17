# 🚀 AI Resume Analyzer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?logo=flask)
![spaCy](https://img.shields.io/badge/spaCy-NLP-blueviolet)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

A Python-based AI-powered web application that intelligently **analyzes and scores resumes** against job descriptions using Natural Language Processing and Machine Learning techniques.

---

## 🌟 Features
- 📄 **Upload Resume** in PDF, DOC, or DOCX format.
- ✨ **Smart Job Title Suggestions** while typing.
- 📊 **Analyze & Score** your resume based on:
  - Skills Match
  - Experience Match
  - Education Match
  - Resume Structure
  - Keyword Relevance
- 🧠 **Detailed Feedback** on resume gaps and improvement areas.
- 📈 **Dynamic Bar Chart** visualization of scoring breakdown.
- 🧪 **Basic Unit Tests** to ensure functionality stability.
- 🎯 Lightweight, fast, and easy to deploy (CPU-only).

---

## 🛠️ Technologies Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **NLP & Machine Learning:** spaCy, HuggingFace Transformers, scikit-learn
- **Resume Parsing:** PyPDF2, python-docx, BeautifulSoup
- **Testing:** Python `unittest`

---

## 📂 Project Structure

```plaintext
AI_resume_analyzer/
├── App/
│   ├── Main/
│   │   ├── static/
│   │   │   ├── css/
│   │   │   │   └── styles.css
│   │   │   ├── js/
│   │   │   │   └── scripts.js
│   │   ├── templates/
│   │   │   ├── base.html
│   │   │   ├── index.html
│   │   │   └── upload.html
│   │   ├── forms.py
│   │   ├── routes.py
│   ├── __init__.py
├── Models/
│   ├── resume_parser.py
│   ├── job_description_parser.py
│   ├── resume_scorer.py
├── Datasets/
│   ├── job_descriptions.csv
│   ├── Resume/
│   │   └── Resume.csv
│   ├── Data/
│       └── (multiple folders with resume HTML files)
├── Kaggle/
│   └── kaggle.json
├── Tests/
│   ├── test_job_description_parser.py
│   ├── test_resume_parser.py
│   └── test_resume_scorer.py
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/AI_resume_analyzer.git
cd AI_resume_analyzer
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download spaCy Model
```bash
python -m spacy download en_core_web_sm
```

### 5. (Optional) Set Kaggle API Key
If needed for datasets:
```bash
mkdir .kaggle
copy your kaggle.json file inside the .kaggle directory
```

### 6. Run the Application
```bash
python run.py
```

Open your browser and visit:  
👉 `http://127.0.0.1:5000/`

---

## 📸 Screens and Workflow

- **Home Screen:**
  - Upload resume
  - Type/select job title with smart suggestions
  - Submit for analysis

- **Result Screen:**
  - View overall Match Score
  - Detailed breakdown across Skills, Experience, Education, Structure, Keywords
  - Visual Bar Chart
  - Bullet-pointed feedback for improvements

---

## 🧪 Running Tests

To run all unit tests:

```bash
python -m unittest discover -s Tests
```

You will see:
- ✅ Test status (OK/Fail/Error)
- ✅ Debug logs if any

---

## 🎨 Customization Options

- ✨ Update CSS inside `App/Main/static/css/styles.css` for new themes.
- ✨ Enhance JavaScript interactivity in `App/Main/static/js/scripts.js`.
- ✨ Extend ML/NLP models inside `Models/` for advanced scoring.

---

## 📌 Notes

- 🚀 This app is optimized for CPU use — no GPU required.
- 📚 Lightweight for academic or portfolio projects.
- 🛡️ Designed with modularity for future improvements (classification models, prediction systems, etc.)

---

# ✨ Happy Analyzing! 🚀
