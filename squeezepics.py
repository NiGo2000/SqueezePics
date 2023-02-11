from flask import Flask, request
import numpy as np
import cv2

app = Flask(__name__)

@app.route("/compress_image", methods=["POST"])
def compress_image():
    # Get the image data from the client
    image_data = request.files.get("image")

    # Read the image data as a numpy array
    image = cv2.imdecode(np.frombuffer(image_data.read(), np.uint8), cv2.IMREAD_UNCHANGED)

    # Get the format and quality parameters from the client
    format = request.form.get("format")
    quality = request.form.get("quality")

    # Check if a format parameter was provided
    if format:
        format = format.lower()

        # Check if the format is JPEG
        if format == "jpeg":
            # Check if a quality parameter was provided
            if quality:
                quality = int(quality)

                # Compress the image using the provided quality
                result, image = cv2.imencode(".jpg", image, [cv2.IMWRITE_JPEG_QUALITY, quality])
            else:
                # Compress the image with default quality
                result, image = cv2.imencode(".jpg", image)
        elif format == "png":
            # Check if a quality parameter was provided
            if quality:
                quality = int(quality)

                # Compress the image using the provided quality
                result, image = cv2.imencode(".png", image, [cv2.IMWRITE_PNG_COMPRESSION, quality])
            else:
                # Compress the image with default quality
                result, image = cv2.imencode(".png", image)
        else:
            # Return an error to the client
            return "Error: Unsupported format", 400
    else:
        # Return an error to the client
        return "Error: Format parameter is required", 400

    # Check if the compression was successful
    if result:
        # Return the compressed image to the client
        return image.tobytes(), 200, {"Content-Type": "image/" + format}
    else:
        # Return an error to the client
        return "Error: Failed to compress image", 500

if __name__ == '__main__':
    app.run(debug=True)
