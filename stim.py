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

import serial
import binascii

ser = serial.Serial('COM3', 115200, timeout=1)

core.rush(True)

nIntervals = 260

n_elements, row_n, col_n = 30, 5, 6  # n_elements 指令数量;  rows 行;  columns 列

pos_y = np.linspace(-0.8, 0.8, row_n)
pos_x = np.linspace(-0.8, 0.8, col_n)

f = np.array([[12.0, 12.2, 12.4, 12.5, 12.7, 12.9],
              [11.0, 11.2, 11.4, 11.5, 11.7, 11.9],
              [10.0, 10.2, 10.4, 10.5, 10.7, 10.9],
              [9.0, 9.2, 9.4, 9.5, 9.7, 9.9],
              [8.0, 8.2, 8.4, 8.5, 8.7, 8.9],])

pos_rect = np.zeros([row_n * col_n, 2])
i = 0
for row in range(row_n):
    for col in range(col_n):
        pos_rect[i, 0] = pos_x[col]
        pos_rect[i, 1] = pos_y[row]
        i += 1

phy = np.array([i * 0.35 % 2 for i in range(n_elements)])  # 指令的相位

win = visual.Window([1920 / 2, 1080 / 2],
                    color=[-1, -1, -1],
                    fullscr=False,
                    allowGUI=False,
                    waitBlanking=True)

multi_stim = visual.ElementArrayStim(win=win, nElements=30, xys=pos_rect, sizes=0.15, elementTex='None',
                                     elementMask='None')

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
                             text='A',
                             font='Arial',
                             pos=(pos_x[0], pos_y[4]), wrapWidth=None, ori=0,
                             color=-1, colorSpace='rgb', opacity=1,
                             languageStyle='LTR',
                             depth=-1.0)
text_temp1.draw()
text_temp2 = visual.TextStim(win=win, name='A',
                             text='B',
                             font='Arial',
                             pos=(pos_x[1], pos_y[4]), wrapWidth=None, ori=0,
                             color=-1, colorSpace='rgb', opacity=1,
                             languageStyle='LTR',
                             depth=-1.0)
text_temp2.draw()
text_temp3 = visual.TextStim(win=win, name='A',
                             text='C',
                             font='Arial',
                             pos=(pos_x[2], pos_y[4]), wrapWidth=None, ori=0,
                             color=-1, colorSpace='rgb', opacity=1,
                             languageStyle='LTR',
                             depth=-1.0)
text_temp3.draw()
text_temp4 = visual.TextStim(win=win, name='A',
                             text='D',
                             font='Arial',
                             pos=(pos_x[3], pos_y[4]), wrapWidth=None, ori=0,
                             color=-1, colorSpace='rgb', opacity=1,
                             languageStyle='LTR',
                             depth=-1.0)
text_temp4.draw()
text_temp5 = visual.TextStim(win=win, name='A',
                             text='E',
                             font='Arial',
                             pos=(pos_x[4], pos_y[4]), wrapWidth=None, ori=0,
                             color=-1, colorSpace='rgb', opacity=1,
                             languageStyle='LTR',
                             depth=-1.0)
text_temp5.draw()
text_temp6 = visual.TextStim(win=win, name='A',
                             text='F',
                             font='Arial',
                             pos=(pos_x[5], pos_y[4]), wrapWidth=None, ori=0,
                             color=-1, colorSpace='rgb', opacity=1,
                             languageStyle='LTR',
                             depth=-1.0)
text_temp6.draw()
text_temp7 = visual.TextStim(win=win, name='A',
                             text='G',
                             font='Arial',
                             pos=(pos_x[0], pos_y[3]), wrapWidth=None, ori=0,
                             color=-1, colorSpace='rgb', opacity=1,
                             languageStyle='LTR',
                             depth=-1.0)
text_temp7.draw()
text_temp8 = visual.TextStim(win=win, name='A',
                             text='H',
                             font='Arial',
                             pos=(pos_x[1], pos_y[3]), wrapWidth=None, ori=0,
                             color=-1, colorSpace='rgb', opacity=1,
                             languageStyle='LTR',
                             depth=-1.0)
text_temp8.draw()
text_temp9 = visual.TextStim(win=win, name='A',
                             text='I',
                             font='Arial',
                             pos=(pos_x[2], pos_y[3]), wrapWidth=None, ori=0,
                             color=-1, colorSpace='rgb', opacity=1,
                             languageStyle='LTR',
                             depth=-1.0)
