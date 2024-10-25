import tkinter as tk
from tkinter import font

window = tk.Tk()

main_font = font.Font(size=52, weight='bold')  
window.geometry("700x360")
#window.resizable(False, False)
window.title("Project Calculator")

current_input = ""


magic_spot = tk.Label(text="", font=main_font, bg="white", fg='black')
magic_spot.pack()

def one(digit):
    global current_input
    current_input += digit
    magic_spot.config(text=current_input)
   
def clear():
    global current_input
    current_input=""
    magic_spot.config(text=current_input) 


def calculate():
    global current_input  
    results = eval(current_input)
    magic_spot.config(text=str(results))
    current_input = str(results)
    
    


one_button = tk.Button(text="1", font=main_font, bg="white", fg='black', command=lambda: one('1'))

two_button = tk.Button(text="2", font=main_font, bg="white", fg='black',  command=lambda: one('2'))
three_button = tk.Button(text="3", font=main_font, bg="white", fg='black',  command=lambda: one('3'))
four_button = tk.Button(text="4", font=main_font, bg="white", fg='black' , command=lambda: one('4'))
five_button = tk.Button(text="5", font=main_font, bg="white", fg='black' , command=lambda: one('5'))
six_button = tk.Button(text="6", font=main_font, bg="white", fg='black' , command=lambda: one('6'))
seven_button = tk.Button(text="7", font=main_font, bg="white", fg='black',  command=lambda: one('7'))
eight_button = tk.Button(text="8", font=main_font, bg="white", fg='black' ,command=lambda: one('8'))
nine_button = tk.Button(text="9", font=main_font, bg="white", fg='black' , command=lambda: one('9'))
addition_button = tk.Button(text="+", font= main_font, bg='white', fg='black' , command=lambda: one('+'))
negative_button = tk.Button(text="-", font= main_font, bg='white', fg='black' , command=lambda: one('-'))
times_button = tk.Button(text="X", font= main_font, bg='white', fg='black',  command=lambda: one('*'))
devide_button = tk.Button(text="%", font= main_font, bg='white', fg='black' , command=lambda: one('%'))
clear_button = tk.Button(text="C", font= main_font, bg='white', fg='black' , command= clear)
equals_button = tk.Button(text="=", font= main_font, bg='white', fg='black' , command=calculate)



one_button.pack(side=tk.LEFT)
two_button.pack(side=tk.LEFT)
three_button.pack(side=tk.LEFT)
four_button.pack(side=tk.LEFT)
five_button.pack(side=tk.LEFT)
six_button.pack(side=tk.LEFT)
seven_button.pack(side=tk.LEFT)
eight_button.pack(side=tk.LEFT)
nine_button.pack(side=tk.LEFT)
addition_button.pack()
negative_button.pack()
times_button.pack()
devide_button.pack()
clear_button.pack()
equals_button.pack()





window.mainloop()
