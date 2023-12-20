import tkinter as tk

def process_command(event=None):
    cmd = entry.get()  # Get the command entered by the user
    output_text.insert(tk.END, f">>> {cmd}\n")  # Display the entered command
    # Perform actions based on the command - For demonstration, just echo the command
    output_text.insert(tk.END, f"{execute_command(cmd)}\n\n")
    entry.delete(0, tk.END)  # Clear the entry field

def execute_command(cmd):
    return f"Executing: {cmd}"  # For this example, just echo the command

root = tk.Tk()
root.title("Simple Terminal")

# Create a text widget to display output
output_text = tk.Text(root, wrap=tk.WORD)
output_text.pack()

# Create an entry widget for user input
entry = tk.Entry(root)
entry.pack(pady=5)
entry.bind("<Return>", process_command)  # Bind Enter key to process command

# Create a button to execute commands
submit_button = tk.Button(root, text="Execute", command=process_command)
submit_button.pack()

root.mainloop()
