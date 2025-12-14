from encode import hide_message
from decode import find_message
from check import check_bmp_file

def main():
    while True:
        print("\n=== BMP Steganography ===")
        print("1. Hide message (encode)")
        print("2. Find message (decode)")
        print("3. Check BMP file")
        print("4. Exit")

        choice = input("Choose 1-4: ").strip()
        if choice == "1":
            hide_message()
        elif choice == "2":
            find_message()
        elif choice == "3":
            check_bmp_file()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
