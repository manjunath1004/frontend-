from flask import Flask, render_template, jsonify  # Ensure this import works

app = Flask(__name__)

# app = Flask(__name__, template_folder='templates')

jobs = [{
    "id": "1.",
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "salary": 100000
}, {
    "id": "2.",
    "title": "Data Scientist",
    "location": "Delhi, India",
    "salary": 150000
}, {
    "id": "3.",
    "title": "Frontend Developer",
    "location": "Remote",
    "salary": 120000
}, {
    "id": "4.",
    "title": "Backend Developer",
    "location": "San Francisco, USA",
    "salary": 150000
}, {
    "id": "5.",
    "title": "Software Engineer",
    "location": "San Francisco, USA",
    "salary": 200000
}]


@app.route("/")
def index():
    return render_template("index.html",jobs=jobs,company_name="SOLO ZEN")


@app.route("/jobs")
def list_jobs():
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
