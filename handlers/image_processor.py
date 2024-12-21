from PIL import ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def apply_black_and_white_filter(self):
        """Применяет чёрно-белый фильтр к изображению."""
        if self.image:
            self.image = self.image.convert('L')
            print("Чёрно-белый фильтр применён.")
        else:
            print("Изображение отсутствует, фильтр невозможен.")

    def add_text(self, text, position=(10, 10), font_size=20):
        """Добавляет текст на изображение."""
        if self.image:
            try:
                draw = ImageDraw.Draw(self.image)
                font = ImageFont.load_default()  # Используем шрифт по умолчанию
                draw.text(position, text, fill="white", font=font)
                print(f"Текст '{text}' добавлен на изображение.")
            except Exception as e:
                print(f"Ошибка при добавлении текста: {e}")
        else:
            print("Изображение отсутствует, добавление текста невозможно.")

    def get_processed_image(self):
        """Возвращает обработанное изображение."""
        return self.image