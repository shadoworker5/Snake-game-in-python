from tkinter import *
from random import *
import tkinter.messagebox as messagebox

class Snake(Tk):
    def __init__(self, width=750, height=750, bg="white"):
        Tk.__init__(self)
        self.title('Snake')
        self.width = width
        self.height = height
        self.time_run = 50
        self.run = 0  
        self.direction = 'Right'
        
        # Menu principal
        self.menu_frame = Frame(self , width = self.width, height = self.height - 720)
        self.menu_frame.pack(side=TOP)
        
        self.btn_start = Button(self.menu_frame, text="Start", command = self.start, bg="blue", fg="white", font="Helvetica 14 bold")
        self.btn_quit = Button(self.menu_frame, text="Exit", command=self.exit_game, bg="red", fg="white", font="Helvetica 14 bold")

        self.level_speed = Scale(self.menu_frame, length=450, orient=HORIZONTAL, label='Speed', troughcolor='dark grey', sliderlength=20, showvalue=50, from_=20, to=1000, tickinterval=140, command= self.update_time)
        self.level_speed.set(500)
        
        self.btn_start.grid(row=0, column=0)
        self.btn_quit.grid(row=0, column=1)
        self.level_speed.grid(row=0, column=2)
        
        self.point = 0
        self.label_point = Label(self.menu_frame, text="Score: "+str(self.point), bg="blue", fg="white", font="Helvetica 14 bold")
        self.label_point.grid(row=0, column=3)
        # Fin du menu principal

        # draw pane
        self.panel_width = self.width
        self.panel_height = self.height - 300
        self.panel = Canvas(self, width = self.panel_width, height = self.panel_height, bg = bg)
        self.panel.pack()

        # draw snake
        self.x, self.y = 10, 10
        self.snake = self.panel.create_rectangle(10, 10, 20, 20,  fill="red")

        # draw apple
        self.xp, self.yp = 55, 55
        self.pomme = 0

        # commande frame
        self.command_frame = Frame(self , width = self.width, height = self.height - 650, bg="red")
        self.command_frame.pack(side=BOTTOM)

        self.btn_top = Button(self.command_frame, text="Top", command = self.forward , bg="blue", fg="white", font="Helvetica 14 bold")
        self.btn_rigth = Button(self.command_frame, text="Rigth", command=self.turn_rigth, bg="blue", fg="white", font="Helvetica 14 bold")
        self.btn_letf = Button(self.command_frame, text="Left", command=self.turn_letf, bg="blue", fg="white", font="Helvetica 14 bold")
        self.btn_bottom = Button(self.command_frame, text="Bottom", command=self.go_bottom, bg="blue", fg="white", font="Helvetica 14 bold")
        
        self.btn_top.pack(side=TOP, anchor=N)
        self.btn_rigth.pack(side=RIGHT, anchor=W)
        self.btn_letf.pack(side=LEFT, anchor=E)
        self.btn_bottom.pack(side=BOTTOM, anchor=S)
        # end command frame

        # draw border
        self.border_left = self.panel.create_line(0, 0, 0, self.panel_height, width = 13)
        self.border_top = self.panel.create_line(0, 0, self.panel_width, 0, width = 12)
        self.border_top = self.panel.create_line(self.panel_width, 0, self.panel_width, self.panel_width, width = 6)
        self.border_top = self.panel.create_line(0, self.panel_height, self.panel_height + 298, self.panel_height, width = 6)
    
    def exit_game(self):
        response = messagebox.askyesno("Alert", "Êtes vous sûr de voilour quitter le jeu?")
        if response == True:
            self.destroy()

    def stop(self):
        self.run = 0
        self.btn_start.configure(text="Start", command=self.start)
        self.panel.delete(self.pomme)

    def start(self):
        self.btn_start.configure(text="Stop", command=self.stop)
        self.run = 1
        self.point = 0
        self.label_point.configure(text="Score: "+str(self.point))
        self.draw_proie()
        self.win()
        self.animate()

    def animate(self):
        if self.direction == 'Right':
            self.turn_rigth()
        if self.direction == 'Left':
            self.turn_letf()
        if self.direction == 'Up':
            self.forward()
        if self.direction == 'Down':
            self.go_bottom()
        self.after(self.time_run, self.animate)

    def lose(self):
        self.run = 0
        self.btn_start.configure(text="Restart", command=self.restart)
        self.panel.delete(self.pomme)
    
    def restart(self):
        if self.y == 5:
            self.direction = 'Down'
        if self.y == 440:
            self.direction = 'Up'
        if self.x == 740:
            self.direction = 'Left'
        if self.x == 5:
            self.direction = 'Right'
        self.btn_start.configure(text="Stop", command=self.stop)
        self.label_point.configure(text="Score: "+str(0))
        self.run = 1
        self.draw_proie()
        self.animate()

    def win(self):
        if self.x - 5 <= self.xp <= self.x + 5 and self.y - 5 <= self.yp <= self.y + 5:
            self.point += 5
            self.x += 5
            self.y += 5
            self.label_point.configure(text="Score: "+str(self.point))
            self.draw_proie()
        self.after(10, self.win)

    def draw_proie(self):
        self.xp = randint(1, 330)
        self.yp = randint(1, 330)
        self.panel.delete(self.pomme)
        self.pomme = self.panel.create_oval(self.xp, self.yp, self.xp + 10, self.yp + 10, fill="green")
        
    def forward(self):
        # go Up
        self.direction = 'Up'

        if self.run == 1:
            self.y -= 5
            if self.y == 5:
                self.lose()
            self.panel.coords(self.snake, self.x, self.y, self.x + 10, self.y + 10)
    
    def turn_rigth(self):
        # turn rigth
        self.direction = 'Right'

        if self.run == 1:
            self.x += 5
            if self.x == 740:
                self.lose()                
            self.panel.coords(self.snake, self.x, self.y, self.x + 10, self.y + 10)

    def turn_letf(self):
        # turn left
        self.direction = 'Left'

        if self.run == 1:
            self.x -= 5
            if self.x == 5:
                self.lose()
            self.panel.coords(self.snake, self.x, self.y, self.x + 10, self.y + 10)

    def go_bottom(self):
        # go back
        self.direction = 'Down'

        if self.run == 1:
            self.y += 5
            if self.y == 440:
                self.lose()
            self.panel.coords(self.snake, self.x, self.y, self.x + 10, self.y + 10)

    def arrow_key(self, event):
        if self.run == 1:
            if event.keysym =="Right":
                self.direction ='Right'
            if event.keysym =="Left":
                self.direction = 'Left'
            if event.keysym =="Up":
                self.direction = 'Up'
            if event.keysym =="Down":
                self.direction = 'Down'

    def update_time(self, x):
        self.time_run = x