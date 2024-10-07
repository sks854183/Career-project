from flask import Flask, render_template, jsonify # type: ignore

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'Location': 'Bengaluru, India',
        'Salary': 'RS.10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'Location': 'Delhi, India',
        'Salary': 'RS.15,00,000'
    },
    {
        'id': 3,
        'title': 'Data Engineer',
        'Location': 'Bengaluru, India',
        'Salary': 'RS.15,00,500'
    },
    {
        'id': 4,
        'title': 'Frontend Engineer',
        'Location': 'Remote',
        'Salary': 'RS.12,00,000'
    },
    {
        'id': 5,
        'title': 'Backend Engineer',
        'Location': 'San Francisco, USA',
        'Salary': '$120,000'
    },
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, Company_name= 'Suman')

@app.route("/api/jobs")
def list_jobs(): 
    return jsonify(JOBS)


if __name__ =="__main__":
   app.run(host='0.0.0.0', port= 8000, debug=True)

