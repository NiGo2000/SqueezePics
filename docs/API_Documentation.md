# SqueezePics API Documentation
The SqueezePics API is an image processing engine that helps reduce the storage and bandwidth needs of every application. It allows clients to easily compress JPEG and PNG images without sacrificing image quality.

## Endpoints
### Compress Image
Compress an image file.

#### Request
+ Method: `POST`
+ URL: `https://api.squeezepics.com/compress`
+ Headers:
	+ `Content-Type`: `multipart/form-data`
+ Body:
	+ `image`: The image file to be compressed. Supported formats are `png` and `jpeg`

#### Response
+ Status Code: `200 OK`
+ Body:
	+ `content`: The compressed image file.

### Error Codes

The SqueezePics API returns the following error codes:

+ `400 Bad Request`: The request is malformed or missing required parameters.
+ `415 Unsupported Media Type`: The request contains an unsupported file format.
+ `500 Internal Server Error`: An unexpected error occurred on the server.

### Error Messages
The SqueezePics API returns error messages in the following format:
```json
{
    "error": "error message"
}
```

## Error Messages
```go
import requests

url = "https://api.squeezepics.com/compress"

image_file = open("example.jpg", "rb")

response = requests.post(url, files={"image": image_file})

if response.status_code == 200:
    compressed_image = response.content
else:
    error = response.json()["error"]
    print("Error:", error)
```






