import time
import tkinter as tk
from PIL import Image, ImageTk
import pygetwindow as gw

# Путь к изображению
image_path = 'fot.jpg'

# Функция для сворачивания всех окон
def minimize_all_windows():
    windows = gw.getAllWindows()
    for window in windows:
        window.minimize()

# Функция для отображения изображения на весь экран
def show_image():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='black')

    img = Image.open(image_path)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    img = img.resize((screen_width, screen_height), Image.LANCZOS)  # Используем LANCZOS вместо ANTIALIAS
    photo = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=photo)
    label.pack()

    # Закрытие окна через 2 минуты
    root.after(120000, root.destroy)  # 120000 ms = 2 минуты
    root.mainloop()

# Основная функция
def main():
    print("Ожидание 40 секунд...")
    time.sleep(40)  # Таймер перед началом отображения
    
    print("Сворачиваем все окна...")
    minimize_all_windows()  # Сворачиваем все окна

    print("Отображаем изображение...")
    # Показываем изображение
    show_image()

if __name__ == "__main__":
    main()
