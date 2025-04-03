from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title': 'Data Engineer',
        'location': 'Bengaluru'
    },
    {
        'id':2,
        'title': 'Data Scientist',
        'location': 'Bengaluru'
    },
    {
        'id':3,
        'title': 'AI Engineer',
        'location': 'Bengaluru'
    },
    {
        'id':4,
        'title': 'Prompt Engineer',
        'location': 'Bengaluru'
    },

]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__=='__main__':
    app.run(debug=True)