import tkinter as tk
from tkinter import ttk

# Define dummy valid credentials for demonstration purposes.
# In a real application, these would come from a secure backend (e.g., database, API).
VALID_USERNAME = "user"
VALID_PASSWORD = "password123" # A simple dummy password

def get_credentials(username_field, password_field, output_label):
    """
    Retrieves the text from both the username and password fields,
    attempts a basic authentication against dummy credentials, and
    updates a display label with the result.
    """
    username = username_field.get()
    password = password_field.get()

    # Clear the fields after retrieval for security/next entry
    username_field.delete(0, tk.END)
    password_field.delete(0, tk.END)

    # --- Authentication Logic ---
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        output_label.config(
            text=f"Login Successful! Welcome, {username}!",
            foreground='green' # Indicate success with green text
        )
    else:
        output_label.config(
            text="Login Failed: Invalid username or password.",
            foreground='red' # Indicate failure with red text
        )
    # Note: In a real application, you would handle authentication with a secure backend
    # using hashing for passwords and proper session management. This is a basic
    # implementation to address the user's immediate inability to "log in".

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
    text="Enter credentials and click 'Submit'.\n(Hint: 'user' / 'password123')", # Added hint
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