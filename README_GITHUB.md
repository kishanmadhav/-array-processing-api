# Array Processing REST API

A Flask-based REST API that processes arrays and returns categorized information including numbers, alphabets, special characters, and various calculations.

## 🚀 Live Demo

**Hosted API:** [https://array-processing-api.onrender.com](https://array-processing-api.onrender.com)

## 📋 API Endpoint

- **Method:** POST
- **Route:** `/bfhl`
- **Status Code:** 200 (success)

### Request Format
```json
{
    "array": ["Hello", "World", 123, 456, "!", "@", "Python", 7.5, "API"]
}
```

### Response Format
```json
{
    "is_success": true,
    "user_id": "kishan_madhav_a_g_29082025",
    "email_id": "user_20250829_112050@example.com",
    "college_roll_number": "202408291120",
    "even_numbers": [456],
    "odd_numbers": [123, 7.5],
    "alphabets_uppercase": ["HELLO", "WORLD", "PYTHON", "API"],
    "special_characters": ["!", "@"],
    "sum_of_numbers": 586.5,
    "concatenated_alphabets_reverse_alternating": "IaP nOhTyP dLrOw OlLeH"
}
```

## 🧪 Test the API

### Using curl:
```bash
curl -X POST https://array-processing-api.onrender.com/bfhl \
  -H "Content-Type: application/json" \
  -d '{"array": ["Hello", "World", 123, 456, "!", "@", "Python", 7.5, "API"]}'
```

### Using Python requests:
```python
import requests

url = "https://array-processing-api.onrender.com/bfhl"
data = {
    "array": ["Hello", "World", 123, 456, "!", "@", "Python", 7.5, "API"]
}

response = requests.post(url, json=data)
print(response.json())
```

### Using Postman:
1. Set method to `POST`
2. Set URL to `https://array-processing-api.onrender.com/bfhl`
3. Set Headers: `Content-Type: application/json`
4. Set Body (raw JSON):
```json
{
    "array": ["Hello", "World", 123, 456, "!", "@", "Python", 7.5, "API"]
}
```

## 🔧 Features

The API processes an input array and returns:
1. **is_success** - Boolean indicating operation status
2. **user_id** - Format: `{full_name_ddmmyyyy}` (e.g., "kishan_madhav_a_g_29082025")
3. **email_id** - Generated email based on timestamp
4. **college_roll_number** - Generated roll number
5. **even_numbers** - Array of even numbers from input
6. **odd_numbers** - Array of odd numbers from input
7. **alphabets_uppercase** - Array of alphabets converted to uppercase
8. **special_characters** - Array of special characters
9. **sum_of_numbers** - Total sum of all numeric values
10. **concatenated_alphabets_reverse_alternating** - All alphabets in reverse order with alternating caps

## 🛠️ Local Development

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/array-processing-api.git
   cd array-processing-api
   ```

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
   - Web Interface: http://localhost:5000/
   - API Endpoint: http://localhost:5000/bfhl
   - Health Check: http://localhost:5000/health

## 🧪 Testing

Run the comprehensive test suite:
```bash
python test_api.py
```

## 🌐 Deployment

This API is deployed on **Render** and can be accessed at:
- **Production URL:** https://array-processing-api.onrender.com
- **API Endpoint:** https://array-processing-api.onrender.com/bfhl

### Alternative Deployment Options

#### Railway
1. Fork this repository
2. Connect to Railway
3. Deploy automatically

#### Heroku
1. Fork this repository
2. Connect to Heroku
3. Set environment variables if needed

#### Vercel
1. Fork this repository
2. Connect to Vercel
3. Deploy as a Python function

## 📊 Processing Logic

1. **Numbers:** Identified and categorized as even/odd (including decimals)
2. **Alphabets:** Converted to uppercase, extracted from mixed strings
3. **Special Characters:** Non-alphanumeric characters
4. **Concatenation:** All alphabets reversed with alternating case (UPPER, lower, UPPER, lower...)

## 🛡️ Error Handling

- **400 Bad Request:** Invalid input format or missing array
- **500 Internal Server Error:** Unexpected errors during processing
- Comprehensive input validation
- Graceful error responses

## 📝 Environment Variables

- `FULL_NAME`: Set your full name for user_id generation (default: "kishan_madhav_a_g")
- `PORT`: Port number for the server (default: 5000)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Links

- **Live API:** https://array-processing-api.onrender.com/bfhl
- **Web Interface:** https://array-processing-api.onrender.com/
- **Health Check:** https://array-processing-api.onrender.com/health
- **API Documentation:** https://array-processing-api.onrender.com/api

---

**Note:** The API is designed to handle various input types and provides comprehensive error handling. The user_id format follows the specification: `{full_name_ddmmyyyy}` where the full name is converted to lowercase.
