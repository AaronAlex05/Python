from breezypythongui import EasyFrame

class QuadrantLabelsApp(EasyFrame):
    """Displays four labels in different quadrants."""
    
    def __init__(self):
        """Sets up the window and labels."""
        EasyFrame.__init__(self, title="Quadrant Labels", width=300, height=200)
        
        # Add labels to the four quadrants (0,0), (0,1), (1,0), (1,1)
        self.addLabel(text="Top Left", row=0, column=0)
        self.addLabel(text="Top Right", row=0, column=1)
        self.addLabel(text="Bottom Left", row=1, column=0)
        self.addLabel(text="Bottom Right", row=1, column=1)

def main():
    """Instantiates and pops up the window."""
    QuadrantLabelsApp().mainloop()

if __name__ == "__main__":
    main()
