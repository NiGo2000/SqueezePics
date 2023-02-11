import requests

url = "http://localhost:5000/compress_image"

image_file = open("image.jpg", "rb")

files = {"image": image_file}

# Provide the format parameter
data = {"format": "jpeg"}

response = requests.post(url, files=files, data=data)

# Check if the response status code is 200 (success)
if response.status_code == 200:
    # Save the returned image
    with open("compressed_image.jpeg", "wb") as f:
        f.write(response.content)
else:
    print("Error:", response.content)


