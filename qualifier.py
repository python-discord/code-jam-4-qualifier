"""
A GUI application for a rocketship launch control panel.
This application is built on tkinter. See the official
documentation and linked resources here:
    https://docs.python.org/3/library/tkinter.html

Requirements:
    Python 3.
"""
import tkinter as tk


class RocketShipControlPanel(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.pilot = None
        self.pilot_label = None
        self.launch_button = Null

    def create_form(self):
        """
        Create the input fields, labels,
        and buttons when called.
        """

        self.pilot_label = tkinter.Label(
            self,
            text="Pilot: ",
        )
        self.pilot = tk.Entry(
            self,
            width=30,
        )
        self.pilot_label.pack(side=TOP)
        self.pilot.pack(side=tk.TOP)

        self.launch_button = tk.Button(
            self,
            text="Launch",
            command=self.do_countdown,
        )
        self.launch_button.pack(side=tk.BOTTOM)

    def do_countdown(self):
        """
        When the user clicks the login button, this callback
        is invoked. Make it do a countdown. The first time
        it is clicked, the button text should change to "3".
        The next time to "2", then to "1", and then to "LIFTOFF!".

        If the username or the password are blank, this
        callback should not do anything.
        """

        raise NotImplementedError

root = tk.Tk()
app = RocketShipControlPanel(master=root)
app.mainloop()
