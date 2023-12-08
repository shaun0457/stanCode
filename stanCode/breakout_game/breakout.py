"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmousemoved, onmouseclicked

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    leben = NUM_LIVES
    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        if not graphics.switch:
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        if graphics.ball.y >= graphics.window.height:
            leben -= 1
            graphics.get_switch_true()
        graphics.remove_bricks()
        if graphics.score == 0 or leben == 0:
            break


if __name__ == '__main__':
    main()
