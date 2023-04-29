import sys
import tkinter
from tkinter import filedialog

from main import get_frames_arr_from_file, cleared_frames_arr, check_sum_coords, visualize


window = tkinter.Tk()
path = filedialog.askopenfilename()
window.destroy()

window = tkinter.Tk()
window.title('CNC_visual')
window.geometry('150x150+1500-800')


def coord_sum_output():
    output.delete(1.0, 'end')
    coord_sum = check_sum_coords(cleared_frames_arr(get_frames_arr_from_file(path)))
    coord_sum = f'Sum of coordinats:\nX: {coord_sum[0]}\nY: {coord_sum[1]}\nZ: {coord_sum[2]}'
    output.insert(1.0, coord_sum)

    
btn_redraw = tkinter.Button(window, text='REDRAW',
                     command= lambda: [coord_sum_output(),
                                       visualize(cleared_frames_arr(get_frames_arr_from_file(path)))
                                       ])
btn_redraw.pack(fill='x')
btn_redraw.focus()

btn_redraw_m = tkinter.Button(window, text='REDRAW MANUAL',
                     command= lambda: [coord_sum_output(),
                                       visualize(cleared_frames_arr(get_frames_arr_from_file(path)), manual=True)
                                       ])
btn_redraw_m.pack(fill='x')

btn_exit = tkinter.Button(window, text='Exit', command=sys.exit)
btn_exit.pack(anchor='s', expand=True)

output = tkinter.Text()

output.pack()

window.mainloop()
