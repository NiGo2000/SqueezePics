import unittest
from PIL import Image
from squeezepics import SqueezePics

class TestSqueezePics(unittest.TestCase):
    def test_compress_image(self):
        image = Image.open("test_image.jpg")
        compressor = SqueezePics()
        compressed_image = compressor.compress_image(image)
        
        self.assertEqual(image.size, compressed_image.size)
        self.assertLess(compressed_image.format, image.format)

    def test_compress_png_image(self):
        image = Image.open("test_image.png")
        compressor = SqueezePics()
        compressed_image = compressor.compress_image(image)
        
        self.assertEqual(image.size, compressed_image.size)
        self.assertLess(compressed_image.format, image.format)

if __name__ == '__main__':
    unittest.main()
