from tkinter import *
from PIL import Image, ImageTk

WIDTH = 900
HEIGHT = 500

def exit_win(*args):
    exit()

def cookie_click(event):
    global score, photo_small
    score += 1
    score_label.config(text=str(score))
    cps_label.config(text=f"Cookies per second: {cps}")
    image_label.config(image=photo_small)
    check_buttons()

def release_click(event):
    image_label.config(image=photo)

def buy_grandma():
    global score, grandma_count, grandma_cost, cps
    if score >= grandma_cost:
        score -= grandma_cost
        grandma_count += 1
        cps += 1
        grandma_cost *= 2
        update_info_labels()
        update_score()

def buy_factory():
    global score, factory_count, factory_cost, cps
    if score >= factory_cost:
        score -= factory_cost
        factory_count += 1
        cps += 10
        factory_cost *= 3
        update_info_labels()
        update_score()

def buy_mega_oven():
    global score, mega_oven_count, mega_oven_cost, cps
    if score >= mega_oven_cost:
        score -= mega_oven_cost
        mega_oven_count += 1
        cps += 50
        mega_oven_cost *= 5
        update_info_labels()
        update_score()

def buy_quantum_bakery():
    global score, quantum_bakery_count, quantum_bakery_cost, cps
    if score >= quantum_bakery_cost:
        score -= quantum_bakery_cost
        quantum_bakery_count += 1
        cps += 200
        quantum_bakery_cost *= 10
        update_info_labels()
        update_score()

def buy_cosmic_confectionery():
    global score, cosmic_confectionery_count, cosmic_confectionery_cost, cps
    if score >= cosmic_confectionery_cost:
        score -= cosmic_confectionery_cost
        cosmic_confectionery_count += 1
        cps += 1000
        cosmic_confectionery_cost *= 20
        update_info_labels()
        update_score()

def buy_time_warp():
    global score, cps, time_warp_count, time_warp_cost, cps
    if score >= time_warp_cost:
        score -= time_warp_cost
        time_warp_count += 1
        cps += 5000
        time_warp_cost *= 50
        update_info_labels()
        update_score()

def update_score():
    global score, cps
    score += cps
    score_label.config(text=str(score))
    cps_label.config(text=f"Cookies per second: {cps}")
    root.after(1000, update_score)
    check_buttons()

def check_buttons():
    buttons = [grandma, factory, mega_oven, quantum_bakery, cosmic_confectionery, time_warp]
    costs = [grandma_cost, factory_cost, mega_oven_cost, quantum_bakery_cost, cosmic_confectionery_cost, time_warp_cost]
    for button, cost in zip(buttons, costs):
        button.config(state=NORMAL if score >= cost else DISABLED)

def update_info_labels():
    labels = [
        (grandma_info_label, grandma_count, 1),
        (factory_info_label, factory_count, 10),
        (mega_oven_info_label, mega_oven_count, 50),
        (quantum_bakery_info_label, quantum_bakery_count, 200),
        (cosmic_confectionery_info_label, cosmic_confectionery_count, 1000),
        (time_warp_info_label, time_warp_count, 5000),
    ]
    for label, count, cps_increase in labels:
        label.config(text=f"{label.cget('text').split(':')[0]}: {count} (CPS: +{count * cps_increase})")

    buttons = [grandma, factory, mega_oven, quantum_bakery, cosmic_confectionery, time_warp]
    costs = [grandma_cost, factory_cost, mega_oven_cost, quantum_bakery_cost, cosmic_confectionery_cost, time_warp_cost]
    for button, cost in zip(buttons, costs):
        button.config(text=f"{button.cget('text').split(' -')[0].strip()} - {cost}")


root = Tk()
root.title("Cookie Clicker")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)

cookie_frame = Frame(root, width=WIDTH-400, height=HEIGHT)
cookie_frame.place(x=0, y=0)

bonus_frame = Frame(root, width=WIDTH-(WIDTH-400), height=HEIGHT, bg="gray")
bonus_frame.place(x=WIDTH-400, y=0)

