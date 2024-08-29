import tkinter as tk
<<<<<<< Updated upstream
from tkinter import PhotoImage
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')  # Use 'Agg' if you want to save the plot to a file instead
=======
from tkinter import PhotoImage, Toplevel, messagebox
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Ensure compatibility with Tkinter
>>>>>>> Stashed changes
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
from scipy import integrate
<<<<<<< Updated upstream
import sys

alpha = 1.
beta = 1.
delta = 1.
gamma = 1.
x0 = 4.
y0 = 2.

def derivative(X, t, alpha, beta, delta, gamma):
    x, y = X
    dotx = x * (alpha - beta * y)
    doty = y * (-delta + gamma * x)
    return np.array([dotx, doty])

def init_plot():
    ax.set_xlim(0, tmax)
    ax.set_ylim(0, 20)
    return ln1, ln2

def update_plot(frame):
    t = np.linspace(0., tmax, Nt)
    X0 = [x0, y0]
    res = integrate.odeint(derivative, X0, t[:frame], args=(alpha, beta, delta, gamma))
    x, y = res.T
    ln1.set_data(t[:frame], x)
    ln2.set_data(t[:frame], y)
    return ln1, ln2
=======
>>>>>>> Stashed changes

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.paused = True
        self.simPress = 0
<<<<<<< Updated upstream

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
        self.exit_button = tk.Button(self.header_frame, command=self.quit, image=self.bg_image_close, compound="center", border = 0)
        self.exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # Main frame, dito mo e store yun animation of predators and prey jelo
        self.main_frame = tk.Frame(self, bg="gray")
        self.main_frame.grid(row=1, column=0, rowspan=4, sticky="nsew", padx=10, pady=10)
        self.main_frame.config(width=int(self.winfo_screenwidth() * 0.4))

        #I am not a king, I am not a god, I am ... Worst
        global fig, ax, ln1, ln2, tmax, Nt
        fig, ax = plt.subplots()
        tmax = 50
        Nt = 1000
        ln1, = ax.plot([], [], 'xb', label='Prey (Sea Lion)')
        ln2, = ax.plot([], [], '+r', label='Predator (Orca)')
        ax.set_title("Lotka-Volterra Model")
        ax.set_xlabel('Time [days]')
        ax.set_ylabel('Population')
        ax.grid()
        ax.legend()

        self.canvas = FigureCanvasTkAgg(fig, master=self.main_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        #dito nyo lagay yung graph nyo
        self.Fibonacci_Frame = tk.Frame(self, bg="gray")  #1st graph
        self.Fibonacci_Frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

        self.Ratio_Frame = tk.Frame(self, bg="gray")        #2nd graph
        self.Ratio_Frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

        self.Another_Frame_1 = tk.Frame(self, bg="gray")    #3rd graph
        self.Another_Frame_1.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

        self.Another_Frame_2 = tk.Frame(self, bg="gray")    #4th graph
        self.Another_Frame_2.grid(row=4, column=1, sticky="nsew", padx=10, pady=5)

        #Bagohin nyo nlng yung yung variable depende sa graph na ilalagay

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
        self.reset_button = tk.Button(self.bottom_Frame, command=self.reset, width=20, height=2, image=self.bg_image_reset, compound="center", border = 0)
        self.reset_button.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Create the simulate button
        self.simulate_button = tk.Button(self.bottom_Frame, command=self.simulate, width=20, height=2, image=self.bg_image_simulate, compound="center", border= 0)
        self.simulate_button.grid(row=0, column=1, sticky="nsew", padx=5, pady=5 )

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
=======
        
        # Initialize instance variables for plot
        self.fig, self.ax = plt.subplots()
        self.ln1, = self.ax.plot([], [], 'xb', label='Prey (Sea Lion)')
        self.ln2, = self.ax.plot([], [], '+r', label='Predator (Orca)')
        self.ax.set_title("Lotka-Volterra Model")
        self.ax.set_xlabel('Time [days]')
        self.ax.set_ylabel('Population')
        self.ax.grid()
        self.ax.legend()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.main_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Set default values for simulation parameters
        self.reset_values()

    def initUI(self):
        self.title("Simulation")
        self.attributes('-fullscreen', True)
        self.resizable(True, True)
        # Configure grid
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
>>>>>>> Stashed changes
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=0)

        self.header_frame = tk.Frame(self, bg="#1B6E7A", height=100)
        self.header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.header_frame.grid_propagate(False)

        self.title_label = tk.Label(self.header_frame, text="Simulation", bg="#1B6E7A", fg="white", font=("Arial", 20))
        self.title_label.pack(side=tk.LEFT, padx=10, pady=10)

        self.bg_image_close = PhotoImage(file="images/close.png")
        self.exit_button = tk.Button(self.header_frame, command=self.quit, image=self.bg_image_close, compound="center", border=0)
        self.exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.main_frame = tk.Frame(self, bg="gray")
        self.main_frame.grid(row=1, column=0, rowspan=4, sticky="nsew", padx=10, pady=10)
        self.main_frame.config(width=int(self.winfo_screenwidth() * 0.4))

        self.bottom_Frame = tk.Frame(self)
        self.bottom_Frame.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)
        self.bottom_Frame.grid_rowconfigure(0, weight=1)
        self.bottom_Frame.grid_columnconfigure(0, weight=1)
        self.bottom_Frame.grid_columnconfigure(1, weight=1)
        self.bottom_Frame.grid_columnconfigure(2, weight=1)

        self.bg_image_reset = PhotoImage(file="images/Reset.png")
        self.bg_image_simulate = PhotoImage(file="images/simulate.png")

        self.reset_button = tk.Button(self.bottom_Frame, command=self.reset, width=20, height=7, image=self.bg_image_reset, compound="center", border=0)
        self.reset_button.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.simulate_button = tk.Button(self.bottom_Frame, command=self.simulate, width=20, height=7, image=self.bg_image_simulate, compound="center", border=0)
        self.simulate_button.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        self.edit_button = tk.Button(self.bottom_Frame, text="Edit", command=self.open_edit_window, width=20, height=7)
        self.edit_button.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        self.validate_cmd = self.register(self.validate_numeric)
        self.entry_values = {}

    def open_edit_window(self):
        self.edit_window = Toplevel(self)
        self.edit_window.title("Edit Entries")
        self.edit_window.geometry("400x400")
        self.edit_window.transient(self)
        self.edit_window.grab_set()
        self.edit_window.lift()

        self.entries = {}
        entry_names = [
            "Initial Population Prey (x0)",
            "Initial Population Predator (y0)",
            "Prey Growth Rate (alpha)",
            "Predation Rate (beta)",
            "Predator Growth Rate (delta)",
            "Predator Consumption Rate (gamma)",
            "Time Interval",
            "Number of Time Steps (Nt)"
        ]

        for i, name in enumerate(entry_names):
            tk.Label(self.edit_window, text=name).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(self.edit_window, validate="key", validatecommand=(self.validate_cmd, "%P"))
            entry.grid(row=i, column=1, padx=10, pady=5)
            entry.insert(0, self.entry_values.get(name, "0"))
            self.entries[name] = entry

        save_button = tk.Button(self.edit_window, text="Save", command=self.save_entries)
        save_button.grid(row=len(entry_names), column=0, padx=10, pady=10)

        cancel_button = tk.Button(self.edit_window, text="Cancel", command=self.edit_window.destroy)
        cancel_button.grid(row=len(entry_names), column=1, padx=10, pady=10)

    def validate_numeric(self, value):
        if value == "":
            return True
        try:
            float(value)
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
            try:
                if name in ["Initial Population Prey (x0)", "Initial Population Predator (y0)", "Time Interval", "Number of Time Steps (Nt)"]:
                    self.entry_values[name] = int(value)  # Convert to integer for specific entries
                else:
                    self.entry_values[name] = float(value)  # Convert to float for other entries
            except ValueError:
                self.entry_values[name] = 0 if name in ["Initial Population Prey (x0)", "Initial Population Predator (y0)", "Time Interval", "Number of Time Steps (Nt)"] else 0.0
            print(f"{name}: {self.entry_values[name]}")  # Print the value for debugging

        # Update tmax and Nt from entry values
        self.tmax = self.entry_values.get("Time Interval", 50)
        self.Nt = self.entry_values.get("Number of Time Steps (Nt)", 1000)

        self.edit_window.destroy()


    def reset(self):
        # Stop the animation if it's running
        if hasattr(self, 'anim') and self.anim.event_source is not None:
            self.anim.event_source.stop()

        # Reset values to default
        self.reset_values()

        # Clear and reset the plot
        self.ax.clear()
        self.ln1, = self.ax.plot([], [], 'xb', label='Prey (Sea Lion)')
        self.ln2, = self.ax.plot([], [], '+r', label='Predator (Orca)')
        self.ax.set_title("Lotka-Volterra Model")
        self.ax.set_xlabel('Time [days]')
        self.ax.set_ylabel('Population')
        self.ax.grid()
        self.ax.legend()
        self.canvas.draw()

        # Reinitialize the simulation parameters
        self.simPress = 0  # Ensure simulate button starts fresh
        self.paused = True  # Ensure simulation is paused initially


    def reset_values(self):
        self.entry_values = {
            "Initial Population Prey (x0)": 40,
            "Initial Population Predator (y0)": 9,
            "Prey Growth Rate (alpha)": 0.1,
            "Predation Rate (beta)": 0.02,
            "Predator Growth Rate (delta)": 0.01,
            "Predator Consumption Rate (gamma)": 0.1,
            "Time Interval": 50,
            "Number of Time Steps (Nt)": 1000
        }
        self.tmax = self.entry_values["Time Interval"]
        self.Nt = self.entry_values["Number of Time Steps (Nt)"]

    def simulate(self):
        if self.simPress < 1:
