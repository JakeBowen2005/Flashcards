BACKGROUND_COLOR = "#B1DDC6"

import tkinter
import pandas
import random

#get words from file
d = pandas.read_csv("data/french_words.csv")
#make new words to learn file
learning_data = d.to_csv("data/words_to_learn.csv", index=False)
learning_words = pandas.read_csv("data/words_to_learn.csv")


french_words = d.to_dict(orient="records")
# print(french_words[random.randint(0,len(french_words))]["French"])
# print(random.choice(french_words))



#generate random words
def gen_words_green():
    global flip_timer, learning_words
    window.after_cancel(flip_timer)
    #delete the word from the words_to_learn file
# Remove the word from the DataFrame and save it to the CSV
    word = front_canvas.itemcget(card_word, "text")
    index = learning_words[learning_words["French"] == word].index
    learning_words = learning_words.drop(index)

# Save the updated DataFrame back to the CSV file
    learning_words.to_csv("data/words_to_learn.csv", index=False)
    

    new_word = french_words[random.randint(0,len(french_words)-1)]["French"]
    front_canvas.itemconfig(canvas_img, image=card_front)
    front_canvas.itemconfig(card_language, text="French", fill="Black")
    front_canvas.itemconfig(card_word, text=new_word, fill="Black")


    flip_timer = window.after(3000, func=flip_cards)

#flip the cards
def flip_cards():
    global current_img, card_front, card_back
    starting_word = front_canvas.itemcget(card_word, "text")
   
    if current_img == card_front:
        front_canvas.itemconfig(canvas_img, image=card_back)
        front_canvas.itemconfig(card_language, text="English", fill="White")
        for entry in french_words:
            if entry["French"] == starting_word:
                englishw = entry["English"]
        front_canvas.itemconfig(card_word, text=englishw, fill="White")


    


#set up webpage first
window = tkinter.Tk()
flip_timer = window.after(3000, func=flip_cards)
window.title("French Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

def green_click():
    print("Green button clicked!")

def red_click():
    print("Red button clicked!")

green_check = tkinter.PhotoImage(file="images/right.png")
green_button = tkinter.Button(image=green_check, command=gen_words_green, highlightthickness=0)
green_button.grid(row=1, column=1)

red_check = tkinter.PhotoImage(file="images/wrong.png")
red_button = tkinter.Button(image=red_check, highlightthickness=0)
red_button.grid(row=1, column=0)

card_front = tkinter.PhotoImage(file="images/card_front.png")
card_back = tkinter.PhotoImage(file="images/card_back.png")
current_img = card_front

front_canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_img = front_canvas.create_image(400,268, image=card_front)
front_canvas.grid(row=0,column=0, columnspan=2)
card_language = front_canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
card_word = front_canvas.create_text(400, 263, text=french_words[random.randint(0,len(french_words)-1)]["French"], font=("Arial", 60, "bold"))



window.mainloop()