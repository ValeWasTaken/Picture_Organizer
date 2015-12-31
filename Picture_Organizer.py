# Picture Organizer - Version 1.0
# Python 3.4
import os
import tkinter as tk
from tkinter import Frame, Button
from PIL import Image, ImageTk
from send2trash import send2trash
import random

tk_root = tk.Tk()
tk_root.title("Picture Organizer")
file_count = 0
p = path = 'C:\\Users\\EXAMPLE_USERNAME\\Desktop\\Test\\'


def search(directory):
    global file_count
    excludes = ['Yes', 'Maybe', 'Skipped', 'Delete']
    for root, subdirs, files in os.walk(directory, topdown=True):
        subdirs[:] = [d for d in subdirs if d not in excludes]
        for file in files:
            if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
                img = os.path.join(root, file)
                file_count += 1
                yield img


def next_image():
    try:
        global photo_path
        photo_path = next(path_generator)
        photo = ImageTk.PhotoImage(Image.open(photo_path))
        picture.configure(image=photo)
        picture.image = photo
    except StopIteration:
        picture.configure(image='', text='All done!')


def move_file(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    r = str(random.randrange(1,999999)) # To make sure no same file names.
    new_file = directory + 'Picture_{0}-{1}.jpg'.format(file_count, r)
    os.rename(photo_path, new_file)


def yes():
    move_file(path + 'Yes\\')
    next_image()


def maybe():
    move_file(path + 'Maybe\\')
    next_image()


def skip():
    move_file(path + 'Skipped\\')
    next_image()


def delete():
    move_file(path + 'Delete\\')
    next_image()

top_frame = Frame(tk_root)
bottom_frame = Frame(tk_root)
top_frame.pack(side='top')
bottom_frame.pack(side='bottom')

path_generator = search(p)
photo_path = next(path_generator)

photo = ImageTk.PhotoImage(Image.open(photo_path))
picture = tk.Label(tk_root, image=photo)
picture.image = photo
picture.pack(side='top')

button_yes = Button(top_frame, text="Yes", command=yes)
button_maybe = Button(top_frame, text="Maybe", command=maybe)
button_skip = Button(top_frame, text="skip", command=skip)
button_delete = Button(bottom_frame, text="Delete", command=delete)

button_yes.pack(side='left')
button_maybe.pack(side='left')
button_skip.pack(side='left')
button_delete.pack(side='bottom')

tk_root.mainloop()
