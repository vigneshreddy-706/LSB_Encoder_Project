from PIL import Image

# Open encoded image
image = Image.open("encoded_image.png")
image = image.convert("RGB")

print("Encoded image loaded successfully!")

width, height = image.size

print("Width :", width)
print("Height :", height)

pixels = image.load()

binary_message = ""

for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y]

        # Read the last bit of Red channel
        binary_message += str(r & 1)

print("Binary Data Extracted!")
print(binary_message[:100])
# Convert binary to text
decoded_message = ""

for i in range(0, len(binary_message), 8):
    byte = binary_message[i:i+8]

    if len(byte) < 8:
        break

    decoded_message += chr(int(byte, 2))

# Stop at End Marker
decoded_message = decoded_message.split("#####")[0]

print("\nDecoded Message:")
print(decoded_message)