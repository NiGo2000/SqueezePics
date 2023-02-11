import unittest
import squeezepics

class TestSqueezePics(unittest.TestCase):
    def test_compress_image(self):
        # Test input image
        input_image = "test_image.jpg"

        # Compress the image using the SqueezePics API
        compressed_image = squeezepics.compress_image(input_image)

        # Check if the compressed image has been successfully generated
        self.assertIsNotNone(compressed_image)

    def test_compress_image_with_quality(self):
        # Test input image
        input_image = "test_image.jpg"

        # Compress the image using the SqueezePics API with a quality of 50
        compressed_image = squeezepics.compress_image(input_image, quality=50)

        # Check if the compressed image has been successfully generated
        self.assertIsNotNone(compressed_image)

    def test_compress_image_with_invalid_quality(self):
        # Test input image
        input_image = "test_image.jpg"

        # Try to compress the image with an invalid quality
        with self.assertRaises(ValueError):
            compressed_image = squeezepics.compress_image(input_image, quality=200)

if __name__ == '__main__':
    unittest.main()
