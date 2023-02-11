# SqueezePics-
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

# Here is a tutorial for using the SqueezePics API:

1. Import the SqueezePics class:
from squeeze_pics import SqueezePics

2. Create an instance of the SqueezePics class:
api = SqueezePics(compression_level=75)

3. Call the compress_image method and pass in the input image path and the desired output path:
api.compress_image('input_image.jpg', 'compressed_image.jpg')

4. The compressed image will be saved to the specified output path.
Note that the compression_level parameter ranges from 0 to 100, with 100 being the highest quality and 0 being the lowest. The default value is 50, which provides a balance between compression and quality.

You can adjust the compression level to your desired level of compression and quality using SqueezePics. Keep in mind that the higher the compression level, the smaller the resulting image size, but the lower the quality of the image.






