import time
import tkinter as tk
from PIL import Image, ImageTk
import pygetwindow as gw

image_path = 'fot.jpg'

def minimize_all_windows():
    windows = gw.getAllWindows()
    for window in windows:
        window.minimize()

def show_image():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='black')

    img = Image.open(image_path)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    img = img.resize((screen_width, screen_height), Image.LANCZOS)  
    photo = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=photo)
    label.pack()

    root.after(120000, root.destroy) 
    root.mainloop()

def main():
    print("Ожидание 40 секунд...")
    time.sleep(40) 
    
    print("Сворачиваем все окна...")
    minimize_all_windows() 

    print("Отображаем изображение...")
  
    show_image()

if __name__ == "__main__":
    main()