image = Image.open("cookie.png")
small_image = image.resize((int(image.width * 0.98), int(image.height * 0.98)))
photo = ImageTk.PhotoImage(image)
photo_small = ImageTk.PhotoImage(small_image)

image_label = Label(cookie_frame, image=photo)
image_label.place(relx=0.5, rely=0.5, anchor=CENTER)
image_label.bind('<Button-1>', cookie_click)
image_label.bind('<ButtonRelease-1>', release_click)

score = 0
grandma_count = 0
grandma_cost = 10
factory_count = 0
factory_cost = 100
mega_oven_count = 0
mega_oven_cost = 500
quantum_bakery_count = 0
quantum_bakery_cost = 5000
cosmic_confectionery_count = 0
cosmic_confectionery_cost = 50000
time_warp_count = 0
time_warp_cost = 200000
cps = 0
score_label = Label(cookie_frame, text=score, font=("Futura", 20))
score_label.place(relx=0.5, y=50, anchor=CENTER)

cps_label = Label(cookie_frame, text=f"Cookies per second: {cps}", font=("Futura", 16))
cps_label.place(relx=0.5, y=80, anchor=CENTER)

bonus_label = Label(bonus_frame, text="Bonuses", font=("Futura", 20))
bonus_label.place(relx=0.5, y=30, anchor=CENTER)

grandma_info_label = Label(bonus_frame, text="Grandmas: 0 (CPS: +0)", font=("Futura", 14))
grandma_info_label.place(relx=0.5, y=70, anchor=CENTER)

factory_info_label = Label(bonus_frame, text="Factories: 0 (CPS: +0)", font=("Futura", 14))
factory_info_label.place(relx=0.5, y=140, anchor=CENTER)

mega_oven_info_label = Label(bonus_frame, text="Mega Ovens: 0 (CPS: +0)", font=("Futura", 14))
mega_oven_info_label.place(relx=0.5, y=210, anchor=CENTER)

quantum_bakery_info_label = Label(bonus_frame, text="Quantum Bakeries: 0 (CPS: +0)", font=("Futura", 14))
quantum_bakery_info_label.place(relx=0.5, y=280, anchor=CENTER)

cosmic_confectionery_info_label = Label(bonus_frame, text="Cosmic Confectioneries: 0 (CPS: +0)", font=("Futura", 14))
cosmic_confectionery_info_label.place(relx=0.5, y=350, anchor=CENTER)

time_warp_info_label = Label(bonus_frame, text="Time Warps: 0 (CPS: +0)", font=("Futura", 14))
time_warp_info_label.place(relx=0.5, y=420, anchor=CENTER)

grandma = Button(bonus_frame, text=f"Buy Grandma - {grandma_cost}", font=("Futura", 10), command=buy_grandma)
grandma.place(relx=0.5, y=100, anchor=CENTER)

factory = Button(bonus_frame, text=f"Buy Factory - {factory_cost}", font=("Futura", 10), command=buy_factory)
factory.place(relx=0.5, y=170, anchor=CENTER)

mega_oven = Button(bonus_frame, text=f"Buy Mega Oven - {mega_oven_cost}", font=("Futura", 10), command=buy_mega_oven)
mega_oven.place(relx=0.5, y=240, anchor=CENTER)

quantum_bakery = Button(bonus_frame, text=f"Buy Quantum Bakery - {quantum_bakery_cost}", font=("Futura", 10), command=buy_quantum_bakery)
quantum_bakery.place(relx=0.5, y=310, anchor=CENTER)

cosmic_confectionery = Button(bonus_frame, text=f"Buy Cosmic Confectionery - {cosmic_confectionery_cost}", font=("Futura", 10), command=buy_cosmic_confectionery)
cosmic_confectionery.place(relx=0.5, y=380, anchor=CENTER)

time_warp = Button(bonus_frame, text=f"Buy Time Warp - {time_warp_cost}", font=("Futura", 10), command=buy_time_warp)
time_warp.place(relx=0.5, y=450, anchor=CENTER)

check_buttons()

root.bind('<Escape>', exit_win)

root.mainloop()