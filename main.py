from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img = img.convert('RGB')  # Ensure it's in RGB mode
    pixels = img.load()

    width, height = img.size

    # Step 1: Mathematical operation on each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    # Step 2: Swap horizontal pixels (simple encryption logic)
    for y in range(height):
        for x in range(0, width - 1, 2):
            pixels[x, y], pixels[x+1, y] = pixels[x+1, y], pixels[x, y]

    img.save(output_path)
    print(f"[+] Image encrypted and saved as '{output_path}'.")


def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img = img.convert('RGB')
    pixels = img.load()

    width, height = img.size

    # Step 1: Undo the pixel swapping
    for y in range(height):
        for x in range(0, width - 1, 2):
            pixels[x, y], pixels[x+1, y] = pixels[x+1, y], pixels[x, y]

    # Step 2: Reverse the mathematical operation
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    img.save(output_path)
    print(f"[+] Image decrypted and saved as '{output_path}'.")


# --- Example Usage ---

# Encrypt the image
encrypt_image("input.jpg", "encrypted_image.jpg", key=50)

# Decrypt the image
decrypt_image("encrypted_image.jpg", "decrypted_image.jpg", key=50)