text_temp9.draw()
text_temp10 = visual.TextStim(win=win, name='A',
                              text='J',
                              font='Arial',
                              pos=(pos_x[3], pos_y[3]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp10.draw()
text_temp11 = visual.TextStim(win=win, name='A',
                              text='K',
                              font='Arial',
                              pos=(pos_x[4], pos_y[3]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp11.draw()
text_temp12 = visual.TextStim(win=win, name='A',
                              text='L',
                              font='Arial',
                              pos=(pos_x[5], pos_y[3]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp12.draw()
text_temp13 = visual.TextStim(win=win, name='A',
                              text='M',
                              font='Arial',
                              pos=(pos_x[0], pos_y[2]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp13.draw()
text_temp14 = visual.TextStim(win=win, name='A',
                              text='N',
                              font='Arial',
                              pos=(pos_x[1], pos_y[2]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp14.draw()
text_temp15 = visual.TextStim(win=win, name='A',
                              text='O',
                              font='Arial',
                              pos=(pos_x[2], pos_y[2]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp15.draw()
text_temp16 = visual.TextStim(win=win, name='A',
                              text='P',
                              font='Arial',
                              pos=(pos_x[3], pos_y[2]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp16.draw()
text_temp17 = visual.TextStim(win=win, name='A',
                              text='Q',
                              font='Arial',
                              pos=(pos_x[4], pos_y[2]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp17.draw()
text_temp18 = visual.TextStim(win=win, name='A',
                              text='R',
                              font='Arial',
                              pos=(pos_x[5], pos_y[2]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp18.draw()
text_temp19 = visual.TextStim(win=win, name='A',
                              text='S',
                              font='Arial',
                              pos=(pos_x[0], pos_y[1]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp19.draw()
text_temp20 = visual.TextStim(win=win, name='A',
                              text='T',
                              font='Arial',
                              pos=(pos_x[1], pos_y[1]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp20.draw()
text_temp21 = visual.TextStim(win=win, name='A',
                              text='U',
                              font='Arial',
                              pos=(pos_x[2], pos_y[1]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp21.draw()
text_temp22 = visual.TextStim(win=win, name='A',
                              text='V',
                              font='Arial',
                              pos=(pos_x[3], pos_y[1]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp22.draw()
text_temp23 = visual.TextStim(win=win, name='A',
                              text='W',
                              font='Arial',
                              pos=(pos_x[4], pos_y[1]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp23.draw()
text_temp24 = visual.TextStim(win=win, name='A',
                              text='X',
                              font='Arial',
                              pos=(pos_x[5], pos_y[1]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp24.draw()
text_temp25 = visual.TextStim(win=win, name='A',
                              text='Y',
                              font='Arial',
                              pos=(pos_x[0], pos_y[0]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp25.draw()
text_temp26 = visual.TextStim(win=win, name='A',
                              text='Z',
                              font='Arial',
                              pos=(pos_x[1], pos_y[0]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp26.draw()
text_temp27 = visual.TextStim(win=win, name='A',
                              text='1',
                              font='Times New Roman',
                              pos=(pos_x[2], pos_y[0]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp27.draw()
text_temp28 = visual.TextStim(win=win, name='A',
                              text='2',
                              font='Times New Roman',
                              pos=(pos_x[3], pos_y[0]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp28.draw()
text_temp29 = visual.TextStim(win=win, name='A',
                              text='3',
                              font='Times New Roman',
                              pos=(pos_x[4], pos_y[0]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp29.draw()
text_temp30 = visual.TextStim(win=win, name='A',
                              text='4',
                              font='Times New Roman',
                              pos=(pos_x[5], pos_y[0]), wrapWidth=None, ori=0,
                              color=-1, colorSpace='rgb', opacity=1,
                              languageStyle='LTR',
                              depth=-1.0)
text_temp30.draw()

trialdur = 3
waitdur = 2
numtrials = 30

win.flip()
core.wait(3)
draw_time = []

def sendTrigger():
    ser.write(b'\x01\xE1\x01\x00\xFF')
    core.wait(0.01)
    ser.write(0)
    print("send")

def sendTrigger_end():
    ser.write(b'\x01\xE1\x01\x00\xFE')
    core.wait(0.01)
    ser.write(0)
    print("send")

for trial in range(numtrials):
    # win.callOnFlip(sendTrigger, trial, 6)
    # win.callOnFlip(sendTrigger)
    sendTrigger()
    Trialclock = core.Clock()
    for frameN in range(nIntervals + 1):
        start_t = Trialclock.getTime()
        # win.callOnFlip(sendTrigger)

        multi_colors = np.zeros([row_n * col_n, 3])
        i = 0
        for row in range(row_n):
            for col in range(col_n):
                multi_colors[i, 0] = (math.sin(2 * math.pi * f[row, col] * frameN * 0.01666 + phy[col]))
                if f[row, col] == 0:
                    multi_colors[i, 0] = -1
                multi_colors[i, 1] = multi_colors[i, 0]
                multi_colors[i, 2] = multi_colors[i, 0]
                i += 1

        multi_stim.colors = multi_colors
        multi_stim.draw()
        text_temp1.draw()
        text_temp2.draw()
        text_temp3.draw()
        text_temp4.draw()
        text_temp5.draw()
        text_temp6.draw()
        text_temp7.draw()
        text_temp8.draw()
        text_temp9.draw()
        text_temp10.draw()
        text_temp11.draw()
        text_temp12.draw()
        text_temp13.draw()
        text_temp14.draw()
        text_temp15.draw()
        text_temp16.draw()
        text_temp17.draw()
        text_temp18.draw()
        text_temp19.draw()
        text_temp20.draw()
        text_temp21.draw()
        text_temp22.draw()
        text_temp23.draw()
        text_temp24.draw()
        text_temp25.draw()
        text_temp26.draw()
        text_temp27.draw()
        text_temp28.draw()
        text_temp29.draw()
        text_temp30.draw()

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

ser.close()
win.fullscr = False
win.close()

core.quit()
