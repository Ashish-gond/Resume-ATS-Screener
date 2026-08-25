
# 📄 Resume ATS Screener

A Python-based Resume Applicant Tracking System (ATS) Screener that analyzes a candidate's resume against a given Job Description and generates an ATS compatibility score.

The application uses **TF-IDF and Cosine Similarity** for resume-job matching and provides skill analysis, missing skills, improvement suggestions, scan history, and PDF reports.

---

## 🚀 Project Overview

Resume ATS Screener is a desktop application built using Python and Tkinter.

The main purpose of this project is to simulate how an Applicant Tracking System (ATS) can evaluate a resume according to a specific job description.

The application allows the user to:

- Upload a resume in PDF format
- Enter a Job Description
- Analyze resume compatibility
- Calculate an ATS score
- Identify matching skills
- Identify missing skills
- Get resume improvement suggestions
- Save ATS reports as PDF
- Maintain previous scan history

---

## 🎯 Objectives

The main objectives of this project are:

1. Automate basic resume screening.
2. Compare resume content with a job description.
3. Calculate resume-job compatibility using NLP techniques.
4. Identify important matching and missing skills.
5. Provide useful resume improvement suggestions.
6. Maintain a history of previous ATS scans.
7. Generate a professional PDF report.

---

## 🛠️ Technologies Used

### Programming Language

- Python

### GUI

- Tkinter
- ttk

### PDF Processing

- PyPDF2
- ReportLab

### Machine Learning / NLP

- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

### Database

- SQLite

### Development Environment

- Visual Studio Code

---

## 🧠 How the ATS Engine Works

The ATS engine follows a simple NLP-based approach.

### Step 1: Resume Upload

The user uploads a resume in PDF format.

The application extracts readable text from the PDF using PyPDF2.

### Step 2: Job Description

The user enters the required job description into the application.

### Step 3: Text Processing

The extracted resume text and job description are processed for comparison.

### Step 4: TF-IDF Vectorization

TF-IDF (Term Frequency-Inverse Document Frequency) converts the resume and job description into numerical vectors.

This helps identify the importance of words and terms appearing in the documents.

### Step 5: Cosine Similarity

Cosine Similarity is used to calculate how similar the resume is to the job description.

The similarity value is converted into an ATS compatibility score.

### Step 6: Skill Analysis

The application checks important technical skills and identifies:

- Matching Skills
- Missing Skills
- Total Skills

### Step 7: Suggestions

If important skills are missing, the application provides resume improvement suggestions.

### Step 8: Report Generation

The final ATS analysis can be saved as a PDF report.

---

## 📊 Features

### 1. Resume Upload

Users can upload PDF resumes directly from the desktop application.

### 2. Job Description Input

Users can enter a complete job description for comparison.

### 3. ATS Score

The system generates a percentage-based ATS compatibility score.

Example:

**ATS Score: 90%**

### 4. Matching Skills

The application displays skills found in both the resume and job description.

Example:

- Java
- Python
- SQL
- MySQL
- Git/GitHub
- Data Structures

### 5. Missing Skills

The system identifies important skills that are present in the job description but missing from the resume.

Example:

- Problem Solving

### 6. Resume Improvement Suggestions

The application suggests keywords that may improve resume compatibility when they genuinely match the candidate's experience.

### 7. Scan History

Previous resume scans are stored using SQLite and can be viewed later.

### 8. PDF Report

Users can save the complete ATS analysis as a PDF report.

The report can contain:

- ATS Score
- Matching Skills
- Missing Skills
- Resume Improvement Suggestions
- Job Description information

---

## 🗂️ Project Structure

```text
Resume_ATS_Screener/
│
├── main.py
├── ats_engine.py
├── database.py
├── ats_history.db
│
├── main_backup.py
├── main_backup_before_breakdown.py
│
├── resumes/
│
└── __pycache__/
