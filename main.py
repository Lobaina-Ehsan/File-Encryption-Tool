from crypto_utils import encrypt_file, decrypt_file

def main():
    print("🔐 File Encryption Tool")
    print("1. Encrypt File")
    print("2. Decrypt File")

    choice = input("Choose (1/2): ").strip()

    if choice == "1":
        file_path = input("Enter file path: ").strip()
        password = input("Enter password: ").strip()

        output = encrypt_file(file_path, password)
        print(f"✅ File encrypted successfully: {output}")

    elif choice == "2":
        file_path = input("Enter encrypted file path: ").strip()
        password = input("Enter password: ").strip()

        output = decrypt_file(file_path, password)
        print(f"✅ File decrypted successfully: {output}")

    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
