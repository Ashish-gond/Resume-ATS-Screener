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
- 📑 ATS screening report
- 🕒 Scan history

---

## ✨ Features

### 📄 Resume Upload
Upload a resume in **PDF format** and extract its text automatically.

### 🎯 ATS Compatibility Score
Compare the resume with the provided Job Description and generate an ATS score.

### 🧠 Resume-Job Matching
Uses **TF-IDF Vectorization** and **Cosine Similarity** to measure the similarity between resume content and job requirements.

### 🛠️ Skill Analysis
Identifies relevant skills found in the resume.

### ❌ Missing Skills
Shows important skills from the Job Description that are not detected in the resume.

### 💡 Improvement Suggestions
Provides suggestions for keywords and skills that can improve resume-job matching.

### 🕒 Scan History
Stores previous ATS screening results using SQLite.

### 📑 PDF Report
Generates and saves a professional ATS screening report in PDF format.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Tkinter | Desktop GUI |
| PyPDF2 | PDF text extraction |
| Scikit-learn | TF-IDF & Cosine Similarity |
| SQLite | Scan history database |
| ReportLab | PDF report generation |
| Git & GitHub | Version control |

---

## 🧠 How ATS Scoring Works

The application follows these main steps:

```text
Resume PDF
     ↓
Extract Resume Text
     ↓
Enter Job Description
     ↓
TF-IDF Vectorization
     ↓
Cosine Similarity
     ↓
Skill Analysis
     ↓
ATS Compatibility Score
     ↓
Missing Skills & Suggestions
     ↓
PDF Report
