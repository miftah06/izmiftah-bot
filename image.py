from PIL import Image

class ImageResizer:
    def __init__(self, path, width):
        self.path = path
        self.width = width
        self.height = self.calculate_height()

    def calculate_height(self):
        with Image.open(self.path) as img:
            original_width, original_height = img.size
            aspect_ratio = original_height / original_width
            return int(self.width * aspect_ratio)

    def resize_image(self):
        with Image.open(self.path) as img:
            resized_img = img.resize((self.width, self.height), Image.Resampling.LANCZOS)
            resized_img.save(f"foto.png")
            return resized_img

    def get_resized_dimensions(self):
        return self.width, self.height

# Contoh penggunaan:
image_path = 'temp.png'
resizer = ImageResizer(image_path, 7240)
resized_image = resizer.resize_image()
print(f"Gambar telah diresize ke ukuran: {resizer.get_resized_dimensions()}")
