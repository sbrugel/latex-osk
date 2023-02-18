import tkinter as tk

bindings = {
    '∧': '\\land',
    '∨': '\\lor',
    '¬': '\\lnot'
}


def key_pressed(string, tbox):
    tbox.insert(tk.END, string)


class Window:

    def __init__(self):
        self.root = tk.Tk()

        self.root.title('LaTeX Keyboard')
        self.root.geometry('415x300')  # base height: 415 x 100 (no buttons, just textbox)

        # textbox, where LaTeX input gets put, gets placed
        input_box = tk.Text(self.root, height=5, width=50)
        input_box.place(x=5, y=5)

        # place buttons based on dictionary items
        x = 5
        y = 200
        for binding in bindings:
            button = tk.Button(self.root, text=binding, width=2, height=2,
                               command=lambda string=bindings[binding]: key_pressed(string, input_box))
            button.place(x=x, y=y)
            x += 30

        self.root.mainloop()


win = Window()
