from cryptography.fernet import Fernet

# 1. Generate a secure secret key and save it
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# 2. Load the key and initialize Fernet
f = Fernet(key)

# 3. Read the original file data
try:
    with open("data.txt", "rb") as file:
        original_data = file.read()

    # 4. Encrypt the data
    encrypted_data = f.encrypt(original_data)

    # 5. Write the encrypted data back to the file
    with open("data.txt", "wb") as file:
        file.write(encrypted_data)

    print("File 'data.txt' successfully encrypted.")

except FileNotFoundError:
    print("Error: 'data.txt' was not found.")