import wx
from socket import *
import numpy
from array import*

APP_EXIT = 1

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        gs = wx.GridSizer(2, 2, 5, 5)

        gs.AddMany( [
            (wx.Button(self, label='7'), 0, wx.EXPAND),
            (wx.Button(self, label='5'), 0, wx.EXPAND),
            (wx.Button(self, label='6'), 0, wx.EXPAND),
            (wx.Button(self, label='*'), 0, wx.EXPAND)])

        vbox.Add(gs, proportion=1, flag=wx.EXPAND)


def main():

    app = wx.App()
    ex = Example(None, title='Review')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
