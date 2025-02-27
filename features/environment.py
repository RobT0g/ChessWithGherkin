from behave import *
import time

step_latency = 2
def after_step(context, step):
    context.chess_board.display_board()
    time.sleep(step_latency)
