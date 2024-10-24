from cryptography.fernet import Fernet
import os

# Display function for the decryption menu
def display_decrypt_menu():
    print("=====================")
    print("  File Decryption Program  ")
    print("=====================")
    print("a) Close program")
    print("b) Decrypt a file")
    print("=====================")

# Function to decrypt the file
def decrypt_file(file_name, key):
    try:
        # Create a Fernet object using the provided key
        cipher_suite = Fernet(key)

        # Read the encrypted file
        with open(file_name, 'rb') as enc_file:
            encrypted_data = enc_file.read()

        # Decrypt the file content
        decrypted_data = cipher_suite.decrypt(encrypted_data)

        # Save the decrypted content to a new file
        decrypted_file_name = f'decrypted_{file_name}'
        with open(decrypted_file_name, 'wb') as dec_file:
            dec_file.write(decrypted_data)

        print(f"File '{file_name}' has been decrypted and saved as '{decrypted_file_name}'.")
    except Exception as e:
        print(f"Decryption failed: {str(e)}")

# Main function to handle UI and decryption
def main():
    while True:
        display_decrypt_menu()
        choice = input("Select an option (a/b): ").lower()
        if choice == 'a':
            print("Exiting program...")
            break
        elif choice == 'b':
            file_name = input("Enter the name of the encrypted file: ")
            if not os.path.exists(file_name):
                print(f"File '{file_name}' not found.")
                continue

            key = input("Enter the encryption key: ")

            # Attempt to decrypt the file
            decrypt_file(file_name, key.encode())
        else:
            print("Invalid option, please choose 'a' or 'b'.")

if __name__ == "__main__":
    main()
