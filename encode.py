def hide_message():
    print("\n--- Hide Message (Encode) ---")
    bmp_file = input("Enter BMP filename: ")
    output_file = input("Enter output filename: ")
    message = input("Enter secret message: ")

    if len(message) == 0:
        print("Error: Message cannot be empty.")
        return

    message += '\0'  

    try:
        with open(bmp_file, 'rb') as f:
            data = bytearray(f.read())
    except FileNotFoundError:
        print(f"Error: File '{bmp_file}' not found.")
        return

    if data[0:2] != b'BM':
        print("Error: Not a valid BMP file.")
        return

    bits = []
    for char in message:
        val = ord(char)
        for i in range(8):
            bits.append((val >> i) & 1)

    bmp_header = 54
    if bmp_header + len(bits) > len(data):
        print("Error: Image too small for this message.")
        return

    for i, bit in enumerate(bits):
        data[bmp_header + i] = (data[bmp_header + i] & 254) | bit

    with open(output_file, 'wb') as f:
        f.write(data)

    print(f"Message hidden in '{output_file}' successfully!")
