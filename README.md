# Array Processing REST API

A Flask-based REST API that processes arrays and returns categorized information including numbers, alphabets, special characters, and various calculations.

## Features

The API processes an input array and returns:
1. **Status** - Success/error status
2. **User ID** - Unique identifier for the request
3. **Email ID** - Generated email based on timestamp
4. **College Roll Number** - Generated roll number
5. **Even Numbers** - Array of even numbers from input
6. **Odd Numbers** - Array of odd numbers from input
7. **Alphabets (Uppercase)** - Array of alphabets converted to uppercase
8. **Special Characters** - Array of special characters
9. **Sum of Numbers** - Total sum of all numeric values
10. **Concatenated Alphabets** - All alphabets in reverse order with alternating caps

## Setup Instructions

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project files**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **The API will be available at:**
   - Local: http://localhost:5000
   - Network: http://0.0.0.0:5000

## API Endpoints

### 1. Process Array (Main Endpoint)
- **URL:** `/process-array`
- **Method:** `POST`
- **Content-Type:** `application/json`

#### Request Body:
```json
{
    "array": ["your", "array", "elements", "here"]
}
```

#### Example Request:
```json
{
    "array": ["Hello", "World", 123, 456, "!", "@", "Python", 7.5, "API"]
}
```

#### Example Response:
```json
{
    "status": "success",
    "user_id": "550e8400-e29b-41d4-a716-446655440000",
    "email_id": "user_20241201_143022@example.com",
    "college_roll_number": "20241201143022",
    "even_numbers": [456],
    "odd_numbers": [123, 7.5],
    "alphabets_uppercase": ["HELLO", "WORLD", "PYTHON", "API"],
    "special_characters": ["!", "@"],
    "sum_of_numbers": 586.5,
    "concatenated_alphabets_reverse_alternating": "IaP nOhTyP dLrOw OlLeH"
}
```

### 2. Health Check
- **URL:** `/health`
- **Method:** `GET`

#### Response:
```json
{
    "status": "healthy",
    "message": "API is running successfully"
}
```

### 3. API Documentation
- **URL:** `/`
- **Method:** `GET`

Returns API documentation and usage information.

## Testing the API

### Using curl:
```bash
curl -X POST http://localhost:5000/process-array \
  -H "Content-Type: application/json" \
  -d '{"array": ["Hello", "World", 123, 456, "!", "@", "Python", 7.5, "API"]}'
```

### Using Python requests:
```python
import requests

url = "http://localhost:5000/process-array"
data = {
    "array": ["Hello", "World", 123, 456, "!", "@", "Python", 7.5, "API"]
}

response = requests.post(url, json=data)
print(response.json())
```

### Using Postman:
1. Set method to `POST`
2. Set URL to `http://localhost:5000/process-array`
3. Set Headers: `Content-Type: application/json`
4. Set Body (raw JSON):
```json
{
    "array": ["Hello", "World", 123, 456, "!", "@", "Python", 7.5, "API"]
}
```

## Error Handling

The API includes comprehensive error handling:

- **400 Bad Request:** Invalid input format or missing array
- **500 Internal Server Error:** Unexpected errors during processing

## Processing Logic

1. **Numbers:** Identified and categorized as even/odd, including decimals
2. **Alphabets:** Converted to uppercase, extracted from mixed strings
3. **Special Characters:** Non-alphanumeric characters
4. **Concatenation:** All alphabets reversed with alternating case (first uppercase, then lowercase, etc.)

## Deployment

For production deployment, consider:
- Using a production WSGI server like Gunicorn
- Setting up proper environment variables
- Implementing authentication if needed
- Using a reverse proxy like Nginx

### Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## License

This project is open source and available under the MIT License.
