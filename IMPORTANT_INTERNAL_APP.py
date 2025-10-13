import tkinter as tk
from tkinter import ttk

def get_credentials(username_field, password_field, output_label):
    """
    Retrieves the text from both the username and password fields and
    updates a display label with the retrieved information.
    """
    username = username_field.get()
    password = password_field.get()

    # Clear the fields after retrieval for security/next entry
    username_field.delete(0, tk.END)
    password_field.delete(0, tk.END)

    # Update the label in the GUI instead of just printing to the console
    output_label.config(
        text=f"Username Entered: '{username}'\nPassword Retrieved (Masked): '{password}'"
    )
    # Note: In a real application, you would handle authentication here.

# --- GUI Setup ---

root = tk.Tk()
root.title("Transformative Enterprise Systems & Trust Information Systems")
root.geometry("700x700")
root.resizable(True, True)

# Configure style for a modern look
style = ttk.Style()
style.configure('TFrame', background='#f0f0f0')
style.configure('TLabel', background='#f0f0f0', font=('Inter', 10))
style.configure('TButton', font=('Inter', 10, 'bold'), padding=5)

main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill='both', expand=True)

# 1. Username Field
ttk.Label(main_frame, text="Username:").pack(pady=(5, 0), anchor='w')
username_entry = ttk.Entry(main_frame, width=40)
username_entry.pack(pady=(0, 10), fill='x')
username_entry.focus() # Set initial focus

# 2. Password Field (using show='*' for masking)
ttk.Label(main_frame, text="Password:").pack(pady=(5, 0), anchor='w')
password_entry = ttk.Entry(main_frame, width=40, show='*')
password_entry.pack(pady=(0, 20), fill='x')

# 3. Output Label
output_display = ttk.Label(
    main_frame,
    text="Credentials will appear here.",
    foreground='#333333',
    justify=tk.LEFT
)
output_display.pack(pady=(10, 5), fill='x', anchor='w')

# 4. Button to trigger the function
# We use a lambda to pass the entry widgets and output label as arguments
login_button = ttk.Button(
    main_frame,
    text="Submit Credentials",
    command=lambda: get_credentials(username_entry, password_entry, output_display)
)
login_button.pack(pady=10)

root.mainloop()
