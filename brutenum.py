from cryptography.fernet import Fernet
import itertools
import os
import base64
import hashlib

# Display function
def display():
    print("=====================")
    print("  Brute Force Program  ")
    print("=====================")
    print("a) Close program")
    print("b) Continue brute force")
    print("=====================")

# Function to load the encrypted file
def load_encrypted_file(filename):
    with open(filename, 'rb') as file:
        return file.read()

# Function to generate a Fernet key from a numeric password
def generate_key_from_password(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

# Function to attempt decryption
def attempt_decrypt(encrypted_data, password):
    try:
        # Create a Fernet cipher using the generated key from the password
        cipher_suite = Fernet(generate_key_from_password(password))
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        return decrypted_data
    except Exception:
        return None  # Return None if decryption fails

# Function to brute-force numeric passwords
def brute_force_numeric(encrypted_data, max_length):
    digits = '0123456789'

    for length in range(1, max_length + 1):
        for password_tuple in itertools.product(digits, repeat=length):
            password = ''.join(password_tuple)  # Join the tuple into a string
            decrypted_data = attempt_decrypt(encrypted_data, password)
            if decrypted_data is not None:
                print(f"[+] Password found: {password}")
                print(f"Decrypted data:\n{decrypted_data.decode()}")
                return
    print("[-] Password not found.")

# Main function
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

            encrypted_data = load_encrypted_file(file_name)
            max_length = int(input("Enter the maximum length of numeric passwords to try: "))
            print("Starting brute force...")
            brute_force_numeric(encrypted_data, max_length)
        else:
            print("Invalid option, please choose 'a' or 'b'.")

if __name__ == "__main__":
    main()
