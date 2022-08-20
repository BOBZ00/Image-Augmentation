import tkinter
from tkinter import *
import tkinter.ttk as ttk
import augment
from tkinter.filedialog import askopenfilenames
from tkinter import filedialog


def read_file():
    # show an "Open" dialog box and return the path to the selected file
    filename = askopenfilenames()
    print(filename)
    return filename


def select_folder():
    path = filedialog.askdirectory()
    #Label(win, text=path, font=13).pack()
    return path


def run():
    paths = read_file()
    # browse=filename
    filename1 = "C:/Users/Ismail/Pictures/Output"
    #augmentation_type = box.get()
    number = int(numberofsamples_textfield.get('1.0', END))
    if (save.get() == 1):
        filename1 = select_folder()
    for path in paths:
        if scaling.get()==1:
            list1 = augment.scaler(path, number)
            if (save.get() == 1):
                augment.save(list1, filename1)
        if zooming.get()==1:
            list1 = augment.zoom(path, number)
            if (save.get() == 1):
                augment.save(list1, filename1)
        if translation.get()==1:
            list1 = augment.translate_img(path, number)
            if (save.get() == 1):
                augment.save(list1, filename1)
        if rotation.get()==1:
            list1 = augment.rotation(path, number)
            if (save.get() == 1):
                augment.save(list1, filename1)
        if cropping.get()==1:
            list1 = augment.cropping(path, number)
            if (save.get() == 1):
                augment.save(list1, filename1)
        if contrast.get()==1:
            list1 = augment.contrast(path, number)
            if (save.get() == 1):
                augment.save(list1, filename1)
        if brightning.get()==1:
            list1 = augment.brightness(path, number)
            if (save.get() == 1):
                augment.save(list1, filename1)
        if blurred.get()==1:
            list1 = augment.blur(path, number)
            if (save.get() == 1):
                augment.save(list1, filename1)

gui = Tk()
gui.title("Data Augmentation")
gui.geometry("700x700")
gui.configure(bg='gray')

TopLabel = Label(gui, text="Augmentation Generator", bg='gray', fg='black', font=("Arial", 20), justify=CENTER)
TopLabel.place(x=250, y=20)

# Augmentation type

# Label
Class2Label = Label(gui, text="Augmentation type", bg='gray', fg='black', font=("Arial", 12), justify=LEFT)
Class2Label.place(x=130, y=60)

#check box for each augmentation
scaling = IntVar()
Checkbutton(gui, text="scale", bg='gray', fg='black', font=("Arial", 12), justify=LEFT, variable=scaling).place(x=150, y=100)

zooming = IntVar()
Checkbutton(gui, text="zoom", bg='gray', fg='black', font=("Arial", 12), justify=LEFT, variable=zooming).place(x=150, y=130)

translation = IntVar()
Checkbutton(gui, text="translate", bg='gray', fg='black', font=("Arial", 12), justify=LEFT, variable=translation).place(x=150, y=160)

rotation = IntVar()
Checkbutton(gui, text="rotate", bg='gray', fg='black', font=("Arial", 12), justify=LEFT, variable=rotation).place(x=150, y=190)

cropping = IntVar()
Checkbutton(gui, text="crop", bg='gray', fg='black', font=("Arial", 12), justify=LEFT, variable=cropping).place(x=250, y=100)

contrast = IntVar()
Checkbutton(gui, text="contrast", bg='gray', fg='black', font=("Arial", 12), justify=LEFT, variable=contrast).place(x=250, y=130)

brightning = IntVar()
Checkbutton(gui, text="brightness", bg='gray', fg='black', font=("Arial", 12), justify=LEFT, variable=brightning).place(x=250, y=160)

blurred = IntVar()
Checkbutton(gui, text="blurriness", bg='gray', fg='black', font=("Arial", 12), justify=LEFT, variable=blurred).place(x=250, y=190)
#################################################################################################################################
# label for number of output samples
numberofsamples = Label(gui, text="Number of Samples", bg='gray', fg='black', font=("Arial", 12),justify=LEFT)
numberofsamples.place(x=170, y=250)

# textbox
numberofsamples_textfield = Text(gui, bg='white', fg='black', width=15, height=1)
numberofsamples_textfield.place(x=170, y=300)

# checkbox
save = IntVar()
Checkbutton(gui, text="Save", bg='gray', fg='black', font=("Arial", 18), justify=LEFT, variable=save).place(x=20, y=590)


# RUN
start = Button(gui, text="START", bg='black', fg='white', command=run)
start.place(x=600, y=600)

gui.mainloop()