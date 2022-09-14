import requests

def main(username,password):
    us = username.replace("\"","\\\"")
    ps = password.replace("\"","\\\"")

    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "Content-Type": "application/json"
    }

    datam = {"returnSecureToken":"true","email":f"{us}","password":f"{ps}"}

    req = requests.post("https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyC8qsoEPOkRDlH3A5E9EqKpUiCxjLVPlho", json=datam, headers=headers)
    if "idToken" in req.text: return "Good Acct"
    elif "EMAIL_NOT_FOUND" or "INVALID_PASSWORD" or "INVALID_EMAIL" or "MISSING_PASSWORD" or "MISSING_EMAIL" or "TOO_MANY_ATTEMPTS_TRY_LATER" in req.text: return "Wrong Acct"
