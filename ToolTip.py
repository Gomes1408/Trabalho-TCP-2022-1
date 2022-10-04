""" Adaptado de tk_ToolTip_class101.py
    Descrição original:
        gives a Tkinter widget a tooltip as the mouse is above the widget
        tested with Python27 and Python34  by  vegaseat  09sep2014
        www.daniweb.com/programming/software-development/code/484591/a-tooltip-class-for-tkinter
        Modified to include a delay time by Victor Zaccardo, 25mar16
"""

from tkinter import Toplevel, Label
class ToolTip(object):
    """
    creates a tooltip for a given widget
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 500  # tempo para apontar o cursor até aparecer a tooltip
        self.wraplength = 180  # tamanho base do widget
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()
    def leave(self, event=None):
        self.unschedule()
        self.hidetip()
    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)
    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)
    def showtip(self, event=None):
        """Cria uma janela toplevel e a esconde para exibir apenas a tooltip"""
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20

        self.tw = Toplevel(self.widget)  # cria a janela toplevel
        self.tw.wm_overrideredirect(True)  # deixa apenas a tooltip
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, 
            text=self.text,
            justify='left',
            background="#ffffff", 
            relief='solid', 
            borderwidth=1,
            wraplength=self.wraplength)
        label.pack(ipadx=1)
    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()