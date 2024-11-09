import json

from flask import Flask, render_template

from functions import get_students_data

app = Flask(__name__)


@app.template_filter('to_json')
def to_json(value):
    return json.dumps(value, ensure_ascii=False)


app.jinja_env.filters['to_json'] = to_json


@app.route('/')
def index():
    return render_template('index.html', students_data=get_students_data('static/students-data.xlsx'))


if __name__ == '__main__':
    app.run()
