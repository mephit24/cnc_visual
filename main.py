import re
import time
import turtle


PATH = ''
DELAY = 0

def get_frames_arr_from_file(path_to_file) -> list:
    with open(path_to_file, 'r', encoding='UTF-8') as file:
        return file.read().split('\n')

class ClearFrame:

    _pattern = '([xX|yY|zZ])([\+|-]\d{6})'
    _coords_etalon = {'X': 0.0, 'Y': 0.0, 'Z': 0.0}  

    def __init__(self, dirty_frame):
        self._dirty_frame = dirty_frame
        _frames = re.findall(self._pattern, self._dirty_frame) 
        self._cleared_frame = self._coords_etalon | {i[0]: int(i[1]) / 100 for i in sorted(_frames)}
        
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


def check_sum_coords(cleared_frames_arr: tuple) -> bool: # TODO
    pass


def visualize(cleared_frames_arr: tuple[ClearFrame]):
    scr = turtle.Screen()
    scr.setup(1280, 800, startx=0, starty=0)
    scr.clear()

    xy_cur = turtle.Turtle()
    xy_cur.penup()
    xy_cur.speed(10)
    xy_cur.pensize(2)
    xy_cur.goto(-300, 50)
    xy_cur.pendown()
    xy_cur.speed(1)

    xz_cur = turtle.Turtle()
    xz_cur.penup()
    xz_cur.speed(10)
    xz_cur.pensize(2)
    xz_cur.goto(200, 50)
    xz_cur.pendown()
    xz_cur.speed(1)

    txt_cur = turtle.Turtle()
    txt_cur.penup()
    txt_cur.speed(10)
    txt_cur.setpos(400, 350)
    txt_cur.pendown()

    for frame in cleared_frames_arr:
        txt_cur.write(frame)
        txt_cur.penup()
        txt_cur.goto(txt_cur.pos() + (0, -15))
        txt_cur.pendown()
        
        xy_cur.setpos(xy_cur.pos() + frame.xy())
        xz_cur.setpos(xz_cur.pos() + frame.xz())
        time.sleep(DELAY)

    turtle.done()
    


if __name__ == '__main__':
    visualize(cleared_frames_arr(get_frames_arr_from_file(PATH)))
