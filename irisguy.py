import tkinter as tk
from main-iris import Iris

class IrisGUI:
    def __init__(self, master):
        self.master = master
        master.title("Iris")

        self.query_label = tk.Label(master, text="Enter your command:")
        self.query_label.pack()

        self.query_entry = tk.Entry(master, width=50, borderwidth=3)
        self.query_entry.pack()

        self.execute_button = tk.Button(master, text="Execute", command=self.execute_query)
        self.execute_button.pack()

        self.result_text = tk.Text(master, height=10, width=50, borderwidth=3)
        self.result_text.pack()

        self.iris = Iris()

    def execute_query(self):
        query = self.query_entry.get()
        result = self.iris.execute_query(query)
        self.result_text.insert(tk.END, result)

root = tk.Tk()
my_gui = IrisGUI(root)
root.mainloop()