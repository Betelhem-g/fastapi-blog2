import requests
import time
import sys

BASE_URL = "http://localhost:8000"

def wait_for_server(max_attempts=10):
    print("🔍 Checking if server is running...")
    
    for attempt in range(max_attempts):
        try:
            response = requests.get(f"{BASE_URL}/", timeout=2)
            if response.status_code == 200:
                print("✅ Server is ready!")
                return True
        except requests.exceptions.RequestException:
            if attempt < max_attempts - 1:
                print(f"⏳ Waiting for server... (attempt {attempt + 1}/{max_attempts})")
                time.sleep(2)
            else:
                print("❌ Server is not responding!")
                return False
    return False

def test_api():
    print("🧪 Testing Blog API...")
    
    if not wait_for_server():
        sys.exit(1)
    
    try:
        # Test registration
        print("\n1️⃣ Testing user registration...")
        register_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword123",
            "full_name": "Test User"
        }
        
        response = requests.post(f"{BASE_URL}/auth/register", json=register_data)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            print("   ✅ Registration successful!")
        elif response.status_code == 400:
            print("   ⚠️  User might already exist, continuing...")
        
        # Test login
        print("\n2️⃣ Testing user login...")
        login_data = {"username": "testuser", "password": "testpassword123"}
        
        response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data["access_token"]
            print("   ✅ Login successful!")
            
            headers = {"Authorization": f"Bearer {access_token}"}
            
            # Test creating a blog post
            print("\n3️⃣ Testing blog post creation...")
            post_data = {
                "title": "My First Blog Post",
                "content": "This is my first blog post content!"
            }
            
            response = requests.post(f"{BASE_URL}/posts", json=post_data, headers=headers)
            if response.status_code == 200:
                print("   ✅ Post created successfully!")
                print("\n🎉 All tests completed successfully!")
            else:
                print(f"   ❌ Post creation failed: {response.text}")
        else:
            print(f"   ❌ Login failed: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_api()