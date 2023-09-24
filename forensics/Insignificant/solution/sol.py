from PIL import Image

#Extract flag using LSB manipulation
def extract_flag(image_path):
    img = Image.open(image_path)

    #Extract message bits from image
    binary_message = ""
    for x in range(img.width):
        for y in range(img.height):
            # Get the pixel value (R,G,B)
            pixel = img.getpixel((x, y))

            #Extract LSB from each pixel value
            for i in range(3):  # For each RGB channel
                bit = pixel[i] & 1
                binary_message += str(bit)

    #Convert binary message to text
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))

    print("Hidden:", message)

extract_flag("chall.png")