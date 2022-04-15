from snake import *

class Login(Tk):
    def __init__(self, width=750, height=750, bg="white"):
        Tk.__init__(self)
        self.title('Authentification')
        self.height = height
        self.width = width

        self.response = Label(self, fg="red", font="Helvetica 16 bold")
        self.response.pack()

        self.login_panel = Frame(self, width=self.width, height=self.height)
        self.login_panel.pack()

        self.pseudo_label = Label(self.login_panel, text="Pseudo", font="Helvetica 14 bold")
        self.password_label = Label(self.login_panel, text="Password", font="Helvetica 14 bold")
        self.pseudo_label.grid(row=0, column=0)
        self.password_label.grid(row=1, column=0)
        
        self.pseudo_value = Entry(self.login_panel, font="Helvetica 14 bold")
        self.password_value = Entry(self.login_panel, show="*", font="Helvetica 14 bold")
        self.pseudo_value.grid(row=0, column=1)
        self.password_value.grid(row=1, column=1)

        self.btn_panel = Frame(self, width=self.width, height=self.height)
        self.btn_panel.pack()

        self.btn_login = Button(self.btn_panel, text="Login", command=self.singin, bg="blue", fg="white", font="Helvetica 14 bold")
        self.btn_exit = Button(self.btn_panel, text="Exit", command=self.destroy, bg="red", fg="white", font="Helvetica 14 bold")
        self.btn_exit.grid(row=0, column=0)
        self.btn_login.grid(row=0, column=1)

    def singin(self):
        if self.pseudo_value.get() == '' or self.password_value.get() == '':
            self.response.configure(text="Please enter your information")
        elif self.pseudo_value.get() != 'shadoworker' or self.password_value.get() != 'tartempion':
            self.response.configure(text="Pseudo or password is incorrect")
        else:
            self.response.configure(text="")
            self.destroy()
            
            start = Snake()
            start.bind("<KeyPress>", start.arrow_key)
            start.mainloop()

    def enter(self, event):
        if event.keysym =="Return":
            self.singin()