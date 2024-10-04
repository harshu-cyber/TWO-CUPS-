from flask import Flask, render_template, request, jsonify
import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('2CUPS.html')  # Assuming the HTML file is directly in 'templates' folder

@app.route('/process', methods=['POST'])
def process():
    message = request.form['user_input']
    result = main.chat_system(message)
    return jsonify({"result": result})  # Return JSON response

if __name__ == '__main__':  # Correct the main check
    app.run(debug=True)
