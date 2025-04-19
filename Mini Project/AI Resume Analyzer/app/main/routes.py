from flask import render_template, flash, redirect, url_for
from . import main
from .forms import ResumeForm
from models.resume_parser import parse_resume, extract_text_from_docx
from models.job_description_parser import parse_job_description
from models.resume_scorer import score_resume, generate_feedback
import pandas as pd

job_data = pd.read_csv('Datasets/job_descriptions.csv')
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(pdf_file):
    from PyPDF2 import PdfReader

    reader = PdfReader(pdf_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

@main.route('/', methods=['GET', 'POST'])
def index():
    import numpy as np
    from werkzeug.utils import secure_filename

    form = ResumeForm()
    if form.validate_on_submit():
        resume_file = form.resume.data
        job_title = form.job_title.data.strip().lower()
        job_data['Job Title'] = job_data['Job Title'].astype(str).str.strip().str.lower()
        match_row = job_data[job_data['Job Title'] == job_title]

        print("Available Titles:", job_data['Job Title'].unique())
        print("User Input:", job_title)
        print(job_title in job_data['Job Title'].values)
        print("No. of job_titles: ", len(job_data['Job Title']))


        if match_row.empty:
            flash('Job title not found in dataset. Please try a different one.', 'danger')
            return redirect(url_for('main.index'))

        job_description = match_row.iloc[0]['Job Description']
        job_responsibilities = match_row.iloc[0]['Responsibilities']
        job_experience = match_row.iloc[0]['Experience']
        job_skills = match_row.iloc[0]['skills']
        job_education = match_row.iloc[0]['Qualifications']


        if resume_file and allowed_file(resume_file.filename):
            filename = secure_filename(resume_file.filename)
            file_extension = filename.rsplit('.', 1)[1].lower()

            if file_extension in {'doc', 'docx'}:
                resume_text = extract_text_from_docx(resume_file)
            elif file_extension == 'pdf':
                resume_text = extract_text_from_pdf(resume_file)
            else:
                resume_text = resume_file.read().decode('utf-8', errors='ignore')

            resume_data = parse_resume(resume_text)
            job_description_data = parse_job_description(
                job_description, job_responsibilities, job_experience, job_skills, job_education
            )
            scores = score_resume(resume_data, job_description_data)

            feedback = generate_feedback(resume_data, job_description_data)

            # Recursively convert NumPy floats to native Python floats
            def convert_numpy(obj):
                if isinstance(obj, dict):
                    return {k: convert_numpy(v) for k, v in obj.items()}
                elif isinstance(obj, (np.float32, np.float64, float, int)):
                    return float(obj)
                else:
                    return obj

            scores = convert_numpy(scores)

            return render_template(
                'upload.html',
                scores=scores,
                feedback=feedback,
                resume_data=resume_data,
                job_data=job_description_data
            )

    return render_template('index.html', form=form)

@main.route('/job-titles')
def get_job_titles():
    from flask import jsonify

    job_titles = job_data['Job Title'].dropna().unique().tolist()
    return jsonify(job_titles)