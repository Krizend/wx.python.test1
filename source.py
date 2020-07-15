import wx

APP_EXIT = 1

class MyFrame(wx.Frame):

    def __init__(self, parent, title='MyFrame Object'):
        super().__init__(parent=parent, title=title, style= wx.SYSTEM_MENU | wx.CLIP_CHILDREN)

        menubar = wx.MenuBar()
        filemenu = wx.Menu()
        # item = wx.MenuItem(filemenu, wx.ID_EXIT, "&Выход", "Выход из приложения")
        # filemenu.Append(item)
        filemenu.Append(APP_EXIT, 'Exit\tCtrl+Q', 'Выходи из программы')

        menubar.Append(filemenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.onQuit, id=APP_EXIT)
    def onQuit(self, event):
        self.Close()

app = wx.App()

frame = MyFrame(None)
frame.Center()
frame.Show()

app.MainLoop()

