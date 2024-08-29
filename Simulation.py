import tkinter as tk
from tkinter import PhotoImage

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.title("Simulation")
        self.attributes('-fullscreen', True)  # Fullscreen mode
        self.resizable(True, True)  # Enabling resizing

        # Configure grid columns and rows
        self.grid_columnconfigure(0, weight=2)  # Main frame column with more weight
        self.grid_columnconfigure(1, weight=1)  # Right-side frames column
        self.grid_rowconfigure(0, weight=0)  # Header row
        self.grid_rowconfigure(1, weight=1)  # Main content row
        self.grid_rowconfigure(2, weight=1)  # Second row
        self.grid_rowconfigure(3, weight=1)  # Third row
        self.grid_rowconfigure(4, weight=1)  # Row for right-side frames
        self.grid_rowconfigure(5, weight=0)  # Row for buttons

        # Load the background image for the header
        self.header_bg_image = PhotoImage(file="images/logo_bg.png")  

        # Header frame with an image background
        self.header_frame = tk.Frame(self, height=100)
        self.header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.header_frame.grid_propagate(False)  # Prevents the frame from resizing to fit its content

        # Label to display the background image in the header frame
        self.header_label = tk.Label(self.header_frame, image=self.header_bg_image)
        self.header_label.place(x=0, y=0, relwidth=1, relheight=1)



        self.bg_image_close = PhotoImage(file="images/close.png")

        # Exit button
        self.exit_button = tk.Button(self.header_frame, command=self.quit, image=self.bg_image_close, compound="center", border=0)
        self.exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # Main frame, where the animation of predators and prey will be stored
        self.main_frame = tk.Frame(self, bg="gray")
        self.main_frame.grid(row=1, column=0, rowspan=4, sticky="nsew", padx=10, pady=10)
        self.main_frame.config(width=int(self.winfo_screenwidth() * 0.4))

        # Graph frames
        self.Fibonacci_Frame = tk.Frame(self, bg="gray")  # 1st graph
        self.Fibonacci_Frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

        self.Ratio_Frame = tk.Frame(self, bg="gray")  # 2nd graph
        self.Ratio_Frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

        self.Another_Frame_1 = tk.Frame(self, bg="gray")  # 3rd graph
        self.Another_Frame_1.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

        self.Another_Frame_2 = tk.Frame(self, bg="gray")  # 4th graph 
        self.Another_Frame_2.grid(row=4, column=1, sticky="nsew", padx=10, pady=5)

        # Bottom frame
        self.bottom_Frame = tk.Frame(self)
        self.bottom_Frame.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)

        # Configure grid weights for rows and columns in bottom_Frame
        self.bottom_Frame.grid_rowconfigure(0, weight=1)
        self.bottom_Frame.grid_columnconfigure(0, weight=1)
        self.bottom_Frame.grid_columnconfigure(1, weight=1)
        self.bottom_Frame.grid_columnconfigure(2, weight=2)

        self.bg_image_reset = PhotoImage(file="images/Reset.png")
        self.bg_image_simulate = PhotoImage(file="images/simulate.png")

        # Create the reset button
        self.reset_button = tk.Button(self.bottom_Frame, command=self.reset, width=20, height=2, image=self.bg_image_reset, compound="center", border=0)
        self.reset_button.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Create the simulate button
        self.simulate_button = tk.Button(self.bottom_Frame, command=self.simulate, width=20, height=2, image=self.bg_image_simulate, compound="center", border=0)
        self.simulate_button.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Right-bottom frame
        self.right_bottom_Frame = tk.Frame(self.bottom_Frame, bg="lightblue")
        self.right_bottom_Frame.grid(row=0, column=2, sticky="nsew", padx=10, pady=5)

        # Configure grid weights for rows and columns in right_bottom_Frame
        self.right_bottom_Frame.grid_rowconfigure(0, weight=1)
        self.right_bottom_Frame.grid_rowconfigure(1, weight=1)
        self.right_bottom_Frame.grid_rowconfigure(2, weight=1)
        self.right_bottom_Frame.grid_columnconfigure(0, weight=1)  # Column for labels
        self.right_bottom_Frame.grid_columnconfigure(1, weight=2)  # Column for entries

        # Create labels and entries inside right_bottom_Frame
        self.entry1_label = tk.Label(self.right_bottom_Frame, text="Entry 1", bg="gray", fg="white", font=("Arial", 10))
        self.entry1_label.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.entry2_label = tk.Label(self.right_bottom_Frame, text="Entry 2", bg="gray", fg="white", font=("Arial", 10))
        self.entry2_label.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        self.entry3_label = tk.Label(self.right_bottom_Frame, text="Entry 3", bg="gray", fg="white", font=("Arial", 10))
        self.entry3_label.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

        self.entry1 = tk.Entry(self.right_bottom_Frame)
        self.entry1.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        self.entry2 = tk.Entry(self.right_bottom_Frame)
        self.entry2.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        self.entry3 = tk.Entry(self.right_bottom_Frame)
        self.entry3.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

        # Ensure right_bottom_Frame expands properly
        self.bottom_Frame.grid_rowconfigure(0, weight=1)
        self.bottom_Frame.grid_columnconfigure(2, weight=1)

        # Ensure right-side frames expand properly
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

    def reset(self):
        # Add functionality for the reset button
        print("Reset button clicked")

    def simulate(self):
        # Add functionality for the simulate button
        print("Simulate button clicked")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
