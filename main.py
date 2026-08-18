import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PyPDF2 import PdfReader
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

from ats_engine import calculate_ats_score, analyze_skills
from database import save_scan, get_scan_history


# =========================================================
# GLOBAL VARIABLES
# =========================================================

resume_text = ""
resume_name = ""


# =========================================================
# UPLOAD RESUME
# =========================================================

def upload_resume():
    global resume_text, resume_name

    file_path = filedialog.askopenfilename(
        title="Select Resume",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not file_path:
        return

    try:
        reader = PdfReader(file_path)
        resume_text = ""

        for page in reader.pages:
            text = page.extract_text()

            if text:
                resume_text += text + "\n"

        if not resume_text.strip():
            messagebox.showwarning(
                "Resume Error",
                "No readable text was found in this PDF."
            )
            return

        resume_name = file_path.replace("\\", "/").split("/")[-1]

        resume_label.config(
            text="Resume Selected: " + resume_name
        )

        messagebox.showinfo(
            "Success",
            f"Resume successfully read!\n\n"
            f"File: {resume_name}\n"
            f"Characters extracted: {len(resume_text)}"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Could not read resume:\n{e}"
        )


# =========================================================
# SCORE CATEGORY
# =========================================================

def get_score_category(score):

    if score >= 80:
        return "Excellent Match"

    elif score >= 60:
        return "Good Match"

    elif score >= 40:
        return "Average Match"

    else:
        return "Low Match"


# =========================================================
# SAVE ATS REPORT
# =========================================================

def save_ats_report(score, matching_skills, missing_skills):

    file_path = filedialog.asksaveasfilename(
        title="Save ATS Report",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
        initialfile="ATS_Report.pdf"
    )

    if not file_path:
        return

    try:

        pdf = canvas.Canvas(
            file_path,
            pagesize=A4
        )

        width, height = A4

        y = height - 25 * mm

        # TITLE
        pdf.setFont("Helvetica-Bold", 20)
        pdf.drawString(
            25 * mm,
            y,
            "Resume ATS Screening Report"
        )

        y -= 12 * mm

        pdf.setFont("Helvetica", 11)
        pdf.drawString(
            25 * mm,
            y,
            "Resume compatibility analysis"
        )

        y -= 18 * mm

        # RESUME
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(
            25 * mm,
            y,
            "Resume:"
        )

        pdf.setFont("Helvetica", 11)
        pdf.drawString(
            48 * mm,
            y,
            resume_name if resume_name else "Unknown"
        )

        y -= 15 * mm

        # SCORE
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(
            25 * mm,
            y,
            "ATS SCORE"
        )

        y -= 10 * mm

        pdf.setFont("Helvetica-Bold", 26)
        pdf.drawString(
            25 * mm,
            y,
            f"{score}%"
        )

        y -= 20 * mm

        # CATEGORY
        pdf.setFont("Helvetica-Bold", 13)
        pdf.drawString(
            25 * mm,
            y,
            get_score_category(score)
        )

        y -= 15 * mm

        # MATCHING SKILLS
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(
            25 * mm,
            y,
            "Matching Skills"
        )

        y -= 9 * mm

        pdf.setFont("Helvetica", 11)

        if matching_skills:

            for skill in matching_skills:

                if y < 25 * mm:
                    pdf.showPage()
                    y = height - 25 * mm
                    pdf.setFont("Helvetica", 11)

                pdf.drawString(
                    30 * mm,
                    y,
                    "[OK] " + str(skill)
                )

                y -= 7 * mm

        else:

            pdf.drawString(
                30 * mm,
                y,
                "No matching skills found."
            )

            y -= 7 * mm

        y -= 8 * mm

        # MISSING SKILLS
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(
            25 * mm,
            y,
            "Missing Skills"
        )

        y -= 9 * mm

        pdf.setFont("Helvetica", 11)

        if missing_skills:

            for skill in missing_skills:

                if y < 25 * mm:
                    pdf.showPage()
                    y = height - 25 * mm
                    pdf.setFont("Helvetica", 11)

                pdf.drawString(
                    30 * mm,
                    y,
                    "[MISSING] " + str(skill)
                )

                y -= 7 * mm

        else:

            pdf.drawString(
                30 * mm,
                y,
                "No missing skills!"
            )

            y -= 7 * mm

        y -= 10 * mm

        # SUGGESTIONS
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(
            25 * mm,
            y,
            "Resume Improvement Suggestions"
        )

        y -= 10 * mm

        pdf.setFont("Helvetica", 10)

        if missing_skills:

            pdf.drawString(
                25 * mm,
                y,
                "Consider adding these keywords if you"
            )

            y -= 6 * mm

            pdf.drawString(
                25 * mm,
                y,
                "genuinely have experience with them:"
            )

            y -= 8 * mm

            pdf.drawString(
                30 * mm,
                y,
                ", ".join(str(x) for x in missing_skills)
            )

        else:

            pdf.drawString(
                25 * mm,
                y,
                "Your resume covers all detected requirements."
            )

        # FOOTER
        pdf.setFont("Helvetica", 8)

        pdf.drawString(
            25 * mm,
            15 * mm,
            "Generated by Resume ATS Screener"
        )

        pdf.save()

        messagebox.showinfo(
            "Report Saved",
            "ATS Report saved successfully!\n\n"
            + file_path
        )

    except Exception as e:

        messagebox.showerror(
            "PDF Error",
            f"Could not save ATS report:\n{e}"
        )


# =========================================================
# CHECK ATS SCORE
# =========================================================

def check_ats_score():

    if not resume_text.strip():

        messagebox.showwarning(
            "Missing Resume",
            "Please upload your resume first."
        )

        return

    job_description = job_text.get(
        "1.0",
        tk.END
    ).strip()

    if not job_description:

        messagebox.showwarning(
            "Missing Job Description",
            "Please enter the Job Description first."
        )

        return

    try:

        score = calculate_ats_score(
            resume_text,
            job_description
        )

        matching_skills, missing_skills = analyze_skills(
            resume_text,
            job_description
        )

        save_scan(
            resume_name,
            score,
            matching_skills,
            missing_skills
        )

        show_results(
            score,
            matching_skills,
            missing_skills
        )

    except Exception as e:

        messagebox.showerror(
            "ATS Error",
            f"Something went wrong:\n{e}"
        )


# =========================================================
# SHOW RESULT WINDOW
# =========================================================

def show_results(score, matching_skills, missing_skills):

    result_window = tk.Toplevel(root)

    result_window.title(
        "ATS Screening Result"
    )

    # IMPORTANT:
    # Larger window so buttons are always visible
    result_window.geometry(
        "850x800"
    )

    result_window.resizable(
        False,
        False
    )

    # =====================================================
    # HEADER
    # =====================================================

    tk.Label(
        result_window,
        text="ATS Screening Result",
        font=("Arial", 24, "bold")
    ).pack(pady=(18, 3))

    tk.Label(
        result_window,
        text="Resume compatibility analysis",
        font=("Arial", 11)
    ).pack(pady=(0, 10))


    # =====================================================
    # SCORE FRAME
    # =====================================================

    score_frame = tk.LabelFrame(
        result_window,
        text="ATS SCORE",
        font=("Arial", 12, "bold"),
        padx=20,
        pady=8
    )

    score_frame.pack(
        fill="x",
        padx=35
    )

    tk.Label(
        score_frame,
        text=f"{score}%",
        font=("Arial", 30, "bold")
    ).pack()

    tk.Label(
        score_frame,
        text=get_score_category(score),
        font=("Arial", 14, "bold")
    ).pack(pady=3)

    progress = ttk.Progressbar(
        score_frame,
        length=550,
        mode="determinate",
        maximum=100
    )

    progress["value"] = score
    progress.pack(pady=8)


    # =====================================================
    # STATISTICS
    # =====================================================

    stats_frame = tk.Frame(
        result_window
    )

    stats_frame.pack(
        pady=10
    )

    total_skills = (
        len(matching_skills)
        + len(missing_skills)
    )

    tk.Label(
        stats_frame,
        text=f"TOTAL SKILLS\n{total_skills}",
        font=("Arial", 11, "bold"),
        width=18
    ).pack(side="left")

    tk.Label(
        stats_frame,
        text=f"MATCHING\n{len(matching_skills)}",
        font=("Arial", 11, "bold"),
        width=18
    ).pack(side="left")

    tk.Label(
        stats_frame,
        text=f"MISSING\n{len(missing_skills)}",
        font=("Arial", 11, "bold"),
        width=18
    ).pack(side="left")


    # =====================================================
    # SKILLS AREA
    # =====================================================

    skills_frame = tk.Frame(
        result_window
    )

    skills_frame.pack(
        fill="x",
        padx=35
    )


    # MATCHING
    left_frame = tk.LabelFrame(
        skills_frame,
        text="Matching Skills",
        font=("Arial", 11, "bold"),
        height=170
    )

    left_frame.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 8)
    )

    left_frame.pack_propagate(False)

    for skill in matching_skills:

        tk.Label(
            left_frame,
            text="[OK] " + str(skill),
            anchor="w",
            font=("Arial", 10)
        ).pack(
            fill="x",
            padx=12,
            pady=2
        )


    # MISSING
    right_frame = tk.LabelFrame(
        skills_frame,
        text="Missing Skills",
        font=("Arial", 11, "bold")
    )

    right_frame.pack(
        side="right",
        fill="both",
        expand=True,
        padx=(8, 0)
    )

    for skill in missing_skills:

        tk.Label(
            right_frame,
            text="[MISSING] " + str(skill),
            anchor="w",
            font=("Arial", 10)
        ).pack(
            fill="x",
            padx=12,
            pady=2
        )


    # =====================================================
    # SUGGESTIONS
    # =====================================================

    suggestion_frame = tk.LabelFrame(
        result_window,
        text="Resume Improvement Suggestions",
        font=("Arial", 11, "bold")
    )

    suggestion_frame.pack(
        fill="x",
        padx=35,
        pady=10
    )

    if missing_skills:

        suggestion = (
            "Consider adding these keywords to your resume "
            "if you genuinely have experience with them:\n\n"
            + ", ".join(
                str(x)
                for x in missing_skills
            )
        )

    else:

        suggestion = (
            "Excellent! Your resume covers all detected "
            "job requirements."
        )

    tk.Label(
        suggestion_frame,
        text=suggestion,
        justify="left",
        wraplength=700,
        font=("Arial", 10)
    ).pack(
        padx=12,
        pady=8
    )


    # =====================================================
    # SAVE REPORT BUTTON
    # =====================================================

    # THIS BUTTON IS INTENTIONALLY HERE
    # SO IT IS ALWAYS VISIBLE

    save_button = tk.Button(
        result_window,
        text="💾  SAVE ATS REPORT AS PDF",
        font=("Arial", 13, "bold"),
        command=lambda: save_ats_report(
            score,
            matching_skills,
            missing_skills
        ),
        padx=35,
        pady=12
    )

    save_button.pack(
        pady=(5, 8)
    )


    # =====================================================
    # CLOSE BUTTON
    # =====================================================

    tk.Button(
        result_window,
        text="Close",
        font=("Arial", 11, "bold"),
        command=result_window.destroy,
        padx=40,
        pady=7
    ).pack(
        pady=(0, 12)
    )


