import os

def main():
    folder = input("Enter the target folder path: ").strip()

    if not os.path.isdir(folder):
        print(f"Error: '{folder}' is not a valid directory.")
        return

    try:
        count = int(input("Enter the number of groups to create: ").strip())
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if count < 1:
        print("Error: Number must be at least 1.")
        return

    for i in range(1, count + 1):
        group_path = os.path.join(folder, f"group{i}")
        os.makedirs(group_path, exist_ok=True)
        print(f"Created: {group_path}")

    print(f"\nDone. {count} group folder(s) created in '{folder}'.")

if __name__ == "__main__":
    main()
