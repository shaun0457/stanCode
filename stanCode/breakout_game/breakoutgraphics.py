"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball



class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.bricks_rows = brick_rows
        self.bricks_coles = brick_cols
        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (self.window.width-self.paddle.width)/2, self.window.height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2 - ball_radius, y=window_height/2 - ball_radius)
        self.ball.filled = True
        # self.window.add(self.ball, window_width/2 - ball_radius, window_height/2 - ball_radius)
        self.ball_radius = ball_radius
        self.window.add(self.ball)

        # Default initial velocity for the ball
        # Initialize our mouse listeners\
        onmouseclicked(self.set_ball_velocity)
        onmousemoved(self.reset_position_mouse)

        # for velocity
        self.__dx = 0
        self.__dy = 0
        self.switch = True

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.bricks = GRect(width=brick_width, height=brick_height)
                self.bricks.filled = True
                # 依比例設定顏色
                if j < 0.2 * brick_rows:
                    self.bricks.fill_color = 'red'
                elif 0.2 * brick_rows <= j < 0.4 * brick_rows:
                    self.bricks.fill_color = 'green'
                elif 0.4 * brick_rows <= j < 0.6 * brick_rows:
                    self.bricks.fill_color = 'blue'
                elif 0.6 * brick_rows <= j < 0.8 * brick_rows:
                    self.bricks.fill_color = 'orange'
                else:
                    self.bricks.fill_color = 'yellow'
                self.window.add(self.bricks, i * (brick_width + brick_spacing), brick_offset + j*(brick_height + brick_spacing))

        self.score = self.bricks_rows * self.bricks_coles

    def set_ball_velocity(self, event):
        # click後，速度設定
        if self.switch:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = - self.__dx
        #click後開關打開
            self.switch = False

    # def rest_ball(self):
    #     self.window.add(self.ball)

    def reset_position_mouse(self, event):
        #平板位置隨滑鼠移動
        self.paddle.x = event.x - self.paddle.width / 2
        if self.paddle.x + self.paddle.width > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        elif self.paddle.x < 0:
            self.paddle.x = 0

    def get_dx(self):
        # 輸出速度給user端
        return self.__dx

    def get_dy(self):
        # 輸出速度給user端
        return self.__dy

    def get_switch_true(self):
        # getter 讓user端可以使用這段code
        # 死掉後，開關關起來且球回原位
        self.switch = True
        self.ball.x = self.window.width/2 - self.ball_radius
        self.ball.y = self.window.height/2 - self.ball_radius

    def remove_bricks(self):
        bricks_objects1 = self.window.get_object_at(self.ball.x, self.ball.y)
        bricks_objects2 = self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.ball_radius)
        bricks_objects3 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y)
        bricks_objects4 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y + 2 * self.ball_radius)
        if bricks_objects1 and bricks_objects1 is not self.paddle:
            self.window.remove(bricks_objects1)
            self.score -= 1
            # self.__dx = - self.__dx
            self.__dy = - self.__dy
        elif bricks_objects2:
            if bricks_objects2 is not self.paddle:
                self.window.remove(bricks_objects2)
                self.score -= 1
                # self.__dx = - self.__dx
                self.__dy = - self.__dy
            else:
                # self.__dx = - self.__dx
                self.ball.y = self.paddle.y - 2 * self.ball_radius
                self.__dy = - self.__dy

        elif bricks_objects3 and bricks_objects3 is not self.paddle:
            self.window.remove(bricks_objects3)
            self.score -= 1
            # self.__dx = - self.__dx
            self.__dy = - self.__dy
        elif bricks_objects4:
            if bricks_objects4 is not self.paddle:
                self.window.remove(bricks_objects4)
                self.score -= 1
                # self.__dx = - self.__dx
                self.__dy = - self.__dy
            else:
                # self.__dx = - self.__dx
                self.ball.y = self.paddle.y - 2 * self.ball_radius
                self.__dy = - self.__dy


        if self.ball.x <= 0 or self.ball.x + 2 * self.ball_radius >= self.window.width:
            self.__dx = - self.__dx
        if self.ball.y <= 0:
            self.__dy = - self.__dy
