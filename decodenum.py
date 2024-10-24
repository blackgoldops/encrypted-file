from cryptography.fernet import Fernet
import os
import base64
import hashlib

# Display function
def display():
    print("=====================")
    print("  File Decryption Program  ")
    print("=====================")
    print("a) Close program")
    print("b) Decrypt a file")
    print("=====================")

# Function to create a Fernet key from a numeric password
def generate_key_from_password(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

# Function to load the encrypted file
def load_encrypted_file(filename):
    with open(filename, 'rb') as file:
        return file.read()

# Function to attempt decryption
def attempt_decrypt(encrypted_data, password):
    try:
        cipher_suite = Fernet(generate_key_from_password(password))
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        return decrypted_data
    except Exception:
        return None  # Return None if decryption fails

# Function to decrypt the file
def decrypt_file(file_name, password):
    encrypted_data = load_encrypted_file(file_name)
    decrypted_data = attempt_decrypt(encrypted_data, password)
    
    if decrypted_data is not None:
        decrypted_file_name = f'decrypted_{file_name[10:]}'  # Remove 'encrypted_' prefix
        with open(decrypted_file_name, 'wb') as dec_file:
            dec_file.write(decrypted_data)
        print(f"File '{file_name}' has been decrypted and saved as '{decrypted_file_name}'.")
    else:
        print("[-] Decryption failed. Invalid password.")

# Main function to handle UI and decryption
def main():
    while True:
        display()
        choice = input("Select an option (a/b): ").lower()
        if choice == 'a':
            print("Exiting program...")
            break
        elif choice == 'b':
            file_name = input("Enter the name of the encrypted file (with extension): ")
            if not os.path.exists(file_name):
                print(f"File '{file_name}' not found.")
                continue

            password = input("Enter the numeric password to decrypt the file: ")
            if not password.isdigit():
                print("Please enter a valid numeric password.")
                continue

            decrypt_file(file_name, password)
        else:
            print("Invalid option, please choose 'a' or 'b'.")

if __name__ == "__main__":
    main()
