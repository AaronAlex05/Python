from breezypythongui import EasyFrame

class HelloWorldApp(EasyFrame):
    """Displays a simple greeting in a window."""
    
    def __init__(self):
        """Sets up the window and label."""
        EasyFrame.__init__(self, title="Hello World GUI")
        
        # Add a label with the text "Hello World"
        self.addLabel(text="Hello World", row=0, column=0)

def main():
    """Instantiates and pops up the window."""
    HelloWorldApp().mainloop()

if __name__ == "__main__":
    main()