# =========================================================
# VIEW HISTORY
# =========================================================

def view_scan_history():

    history_window = tk.Toplevel(root)

    history_window.title(
        "ATS Scan History"
    )

    history_window.geometry(
        "950x550"
    )

    tk.Label(
        history_window,
        text="ATS Scan History",
        font=("Arial", 22, "bold")
    ).pack(pady=15)

    table_frame = tk.Frame(
        history_window
    )

    table_frame.pack(
        fill="both",
        expand=True,
        padx=20
    )

    columns = (
        "ID",
        "Resume",
        "Score",
        "Matching",
        "Missing",
        "Date"
    )

    table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )

    for column in columns:

        table.heading(
            column,
            text=column
        )

    table.column("ID", width=50)
    table.column("Resume", width=180)
    table.column("Score", width=100)
    table.column("Matching", width=250)
    table.column("Missing", width=250)
    table.column("Date", width=150)

    scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=table.yview
    )

    table.configure(
        yscrollcommand=scrollbar.set
    )

    table.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    try:

        records = get_scan_history()

        for record in records:

            table.insert(
                "",
                "end",
                values=(
                    record[0],
                    record[1],
                    f"{record[2]}%",
                    record[3],
                    record[4],
                    record[5]
                )
            )

    except Exception as e:

        messagebox.showerror(
            "Database Error",
            str(e)
        )

    tk.Button(
        history_window,
        text="Close",
        command=history_window.destroy,
        padx=35,
        pady=7
    ).pack(pady=15)


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title(
    "Resume ATS Screener"
)

