import customtkinter as ctk

# ===============================
# JARVIS GUI
# Developer : Harish
# Version : 5.0
# ===============================

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


app = ctk.CTk()

app.title("JARVIS AI Assistant")
app.geometry("1200x700")
app.resizable(False, False)

# ===============================
# TITLE
# ===============================

title = ctk.CTkLabel(
    app,
    text="JARVIS AI",
    font=("Segoe UI", 38, "bold")
)

title.pack(pady=(30, 10))


# ===============================
# AI ORB
# ===============================

orb = ctk.CTkCanvas(
    app,
    width=220,
    height=220,
    bg="#242424",
    highlightthickness=0
)

orb.pack()

circle = orb.create_oval(
    40,
    40,
    180,
    180,
    fill="#00BFFF",
    outline=""
)

grow = True


def animate():

    global grow

    x1, y1, x2, y2 = orb.coords(circle)

    if grow:
        orb.scale(circle, 110, 110, 1.01, 1.01)
    else:
        orb.scale(circle, 110, 110, 0.99, 0.99)

    x1, y1, x2, y2 = orb.coords(circle)

    if x1 < 20:
        grow = True

    if x1 > 40:
        grow = False

    app.after(40, animate)


animate()


# ===============================
# STATUS
# ===============================

status = ctk.CTkLabel(
    app,
    text="Status : Idle",
    font=("Segoe UI", 20)
)

status.pack(pady=20)


# ===============================
# CHAT BOX
# ===============================

chat = ctk.CTkTextbox(
    app,
    width=850,
    height=220,
    font=("Consolas", 15)
)

chat.pack(pady=10)

chat.insert("end", "Jarvis : Welcome Harish 👋\n")
chat.insert("end", "Jarvis : System Ready.\n\n")

chat.configure(state="disabled")


# ===============================
# BUTTONS
# ===============================

button_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

button_frame.pack(pady=20)


start_button = ctk.CTkButton(
    button_frame,
    text="🎤 Start Listening",
    width=180
)

start_button.grid(row=0, column=0, padx=10)


stop_button = ctk.CTkButton(
    button_frame,
    text="⛔ Stop",
    width=120,
    fg_color="red",
    hover_color="#8B0000"
)

stop_button.grid(row=0, column=1, padx=10)


exit_button = ctk.CTkButton(
    button_frame,
    text="Exit",
    width=120,
    command=app.destroy
)

exit_button.grid(row=0, column=2, padx=10)


app.mainloop()