from tkinter import *
from PIL import Image, ImageTk
import random
# main window
root = Tk()
root.title("Easy Game")
root.configure(background= "#9b59b6")

# loading image
def load_img(file_path):
    img = Image.open(f"images/{file_path}")
    img = img.resize((150,150))
    return ImageTk.PhotoImage(img)
    
# images loading
user_imgs = {"rock": load_img("rock-user.png"), "paper": load_img("paper-user.png"), "scissor": load_img("scissor-user.png")}
comp_imgs = {"rock": load_img("rock.png"), "paper": load_img("paper.png"), "scissor": load_img("scissor.png")}

# labels:- to show text or images 
comp_label = Label(root, text = "computer's choice", background= "#9b59b6", image = comp_imgs["rock"])
user_label = Label(root, text = "your choice", background= "#9b59b6",  image = user_imgs["rock"])
comp_label.grid(row = 1, column = 0)
user_label.grid(row = 1, column = 4)

comp_score = Label(root, text=0, background= "#9b59b6" , foreground= "black" )
user_score = Label(root, text=0, background= "#9b59b6" , foreground= "black" )
comp_score.grid(row = 1, column = 1)
user_score.grid(row = 1, column = 3)

# update messages 
msg = Label(root, background= "#9b59b6", text = "Start game!" , fg = "black" , font = 50)
msg.grid(row=3, column=2)

#score update
def update_score(Label):
    score = int(Label["text"]) + 1
    Label.configure(text = str(score))

# game logic
def play(user_choice):
    options = ["rock", "paper", "scissor"]
    comp_choice = random.choice(options)

# updating images
    user_label.configure(image=user_imgs[user_choice])
    comp_label.configure(image=comp_imgs[comp_choice])

# winner
    if user_choice == comp_choice:
        msg.configure(text="It's a tie!")
    elif (user_choice == "rock" and comp_choice == "scissor") or \
            (user_choice == "scissor" and comp_choice == "paper") or \
            (user_choice == "paper" and comp_choice == "rock"):
        msg.configure(text = "You win!")
        update_score(user_score)
    else:
        msg.configure(text = "computer Wins!")
        update_score(comp_score)

        # buttons
rock = Button(root, width=20, height=2, text="Rock", background="green", foreground="Black", command=lambda: play("rock"))
rock.grid(row = 2, column = 1)
scissor = Button(root, width=20, height=2, text="scissor", background="red", foreground="Black", command=lambda: play("scissor"))
scissor.grid(row = 2, column = 2)
paper = Button(root, width=20, height=2, text="paper", background="blue", foreground="Black", command=lambda: play("paper"))
paper.grid(row = 2, column = 3)

root.mainloop()

