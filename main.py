from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

to_learn = pandas.DataFrame.to_dict(data, orient="records")
current_card = {}


# --------------- Remove correct word --------------- #
def remove_word():
    to_learn.remove(current_card)
    learn_data = pandas.DataFrame(to_learn)
    learn_data.to_csv("./data/words_to_learn.csv", index=False)
    random_word()


# --------------- Random word Display --------------- #
def random_word():
    global current_card, card_flip
    window.after_cancel(card_flip)
    current_card = random.choice(to_learn)
    random_french_word = current_card["French"]
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{random_french_word}", fill="black")
    card_flip = window.after(3000, show_english_translation)


# --------------- Show English translation ------------ #
def show_english_translation():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{current_card['English']}", fill="white")


# ----------------------- UI Set-Up ------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

card_flip = window.after(3000, show_english_translation)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
title_text = canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Button
right_btn_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_btn_img, highlightthickness=0, command=remove_word)
right_btn.grid(row=1, column=0)

wrong_btn_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, command=random_word)
wrong_btn.grid(row=1, column=1)

random_word()

window.mainloop()
