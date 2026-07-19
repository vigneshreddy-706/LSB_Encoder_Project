from PIL import Image

# Open image
image = Image.open("sample.png")

# Convert RGBA to RGB
image = image.convert("RGB")

print("Image loaded successfully!")

# Image size
width, height = image.size


print("Width :", width)
print("Height :", height)

# First pixel
pixel = image.getpixel((0, 0))
print(pixel)

# Secret message
secret_message = input("Enter the secret message: ")
secret_message += "#####"
# Convert message to binary
binary_message = ""

for char in secret_message:
    binary_message += format(ord(char), "08b")
# Check if message fits in image
if len(binary_message) > width * height:
    print("Error: Message is too large for this image!")
    exit()
print("Binary Message :", binary_message)

# Load pixels
pixels = image.load()

data_index = 0

# Hide message in image
for y in range(height):
    for x in range(width):

        if data_index >= len(binary_message):
            break

        r, g, b = pixels[x, y]

        # Change only the last bit of Red channel
        r = (r & 254) | int(binary_message[data_index])

        pixels[x, y] = (r, g, b)

        data_index += 1

    if data_index >= len(binary_message):
        break

# Save encoded image
image.save("encoded_image.png")

print("Message hidden successfully!")
print("Encoded image saved as encoded_image.png")