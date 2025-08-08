from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")


def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")


def main():
    print("Image Encryption/Decryption Tool")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").strip().upper()
    input_path = input("Enter input image path: ")
    output_path = input("Enter output image path: ")
    key = int(input("Enter encryption key (integer): "))

    if choice == 'E':
        encrypt_image(input_path, output_path, key)
    elif choice == 'D':
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice. Please select 'E' or 'D'.")


if __name__ == "__main__":
    main()
