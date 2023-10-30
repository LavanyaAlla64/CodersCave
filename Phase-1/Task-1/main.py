import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "AC":
        entry.delete(0, tk.END)
    elif text == "DEL":
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[:-1])
    else:
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current + text)

root = tk.Tk()
root.geometry("300x400")
root.title("Calculator")

entry = tk.Entry(root, font="Helvetica 20")
entry.pack(fill=tk.BOTH, expand=True)

button_frame = tk.Frame(root)
button_frame.pack(fill=tk.BOTH, expand=True)

button_labels = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("00", 4, 1), (".", 4, 2), ("+", 4, 3),
    ("AC", 5, 0), ("DEL", 5, 1), ("%", 5, 2), ("=", 5, 3),
]

buttons = []

for (text, row, col) in button_labels:
    button = tk.Button(button_frame, text=text, font="Helvetica 20")
    button.grid(row=row, column=col, sticky="nsew")
    button.bind("<Button-1>", on_button_click)  # Bind the button click event
    buttons.append(button)

for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)

for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)

root.mainloop()
