from cryptography.fernet import Fernet
import os
import base64
import hashlib

# Display function
def display_encrypt_menu():
    print("=====================")
    print("  File Encryption Program  ")
    print("=====================")
    print("a) Close program")
    print("b) Encrypt a file")
    print("=====================")

# Function to create a Fernet key from a numeric password
def generate_key_from_password(password):
    # Hash the password to get a valid Fernet key
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

# Function to encrypt the file
def encrypt_file(file_name, password):
    key = generate_key_from_password(password)  # Generate key from password
    cipher_suite = Fernet(key)

    with open(file_name, 'rb') as file:
        original_file = file.read()

    encrypted_file = cipher_suite.encrypt(original_file)

    encrypted_file_name = f'encrypted_{file_name}'
    with open(encrypted_file_name, 'wb') as enc_file:
        enc_file.write(encrypted_file)

    print(f"File '{file_name}' has been encrypted and saved as '{encrypted_file_name}'.")
    return key.decode()  # Return the key for reference, but not needed for decryption

# Main function to handle UI and encryption
def main():
    while True:
        display_encrypt_menu()
        choice = input("Select an option (a/b): ").lower()
        if choice == 'a':
            print("Exiting program...")
            break
        elif choice == 'b':
            file_name = input("Enter the name of the file to encrypt (with extension): ")
            if not os.path.exists(file_name):
                print(f"File '{file_name}' not found.")
                continue

            password = input("Enter a numeric password to encrypt the file: ")
            encrypt_file(file_name, password)
        else:
            print("Invalid option, please choose 'a' or 'b'.")

if __name__ == "__main__":
    main()
