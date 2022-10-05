from tkinter import *
import random
import time


def brosok():
    x = random.choice(['картинки для игры/b.png',
                       'картинки для игры/b2.png',
                       'картинки для игры/b3.png',
                       'картинки для игры/b4.png',
                       'картинки для игры/b5.png',
                       'картинки для игры/b6.png'])

    return x


def img(event):
    global b1, b2
    for i in range(10):
        b1 = PhotoImage(file=(brosok()))
        b2 = PhotoImage(file=(brosok()))
        lab1['image'] = b1
        lab2['image'] = b2
        root.update()
        time.sleep(0.07)


root = Tk()

# Размер приложения
root.geometry('400x200')

# Название приложения
root.title('Игра в кости. сделай бросок!')

# Самостоятельное растягивание окна FALSE
root.resizable(height=False, width=False)

# Иконка приложения
root.iconphoto(True, PhotoImage(file=('картинки для игры/iconka.png')))

# Бэкграунд
font = PhotoImage(file=('картинки для игры/holst.png'))
Label(root, image=font).pack()

lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)

lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)

root.bind('<1>', img)

# Запуск приложения
root.mainloop()
