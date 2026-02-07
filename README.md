# GitHub Test Repository

This repository contains **intentionally vulnerable code** for testing the SecureCodeAI agent.

## Files

- `api.py` - Flask API with SQL Injection vulnerabilities
- `users.py` - User management with Command Injection vulnerabilities

## ⚠️ WARNING

**DO NOT use this code in production!** These files contain security vulnerabilities for testing purposes only.

## How to Test

1. The SecureCodeAI agent will scan this repository
2. It will find the vulnerabilities
3. It will generate patches
4. You approve or reject the patches

## Expected Vulnerabilities

- SQL Injection (CWE-89)
- Command Injection (CWE-78)  
- Path Traversal (CWE-22)
- Hardcoded Secrets (CWE-798)
