from tkinter import *
import pandas
import random
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
GRADIENT_COLOR = "#98fb98"
Background_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv")
learn = data.to_dict(orient="records")
card = {}


# ------------------------------------Create New Flash Cards---------------------#
def french_words():
    global card
    global card_flip
    window.after_cancel(card_flip)
    card = random.choice(learn)
    canvas.itemconfig(title, text="French", fill="Black")
    canvas.itemconfig(word, text=card["French"], fill="Black")
    canvas.itemconfig(card_background, image=front_image)
    card_flip = window.after(3000, func=eng_words)


def eng_words():
    canvas.itemconfig(title, text="English", fill="RoyalBlue")
    canvas.itemconfig(word, text=card["English"], fill="RoyalBlue")
    canvas.itemconfig(card_background, image=back_image)


def speak():
    engine.say(card["French"])
    engine.runAndWait()


# ------------------------------------UI Setup--------------------------------#
# window
window = Tk()
window.title("French Flashy")
window.config(padx=30, pady=30, bg=GRADIENT_COLOR)
window.iconbitmap("images/icon.ico")
window.resizable(0, 0)
card_flip = window.after(3000, func=eng_words)

# Canvas Image
canvas = Canvas(width=800, height=526)
canvas.config(bg=GRADIENT_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_image)
title = canvas.create_text(400, 100, text="", font=("Book Antiqua", 40, "italic"))
word = canvas.create_text(400, 260, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=3)

# Buttons
right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, border=0, bg=GRADIENT_COLOR, command=french_words)
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, border=0, bg=GRADIENT_COLOR, command=french_words)
speak_button_image = PhotoImage(file="images/speaker.png")
speak_button = Button(image=speak_button_image, command=speak, highlightthickness=0, border=0)

speak_button.place(x=700, y=25)
right_button.grid(row=1, column=2)
wrong_button.grid(row=1, column=0)

french_words()

window.mainloop()
