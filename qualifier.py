"""
A GUI application which shows you a simple login form.
This application is built on tkinter. See the official
documentation and linked resources here:
    https://docs.python.org/3/library/tkinter.html

Requirements:
    Python 3.
"""

import tkinter as tk


class LoginApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
            
    def create_form(self):
        # Create the login button along with username
        # and password fields.
        self.login_button = tk.Button(self)
        self.login_button['text'] = "Login"
        self.login_button['command'] = self.do_login
        self.login_button.pack(side="bottom")

    def do_login(self):
        # When the user clicks the login button, this callback
        # is invoked. Change it to have it update the login button
        # text to something completely meaningless.
        raise NotImplementedError("Don't know how to login.")


root = tk.Tk()
app = LoginApplication(master=root)
app.mainloop()
