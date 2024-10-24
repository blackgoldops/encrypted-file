from cryptography.fernet import Fernet
import os

# Display function
def display_encrypt_menu():
    print("=====================")
    print("  File Encryption Program  ")
    print("=====================")
    print("a) Close program")
    print("b) Encrypt a file")
    print("=====================")

# Function to generate a key and save it
def generate_key():
    return Fernet.generate_key()

# Function to encrypt the file
def encrypt_file(file_name, key):
    # Create a Fernet object using the key
    cipher_suite = Fernet(key)

    # Read the original file
    with open(file_name, 'rb') as file:
        original_file = file.read()

    # Encrypt the file content
    encrypted_file = cipher_suite.encrypt(original_file)

    # Save the encrypted file
    encrypted_file_name = f'encrypted_{file_name}'
    with open(encrypted_file_name, 'wb') as enc_file:
        enc_file.write(encrypted_file)

    print(f"File '{file_name}' has been encrypted and saved as '{encrypted_file_name}'.")
    return key.decode()

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
            
            # Generate encryption key
            key = generate_key()

            # Encrypt the file
            encrypt_file(file_name, key)

            # Display encryption key (this would normally be securely stored)
            print(f"Encryption Key: {key.decode()} (Save this key to decrypt the file later!)")
        else:
            print("Invalid option, please choose 'a' or 'b'.")

if __name__ == "__main__":
    main()
