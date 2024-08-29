import tkinter as tk
from tkinter import PhotoImage, Toplevel, messagebox

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.title("Simulation")
        self.attributes('-fullscreen', True)  # Fullscreen mode
        self.resizable(True, True)  # Disabling resizing

        # Configure grid columns and rows
        self.grid_columnconfigure(0, weight=2)  # Main frame column with more weight
        self.grid_columnconfigure(1, weight=1)  # Right-side frames column
        self.grid_rowconfigure(0, weight=0)  # Header row
        self.grid_rowconfigure(1, weight=1)  # Main content row
        self.grid_rowconfigure(2, weight=1)  # Second row
        self.grid_rowconfigure(3, weight=1)  # Third row
        self.grid_rowconfigure(4, weight=1)  # Row for right-side frames
        self.grid_rowconfigure(5, weight=0)  # Row for buttons

        # Header frame with a height of 100 pixels
        self.header_frame = tk.Frame(self, bg="#1B6E7A", height=100)
        self.header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.header_frame.grid_propagate(False)  # Prevents the frame from resizing to fit its content

        # Title label
        self.title_label = tk.Label(self.header_frame, text="Simulation", bg="#1B6E7A", fg="white", font=("Arial", 20))
        self.title_label.pack(side=tk.LEFT, padx=10, pady=10)

        self.bg_image_close = PhotoImage(file="images/close.png")

        # Exit button
        self.exit_button = tk.Button(self.header_frame, command=self.quit, image=self.bg_image_close, compound="center", border=0)
        self.exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # Main frame
        self.main_frame = tk.Frame(self, bg="gray")
        self.main_frame.grid(row=1, column=0, rowspan=4, sticky="nsew", padx=10, pady=10)
        self.main_frame.config(width=int(self.winfo_screenwidth() * 0.4))

        # Frames for graphs
        self.Fibonacci_Frame = tk.Frame(self, bg="gray")  # 1st graph
        self.Fibonacci_Frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

        self.Ratio_Frame = tk.Frame(self, bg="gray")  # 2nd graph
        self.Ratio_Frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

        self.Another_Frame_1 = tk.Frame(self, bg="gray")  # 3rd graph
        self.Another_Frame_1.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

        self.Another_Frame_2 = tk.Frame(self, bg="gray")  # 4th graph
        self.Another_Frame_2.grid(row=4, column=1, sticky="nsew", padx=10, pady=5)

        # Bottom frame for buttons
        self.bottom_Frame = tk.Frame(self)
        self.bottom_Frame.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)

        # Configure grid weights for rows and columns in bottom_Frame
        self.bottom_Frame.grid_rowconfigure(0, weight=1)
        self.bottom_Frame.grid_columnconfigure(0, weight=1)
        self.bottom_Frame.grid_columnconfigure(1, weight=1)
        self.bottom_Frame.grid_columnconfigure(2, weight=1)

        self.bg_image_reset = PhotoImage(file="images/Reset.png")
        self.bg_image_simulate = PhotoImage(file="images/simulate.png")

        # Create the reset button
        self.reset_button = tk.Button(self.bottom_Frame, command=self.reset, width=20, height=7, image=self.bg_image_reset, compound="center", border=0)
        self.reset_button.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Create the simulate button
        self.simulate_button = tk.Button(self.bottom_Frame, command=self.simulate, width=20, height=7, image=self.bg_image_simulate, compound="center", border=0)
        self.simulate_button.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Create the "Edit" button in bottom_Frame
        self.edit_button = tk.Button(self.bottom_Frame, text="Edit", command=self.open_edit_window, width=20, height=7)
        self.edit_button.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        # Define validation command
        self.validate_cmd = self.register(self.validate_numeric)

        # Initialize variables for storing entry values
        self.entry_values = {
            "Initial Population Predator": 50,
            "Initial Population Prey": 100,
            "Predator Birth Rate": 0.1,
            "Prey Birth Rate": 0.2,
            "Predator Death Rate": 0.05,
            "Prey Death Rate": 0.1,
            "Predator Reproduction Rate": 0.02,
            "Prey Reproduction Rate": 0.03,
            "Simulation Duration": 100
        }

    def open_edit_window(self):
    # Create a new top-level window
        self.edit_window = Toplevel(self)
        self.edit_window.title("Edit Entries")
        self.edit_window.geometry("400x400")  # Increased height to accommodate more entries

        # Ensure the Toplevel window stays on top
        self.edit_window.transient(self)  # Set the main window as the owner of this Toplevel
        self.edit_window.grab_set()  # Ensure focus is on the Toplevel window
        self.edit_window.lift()  # Bring the Toplevel window to the front

        self.entries = {}  # Dictionary to store entry widgets with descriptive keys

        # Define the names for the entries
        entry_names = [
            "Initial Population Predator",
            "Initial Population Prey",
            "Predator Birth Rate",
            "Prey Birth Rate",
            "Predator Death Rate",
            "Prey Death Rate",
            "Predator Reproduction Rate",
            "Prey Reproduction Rate",
            "Simulation Duration"
        ]

        # Create labels and entries based on the names and initial values
        for i, name in enumerate(entry_names):
            tk.Label(self.edit_window, text=name).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(self.edit_window, validate="key", validatecommand=(self.validate_cmd, "%P"))
            entry.grid(row=i, column=1, padx=10, pady=5)
            entry.insert(0, self.entry_values[name])  # Set the initial value
            self.entries[name] = entry  # Store entry with its descriptive name

        # Create Save and Cancel buttons
        save_button = tk.Button(self.edit_window, text="Save", command=self.save_entries)
        save_button.grid(row=len(entry_names), column=0, padx=10, pady=10)

        cancel_button = tk.Button(self.edit_window, text="Cancel", command=self.edit_window.destroy)
        cancel_button.grid(row=len(entry_names), column=1, padx=10, pady=10)


    def validate_numeric(self, value):
        """Validation command to check if the input is a valid number."""
        if value == "":
            return True  # Allow empty input
        try:
            float(value)  # Try converting to float
            return True
        except ValueError:
            return False

    def save_entries(self):
        # Check for empty entries
        for name, entry in self.entries.items():
            if entry.get().strip() == "":
                messagebox.showwarning("Input Error", f"Please enter a value for '{name}'.")
                return  

        # Save the entries to instance variables
        for name, entry in self.entries.items():
            value = entry.get().strip()  # Get the value from the entry and strip any extra whitespace
            if name in ["Initial Population Predator", "Initial Population Prey", "Simulation Duration"]:
                # Convert to integer for specific entries
                try:
                    self.entry_values[name] = int(value)
                except ValueError:
                    self.entry_values[name] = 0  # Default to 0 if conversion fails
            else:
                # Convert to float for other entries
                try:
                    self.entry_values[name] = float(value)
                except ValueError:
                    self.entry_values[name] = 0.0  # Default to 0.0 if conversion fails
            print(f"{name}: {self.entry_values[name]}")  # Print the value for debugging
        self.edit_window.destroy()

    def reset(self):
        # Add functionality for the reset button
        print("Reset button clicked")

    def simulate(self):
        # Add functionality for the simulate button
        print("Simulate button clicked")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
