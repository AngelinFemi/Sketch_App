import tkinter as tk
from tkinter import colorchooser

class SketchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Colorful Sketch App 🎨")

        # Canvas setup
        self.canvas = tk.Canvas(self.root, bg="white", width=600, height=400)
        self.canvas.pack(pady=10)

        # Default color
        self.current_color = "black"

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        self.color_button = tk.Button(button_frame, text="Pick Color 🎨", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(button_frame, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        self.eraser_button = tk.Button(button_frame, text="Eraser", command=self.use_eraser)
        self.eraser_button.pack(side=tk.LEFT, padx=5)

        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # Track last position
        self.last_x, self.last_y = None, None

    def choose_color(self):
        """Opens a color picker and updates the drawing color"""
        color = colorchooser.askcolor()[1]
        if color:
            self.current_color = color

    def use_eraser(self):
        """Changes the color to white (eraser effect)"""
        self.current_color = "white"

    def clear_canvas(self):
        """Clears the entire canvas"""
        self.canvas.delete("all")

    def paint(self, event):
        """Draws on the canvas with the selected color"""
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                    fill=self.current_color, width=5, capstyle=tk.ROUND, smooth=True)
        self.last_x, self.last_y = event.x, event.y

    def reset(self, event):
        """Resets the last position after releasing the mouse"""
        self.last_x, self.last_y = None, None

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = SketchApp(root)
    root.mainloop()
