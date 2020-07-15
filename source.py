import wx


class MyFrame(wx.Frame):
    
    def __init__(self, parent, title='MyFrame Object'):
        super().__init__(parent=parent, title=title, style= wx.SYSTEM_MENU | wx.CLIP_CHILDREN)

        menubar = wx.MenuBar()
        filemenu = wx.Menu()
        item = wx.MenuItem(filemenu, wx.ID_EXIT, "Выход", "Выход из приложения")
        filemenu.Append(item)

        menubar.Append(filemenu, "&Файл")
        self.SetMenuBar(menubar)


app = wx.App()

frame = MyFrame(None)
frame.Center()
frame.Show()

app.MainLoop()

