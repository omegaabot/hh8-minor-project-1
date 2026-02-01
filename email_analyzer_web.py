import os
from flask import Flask, render_template, request, flash
from email_simple_output import analyze_email

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flashing messages

UPLOAD_FOLDER = "uploaded_emails"
if not os.path.exists(UPLOAD_FOLDER):  # Create directory if it doesn't exist
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def index():
    """Render the main page."""
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    """Handle file upload and email analysis."""
    if "file" not in request.files:
        flash("No file selected. Please upload an email file.")
        return render_template("index.html")

    file = request.files["file"]

    if file.filename == "":
        flash("No file selected. Please upload a valid email file.")
        return render_template("index.html")

    # Save the file temporarily
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    try:
        # Run email analysis and capture results
        results = analyze_email(file_path)
        return render_template("results.html", results=results)
    except Exception as e:
        flash(f"An error occurred: {str(e)}")
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)