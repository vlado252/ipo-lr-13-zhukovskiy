from PIL import Image

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None

    def load_image(self):
        """Загружает изображение из указанного пути."""
        try:
            self.image = Image.open(self.image_path)
            print(f"Изображение загружено: {self.image_path}")
        except Exception as e:
            print(f"Ошибка при загрузке изображения: {e}")

    def save_image(self, save_path):
        """Сохраняет текущее изображение по указанному пути."""
        if self.image:
            self.image.save(save_path)
            print(f"Изображение сохранено: {save_path}")
        else:
            print("Изображение не загружено, сохранение невозможно.")

    def rotate_image(self):
        """Поворачивает изображение на 90 градусов."""
        if self.image:
            self.image = self.image.rotate(90, expand=True)
            print("Изображение повернуто на 90 градусов.")
        else:
            print("Изображение не загружено, поворот невозможен.")

    def crop_image(self):
        """Обрезает изображение до размера 150x150 пикселей."""
        if self.image:
            self.image = self.image.crop((0, 0, 150, 150))
            print("Изображение обрезано до размера 150x150 пикселей.")
        else:
            print("Изображение не загружено, обрезка невозможна.")

    def get_image(self):
        """Возвращает текущее изображение."""
        return self.image