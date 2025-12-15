def find_message():
    print("\n--- Find Hidden Message (Decode) ---")
    bmp_file = input("Enter BMP filename: ")

    try:
        with open(bmp_file, 'rb') as f:
            data = bytearray(f.read())
    except FileNotFoundError:
        print(f"Error: File '{bmp_file}' not found.")
        return

    if data[0:2] != b'BM':
        print("Error: Not a valid BMP file.")
        return

    bmp_header = 54
    message = ""
    bits_collected = 0
    current_char = 0

    for i in range(bmp_header, len(data)):
        current_char |= (data[i] & 1) << bits_collected
        bits_collected += 1

        if bits_collected == 8:
            if current_char == 0:
                break
            message += chr(current_char)
            current_char = 0
            bits_collected = 0

    if message:
        print(f"Hidden message: {message}")
    else:
        print("No hidden message found.")
