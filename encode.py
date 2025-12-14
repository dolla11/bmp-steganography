def hide_message():
    print("\n--- Hide Message (Encode) ---")
    bmp_file = input("Enter BMP filename: ").strip()
    output_file = input("Enter output filename: ").strip()
    message = input("Enter secret message: ").strip()

    if not message:
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

    start = 54
    if start + len(bits) > len(data):
        print("Error: Image too small for this message.")
        return

    for i, bit in enumerate(bits):
        data[start + i] = (data[start + i] & 0xFE) | bit

    with open(output_file, 'wb') as f:
        f.write(data)

    print(f"Message hidden in '{output_file}' successfully!")
