from cryptography.fernet import Fernet
import itertools
import os

# Display function
def display():
    print("=====================")
    print("  Brute Force Program  ")
    print("=====================")
    print("a) Close program")
    print("b) Start brute force")
    print("=====================")

# Function to load the encrypted file
def load_encrypted_file(filename):
    with open(filename, 'rb') as file:
        return file.read()

# Function to attempt decryption with a key
def attempt_decrypt(encrypted_data, key):
    try:
        # Create a Fernet cipher using the provided key
        cipher_suite = Fernet(key)
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        return decrypted_data
    except Exception:
        return None  # Return None if decryption fails

# Function to brute-force keys
def brute_force_decryption(encrypted_data, max_attempts):
    for _ in range(max_attempts):
        # Generate a random key for brute force
        key = Fernet.generate_key()
        decrypted_data = attempt_decrypt(encrypted_data, key)
        if decrypted_data is not None:
            print(f"[+] Correct Key Found: {key.decode()}")
            print(f"Decrypted data:\n{decrypted_data.decode()}")
            return True
    print("[-] No correct key found within the attempt limit.")
    return False

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

            encrypted_data = load_encrypted_file(file_name)
            max_attempts = int(input("Enter the maximum number of brute-force attempts: "))

            print("Starting brute force...")
            brute_force_decryption(encrypted_data, max_attempts)
        else:
            print("Invalid option, please choose 'a' or 'b'.")

if __name__ == "__main__":
    main()
