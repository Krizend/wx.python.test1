import wx, random
from math import sqrt

APP_EXIT = 1
APP_DRAW = 2

class MyFrame(wx.Frame):

    def __init__(self, parent, title='MyFrame Object'):
        super().__init__(parent=parent, title=title, size=(500,500), style= wx.SYSTEM_MENU | wx.CLIP_CHILDREN)

        menubar = wx.MenuBar()
        filemenu = wx.Menu()
        # item = wx.MenuItem(filemenu, wx.ID_EXIT, "&Выход", "Выход из приложения")
        # filemenu.Append(item)
        filemenu.Append(APP_EXIT, 'Exit\tCtrl+Q', 'Выходи из программы')
        filemenu.Append(APP_DRAW, 'Draw\tCtrl+D', 'Нарисовать рандомные линии')

        menubar.Append(filemenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.onQuit, id=APP_EXIT)
        self.Bind(wx.EVT_MENU, self.OnPaint, id=APP_DRAW)
        self.Centre()
        self.Show(True)


        self.color = {
            'blue': wx.Colour(0, 0, 255),
            'red': wx.Colour(255, 0, 0),
            'green': wx.Colour(0, 255, 0),
            'black': wx.Colour(0, 0, 0),
        }

    def OnPaint(self, event):
        dc = wx.ClientDC(self)
        brush = wx.Brush("white")
        dc.SetBackground(brush)
        dc.Clear()

        count = 0
        while count != 30: 
            x2, y2 = random.randint(100, 400), random.randint(100, 400)

            if x2 > 250 and y2 < 250:
                pen = wx.Pen(self.color['red'])
                dc.SetPen(pen)
            elif x2 > 250:
                pen = wx.Pen(self.color['green'])
                dc.SetPen(pen)
            elif y2 > 250:
                pen = wx.Pen(self.color['blue'])
                dc.SetPen(pen)
            else:
                pen = wx.Pen(self.color['black'])
                dc.SetPen(pen)

            xwidth = abs(x2 - 250) 
            yheiht = abs(y2 - 250) 

            line = sqrt(xwidth**2 + yheiht**2)

            if 149 <= line <= 150:

                dc.DrawLine(250, 250, x2, y2)
                count += 1

    def onQuit(self, event):
        self.Close()

app = wx.App()

frame = MyFrame(None)
frame.Center()
frame.Show()

app.MainLoop()

