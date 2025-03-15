import tkinter as tk
import pytz
from datetime import datetime

class FloatingClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure_window()
        self.initialize_variables()
        self.create_main_frame()
        self.create_context_menu()
        self.add_timezone("UTC")  # Default timezone
        self.update_time()

    def configure_window(self):
        """Configures the window settings."""
        self.overrideredirect(True)
        self.wm_attributes('-topmost', True)
        self.wm_attributes('-alpha', 0.7)

        # Bind drag events globally
        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<ButtonRelease-1>", self.stop_move)
        self.bind("<B1-Motion>", self.on_move)
        self.bind("<Button-3>", self.show_context_menu)

        # Set initial position near center
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"+{screen_width//4}+{screen_height//4}")

    def initialize_variables(self):
        """Initializes necessary variables."""
        self.x, self.y = 0, 0
        self.transparency = 0.7
        self.time_widgets = []

        self.timezone_dict = {
            "UTC": "UTC",
            "US/Eastern": "New York",
            "Europe/London": "London",
            "Asia/Tokyo": "Tokyo",
            "Asia/Shanghai": "Shanghai",
            "Asia/Hong_Kong": "Hong Kong",
            "Asia/Jakarta": "Jakarta",
        }

    def create_main_frame(self):
        """Creates the main container for timezones."""
        self.frame = tk.Frame(self, bg='black')
        self.frame.pack(padx=10, pady=10)

    def create_context_menu(self):
        """Creates the right-click menu with options."""
        self.context_menu = tk.Menu(self, tearoff=0)

        # Add Timezone submenu
        self.timezone_menu = tk.Menu(self.context_menu, tearoff=0)
        for tz_id, display_name in self.timezone_dict.items():
            self.timezone_menu.add_command(label=display_name, command=lambda z=tz_id: self.add_timezone(z))
        self.context_menu.add_cascade(label="Add Timezone", menu=self.timezone_menu)

        # Transparency submenu
        self.transparency_menu = tk.Menu(self.context_menu, tearoff=0)
        for t in [x / 10 for x in range(1, 11)]:  # Generates [0.1, 0.2, ..., 1.0]
            self.transparency_menu.add_command(label=f"{int(t * 100)}%", command=lambda v=t: self.set_transparency(v))
        self.context_menu.add_cascade(label="Transparency", menu=self.transparency_menu)

        self.context_menu.add_command(label="Help", command=self.show_help)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Exit", command=self.destroy)

    def add_timezone(self, timezone_id):
        """Adds a new timezone row to the display."""
        display_name = self.timezone_dict.get(timezone_id, timezone_id)

        # Create a frame for the timezone
        time_frame = tk.Frame(self.frame, bg='black')
        time_frame.pack(fill=tk.X, pady=(5, 0))

        # Create labels
        zone_label = self.create_label(time_frame, display_name, font=('Helvetica', 14), width=10)
        time_label = self.create_label(time_frame, "00:00:00", font=('Helvetica', 18))

        # Store references
        self.time_widgets.append((timezone_id, zone_label, time_label, time_frame))

        # Bind double-click to remove
        for widget in (time_frame, zone_label, time_label):
            widget.bind("<Double-Button-1>", lambda e, f=time_frame, t=timezone_id: self.remove_timezone(f, t))

    def create_label(self, parent, text, font, width=None):
        """Creates and returns a label with given properties."""
        label = tk.Label(parent, text=text, font=font, bg='black', fg='white', width=width, anchor='e' if width else None)
        label.pack(side=tk.LEFT, padx=(0, 10) if width else (0, 0))
        return label

    def remove_timezone(self, frame, timezone_id):
        """Removes a timezone from the display, ensuring at least one remains."""
        if len(self.time_widgets) > 1:
            frame.destroy()
            self.time_widgets = [w for w in self.time_widgets if w[0] != timezone_id or w[3] != frame]

    def update_time(self):
        """Updates time for all displayed timezones."""
        for timezone_id, zone_label, time_label, frame in self.time_widgets:
            try:
                current_time = datetime.now(pytz.timezone(timezone_id)).strftime('%H:%M:%S')
                time_label.config(text=current_time)
            except Exception:
                time_label.config(text="Error")

        self.after(1000, self.update_time)

    def show_context_menu(self, event):
        """Displays the right-click menu."""
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()

    def show_help(self):
        """Displays the help window."""
        help_window = tk.Toplevel(self)
        help_window.title("Floating Clock Help")
        help_window.geometry("400x450")

        help_text = """
Floating World Clock - Help

Features:
• Multiple timezone display with custom labels
• Transparent, borderless window
• Always stays on top of other windows
• Completely movable
• Customizable transparency

Controls:
• Left-click and drag: Move the clock window
• Right-click: Open the menu
• Double-click on a timezone: Remove that timezone

Menu Options:
• Add Timezone: Add a new timezone to the display
• Transparency: Adjust the window transparency
• Help: Show this help window
• Exit: Close the application

Tips:
• You can customize timezone display names in the code
• The clock will always stay on top of other windows
• At least one timezone will always remain visible
• The window position is saved until the app is closed

This floating clock application was created using AI assistants, 
including ChatGPT by OpenAI and Claude by Anthropic.

© 2025 - Floating World Clock
        """

        tk.Label(help_window, text=help_text, justify=tk.LEFT, padx=20, pady=20, wraplength=360).pack(fill=tk.BOTH, expand=True)
        tk.Button(help_window, text="Close", command=help_window.destroy, width=10).pack(pady=10)

    def set_transparency(self, value):
        """Updates window transparency."""
        self.transparency = float(value)
        self.wm_attributes('-alpha', self.transparency)

    def start_move(self, event):
        """Starts window drag movement."""
        self.x, self.y = event.x, event.y

    def stop_move(self, event):
        """Stops window drag movement."""
        self.x, self.y = None, None

    def on_move(self, event):
        """Handles window drag movement."""
        x, y = self.winfo_x() + (event.x - self.x), self.winfo_y() + (event.y - self.y)
        self.geometry(f"+{x}+{y}")

if __name__ == "__main__":
    FloatingClock().mainloop()
