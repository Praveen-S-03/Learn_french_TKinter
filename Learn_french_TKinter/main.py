import tkinter
import random
import pandas
#-----------------Data Frame-----------------#
current_card={}
data={}
try:
    sheet = pandas.read_csv("data/things_to_learn.csv")
except FileNotFoundError:
    original_data =pandas.read_csv("data/french_words.csv")
    data=original_data.to_dict(orient="records")
else:
    data = sheet.to_dict(orient="records")

#-----------------functions------------#
def is_known():
    data.remove(current_card)
    next_card()
    second_data =pandas.DataFrame(data)
    second_data.to_csv("data/things_to_learn.csv",index=False)
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    canvas.itemconfig(canvas_title,text="French",fill="black")
    canvas.itemconfig(canvas_text,text=current_card["French"],fill="black")
    canvas.itemconfig(card_image,image=card_front)
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_title, text="English",fill="white")
    canvas.itemconfig(canvas_text, text=current_card["English"],fill="white")
    canvas.itemconfig(card_image, image=card_back)

#----------Setting up the UI ------------------#
BACKGROUND_COLOR = "#B1DDC6"
window = tkinter.Tk()
window.title("Flashy")
window.config(pady=50,padx=50,background=BACKGROUND_COLOR)
flip_timer=window.after(3000, func=flip_card)
canvas = tkinter.Canvas(width=800,height=526)


#-------------------images------------#
card_back=tkinter.PhotoImage(file="images/card_back.png")
card_front =tkinter.PhotoImage(file="images/card_front.png")
right = tkinter.PhotoImage(file="images/right.png")
wrong = tkinter.PhotoImage(file="images/wrong.png")
card_image = canvas.create_image(400,263,image=card_front)
canvas.config(background=BACKGROUND_COLOR , highlightthickness=0)
canvas_title = canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
canvas_text = canvas.create_text(400,263,text="Word",font=("Arial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

#-------------button--------------#
right_button =tkinter.Button(image=right,highlightthickness=0,background=BACKGROUND_COLOR,command=is_known)
right_button.grid(row=1,column=0,padx=50,pady=50)
wrong_button = tkinter.Button(image=wrong,highlightthickness=0,background=BACKGROUND_COLOR,command=next_card)
wrong_button.grid(row=1,column=1,padx=50,pady=50)

next_card()

window.mainloop()
