"""
    Stage: Development-01
    @author: Arda Çelik, 119202051
    @author: Yiğit Cem Hoşoğlu, 120202046 
"""

import tkinter as library


class LoginWindow:
    # constructor
    def __init__(self):
        self.window = library.Tk()

        self._initializeGUI()
        self._addGUIElementsToFrame()
        self.window.title("Library")
        # start the GUI frame
        self.window.mainloop()
        


    """
    +++
        Initialize GUI elements. If it is necessary, you can add
        more elements.

        ! PLEASE RENAME THE OBJECTS ACCORDING TO THEIR PURPOSES !
        ! YOU CAN ADD MORE ELEMENTS IF IT IS NECESSARY !
    """
    def _initializeGUI(self):
        self.lbl01 = library.Label(text="Username")
        self.lbl02 = library.Label(text="Password")

        self.txt01 = library.Entry(width=30)
        self.txt02 = library.Entry(width=30)

        self.btn01 = library.Button(text="Login")
        self.btn02 = library.Button(text="Forgot Password")
        self.btn03 = library.Button(text="Cancel")


        self.btn01.bind("<Button-1>", self.handle_click)
        self.btn02.bind("<Button-2>", self.handle_click)
        self.btn03.bind("<Button-3>", self.handle_click)
        


    """
    +++
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        self.lbl01.grid(row=0, column=0, padx=10, pady=5)
        self.txt01.grid(row=0, column=1, padx=10, pady=5)

        self.lbl02.grid(row=1, column=0, padx=10, pady=5)
        self.txt02.grid(row=1, column=1, padx=10, pady=5)

        self.btn01.grid(row=2, column=0, padx=5, pady=5)
        self.btn02.grid(row=2, column=1, padx=5, pady=5)
        self.btn03.grid(row=2, column=2, padx=5, pady=5)

    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.

        :param event: action event for detecting which button is clicked
    """
    def handle_click(self, event):
        if event.widget == self.btn01: 
            if self.txt01.get() == "test" and self.txt02.get() == 'test123': 
                
                self.window01 = library.Tk()
                self.window01.title("New Tab")
                
                self._initializeGUI()
                self._addGUIElementsToFrame()
               
                # start the GUI frame
                self.window01.mainloop()

                





# main method for testing the application
if __name__ == "__main__":
    LoginWindow()
