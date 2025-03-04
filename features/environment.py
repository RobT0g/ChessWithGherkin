from behave import *
import time

step_latency = 0.05
def before_step(context, step):
    '''This function is called before each step is executed'''
    pass

def after_step(context, step):
    '''This function is called after each step is executed'''
    context.chess_board.display_board()
    time.sleep(step_latency)
