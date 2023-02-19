import tkinter as tk

bindings = {
    'Math Symbols': 'SEPARATOR',
    '∧': '\\land',
    '∨': '\\lor',
    '¬': '\\lnot',
    '≤': '\\leq',
    '≥': '\\geq',
    '≠': '\\neq',
    '≡': '\\equiv',
    '≅': '\\cong',
    '≃': '\\simeq',
    '∼': '\\sim',
    '≈': '\\approx',
    '×': '\\times',
    '÷': '\\div',
    '±': '\\pm',
    '·': '\\cdot',
    '∘': '\\circ',
    '\'': '\\prime',
    '⋯': '\\cdots',
    '∞': '\\infty',
    '⊃': '\\supset',
    '⊅': '\\not\\supset',
    '⊂': '\\subset',
    '⊄': '\\not\\subset',
    '⊆': '\\subseteq',
    '⊈': '\\nsubseteq',
    '⊇': '\\supseteq',
    '⊉': '\\nsupseteq',
    '∀': '\\forall',
    '∃': '\\exists',
    '∈': '\\in',
    '∉': '\\notin',
    '→': '\\rightarrow',
    '←': '\\leftarrow',
    '⇒': '\\Rightarrow',
    '⇐': '\\Leftarrow',
    '⇔': '\\Leftrightarrow',
    '∪': '\\cup',
    '∩': '\\cap',
    '|': '\\mid',
    '∥': '\\parallel',
    '⊥': '\\perp',
}

'''
When a button is pressed, insert 'string' to the end of the current text in the 'tbox' object
'''


def binding_pressed(string, tbox):
    tbox.insert(tk.INSERT, string)


'''
Draw buttons for all items in the bindings dictionary that match 'filter'.
Drawing starts at 'x' and 'y'. Automatically moves down a row when 'x' exceeds 'max_width'.
Items drawn on 'root'.
'''


def draw_contents(max_width, root, x=10, y=90, filter='', input_text='', top_state=False):
    # if we redraw, destroy everything
    for widget in root.winfo_children():
        widget.destroy()

    # textbox, where LaTeX input gets put, gets placed
    input_box = tk.Text(root, height=5, width=50)
    input_box.place(x=5, y=5)
    input_box.insert('1.0', input_text)  # insert new text

    # place search box and "on top" checkbox
    search_box = tk.Text(root, height=1, width=10)
    search_box.place(x=155, y=95)

    toggle_on_top = tk.BooleanVar(value=top_state)
    on_top = tk.Checkbutton(root, variable=toggle_on_top, text='Keep window on top',
                            command=lambda b=toggle_on_top: root.wm_attributes('-topmost', b.get()))
    on_top.place(x=280, y=95)

    search_button = tk.Button(root, height=1, width=5, text='Search',
                              command=lambda: draw_contents(max_width, root,
                                                            filter=search_box.get('1.0', 'end').rstrip('\n'),
                                                            input_text=input_box.get('1.0', 'end').rstrip('\n'),
                                                            top_state=toggle_on_top.get()))
    search_button.place(x=225, y=92)

    # place buttons and labels based on dictionary items
    for binding in bindings:
        if bindings[binding] == 'SEPARATOR':
            x = 10
            if not y == 90:
                y += 30
            label = tk.Label(root, text=binding, font=("Helvetica", 14, "bold"))
            label.place(x=x, y=y)
            if y == 90:
                y += 30
        else:
            if filter in bindings[binding]:
                button = tk.Button(root, text=binding, width=2, height=2,
                                   command=lambda string=bindings[binding]: binding_pressed(string, input_box))
                button.place(x=x, y=y)
                x += 30
                if x > max_width - 50:
                    x = 5
                    y += 50

    root.geometry(str(max_width) + 'x' + str(y + 50))  # base height: 415 x 100 (no buttons, just textbox)


class Window:

    def __init__(self):
        self.root = tk.Tk()

        win_width = 415

        self.root.title('LaTeX Keyboard')

        draw_contents(win_width, self.root, filter='')

        self.root.mainloop()


win = Window()
