# 📄 Resume ATS Screener

A Python-based **Applicant Tracking System (ATS) Resume Screener** that analyzes a candidate's resume against a given Job Description and generates an ATS compatibility score.

The application uses **TF-IDF and Cosine Similarity** for resume-job matching and provides skill analysis, missing skills, improvement suggestions, scan history, and PDF reports.

---

## 🚀 Project Overview

Resume ATS Screener is a desktop application developed using **Python and Tkinter**.

The main purpose of this project is to simulate how an Applicant Tracking System (ATS) evaluates a resume according to a specific job description.

It helps candidates understand:

- 📊 ATS compatibility score
- ✅ Matching skills
- ❌ Missing skills
- 💡 Resume improvement suggestions
- 📑 PDF ATS report
- 🕒 Resume scan history

---

## ✨ Features

### 📤 Resume Upload
Upload a resume in **PDF format** and extract its text automatically.

### 📝 Job Description Analysis
Enter the target job description to compare it with the candidate's resume.

### 📊 ATS Score
Calculates a compatibility score using:

- TF-IDF Vectorization
- Cosine Similarity

### 🛠️ Skill Analysis
Identifies skills that are:

- Present in the resume
- Required by the job description
- Missing from the resume

### 💡 Improvement Suggestions
Provides suggestions to improve resume-job matching.

### 📑 PDF Report
Generates a professional ATS analysis report in PDF format.

### 🕒 Scan History
Stores previous ATS scans using SQLite database.

---

## 🧠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application development |
| Tkinter | Graphical User Interface |
| PyPDF2 | PDF text extraction |
| Scikit-learn | TF-IDF & Cosine Similarity |
| NumPy | Numerical processing |
| SQLite | Scan history database |
| ReportLab | PDF report generation |

---

## 🔍 How ATS Scoring Works

The system converts the resume and job description into numerical vectors using **TF-IDF (Term Frequency-Inverse Document Frequency)**.

Then it calculates their similarity using **Cosine Similarity**.

A higher similarity means the resume contains more relevant content for the selected job description.

### Basic Process

```text
Resume PDF
    ↓
Text Extraction
    ↓
Text Preprocessing
    ↓
TF-IDF Vectorization
    ↓
Cosine Similarity
    ↓
ATS Score
    ↓
Skill Analysis
    ↓
Improvement Suggestions
    ↓
PDF Report
