import sqlite3
from datetime import datetime


DATABASE_NAME = "ats_history.db"


# =========================================================
# CREATE DATABASE TABLE
# =========================================================

def create_database():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scan_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            resume_name TEXT,
            ats_score REAL,
            matching_skills TEXT,
            missing_skills TEXT,
            scan_date TEXT
        )
    """)

    connection.commit()
    connection.close()


# =========================================================
# SAVE SCAN HISTORY
# =========================================================

def save_scan(
    resume_name,
    ats_score,
    matching_skills,
    missing_skills
):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    matching_text = ", ".join(
        str(skill) for skill in matching_skills
    )

    missing_text = ", ".join(
        str(skill) for skill in missing_skills
    )

    scan_date = datetime.now().strftime(
        "%d-%m-%Y %H:%M"
    )

    cursor.execute("""
        INSERT INTO scan_history (
            resume_name,
            ats_score,
            matching_skills,
            missing_skills,
            scan_date
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        resume_name,
        ats_score,
        matching_text,
        missing_text,
        scan_date
    ))

    connection.commit()
    connection.close()


# =========================================================
# GET SCAN HISTORY
# =========================================================

def get_scan_history():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            resume_name,
            ats_score,
            matching_skills,
            missing_skills,
            scan_date
        FROM scan_history
        ORDER BY id DESC
    """)

    records = cursor.fetchall()

    connection.close()

    return records


# =========================================================
# INITIALIZE DATABASE
# =========================================================

create_database()