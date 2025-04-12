from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend access

@app.route('/')
def home():
    return "AI Code Assistant Backend Running"

@app.route('/analyze', methods=['POST'])
def analyze_code():
    data = request.get_json()
    code = data.get('code')
    lang = data.get('lang')

    # TODO: Plug AI model here (e.g., CodeT5) for bug detection & fixing
    fixed_code = code.replace("print", "print")  # Dummy replacement
    explanation = "Identified no major bugs. All 'print' functions are assumed correct."  # Dummy explanation

    return jsonify({
        "fixed_code": fixed_code,
        "explanation": explanation
    })


@app.route('/refactor', methods=['POST'])
def refactor_code():
    data = request.get_json()
    code = data.get('code')
    lang = data.get('lang')

    # TODO: Plug AI model here for refactoring
    refactored_code = "# Refactored Version\n" + code  # Dummy prefix
    explanation = "Improved structure by adding comments and organizing the code."  # Dummy explanation

    return jsonify({
        "refactored_code": refactored_code,
        "explanation": explanation
    })

if __name__ == '__main__':
    app.run(debug=True)
