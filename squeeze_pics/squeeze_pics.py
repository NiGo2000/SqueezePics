import os
import cv2

class SqueezePics:
    def __init__(self, input_path, output_path, compression_level=50):
        self.input_path = input_path
        self.output_path = output_path
        self.compression_level = compression_level

    def compress_image(self, image_path):
        image = cv2.imread(image_path)
        height, width, channels = image.shape
        compression_param = [cv2.IMWRITE_JPEG_QUALITY, self.compression_level]
        result, enc_img = cv2.imencode('.jpg', image, compression_param)
        return enc_img.tobytes()

    def compress_images(self):
        images = []
        for filename in os.listdir(self.input_path):
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                image_path = os.path.join(self.input_path, filename)
                image = self.compress_image(image_path)
                images.append(image)
                compressed_image_path = os.path.join(self.output_path, filename)
                with open(compressed_image_path, 'wb') as f:
                    f.write(image)
        return images