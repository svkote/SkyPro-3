from flask import Flask, render_template
from functions import *  # Такой импорт сделан преднамерено, хоть и не по правилам

app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def page_index():
    data = load_candidates()
    return render_template('index.html', data=data)


# `load_candidates()`, которая загрузит данные из файла
# `get_all()`, которая покажет всех кандидатов
# `get_by_pk(pk)`, которая вернет кандидата по pk
# `get_by_skill(skill_name)`, которая вернет кандидатов по навыку

if __name__ == '__main__':
    app.run()
