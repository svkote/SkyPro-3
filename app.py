from flask import Flask, render_template
from functions import *  # Такой импорт сделан преднамерено, хоть и не по правилам

app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def page_index():
    data = load_candidates()
    return render_template('index.html', data=data)


@app.route("/candidates/<int:pk>")
def show_candidate(pk):
    candidate = get_by_pk(pk)
    return render_template('show_candidate.html', candidate=candidate)


@app.route("/skills/<skill>")
def show_candidates_by_skill(skill):
    candidates = get_by_skill(skill)
    return render_template('show_candidates_by_skill.html', candidates=candidates)


if __name__ == '__main__':
    app.run()
