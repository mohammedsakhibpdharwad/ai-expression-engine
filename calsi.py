import customtkinter as ctk

# Set theme and appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create main window
app = ctk.CTk()
app.title("Modern Calculator")
app.geometry("360x520")
app.resizable(False, False)

# Entry display
entry = ctk.CTkEntry(app, width=320, height=70, corner_radius=15, justify="right", font=("Poppins", 28))
entry.place(x=20, y=30)

# Flag to track if result was shown
result_shown = False

# Functionality
def click(value):
    global result_shown

    if value == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, "end")
            entry.insert("end", result)
            result_shown = True  # mark result as shown
        except Exception:
            entry.delete(0, "end")
            entry.insert("end", "Error")
            result_shown = True

    elif value == "C":
        entry.delete(0, "end")
        result_shown = False

    else:
        if result_shown:
            # If last action was "=", start new number
            entry.delete(0, "end")
            result_shown = False
        entry.insert("end", value)

# Button layout
buttons = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="],
]

# Create buttons dynamically
y_pos = 130
for row in buttons:
    x_pos = 20
    for b in row:
        button = ctk.CTkButton(
            app,
            text=b,
            width=70,
            height=60,
            corner_radius=12,
            fg_color="#1f6aa5" if b in ["=", "C"] else "#2a2d2e",
            hover_color="#3a7ebf" if b in ["=", "C"] else "#3b3b3b",
            font=("Poppins", 22, "bold"),
            command=lambda val=b: click(val)
        )
        button.place(x=x_pos, y=y_pos)
        x_pos += 80
    y_pos += 70

# Footer label
footer = ctk.CTkLabel(app, text="Developed by [Your Name]", font=("Poppins", 12))
footer.place(relx=0.5, rely=0.95, anchor="center")

app.mainloop()
