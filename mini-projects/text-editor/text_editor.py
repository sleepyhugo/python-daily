from tkinter import *
from tkinter import filedialog, messagebox

current_file = None


def new_file():
    global current_file
    current_file = None
    text_area.delete("1.0", END)
    root.title("My Python Text Editor - Untitled")


def open_file():
    global current_file
    filepath = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return  # User cancelled

    current_file = filepath
    text_area.delete("1.0", END)

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            text_area.insert("1.0", f.read())
    except Exception as e:
        messagebox.showerror("Error", f"Could not open file:\n{e}")
        return

    root.title(f"My Python Text Editor - {filepath}")


def save_file():
    global current_file

    if current_file is None:
        save_file_as()
        return

    try:
        with open(current_file, "w", encoding="utf-8") as f:
            content = text_area.get("1.0", END)
            f.write(content)
        messagebox.showinfo("Saved", "File saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save file:\n{e}")


def save_file_as():
    global current_file
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return  # User cancelled

    current_file = filepath

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            content = text_area.get("1.0", END)
            f.write(content)
        root.title(f"My Python Text Editor - {filepath}")
        messagebox.showinfo("Saved", "File saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save file:\n{e}")


def quit_app():
    root.destroy()


# UI SETUP

root = Tk()
root.title("My Python Text Editor - Untitled")
root.minsize(width=600, height=400)

# Text area
text_area = Text(root, wrap="word", undo=True)
text_area.pack(fill="both", expand=True)

# Scrollbar
scrollbar = Scrollbar(text_area)
scrollbar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)

# Menu bar
menubar = Menu(root)

# File menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save As...", command=save_file_as)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit_app)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

root.mainloop()
