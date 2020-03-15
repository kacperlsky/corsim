import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

top = tk.Tk()

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)
# a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5]) - This is just an example

canvas = FigureCanvasTkAgg(f, master=top)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

top.mainloop()
