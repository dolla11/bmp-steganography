def check_bmp_file():
    print("\n--- Check BMP File ---")
    filename = input("Enter BMP filename: ").strip()
    import os

    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return

    size = os.path.getsize(filename)
    print(f"File size: {size} bytes")

    with open(filename, 'rb') as f:
        header = f.read(2)

    if header == b'BM':
        print("Valid BMP file.")
        if size >= 54:
            capacity = (size - 54) // 8
            print(f"Approx. max message length: {capacity} characters")
    else:
        print("Not a valid BMP file.")
