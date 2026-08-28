from cryptography.fernet import Fernet

try:
    # 1. Load the secret key
    with open("secret.key", "rb") as key_file:
        key = key_file.read()

    f = Fernet(key)

    # 2. Read the encrypted file data
    with open("data.txt", "rb") as file:
        encrypted_data = file.read()

    # 3. Decrypt the data
    decrypted_data = f.decrypt(encrypted_data)

    # 4. Write the original data back to the file
    with open("data.txt", "wb") as file:
        file.write(decrypted_data)

    print("File 'data.txt' successfully decrypted.")

except FileNotFoundError:
    print("Error: Required file ('data.txt' or 'secret.key') was not found.")
except Exception as e:
    print(f"Decryption failed: {e}")