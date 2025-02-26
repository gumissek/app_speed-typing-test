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
TIMER_COUNTER = 60
TIMER = None
SCORE = 0
FONT = ('Arial', 35, 'bold')
SCORE_BOARD = None


def timer(time):
    global TIMER
    global SCORE_BOARD
    if time > 0:
        canva.itemconfig(time_text, text=time)
        TIMER = window.after(1000, timer, time - 1)
    else:
        canva.itemconfig(time_text, text=time)
        window.after_cancel(TIMER)
        canva.config(background='lightgreen')
        SCORE_BOARD = canva.create_text(250, 230, text=f'YOUR SCORE IS: {SCORE}\n'
                                                       f'Words per minute = {SCORE / (TIMER_COUNTER / 60)}',
                                        fill='black', font=FONT)
        entry.insert(0, 'Retype word:')


def reset_timer():
    if TIMER != None:
        window.after_cancel(TIMER)
    if SCORE_BOARD != None:
        canva.delete(SCORE_BOARD)


def get_new_word():
    random_word = random.choice(words)
    canva.itemconfig(statement, text=f'{random_word}')


def update_score():
    canva.itemconfig(score_label, text=f'Score:{SCORE}')


def begin():
    global SCORE
    SCORE = 0
    canva.config(background='lightyellow')
    reset_timer()
    timer(TIMER_COUNTER)
    get_new_word()
    update_score()
    entry.delete(0, 'end')
    entry.focus()


def check(event=None):
    global SCORE
    random_word = canva.itemcget(statement, 'text')
    if entry.get() == random_word:
        SCORE += 1
        get_new_word()
    update_score()
    entry.delete(0, 'end')


window = Tk()
window.title('Speed typing test')
window.config(padx=20, pady=20, background='gray')

canva = Canvas(width=500, height=300, background='lightyellow')
canva.config(highlightthickness=0)
time_label = canva.create_text(220, 50, text='Time:', font=FONT, fill='black')
time_text = canva.create_text(300, 50, text=f'{TIMER_COUNTER}', font=FONT, fill='black')
statement = canva.create_text(250, 170, text='WORD:', font=FONT, fill='black')
score_label = canva.create_text(250, 100, text=f'Score:{SCORE}', font=FONT, fill='black')
canva.grid(row=0, column=0, columnspan=3)

button = Button(text='START', command=begin, background='white')
button.grid(row=1, column=1)
entry = Entry(bg='white', fg='black')
entry.insert(0, 'Retype word:')
entry.grid(row=1, column=2)

window.bind('<Return>', check)

window.mainloop()
