# SqueezePics API
The SqueezePics API is designed to help reduce the storage and bandwidth requirements of image-intensive applications. The main motive of this API is to provide an easy-to-use tool for compressing images in a way that balances the tradeoff between file size and image quality. This can be especially useful in scenarios where storage space or bandwidth are limited, such as mobile or web applications.

The API can help your projects in several ways:

Reduce storage costs: By compressing images, you can significantly reduce the storage requirements of your application, which can help you save on storage costs.

Faster load times: Compressed images are smaller in size and require less bandwidth to transfer, which can result in faster page load times for your users.

Improved user experience: Faster page load times and reduced storage requirements can result in a better user experience for your users, particularly for those with limited internet connections.

Easy integration: The SqueezePics API is designed to be easy to integrate into your existing applications, with a simple interface for compressing images. This can help save time and reduce the development effort required to implement image compression in your applications.

The API can be specifically helpful in the following scenarios:

Mobile applications: Mobile devices often have limited storage space and limited internet connectivity, making image compression an important consideration for mobile developers.

Web applications: Web applications often involve a large number of images, which can result in slow page load times and increased storage requirements. The Image Compression API can help you reduce the file size of these images and improve the user experience of your web applications.

Image hosting and sharing services: Image hosting and sharing services often require a large amount of storage and bandwidth, making image compression an important consideration. By using the SqueezePics API, you can reduce the storage and bandwidth requirements of your image hosting and sharing services, which can help you save on costs and improve the user experience.

# Features

+ Supports both JPEG and PNG image formats
+ Minimal loss in image quality
+ Easy to use API

# Usage
To use the SqueezePics API, make a request to the API endpoint with the desired image file. The API will return the compressed image.

Example:

```python
import requests

url = "https://api.squeezepics.com/compress"

image_file = open("example.jpg", "rb")

response = requests.post(url, files={"image": image_file})

compressed_image = response.content
```

In this example, the requests library is used to make a POST request to the API endpoint with the desired image file. The compressed image is returned in the response.content variable.

# Requirements
The SqueezePics API requires the following packages:

+ Pillow
+ numpy

You can install these packages using the following command:

```python
pip install -r requirements.txt
```


