import re

def check_password_strength():
    print("--- Simple Password Strength Checker ---")
    password = input("Enter a password to test: ")
    
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make it at least 8 characters long.")
        
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")
        
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")
        
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")
        
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")
        
    print(f"\nStrength Score: {score}/5")
    if score == 5:
        print("Great Password!")
    else:
        print("Status: Weak Password. Suggestions:")
        for tip in feedback:
            print(f"- {tip}")

if __name__ == "__main__":
    check_password_strength()
