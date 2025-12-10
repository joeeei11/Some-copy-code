#!/usr/bin/env python
# -*- coding: utf-8 -*-

from builtins import range
from psychopy import visual, logging, core, event
visual.useFBO = True  # if available (try without for comparison)
import math
import numpy as np

import matplotlib
matplotlib.use('Qt5Agg')  # change this to control the plotting 'back end'
import pylab

# import serial
import binascii

# ser = serial.Serial('COM3', 115200, timeout=1)

core.rush(True)

nIntervals = 260

row_n = 5
col_n = 5

pos_y = np.linspace(-0.7, 0.7, 5)
pos_x = np.linspace(-0.7, 0.7, 5)

f = np.array([[0.0, 0.0, 10.4, 0.0, 0.0],
              [0.0, 0.0, 10.2, 0.0, 0.0],
              [8.0, 9.0, 10.0, 11.0, 12.0],
              [0.0, 0.0, 9.8, 0.0, 0.0],
              [0.0, 0.0, 9.6, 0.0, 0.0]])

pos_rect = np.zeros([row_n*col_n, 2])
i = 0
for row in range(row_n):
    for col in range(col_n):
        pos_rect[i, 0] = pos_x[col]
        pos_rect[i, 1] = pos_y[row]
        i += 1

phy = [0, math.pi/4, math.pi/2, 3*math.pi/4, math.pi]c

win = visual.Window([1920/3, 1080/3],
                    color=[-1, -1, -1],
                    fullscr=False,
                    allowGUI=False,
                    waitBlanking=True)

multi_stim = visual.ElementArrayStim(win=win, nElements=25, xys = pos_rect, sizes = 0.15, elementTex = 'None', elementMask = 'None')
multi_stim.draw()
polygon = []
for row in range(row_n):
    for col in range(col_n):
        rect_temp = visual.Rect(
            win=win, name='polygon',
            width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
            ori=0, pos=(pos_x[col], pos_y[row]),
            lineWidth=1, lineColor=[1, 1, 1], lineColorSpace='rgb',
            fillColor=[1, 1, 1], fillColorSpace='rgb',
            opacity=1, depth=0.0, interpolate=True)

text_temp1 = visual.TextStim(win=win, name='A',
    text='B',
    font='Arial',
    pos=(pos_x[2], pos_y[1]), wrapWidth=None, ori=0,
    color=-1, colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0)
text_temp1.draw()
text_temp2 = visual.TextStim(win=win, name='A',
    text='L',
    font='Arial',
    pos=(pos_x[1], pos_y[2]), wrapWidth=None, ori=0,
    color=-1, colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0)
text_temp2.draw()
text_temp3 = visual.TextStim(win=win, name='A',
    text='L+',
    font='Arial',
    pos=(pos_x[0], pos_y[2]), wrapWidth=None, ori=0,
    color=-1, colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0)
text_temp3.draw()
text_temp4 = visual.TextStim(win=win, name='A',
    text='S',
    font='Arial',
    pos=(pos_x[2], pos_y[2]), wrapWidth=None, ori=0,
    color=-1, colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0)
text_temp4.draw()
text_temp5 = visual.TextStim(win=win, name='A',
    text='F',
    font='Arial',
    pos=(pos_x[2], pos_y[3]), wrapWidth=None, ori=0,
    color=-1, colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0)
text_temp5.draw()
text_temp6 = visual.TextStim(win=win, name='A',
    text='F+',
    font='Arial',
    pos=(pos_x[2], pos_y[4]), wrapWidth=None, ori=0,
    color=-1, colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0)
text_temp6.draw()
text_temp7 = visual.TextStim(win=win, name='A',
    text='B+',
    font='Arial',
    pos=(pos_x[2], pos_y[0]), wrapWidth=None, ori=0,
    color=-1, colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0)
text_temp7.draw()
text_temp8 = visual.TextStim(win=win, name='A',
    text='R',
    font='Arial',
    pos=(pos_x[3], pos_y[2]), wrapWidth=None, ori=0,
    color=-1, colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0)
text_temp8.draw()
text_temp9 = visual.TextStim(win=win, name='A',
    text='R+',
    font='Arial',
    pos=(pos_x[4], pos_y[2]), wrapWidth=None, ori=0,
    color=-1, colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0)
text_temp9.draw()

trialdur = 3
waitdur = 2
numtrials = 27

win.flip()
core.wait(3)
draw_time = []

def sendTrigger():
    ser.write(b'\x01\xE1\x01\x00\xFF')
    #core.wait(0.01)
    #ser.write(0)
    #print("send")

def sendTrigger_end():
    ser.write(b'\x01\xE1\x01\x00\xFE')
    #core.wait(0.01)
    #ser.write(0)
    #print("send")

for trial in range(numtrials):
    # win.callOnFlip(sendTrigger, trial, 6)
    #win.callOnFlip(sendTrigger)
    sendTrigger()
    Trialclock = core.Clock()
    for frameN in range(nIntervals + 1):
        start_t = Trialclock.getTime()
        # win.callOnFlip(sendTrigger)

        multi_colors = np.zeros([row_n*col_n, 3])
        i = 0
        for row in range(row_n):
            for col in range(col_n):
                multi_colors[i, 0] = (math.sin(2*math.pi*f[row, col]*frameN*0.01666 + phy[col]))
                if f[row, col] == 0:
                    multi_colors[i, 0] = -1
                multi_colors[i, 1] = multi_colors[i, 0]
                multi_colors[i, 2] = multi_colors[i, 0]
                i += 1

        multi_stim.colors = multi_colors
        multi_stim.draw()
        # text_temp1.draw()
        # text_temp2.draw()
        # text_temp3.draw()
        # text_temp4.draw()
        # text_temp5.draw()
        # text_temp6.draw()
        # text_temp7.draw()
        # text_temp8.draw()
        # text_temp9.draw()

        draw_time.append(Trialclock.getTime() - start_t)
        if event.getKeys():
            print('stopped early')
            break
        win.logOnFlip(msg='frame=%i' % frameN, level=logging.EXP)
        win.flip(clearBuffer=True)
    win.flip()
    sendTrigger_end()
    core.wait(waitdur)

    # reset clock for next trial



#ser.close()
win.fullscr = False
win.close()


core.quit()