root.geometry(
    "800x700"
)

root.resizable(
    False,
    False
)


# =========================================================
# TITLE
# =========================================================

tk.Label(
    root,
    text="Resume ATS Screener",
    font=("Arial", 26, "bold")
).pack(pady=(25, 5))


tk.Label(
    root,
    text="Check how well your resume matches a job description",
    font=("Arial", 11)
).pack()


# =========================================================
# UPLOAD
# =========================================================

tk.Button(
    root,
    text="Upload Resume (PDF)",
    font=("Arial", 12, "bold"),
    command=upload_resume,
    padx=25,
    pady=10
).pack(pady=20)


resume_label = tk.Label(
    root,
    text="No resume selected",
    font=("Arial", 10)
)

resume_label.pack()


# =========================================================
# JOB DESCRIPTION
# =========================================================

tk.Label(
    root,
    text="Job Description",
    font=("Arial", 14, "bold")
).pack(pady=(25, 5))


job_text = tk.Text(
    root,
    width=85,
    height=13,
    font=("Arial", 10)
)

job_text.pack()


# =========================================================
# CHECK ATS
# =========================================================

tk.Button(
    root,
    text="Check ATS Score",
    font=("Arial", 13, "bold"),
    command=check_ats_score,
    padx=30,
    pady=12
).pack(pady=18)


# =========================================================
# HISTORY
# =========================================================

tk.Button(
    root,
    text="View Scan History",
    font=("Arial", 11, "bold"),
    command=view_scan_history,
    padx=25,
    pady=8
).pack()


# =========================================================
# START
# =========================================================

root.mainloop()