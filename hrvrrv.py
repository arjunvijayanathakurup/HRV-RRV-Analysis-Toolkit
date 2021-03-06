#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Dec 12, 2019 11:49:54 AM IST  platform: Windows NT

import sys
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import Canvas
from tkinter import messagebox
import mne
import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join
from scipy.signal import butter, freqs, filtfilt
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from matplotlib.figure import Figure
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from RRV_preview import vp_start_rrvpreview
from HRV_preview import vp_start_hrvpreview, send_hrv_preview
import configparser
from os.path import join as pjoin
from hrv import send_hrv_process
# from hrv import *
from rrvnew import *

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import hrvrrv_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, top
    root = tk.Tk()
    hrvrrv_support.set_Tk_var()
    top = Anxity (root)
    hrvrrv_support.init(root, top)
    
    root.protocol("WM_DELETE_WINDOW", destroy_root)
    # root.protocol("WM_DELETE_WINDOW", destroy_Anxity)
    # root.protocol("WM_DELETE_WINDOW", hrvrrv_support.destroy_window)
    root.mainloop()

w = None

def destroy_root():
    global root
    root.quit()
    # root = None

def create_Anxity(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    hrvrrv_support.set_Tk_var()
    top = Anxity (w)
    hrvrrv_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Anxity():
    global w, root
    root.destroy()
    w.destroy()
    root = None
    w = None

def channel_id(channel, val):   
    j =0
    for i in channel:
        if(i == val):
            return j
        j+=1

class Anxity:

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1279x696+54+21")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("HRV RRV Analysis Toolkit")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#646464646464")

        self.readedfbtn = tk.Button(top, command=self.openFile)
        self.readedfbtn.place(relx=0.07, rely=0.172, height=44, width=97)
        self.readedfbtn.configure(activebackground="#ececec")
        self.readedfbtn.configure(activeforeground="#000000")
        self.readedfbtn.configure(background="#d9d9d9")
        self.readedfbtn.configure(disabledforeground="#a3a3a3")
        self.readedfbtn.configure(foreground="#000000")
        self.readedfbtn.configure(highlightbackground="#d9d9d9")
        self.readedfbtn.configure(highlightcolor="black")
        self.readedfbtn.configure(pady="0")
        self.readedfbtn.configure(text='''Read EDF''')

        self.filestat = tk.Label(top)
        self.filestat.place(relx=0.195, rely=0.158, height=21, width=884)
        self.filestat.configure(activebackground="#f9f9f9")
        self.filestat.configure(activeforeground="black")
        self.filestat.configure(background="#d9d9d9")
        self.filestat.configure(disabledforeground="#a3a3a3")
        self.filestat.configure(foreground="#000000")
        self.filestat.configure(highlightbackground="#d9d9d9")
        self.filestat.configure(highlightcolor="black")
        self.filestat.configure(justify='left')
        self.filestat.configure(text='''No file Selected''')

        self.TProgressbar1 = ttk.Progressbar(top)
        self.TProgressbar1.place(relx=0.195, rely=0.201, relwidth=0.727
                , relheight=0.0, height=22)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.203, rely=0.043, height=51, width=734)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {@Adobe Fangsong Std R} -size 30 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''HRV RRV Analysis Toolkit''')

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.008, rely=0.287, relwidth=0.985)

        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.493, rely=0.287, relheight=0.69)
        self.TSeparator2.configure(orient="vertical")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.TSeparator3 = ttk.Separator(top)
        self.TSeparator3.place(relx=0.008, rely=0.345, relwidth=0.985)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.172, rely=0.302, height=21, width=154)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''HRV''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.672, rely=0.302, height=21, width=174)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''RRV''')

        self.previewHrvBtn = tk.Button(top, command = self.hrv_preview)
        self.previewHrvBtn.place(relx=0.390, rely=0.302, height=24, width=120)
        self.previewHrvBtn.configure(activebackground="#ececec")
        self.previewHrvBtn.configure(activeforeground="#000000")
        self.previewHrvBtn.configure(background="#d9d9d9")
        self.previewHrvBtn.configure(disabledforeground="#a3a3a3")
        self.previewHrvBtn.configure(foreground="#000000")
        self.previewHrvBtn.configure(highlightbackground="#d9d9d9")
        self.previewHrvBtn.configure(highlightcolor="black")
        self.previewHrvBtn.configure(pady="0")
        self.previewHrvBtn.configure(text='''Preview Filtered Data''')

        self.previewRrvBtn = tk.Button(top, command = self.rrv_preview)
        self.previewRrvBtn.place(relx=0.890, rely=0.302, height=24, width=120)
        self.previewRrvBtn.configure(activebackground="#ececec")
        self.previewRrvBtn.configure(activeforeground="#000000")
        self.previewRrvBtn.configure(background="#d9d9d9")
        self.previewRrvBtn.configure(disabledforeground="#a3a3a3")
        self.previewRrvBtn.configure(foreground="#000000")
        self.previewRrvBtn.configure(highlightbackground="#d9d9d9")
        self.previewRrvBtn.configure(highlightcolor="black")
        self.previewRrvBtn.configure(pady="0")
        self.previewRrvBtn.configure(text='''Preview Filtered Data''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.047, rely=0.79, height=21, width=78)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Starting Point''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.047, rely=0.833, height=21, width=74)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Ending Point''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.117, rely=0.833,height=20, relwidth=0.12)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.117, rely=0.79,height=20, relwidth=0.12)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")
        self.Entry2.configure(text = '''0''')

        self.TProgressbar2 = ttk.Progressbar(top)
        self.TProgressbar2.place(relx=0.031, rely=0.905, relwidth=0.383
                , relheight=0.0, height=22)

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.594, rely=0.848,height=20, relwidth=0.128)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")

        self.Entry4 = tk.Entry(top)
        self.Entry4.place(relx=0.821, rely=0.848,height=20, relwidth=0.136)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(selectforeground="black")

        self.Label4_2 = tk.Label(top)
        self.Label4_2.place(relx=0.516, rely=0.848, height=21, width=78)
        self.Label4_2.configure(activebackground="#f9f9f9")
        self.Label4_2.configure(activeforeground="black")
        self.Label4_2.configure(background="#d9d9d9")
        self.Label4_2.configure(disabledforeground="#a3a3a3")
        self.Label4_2.configure(foreground="#000000")
        self.Label4_2.configure(highlightbackground="#d9d9d9")
        self.Label4_2.configure(highlightcolor="black")
        self.Label4_2.configure(text='''Starting point''')

        self.Label5_4 = tk.Label(top)
        self.Label5_4.place(relx=0.751, rely=0.848, height=21, width=74)
        self.Label5_4.configure(activebackground="#f9f9f9")
        self.Label5_4.configure(activeforeground="black")
        self.Label5_4.configure(background="#d9d9d9")
        self.Label5_4.configure(disabledforeground="#a3a3a3")
        self.Label5_4.configure(foreground="#000000")
        self.Label5_4.configure(highlightbackground="#d9d9d9")
        self.Label5_4.configure(highlightcolor="black")
        self.Label5_4.configure(text='''Ending Point''')

        self.TProgressbar3 = ttk.Progressbar(top)
        self.TProgressbar3.place(relx=0.516, rely=0.905, relwidth=0.383
                , relheight=0.0, height=22)

        self.processhrv = tk.Button(top, command = lambda: send_hrv_process(self.y_peaks, self.x, self.y, self.sig, self.filename, self.TProgressbar2))        
        self.processhrv.place(relx=0.43, rely=0.905, height=24, width=57)
        self.processhrv.configure(activebackground="#ececec")
        self.processhrv.configure(activeforeground="#000000")
        self.processhrv.configure(background="#d9d9d9")
        self.processhrv.configure(disabledforeground="#a3a3a3")
        self.processhrv.configure(foreground="#000000")
        self.processhrv.configure(highlightbackground="#d9d9d9")
        self.processhrv.configure(highlightcolor="black")
        self.processhrv.configure(pady="0")
        self.processhrv.configure(text='''Process''')

        self.processrrv = tk.Button(top, command = lambda: vp_start_rrvprocess(self.y_peaks, self.x, self.y, self.sig, self.filename, self.TProgressbar3))
        self.processrrv.place(relx=0.915, rely=0.905, height=24, width=61)
        self.processrrv.configure(activebackground="#ececec")
        self.processrrv.configure(activeforeground="#000000")
        self.processrrv.configure(background="#d9d9d9")
        self.processrrv.configure(disabledforeground="#a3a3a3")
        self.processrrv.configure(foreground="#000000")
        self.processrrv.configure(highlightbackground="#d9d9d9")
        self.processrrv.configure(highlightcolor="black")
        self.processrrv.configure(pady="0")
        self.processrrv.configure(text='''Process''')

        self.var = tk.StringVar()

        self.style.map('TRadiobutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.chest = ttk.Radiobutton(top)
        self.chest.place(relx=0.538, rely=0.785, relwidth=0.062, relheight=0.0
                , height=21)
        self.chest.configure(variable=self.var, value = 'CHEST')
        self.chest.configure(text='''Chest''')

        self.abdomen = ttk.Radiobutton(top)
        self.abdomen.place(relx=0.616, rely=0.785, relwidth=0.059, relheight=0.0
                , height=21)
        self.abdomen.configure(variable=self.var, value = 'ABD')
        self.abdomen.configure(text='''Abdomen''')

        self.flow = ttk.Radiobutton(top)
        self.flow.place(relx=0.718, rely=0.785, relwidth=0.037, relheight=0.0
                , height=21)
        self.flow.configure(variable=self.var, value = 'FLOW')
        self.flow.configure(text='''Flow''')

        self.TSeparator4 = ttk.Separator(top)
        self.TSeparator4.place(relx=0.993, rely=0.287, relheight=0.69)
        self.TSeparator4.configure(orient="vertical")

        self.TSeparator5 = ttk.Separator(top)
        self.TSeparator5.place(relx=0.008, rely=0.977, relwidth=0.985)

        self.TSeparator6 = ttk.Separator(top)
        self.TSeparator6.place(relx=0.008, rely=0.287, relheight=0.69)
        self.TSeparator6.configure(orient="vertical")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.039, rely=0.374, relheight=0.395
                , relwidth=0.434)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(self.Frame1)
        self.Canvas1.place(relx=0.018, rely=0.036, relheight=0.92, relwidth=0.96)

        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.516, rely=0.374, relheight=0.395
                , relwidth=0.442)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Canvas2 = tk.Canvas(self.Frame2)
        self.Canvas2.place(relx=0.018, rely=0.036, relheight=0.92
                , relwidth=0.961)
        self.Canvas2.configure(background="#d9d9d9")
        self.Canvas2.configure(borderwidth="2")
        self.Canvas2.configure(highlightbackground="#d9d9d9")
        self.Canvas2.configure(highlightcolor="black")
        self.Canvas2.configure(insertbackground="black")
        self.Canvas2.configure(relief="ridge")
        self.Canvas2.configure(selectbackground="#c4c4c4")
        self.Canvas2.configure(selectforeground="black")

        self.Button1 = tk.Button(top, command = self.load_config_hrv)
        self.Button1.place(relx=0.375, rely=0.805, height=24, width=57)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Load''')

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.289, rely=0.805, height=21, width=99)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Parameter Config''')

        self.Button2 = tk.Button(top, command = self.save_config_hrv)
        self.Button2.place(relx=0.43, rely=0.805, height=24, width=57)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Save''')

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.774, rely=0.79, height=21, width=99)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Parameter Config''')

        self.Button3 = tk.Button(top, command = self.load_config_rrv)
        self.Button3.place(relx=0.86, rely=0.79, height=24, width=57)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Load''')

        self.Button4 = tk.Button(top, command = self.save_config_rrv)
        self.Button4.place(relx=0.915, rely=0.79, height=24, width=55)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Save''')

        # self.Button1 = tk.Button(top)
        # self.Button1.place(relx=0.465, rely=0.950, height=24, width=70)
        # self.Button1.configure(activebackground="#ececec")
        # self.Button1.configure(activeforeground="#000000")
        # self.Button1.configure(background="#d9d9d9")
        # self.Button1.configure(disabledforeground="#a3a3a3")
        # self.Button1.configure(foreground="#000000")
        # self.Button1.configure(highlightbackground="#d9d9d9")
        # self.Button1.configure(highlightcolor="black")
        # self.Button1.configure(pady="0")
        # self.Button1.configure(text='''Predict''')


        self.y_peaks = 0
        self.x = 0
        self.y = 0
        self.sig = 0
    def openFile(self):
        import time
        self.TProgressbar1['value'] = 0
        time.sleep(0.5) 
        self.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("EDF files","*.edf"),("all files","*.*")))
        # print(filename)
        self.TProgressbar1['value'] = 20
        time.sleep(0.5) 
        self.data = mne.io.read_raw_edf(self.filename)
        self.TProgressbar1['value'] = 40
        time.sleep(0.5) 
        self.raw_data = self.data.get_data()
        self.TProgressbar1['value'] = 50
        time.sleep(0.5)
        # you can get the metadata included in the file and a list of all channels:
        self.info = self.data.info
        self.TProgressbar1['value'] = 60
        time.sleep(0.5) 
        self.channels = self.data.ch_names
        self.TProgressbar1['value'] = 80
        time.sleep(0.5) 
        self.filestat['text'] = " Loaded: "+ self.filename
        self.TProgressbar1['value'] = 100

    def hrv_preview (self):
        data = mne.io.read_raw_edf(self.filename)
        raw_data = data.get_data()
        # you can get the metadata included in the file and a list of all channels:
        # info = data.info
        channels = data.ch_names
        ecgl = raw_data[channel_id(channels, "ECGL")]
        ecgr = raw_data[channel_id(channels, "ECGR")]
        sig = ecgl- ecgr
        del data
        del ecgl
        del ecgr

        self.st = self.Entry1.get()
        self.en = self.Entry2.get()
        if self.Entry1.get():
            pass
        else:
            self.Entry1.insert(0, str(len(sig)));
            # messagebox.showwarning("Warning", "Please enter the starting position")
            
        if self.Entry2.get():
            pass
        else:
            self.Entry2.insert(0, str(0))
            # messagebox.showwarning("Warning", "Please enter the ending position")

        self.st = int(self.st)
        self.en = int(self.en)

        sig = sig[self.en : self.st]
        fs = 256
        n = len(sig)
        fc = 4
        duration_sec = n / fs
        duration_min = duration_sec / 60

        b, a = butter(6, fc/(fs/2), 'low', analog=False)
        y = filtfilt(b, a, sig)
        peaks, _ = find_peaks(y, distance = 150, height=0)
        beat_count = len(peaks)
        self.y_peaks = y[peaks]
        self.x = peaks
        self.y = y
        self.sig = sig
        del beat_count
        del duration_min

        config = configparser.ConfigParser()
        config['Process configuration'] = {'y_peaks': self.y_peaks, 'x': self.x, 'y': self.y, 'sig': self.sig, 'filename': self.filename, 'Tprogressbar': self.TProgressbar2}
        with open(self.filename+'hrv_process.ini', 'w') as configfile:
            config.write(configfile)
        send_hrv_preview(top, self.y, self.x, self.y_peaks)

    def rrv_preview(self):
        data = mne.io.read_raw_edf(self.filename)
        raw_data = data.get_data()
        # isnfo = data.info
        channels = data.ch_names
        fs = 256
        fc = 0.5   

        sel_val = self.var.get()
        self.radio_button_val = sel_val
        
        if sel_val == 'FLOW':
            b, a = butter(6, fc/(fs/2), 'low', analog=False)
            sig = raw_data[channel_id(channels, "FLOW")]
            self. str = self.Entry3.get()
            self.enr = self.Entry4.get()
            if self.Entry3.get():
                pass
            else:
                self.Entry3.insert(0, str(0))
                # messagebox.showwarning("Warning", "Please enter the starting position")
                
            if self.Entry4.get():
                pass
            else:
                self.Entry4.insert(0, str(len(sig)))
                # messagebox.showwarning("Warning", "Please enter the ending position")
            self.str = int(self.str)
            self.enr = int(self.enr) 

            sig = sig[self.str:self.enr]
            # Filtering the signal
            y = filtfilt(b, a, sig)
            peaks, _ = find_peaks(y, distance = 150, height=0)
            peaks_num = (len(peaks))
            x = y[peaks]
            v = peaks
            p = y
            self.y_peaks = y[peaks]
            self.x = peaks
            self.y = y
            self.sig = sig
            vp_start_rrvpreview(p, v, x, 1)

            
        elif sel_val == 'ABD':
            b, a = butter(6, fc/(fs/2), 'low', analog=False)
            sig = raw_data[channel_id(channels, "ABD")]
            
            self. str = self.Entry3.get()
            self.enr = self.Entry4.get()
            if self.Entry3.get():
                pass
            else:
                self.Entry3.insert(0, str(0))
                # messagebox.showwarning("Warning", "Please enter the starting position")
                
            if self.Entry4.get():
                pass
            else:
                self.Entry4.insert(0, str(len(sig)))
                # messagebox.showwarning("Warning", "Please enter the ending position")
            self.str = int(self.str)
            self.enr = int(self.enr)


            sig = sig[self.str:self.enr]
            # Filtering the signal
            y = filtfilt(b, a, sig)
            peaks, _ = find_peaks(y, distance = 150, height=0)
            peaks_num = (len(peaks))
            x = y[peaks]
            v = peaks
            p = y
            self.y_peaks = y[peaks]
            self.x = peaks
            self.y = y
            self.sig = sig
            vp_start_rrvpreview(p, v, x, 2)

            
        else:
            b, a = butter(6, fc/(fs/2), 'low', analog=False)
            sig = raw_data[channel_id(channels, "CHEST")]
            
            self. str = self.Entry3.get()
            self.enr = self.Entry4.get()
            if self.Entry3.get():
                pass
            else:
                self.Entry3.insert(0, str(0))
                # messagebox.showwarning("Warning", "Please enter the starting position")
                
            if self.Entry4.get():
                pass
            else:
                self.Entry4.insert(0, str(len(sig)))
                # messagebox.showwarning("Warning", "Please enter the ending position")
            self.str = int(self.str)
            self.enr = int(self.enr)


            sig = sig[self.str:self.enr]
            # Filtering the signal
            y = filtfilt(b, a, sig)
            peaks, _ = find_peaks(y, distance = 150, height=0)
            peaks_num = (len(peaks))
            x = y[peaks]
            v = peaks
            p = y
            self.y_peaks = y[peaks]
            self.x = peaks
            self.y = y
            self.sig = sig
            vp_start_rrvpreview(p, v, x, 3)


        del data      

    def save_config_hrv(self):
        file = [('Text Document', '*.txt')] 
        f = filedialog.asksaveasfile(mode='w', filetypes = file, defaultextension = file)
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        text = "File Name :" + self.filename + "\n" +  'Starting Point :' + str(self.st) + "\n" + 'Ending Point :' +  str(self.en)
        f.write(text)
        f.close()

    def load_config_hrv(self):
        file = [('Text Document', '*.txt')] 
        f = filedialog.askopenfilename(title = "Select File", filetypes = file)
        with open(f, 'r') as file:
            fi = file.read()
            newval = fi.split('\n')
            print(newval)
            for i in range(0, len(newval)):
                if(newval[i].split(':')[0] == 'Starting Point '):
                    self.Entry1.delete(0, tk.END)
                    self.Entry1.insert(0, int((newval[i].split(':')[1])))
                elif (newval[i].split(':')[0] == 'Ending Point '):
                    self.Entry2.delete(0, tk.END)
                    self.Entry2.insert(0, int((newval[i].split(':')[1])))

    def save_config_rrv(self):
        file = [('Text Document', '*.txt')] 
        f = filedialog.asksaveasfile(mode='w', filetypes = file, defaultextension = file)
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        text = "File Name :" + self.filename + "\n" +  'Starting Point :' + str(self.str) + "\n" + 'Ending Point :' +  str(self.enr) + "\n" + 'Channel Field :' + self.radio_button_val
        f.write(text)
        f.close()

    def load_config_rrv(self):
        file = [('Text Document', '*.txt')] 
        f = filedialog.askopenfilename(title = "Select File", filetypes = file)
        with open(f, 'r') as file:
            fi = file.read()
            newval = fi.split('\n')
            print(newval)
            for i in range(0, len(newval)):
                if(newval[i].split(':')[0] == 'Starting Point '):
                    self.Entry3.delete(0, tk.END)
                    self.Entry3.insert(0, int((newval[i].split(':')[1])))
                elif (newval[i].split(':')[0] == 'Ending Point '):
                    self.Entry4.delete(0, tk.END)
                    self.Entry4.insert(0, int((newval[i].split(':')[1])))
                elif(newval[i].split(':')[0] == 'Channel Field '):
                    temp_val = (newval[i].split(':')[1])
                    if temp_val == 'FLOW':
                        self.var.set('FLOW')
                    elif temp_val == 'ABD':
                        self.var.set('ABD')
                    else:
                        self.var.set('CHEST')
        # self.Entry3.delete(0, tk.END)
        # self.Entry3.insert(0, start_p)
        # self.Entry4.delete(0, tk.END)
        # self.Entry4.insert(0, end_p)

    def progress_hrv(self, val):
        self.TProgressbar2['value'] = int(val)

    def progress_rrv(self, val):
        self.TProgressbar3['value'] = int(val)

    # def predict():


if __name__ == '__main__':
    vp_start_gui()





