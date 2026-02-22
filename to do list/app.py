from flask import Flask, render_template, request, redirect, url_for
from scripts import tasks, add_task, update_task_status, delete_task

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['GET', 'POST'])
def add_task_page():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        add_task(title, description)
        return redirect(url_for('home'))

    return render_template('add_task.html')

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    update_task_status(task_id)
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete_one_task(task_id):
    delete_task(task_id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)