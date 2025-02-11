from flask import render_template, request, redirect, url_for
from main import get_response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    response = get_response(user_message)
    return render_template('index.html', response=response)
