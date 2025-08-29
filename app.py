from flask import Flask, request, jsonify, render_template
import re
import uuid
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_array():
    try:
        # Get the input array from the request
        data = request.get_json()
        
        if not data or 'array' not in data:
            return jsonify({
                'is_success': False,
                'error': 'Please provide an array in the request body with key "array"'
            }), 400
        
        input_array = data['array']
        
        if not isinstance(input_array, list):
            return jsonify({
                'is_success': False,
                'error': 'Input must be an array'
            }), 400
        
        # Process the array
        result = process_array_data(input_array)
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            'is_success': False,
            'error': f'An error occurred: {str(e)}'
        }), 500

def process_array_data(input_array):
    """Process the input array and return the required information."""
    
    # Get full name from environment variable or use default
    full_name = os.getenv('FULL_NAME', 'kishan_madhav_a_g').lower()
    current_date = datetime.now().strftime('%d%m%Y')
    user_id = f"{full_name}_{current_date}"
    
    # Initialize result dictionary
    result = {
        'is_success': True,
        'user_id': user_id,
        'email_id': f"user_{datetime.now().strftime('%Y%m%d_%H%M%S')}@example.com",
        'college_roll_number': f"2024{datetime.now().strftime('%m%d%H%M')}",
        'even_numbers': [],
        'odd_numbers': [],
        'alphabets_uppercase': [],
        'special_characters': [],
        'sum_of_numbers': 0,
        'concatenated_alphabets_reverse_alternating': ""
    }
    
    # Process each element in the array
    all_alphabets = []
    
    for item in input_array:
        item_str = str(item)
        
        # Check if it's a number
        if item_str.replace('-', '').replace('.', '').isdigit():
            num = float(item_str)
            if num.is_integer():
                num = int(num)
                if num % 2 == 0:
                    result['even_numbers'].append(num)
                else:
                    result['odd_numbers'].append(num)
                result['sum_of_numbers'] += num
            else:
                # Handle decimal numbers
                if num % 2 == 0:
                    result['even_numbers'].append(num)
                else:
                    result['odd_numbers'].append(num)
                result['sum_of_numbers'] += num
        
        # Check if it's an alphabet
        elif item_str.isalpha():
            result['alphabets_uppercase'].append(item_str.upper())
            all_alphabets.extend(list(item_str))
        
        # Check if it's a special character
        elif len(item_str) == 1 and not item_str.isalnum():
            result['special_characters'].append(item_str)
        
        # Handle mixed strings (containing both alphabets and other characters)
        else:
            # Extract alphabets from mixed strings
            alphabets = re.findall(r'[a-zA-Z]', item_str)
            if alphabets:
                result['alphabets_uppercase'].extend([alpha.upper() for alpha in alphabets])
                all_alphabets.extend(alphabets)
            
            # Extract special characters
            special_chars = re.findall(r'[^a-zA-Z0-9\s]', item_str)
            result['special_characters'].extend(special_chars)
    
    # Create concatenated alphabets in reverse order with alternating caps
    if all_alphabets:
        reversed_alphabets = all_alphabets[::-1]  # Reverse the list
        alternating_caps = []
        for i, char in enumerate(reversed_alphabets):
            if i % 2 == 0:
                alternating_caps.append(char.upper())
            else:
                alternating_caps.append(char.lower())
        result['concatenated_alphabets_reverse_alternating'] = ''.join(alternating_caps)
    
    return result

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'message': 'API is running successfully'
    }), 200

@app.route('/', methods=['GET'])
def home():
    """Home endpoint with web interface."""
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def api_docs():
    """API documentation endpoint."""
    return jsonify({
        'message': 'Array Processing API',
        'endpoints': {
            'POST /bfhl': 'Process an array and return categorized results',
            'GET /health': 'Health check endpoint',
            'GET /': 'Web interface',
            'GET /api': 'This documentation'
        },
        'usage': {
            'method': 'POST',
            'url': '/bfhl',
            'body': {
                'array': ['your', 'array', 'elements', 'here']
            }
        }
    }), 200

# Keep the old endpoint for backward compatibility
@app.route('/process-array', methods=['POST'])
def process_array_legacy():
    """Legacy endpoint for backward compatibility."""
    return process_array()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