<<<<<<< Updated upstream
            self.anim = FuncAnimation(fig, update_plot, init_func=init_plot, frames=Nt, interval=20, blit=True)
            self.simPress += 1

=======
            self.anim = FuncAnimation(self.fig, self.update_plot, init_func=self.init_plot, frames=self.Nt, interval=20, blit=True)
            self.simPress += 1
>>>>>>> Stashed changes
        if self.paused:
            self.anim.event_source.start()
        else:
            self.anim.event_source.stop()
        self.paused = not self.paused
<<<<<<< Updated upstream
=======

    def init_plot(self):
        self.ln1.set_data([], [])
        self.ln2.set_data([], [])
        self.ax.set_xlim(0, self.tmax)
        self.ax.set_ylim(0, 20)  # Adjust as needed
        return self.ln1, self.ln2

    def update_plot(self, frame):
        alpha = self.entry_values["Prey Growth Rate (alpha)"]
        beta = self.entry_values["Predation Rate (beta)"]
        delta = self.entry_values["Predator Growth Rate (delta)"]
        gamma = self.entry_values["Predator Consumption Rate (gamma)"]
        x0 = self.entry_values["Initial Population Prey (x0)"]
        y0 = self.entry_values["Initial Population Predator (y0)"]

        def dpop(t, z):
            x, y = z
            dxdt = alpha * x - beta * x * y
            dydt = delta * x * y - gamma * y
            return [dxdt, dydt]

        t = np.linspace(0, self.tmax, self.Nt)
        sol = integrate.solve_ivp(dpop, [0, self.tmax], [x0, y0], t_eval=t)

        self.ln1.set_data(t[:frame], sol.y[0, :frame])
        self.ln2.set_data(t[:frame], sol.y[1, :frame])

        # Adjust axis limits
        self.ax.set_xlim(0, self.tmax)
        self.ax.set_ylim(0, max(max(sol.y[0, :]), max(sol.y[1, :])) + 10)

        return self.ln1, self.ln2
>>>>>>> Stashed changes

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()

