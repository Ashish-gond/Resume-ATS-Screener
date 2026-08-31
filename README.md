# 📄 Resume ATS Screener

A Python-based **Applicant Tracking System (ATS) Resume Screener** that analyzes a candidate's resume against a given Job Description and generates an ATS compatibility score.

The application uses **TF-IDF and Cosine Similarity** for resume-job matching and provides skill analysis, missing skills, improvement suggestions, scan history, and PDF reports.

---

## 🚀 Project Overview

Resume ATS Screener is a desktop application developed using **Python and Tkinter**.

The main purpose of this project is to simulate how an Applicant Tracking System evaluates a resume according to a specific job description.

It helps candidates understand:

- 📊 ATS compatibility score
- ✅ Matching skills
- ❌ Missing skills
- 💡 Resume improvement suggestions
- 📜 Previous scan history
- 📄 ATS report generation

---

## ✨ Features

### 📤 Resume Upload
Upload a resume in **PDF format**.

### 📝 Job Description Analysis
Enter the job description against which the resume should be evaluated.

### 📊 ATS Score
Generates an ATS compatibility score based on resume and job-description similarity.

### 🧠 TF-IDF + Cosine Similarity
Uses Natural Language Processing techniques to calculate the similarity between the resume and job description.

### 🛠️ Skill Analysis
Identifies relevant skills found in the resume.

### ❌ Missing Skills
Highlights important skills that are present in the job description but missing from the resume.

### 💡 Improvement Suggestions
Provides suggestions to improve resume-job compatibility.

### 📜 Scan History
Stores previous ATS scans using SQLite.

### 📄 PDF Report
Generates a professional ATS analysis report in PDF format.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application development |
| Tkinter | Graphical User Interface |
| Scikit-learn | TF-IDF and Cosine Similarity |
| PyPDF2 | Extract text from PDF resumes |
| SQLite | Store scan history |
| ReportLab | Generate PDF reports |

---

## 📁 Project Structure

```text
Resume-ATS-Screener/
│
├── resumes/
│   └── Ashish_Gond_Resume (4).pdf
│
├── main.py
├── ats_engine.py
├── database.py
├── ats_history.db
├── requirements.txt
├── README.md
├── .gitignore
│
└── main_backup.py
