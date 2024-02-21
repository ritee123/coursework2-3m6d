from cryptography.fernet import Fernet
import json
from stegano import lsb
import pandas as pd

# Function to generate and return a new encryption key
def generate_key():
    return Fernet.generate_key()

# Function to encrypt a message using the provided key
def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message using the provided key
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Generate an encryption key (you should save this securely!)
key = generate_key()

image_path = "images/profileimg.png"
decoded_data = lsb.reveal(image_path)
decoded_data = json.loads(decoded_data)
new_data = decoded_data["users"]

print("NAME | CITIZENSHIP | PHONE | ADDRESS | EMAIL | ACCOUNT TYPE | ACCOUNT NUMBER | ENCRYPTED PIN")

for i in new_data:
    # Encrypt the PIN
    encrypted_pin = encrypt_message(str(i[7]), key)
    print(i[0], i[1], i[2], i[3], i[4], i[5], i[6], encrypted_pin)

# Example of decrypting a PIN (replace 'encrypted_pin' with an actual encrypted PIN from your output)
# decrypted_pin = decrypt_message(encrypted_pin, key)
# print("Decrypted PIN:", decrypted_pin)
