import re
import time
import turtle


PATH = ''
DELAY = 0

def get_frames_arr_from_file(path_to_file) -> list:
    with open(path_to_file, 'r', encoding='UTF-8') as file:
        return file.read().split('\n')

class ClearFrame:

    _pattern = r'([xX|yY|zZ])([\+|-]?\d{4}\.?\d{2})'
    _zero_coords = {'X': 0.0, 'Y': 0.0, 'Z': 0.0}  

    def __init__(self, dirty_frame):
        self._dirty_frame = dirty_frame
        _frame = re.findall(self._pattern, self._dirty_frame)
        self._frame_dict = {coord[0]: int(coord[1].replace('.', '')) / 100 for coord in sorted(_frame)}
        self._cleared_frame = self._zero_coords | self._frame_dict
        
    def __repr__(self):
        return self._dirty_frame

    def xyz_dict(self) -> dict:
        return self._cleared_frame

    def xyz(self) -> tuple[float]:
        return tuple(self._cleared_frame.values())

    def xy(self) -> tuple[float]:
        return self.xyz()[0], self.xyz()[1]

    def xz(self) -> tuple[float]:
        return self.xyz()[0], self.xyz()[2]


def cleared_frames_arr(dirty_frames_arr: list) -> tuple[ClearFrame]:
    cleared_arr = []
    for frame in dirty_frames_arr:
        cleared_arr.append(ClearFrame(frame))
    return tuple(cleared_arr)


def check_sum_coords(cleared_frames_arr):
    xgen = (coor.xyz()[0] for coor in cleared_frames_arr)
    ygen = (coor.xyz()[1] for coor in cleared_frames_arr)
    zgen = (coor.xyz()[2] for coor in cleared_frames_arr)
    return (sum(xgen), sum(ygen), sum(zgen))


def visualize(cleared_frames_arr: tuple[ClearFrame], manual=False):
    scr = turtle.Screen()
    scr.setup(1280, 900, startx=0, starty=0)
    scr.clear()

    xy_cur = turtle.Turtle()
    xy_cur.penup()
    xy_cur.speed(10)
    xy_cur.pensize(2)
    xy_cur.goto(-300, 50)
    xy_cur.pendown()
    xy_cur.speed(3)

    xz_cur = turtle.Turtle()
    xz_cur.penup()
    xz_cur.speed(10)
    xz_cur.pensize(2)
    xz_cur.goto(200, 50)
    xz_cur.pendown()
    xz_cur.speed(3)

    txt_cur = turtle.Turtle()
    txt_cur.penup()
    txt_cur.speed(10)
    txt_cur.setpos(400, 400)
    txt_cur.pendown()

    for frame in cleared_frames_arr:
        txt_cur.write(frame)
        txt_cur.penup()
        txt_cur.goto(txt_cur.pos() + (0, -12))
        txt_cur.pendown()

        xy_cur.setpos(xy_cur.pos() + frame.xy())
        xz_cur.setpos(xz_cur.pos() + frame.xz())
        if manual:
            turtle.numinput('Next', 'Step (only 1):', default=1, minval=1, maxval=1)
            continue
        time.sleep(DELAY)

    turtle.done()


if __name__ == '__main__':
    visualize(cleared_frames_arr(get_frames_arr_from_file(PATH)))
