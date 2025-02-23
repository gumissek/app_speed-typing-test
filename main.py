import random
from tkinter import *

words = [
    "Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit", "Integer",
    "tempus", "commodo", "tempor", "Nulla", "dapibus", "risus", "vel", "semper", "maximus",
    "Nullam", "a", "auctor", "leo", "Pellentesque", "habitant", "morbi", "tristique", "senectus",
    "et", "netus", "et", "malesuada", "fames", "ac", "turpis", "egestas", "Cras", "sit", "amet",
    "egestas", "felis", "eget", "finibus", "magna", "Vivamus", "non", "metus", "non", "dui",
    "feugiat", "iaculis", "Nulla", "eu", "auctor", "erat", "Nam", "finibus", "enim", "et", "dui",
    "accumsan", "aliquet", "Interdum", "et", "malesuada", "fames", "ac", "ante", "ipsum", "primis",
    "in", "faucibus", "Orci", "varius", "natoque", "penatibus", "et", "magnis", "dis", "parturient",
    "montes", "nascetur", "ridiculus", "mus", "Vestibulum", "tincidunt", "laoreet", "tempus", "Nam",
    "vel", "nunc", "ut", "lorem", "pretium", "scelerisque", "id", "sed", "nibh", "Vivamus", "felis",
    "justo", "bibendum", "vitae", "lacus", "a", "lobortis", "efficitur", "est", "Cras", "blandit",
    "neque", "sit", "amet", "sapien", "volutpat", "non", "mollis", "mauris", "euismod", "Curabitur",
    "arcu", "nisi", "cursus", "vel", "tristique", "a", "maximus", "a", "mauris"
]
words_60=[]
for i in range(60):
    words_60.append(random.choice(words))

def update_score():
    canva.itemconfig(score_label,text=f'Score:{SCORE}/60')


def begin():
    random_word=random.choice(words_60)
    canva.config(background='green')
    canva.itemconfig(statement,text=f'{random_word}')


def check(event=None):
    global SCORE
    random_word=canva.itemcget(statement,'text')
    if entry.get() == random_word:
        SCORE+=1
    update_score()



SCORE=0

window = Tk()
window.title('Speed typing test')
window.config(padx=20,pady=20)

canva= Canvas(width=500,height=300,background='blue')
canva.config(highlightthickness=0)
time = canva.create_text(250,50,text='Time:')
statement=canva.create_text(250,80,text='Statement:')
score_label=canva.create_text(250,100,text=f'Score:{SCORE}/60')
canva.grid(row=0,column=0,columnspan=3)

button= Button(text='START',command=begin)
button.grid(row=1,column=1)
entry =Entry()
entry.grid(row=1,column=2)

window.bind('<Return>',check)


window.mainloop()