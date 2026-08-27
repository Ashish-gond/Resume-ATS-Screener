# 📄 Resume ATS Screener

A Python-based **Resume Applicant Tracking System (ATS) Screener** that analyzes a candidate's resume against a given Job Description and generates an ATS compatibility score.

The application uses **TF-IDF and Cosine Similarity** for resume-job matching and provides skill analysis, missing skills, improvement suggestions, scan history, and PDF reports.

---

## 🚀 Project Overview

Resume ATS Screener is a desktop application developed using **Python and Tkinter**.

The main purpose of this project is to simulate how an Applicant Tracking System (ATS) evaluates a resume according to a specific job description.

The application helps candidates understand how well their resume matches a particular job role and what improvements can be made.

---

## ✨ Features

- 📄 Upload Resume in PDF format
- 📝 Enter Job Description
- 📊 Calculate ATS Compatibility Score
- 🧠 Resume and Job Description matching using TF-IDF
- 🔍 Cosine Similarity based scoring
- ✅ Identify matching skills
- ❌ Identify missing skills
- 💡 Provide resume improvement suggestions
- 📜 Maintain scan history using SQLite
- 📑 Generate ATS analysis reports in PDF format
- 🖥️ User-friendly Tkinter desktop interface

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Tkinter | Graphical User Interface |
| PyPDF2 | Extract text from PDF resumes |
| Scikit-learn | TF-IDF and Cosine Similarity |
| NumPy | Numerical computation |
| SQLite | Store scan history |
| ReportLab | Generate PDF reports |

---

## 🧠 How ATS Scoring Works

The application follows these basic steps:

1. User uploads a resume in PDF format.
2. Resume text is extracted using **PyPDF2**.
3. User enters the target Job Description.
4. Resume and Job Description are converted into numerical vectors using **TF-IDF**.
5. **Cosine Similarity** is calculated between the resume and job description.
6. The similarity value is converted into an ATS compatibility score.
7. The application analyzes matching and missing skills.
8. Improvement suggestions are displayed.
9. The scan can be stored in SQLite history.
10. A PDF report can be generated.

---

## 📐 ATS Matching Process

```text
Resume PDF
     ↓
Text Extraction
     ↓
Resume Text
     ↓
TF-IDF Vectorization
     ↓
Cosine Similarity
     ↓
ATS Score
     ↓
Skill Analysis
     ↓
Suggestions & Report
