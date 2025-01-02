from flask import Flask, render_template, url_for, jsonify, request
import project

import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    try:
        # Run the project.py script
        result = subprocess.run(
            ['python', 'project.py'],  # Command to execute project.py
            capture_output=True,       # Capture the output
            text=True                  # Get output as a string
        )
        # Return the output from the script
        return jsonify(output=result.stdout, error=result.stderr)
    except Exception as e:
        # Handle exceptions and return the error message
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)

