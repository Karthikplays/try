import tkinter as tk  
from tkinter import messagebox  

def register():  
    name = name_entry.get()  
    email = email_entry.get()  
    password = password_entry.get()  
    
    if not name or not email or not password:  
        messagebox.showwarning("Input Error", "Please fill in all fields")  
        return  

    # Here you can add code to save the data, like writing to a file or database  
    messagebox.showinfo("Registration Successful", f"Welcome, {name}!")  

# Create the main window  
root = tk.Tk()  
root.title("Registration Form")  

# Create and place the labels and entry fields  
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)  
name_entry = tk.Entry(root)  
name_entry.grid(row=0, column=1, padx=10, pady=10)  

tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=10)  
email_entry = tk.Entry(root)  
email_entry.grid(row=1, column=1, padx=10, pady=10)  

tk.Label(root, text="Password").grid(row=2, column=0, padx=10, pady=10)  
password_entry = tk.Entry(root, show='*')  
password_entry.grid(row=2, column=1, padx=10, pady=10)  

# Create and place the register button  
register_button = tk.Button(root, text="Register", command=register)  
register_button.grid(row=3, columnspan=2, pady=10)  

# Run the application  
root.mainloop()
