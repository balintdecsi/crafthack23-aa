from flask import Flask, render_template, request, url_for, flash, redirect
from dev.src.seon import get_user_score

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b5050c392097268742d148b8dfc7afb646a629a83d75c660'

messages = [{'content': 'Message One Content'}]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        content = request.form['content']

        if not content:
            flash('Content is required!')
        # elif 'https' not in content:
        #     flash('Content must have https in it!')
        else:
            messages[0] = {'content': 'score for this-1, 1]}
            return redirect(url_for('index'))

    return render_template('create.html')