"""
Simple Flask API with SQL Injection vulnerability
Upload this to GitHub to test the agent!
"""
from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    """VULNERABLE: SQL Injection in login"""
    username = request.form.get("username")
    password = request.form.get("password")
    
    # VULNERABILITY: String concatenation allows SQL injection
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(query)
    
    user = cursor.fetchone()
    if user:
        return {"message": "Login successful"}
    return {"message": "Login failed"}, 401

@app.route("/search")
def search():
    """VULNERABLE: SQL Injection in search"""
    term = request.args.get("q")
    
    # VULNERABILITY: Direct string formatting
    query = "SELECT * FROM products WHERE name LIKE '%" + term + "%'"
    
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute(query)
    
    return {"results": cursor.fetchall()}

if __name__ == "__main__":
    app.run(debug=True)
