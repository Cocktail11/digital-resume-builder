from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/builder")
def builder():
    return render_template("builder.html")
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory("uploads", filename)

@app.route("/generate", methods=["POST"])
def generate():
    profile_picture = request.files.get("profile_picture")
    if profile_picture and profile_picture.filename:
        filename = profile_picture.filename
        profile_picture.save(os.path.join("uploads", filename))
    else:
        filename = None
    name = request.form.get("full_name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    address = request.form.get("address")
    objective = request.form.get("objective")

    degree = request.form.get("degree")
    college = request.form.get("college")
    graduation_year = request.form.get("graduation_year")
    cgpa = request.form.get("cgpa")

    skills = request.form.get("skills")

    project_title = request.form.get("project_title")
    project_description = request.form.get("project_description")
    technologies = request.form.get("technologies")

    project_title_2 = request.form.get("project_title_2")
    project_description_2 = request.form.get("project_description_2")
    technologies_2 = request.form.get("technologies_2")

    job_title = request.form.get("job_title")
    company = request.form.get("company")
    duration = request.form.get("duration")
    experience_description = request.form.get("experience_description")

    certifications = request.form.get("certifications")
    achievements = request.form.get("achievements")

    return render_template(
        "resume.html",
        profile_picture=filename,
        name=name,
        email=email,
        phone=phone,
        address=address,
        objective=objective,
        degree=degree,
        college=college,
        graduation_year=graduation_year,
        cgpa=cgpa,
        skills=skills,
        project_title=project_title,
        project_description=project_description,
        technologies=technologies,
        project_title_2=project_title_2,
        project_description_2=project_description_2,
        technologies_2=technologies_2,
        job_title=job_title,
        company=company,
        duration=duration,
        experience_description=experience_description,
        certifications=certifications,
        achievements=achievements
    )
if __name__ == "__main__":
    app.run(debug=True)