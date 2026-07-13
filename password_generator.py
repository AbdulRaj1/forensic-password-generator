import random
import string

def generate_password(phrase, security):
    if security == "1":
        scrambled_phrase = ''.join(random.sample(phrase, len(phrase)))
        # This will be a simple password generator that uses the phrase and adds random characters
        password = scrambled_phrase + ''.join(random.choices(string.digits, k=6))
        return password
    elif security == "2":
        scrambled_phrase = ''.join(random.sample(phrase, len(phrase)))
        # This will be a more complex password generator that uses the phrase and adds random characters, numbers, and symbols
        password = scrambled_phrase + ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
        return password
    else:
        return "Invalid security level. Please choose 1 or 2."

phrase = input("Please enter a phrase: ")
security = input("Please enter a security level (1 or 2): ")

print("Generating password...")
print("Your password is: " + generate_password(phrase, security))
