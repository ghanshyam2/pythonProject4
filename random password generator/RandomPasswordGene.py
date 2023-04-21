from tkinter import *
import string
import random
import pyperclip


def generator():
    Lower_Case_Alphabets = string.ascii_lowercase
    Upper_Case_Alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all = Lower_Case_Alphabets + Upper_Case_Alphabets + numbers + special_characters
    password_length = int(length_Box.get())

    if choice.get() == 1:
        passwordField.insert(0, random.sample(Lower_Case_Alphabets, password_length))

    if choice.get() == 2:
        passwordField.insert(0, random.sample(Lower_Case_Alphabets + Upper_Case_Alphabets, password_length))

    if choice.get() == 3:
        passwordField.insert(0, random.sample(all, password_length))


def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)


root = Tk()
root.config(bg='olive')
choice = IntVar()
Font = ('arial', 30, 'bold')

passwordLabel = Label(root, text='Random Password Generator', font=('BOSTON', 30, 'italic', 'bold'), bg='white',
                      fg='black')
passwordLabel.grid(pady=10)

weakradioButton = Radiobutton(root, text='Weak Password', value=1, variable=choice,
                              font=('arial', 20, 'italic', 'bold'), fg='purple')
weakradioButton.grid(pady=10)

mediumradioButton = Radiobutton(root, text='Medium Password', value=2, variable=choice,
                                font=('arial', 20, 'italic', 'bold'), fg='blue')
mediumradioButton.grid(pady=10)

strongradioButton = Radiobutton(root, text='Strong Password', value=3, variable=choice,
                                font=('arial', 20, 'italic', 'bold'), fg='red')
strongradioButton.grid(pady=10)

lengthLabel = Label(root, text='Password Length: ', font=Font, bg='olive', fg='black')
lengthLabel.grid(pady=10)

length_Box = Spinbox(root, from_=5, to_=30, width=5, font=Font)
length_Box.grid(pady=10)

generateButton = Button(root, text='Generate New Password', font=Font, command=generator)
generateButton.grid(pady=10)

passwordField = Entry(root, width=30, bd=2, font=Font)
passwordField.grid()

copyButton = Button(root, text='Copy', font=Font, command=copy)
copyButton.grid(pady=10)

print("Made with Love from Ghanshyam")
root.mainloop()
