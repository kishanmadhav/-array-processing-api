import requests
import json

def test_api():
    """Test the array processing API with various test cases."""
    
    base_url = "http://localhost:5000"
    
    # Test cases
    test_cases = [
        {
            "name": "Basic Test",
            "array": ["Hello", "World", 123, 456, "!", "@", "Python", 7.5, "API"]
        },
        {
            "name": "Numbers Only",
            "array": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        },
        {
            "name": "Alphabets Only",
            "array": ["apple", "banana", "cherry", "date"]
        },
        {
            "name": "Special Characters Only",
            "array": ["!", "@", "#", "$", "%", "&", "*"]
        },
        {
            "name": "Mixed Content",
            "array": ["Hello123", "World!", "Python@2024", "API#Test", 42, 3.14, "Flask"]
        },
        {
            "name": "Empty Array",
            "array": []
        }
    ]
    
    print("🚀 Testing Array Processing API")
    print("=" * 50)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📝 Test Case {i}: {test_case['name']}")
        print(f"Input Array: {test_case['array']}")
        
        try:
            # Make API request
            response = requests.post(
                f"{base_url}/bfhl",
                json={"array": test_case['array']},
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                result = response.json()
                print("✅ Success!")
                print(f"Success: {result['is_success']}")
                print(f"User ID: {result['user_id']}")
                print(f"Email: {result['email_id']}")
                print(f"Roll Number: {result['college_roll_number']}")
                print(f"Even Numbers: {result['even_numbers']}")
                print(f"Odd Numbers: {result['odd_numbers']}")
                print(f"Alphabets (Uppercase): {result['alphabets_uppercase']}")
                print(f"Special Characters: {result['special_characters']}")
                print(f"Sum of Numbers: {result['sum_of_numbers']}")
                print(f"Concatenated Alphabets (Reverse, Alternating): {result['concatenated_alphabets_reverse_alternating']}")
            else:
                print(f"❌ Error: {response.status_code}")
                print(f"Response: {response.text}")
                
        except requests.exceptions.ConnectionError:
            print("❌ Connection Error: Make sure the API server is running on http://localhost:5000")
            break
        except Exception as e:
            print(f"❌ Unexpected Error: {str(e)}")
    
    print("\n" + "=" * 50)
    print("🏁 Testing completed!")

def test_health_check():
    """Test the health check endpoint."""
    try:
        response = requests.get("http://localhost:5000/health")
        if response.status_code == 200:
            print("✅ Health check passed!")
            print(f"Response: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Health check failed: Server not running")

if __name__ == "__main__":
    print("🔍 Testing API Health Check...")
    test_health_check()
    
    print("\n🧪 Running API Tests...")
    test_api()
