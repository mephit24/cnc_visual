import sys
import tkinter
from tkinter import filedialog

import main


window = tkinter.Tk()
path = filedialog.askopenfilename()
window.destroy()

window = tkinter.Tk()
window.title('CNC_visual')
window.geometry('50x150+1500-800')

btn_redraw = tkinter.Button(window, text='REDRAW',
                     command=lambda: main.visualize(main.cleared_frames_arr(main.get_frames_arr_from_file('myfile.txt'))))
btn_redraw.grid(column=0)
btn_redraw.focus()
btn_redraw.pack(fill='x')

btn_exit = tkinter.Button(window, text='Exit', command=sys.exit)
btn_exit.pack(anchor='s', expand=True)

window.mainloop()
