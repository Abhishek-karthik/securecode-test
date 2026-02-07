"""
User management with vulnerabilities
Upload this to GitHub to test the agent!
"""
import os
import subprocess

def create_user_directory(username):
    """VULNERABLE: Command Injection"""
    # VULNERABILITY: User input in os.system
    os.system(f"mkdir /users/{username}")

def backup_user_data(user_id):
    """VULNERABLE: Command Injection"""
    # VULNERABILITY: subprocess with shell=True
    subprocess.run(f"tar -czf backup_{user_id}.tar.gz /data/{user_id}", shell=True)

def get_user_files(username):
    """VULNERABLE: Path Traversal"""
    # VULNERABILITY: No validation of user input
    with open(f"/data/users/{username}/files.txt", "r") as f:
        return f.read()

class User:
    """Simple user class"""
    
    def __init__(self, username, password):
        self.username = username
        # VULNERABILITY: Storing password in plain text
        self.password = password
import os
api_key = os.environ.get('API_KEY')
