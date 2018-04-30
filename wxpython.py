import wx
import wx.grid

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World!")
frame.Show(True)
panel = wx.Panel(frame)
wx.TextCtrl(panel)
app.MainLoop()