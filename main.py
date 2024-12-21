from handlers.image_handler import ImageHandler
from handlers.image_processor import ImageProcessor


def main_menu():
    print("\n--- Меню работы с изображением ---")
    print("1. Повернуть изображение на 90 градусов")
    print("2. Обрезать изображение до 150x150")
    print("3. Применить чёрно-белый фильтр")
    print("4. Добавить текст 'Вариант 2'")
    print("5. Сохранить изображение")
    print("6. Показать изображение")
    print("7. Выход")
    return input("Выберите действие: ")

if __name__ == "__main__":
    handler = ImageHandler("image_5.jpg")
    handler.load_image()

    processor = ImageProcessor(handler.get_image())

    while True:
        choice = main_menu()

        if choice == "1":
            handler.rotate_image()
            processor = ImageProcessor(handler.get_image())

        elif choice == "2":
            handler.crop_image()
            processor = ImageProcessor(handler.get_image())

        elif choice == "3":
            processor.apply_black_and_white_filter()

        elif choice == "4":
            processor.add_text("Вариант 2", position=(10, 10))

        elif choice == "5":
            save_path = input("Введите путь для сохранения изображения: ")
            if processor.get_processed_image():
                processor.get_processed_image().save(save_path)
                print(f"Изображение сохранено: {save_path}")
            else:
                print("Нет обработанного изображения для сохранения.")

        elif choice == "6":
            if processor.get_processed_image():
                processor.get_processed_image().show()
            elif handler.get_image():
                handler.get_image().show()
            else:
                print("Изображение не загружено.")

        elif choice == "7":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")