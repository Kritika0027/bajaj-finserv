from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins for simplicity

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        data = request.get_json()

        # Extracting fields from the request
        status = "success"
        user_id = data.get('user_id')
        college_email_id = data.get('college_email_id')
        college_roll_number = data.get('college_roll_number')

        # Extracting input data and separating numbers and alphabets
        input_data = data.get('input_data', "")

        # Separating numbers and alphabets
        numbers = [char for char in input_data if char.isdigit()]
        alphabets = [char for char in input_data if char.isalpha()]

        # Creating the response
        response = {
            "status": status,
            "user_id": user_id,
            "college_email_id": college_email_id,
            "college_roll_number": college_roll_number,
            "numbers_array": numbers,
            "alphabets_array": alphabets
        }

        return jsonify(response), 200

    if request.method == 'GET':
        # Generate an operation code (you can customize this logic)
        operation_code = "OP123456"  # Placeholder operation code
        return jsonify({"operation_code": operation_code}), 200

if __name__ == '__main__':
    app.run(debug=True)
