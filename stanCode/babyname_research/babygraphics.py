"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_co = (width - 2*GRAPH_MARGIN_SIZE) // len(YEARS)
    x_place = GRAPH_MARGIN_SIZE + year_index * x_co

    return x_place


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width = LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width = LINE_WIDTH)

    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT, width = LINE_WIDTH)

    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width = LINE_WIDTH)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text = YEARS[i], anchor = tkinter.NW)




def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    # 畫線:
    # 需要X1 X2 Y1 Y2, X1 X2 for i in range(len(year))
    # x1=i x2=i+1 找前後點 get_coordinate

    # y 的分布: (height - 2*Margin)/排名數(1000)
    # Y1:i 不確定是否有排名 if YEAR[i] in name_data[name]；
    #       如果有則有排名和位置  rank = name_data[name][YEAR[i]]; Y1 = (rank * y分布) + Margin; name = (x1+dx, y1, text = name, rank, color)
    #       如果沒位置為Y1 = Height - Margin(最底); 名字為* Y1 = (rank * y分布) + Margin; name = (x1+dx, y1, text = name, *, rank, color)
    # Y2:i+1 不確定是否有排名 if YEAR[i] in name_data[name]；如果有
    # Y2同理Y1


    rank_y = (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/1000
    color_num = 0

    for name in lookup_names:
        color_num += 1
        if color_num > 3:
            color_num = 0
        color = COLORS[color_num]
        for i in range(len(YEARS)-1):
            x1 = get_x_coordinate(CANVAS_WIDTH, i) # 1~11
            x2 = get_x_coordinate(CANVAS_WIDTH, i+1) # 2~12
            if str(YEARS[i]) in (name_data[name]):
                rank = name_data[name][str(YEARS[i])]
                y1 = int(rank) * rank_y +GRAPH_MARGIN_SIZE
                canvas.create_text(x1+TEXT_DX, y1, text=f'{name} {rank}', anchor = tkinter.SW, fill=color)
            else:#年份不在名字資料裡(無排名)
                y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                canvas.create_text(x1+TEXT_DX, y1, text=f'{name}, *', anchor = tkinter.SW,fill=color)

            if str(YEARS[i+1]) in (name_data[name]): #因前面i因x前後點問題-1 現在加1
                rank = name_data[name][str(YEARS[i+1])]
                y2 = int(rank) * rank_y + GRAPH_MARGIN_SIZE
                if i + 2 == len(YEARS): # 如果是最後一個資料 i+1 == 11 但len(YEARS)==12 所以這裡 i+2
                    canvas.create_text(x2+TEXT_DX, y2, text=f'{name} {rank}', anchor = tkinter.SW, fill=color)
            else:  # 年份不在名字資料裡(無排名)
                y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                if i + 2 == len(YEARS):
                    canvas.create_text(x2+TEXT_DX, y2, text=f'{name},*', anchor = tkinter.SW, fill=color)
            canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)





# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
