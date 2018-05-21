import wx

class GUI_DNAtranslate_Output(wx.Panel):
    def __init__(self, bb_parent):
        
        wx.Panel.__init__(self, bb_parent, style=wx.BORDER_SUNKEN)
        # Input parameters
        self.fdna = wx.TextCtrl(self, style=wx.TE_READONLY | wx.HSCROLL)
        self.cdna = wx.TextCtrl(self, style=wx.TE_READONLY | wx.HSCROLL)
        self.frna = wx.TextCtrl(self, style=wx.TE_READONLY | wx.HSCROLL)
        self.crna = wx.TextCtrl(self, style=wx.TE_READONLY | wx.HSCROLL)
        self.fpro = wx.TextCtrl(self, style=wx.TE_READONLY | wx.HSCROLL)
        self.cpro = wx.TextCtrl(self, style=wx.TE_READONLY | wx.HSCROLL)
        
        # Buttons
        self.stop = wx.Button(self, label="Quit")
        self.prev = wx.Button(self, label="Previous")
        
        # Placing of items in frame
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(wx.StaticText(self, label="Forward DNA Sequence:"), 1,
                wx.EXPAND | wx.ALL)
        box.Add(self.fdna, 1, wx.EXPAND | wx.ALL)
        box.Add(wx.StaticText(self, label="Forward RNA Sequence:"), 1,
                wx.EXPAND | wx.ALL)
        box.Add(self.frna, 1, wx.EXPAND | wx.ALL)
        box.Add(wx.StaticText(self, label="Forward protein Sequence:"), 1,
                wx.EXPAND | wx.ALL)
        box.Add(self.fpro, 1, wx.EXPAND | wx.ALL)
        box.Add(wx.StaticText(self, label="Complement DNA Sequence:"), 1,
                wx.EXPAND | wx.ALL)
        box.Add(self.cdna, 1, wx.EXPAND | wx.ALL)
        box.Add(wx.StaticText(self, label="Complement RNA Sequence:"), 1,
                wx.EXPAND | wx.ALL)
        box.Add(self.crna, 1, wx.EXPAND | wx.ALL)
        box.Add(wx.StaticText(self, label="Complement protein Sequence:"), 1,
                wx.EXPAND | wx.ALL)
        box.Add(self.cpro, 1, wx.EXPAND | wx.ALL)
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.stop, 1, wx.EXPAND | wx.ALL)
        hbox.Add(self.prev, 1, wx.EXPAND | wx.ALL)
        box.Add(hbox, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(box)

if __name__ == "__main__":
    class Frame(wx.Frame):
        def __init__(self, s_parent, s_title="GUI_DNAtranslate_Output"):
            wx.Frame.__init__(self, s_parent, title=s_title, size=(200, 300))
            panel = wx.Panel(self)
            panel1 = GUI_DNAtranslate_Output(panel)
            box = wx.BoxSizer()
            box.Add(panel1, 1, wx.EXPAND | wx.ALL)
            panel.SetSizer(box)
            self.Centre()
            self.Show(True)
    app = wx.App(False)
    Frame(None)
    app.MainLoop()