import tkinter as tk

def save_chat_id():
    chat_id = entry.get()
    with open('config.txt', 'w') as file:
        file.write(f"CHAT_ID={chat_id}")
    label.config(text="✅ Chat ID saved successfully!")

app = tk.Tk()
app.title("Chat ID Setup")

tk.Label(app, text="Enter your Telegram Chat ID:").pack()
entry = tk.Entry(app, width=30)
entry.pack()

tk.Button(app, text="Save", command=save_chat_id).pack()
label = tk.Label(app, text="")
label.pack()

app.mainloop()
