from tkinter import *
import tkinter.font as font
import random
import tkinter.messagebox as msgbox


# When closing the opening window it dispays a thank you for playing message
def display_msg():
    msgbox.showinfo(title="", message="thanks for playing")
    root.destroy()
root = Tk()
root.protocol("WM_DELETE_WINDOW", display_msg)

# This is setting up player and computer scoring        
player_score = 0
computer_score = 0
options = [('rock',0), ('paper',1), ('scissors',2)]

def player_choice(player_input):
    global player_score, computer_score

    computer_input = get_computer_choice()

    player_choice_label.config(text = 'Your Selected : ' + player_input[0])
    computer_choice_label.config(text = 'Computer Selected : ' + computer_input[0])
#The if and elif statments
    if(player_input == computer_input):        #computer and player inputed same score
        winner_label.config(text = "Its a Tie")
    elif((player_input[1] - computer_input[1]) % 3 == 1): #player has beaten computer 
        player_score += 1
        winner_label.config(text="You Won!")
        player_score_label.config(text = 'Your Score : ' + str(player_score))
    else:
        computer_score += 1
        winner_label.config(text="Computer Won!") #Lastly computer has won
        computer_score_label.config(text='Your Score : ' + str(computer_score))

#This is making the random computer choice 
def get_computer_choice():
    return random.choice(options)

app_font = font.Font(size = 12)

game_window = Tk()
game_window.title("Rock Paper Scissors Game")

#Displaying the game title
game_title = Label(text = 'Rock Paper Scissors', font = font.Font(size = 20), fg = 'black')
game_title.pack()


winner_label = Label(text = "Click one of the choices to start", fg = 'black', font = font.Font(size = 13), pady = 8)
winner_label.pack()

input_frame = Frame(game_window)
input_frame.pack()

#Displaying the button appearance options
player_options = Label(input_frame, text = "Your choices : ", font = app_font, fg = 'black')
player_options.grid(row = 0, column = 0, pady = 8)
# The rock button appearance options 
rock_btn = Button(input_frame, text = 'Rock', width = 15, bd = 0, bg = 'grey', pady = 5, command = lambda: player_choice(options[0]))
rock_btn.grid(row = 1, column = 1, padx = 4, pady = 3)
# The paper button appearance options 
paper_btn = Button(input_frame, text = 'Paper', width = 15, bd = 0, bg = 'white', pady = 5, command = lambda: player_choice(options[1]))
paper_btn.grid(row = 1, column = 2, padx = 4, pady = 3)
# The scissors button appearance options 
scissors_btn = Button(input_frame, text = 'Scissors', width = 15, bd = 0, bg = 'red', pady = 5, command = lambda: player_choice(options[2]))
scissors_btn.grid(row = 1, column = 3, padx = 4, pady = 3)

#Displaying the computer/player scores and there appearces 
score_label = Label(input_frame, text = 'Score : ', font = app_font, fg = 'black')
score_label.grid(row = 2, column = 0)

player_choice_label = Label(input_frame, text = 'Your Selected:  ', font = app_font)
player_choice_label.grid(row = 3, column = 1, pady = 5)

player_score_label = Label(input_frame, text = 'Your Score:  ', font = app_font)
player_score_label.grid(row = 3, column = 2, pady = 5)

computer_choice_label = Label(input_frame, text = 'Computer Selected:  ', font = app_font, fg = 'black')
computer_choice_label.grid(row = 4, column = 1, pady = 5)

computer_score_label = Label(input_frame, text = 'Computer Score :  ', font = app_font, fg = 'black')
computer_score_label.grid(row = 4, column = 2, padx = (10,0), pady = 5)

game_window.geometry('700x300')
game_window.mainloop()
