import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master.title("Acoustic")
        self.master.geometry("400x400")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
    