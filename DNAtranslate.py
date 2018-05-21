import sys

import wx

from ESC_DNAtranslate import ESC_DNAtranslate
from GUI_DNAtranslate_Input import GUI_DNAtranslate_Input
from GUI_DNAtranslate_Output import GUI_DNAtranslate_Output

class RFSeq(wx.Frame):
    def __init__(self, s_parent, s_title="RFSeq"):
        wx.Frame.__init__(self, s_parent, title=s_title, style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)
        self.panel = wx.Panel(self)
        box = wx.BoxSizer()
        self.frames()
        self.hiding()
        self.panel.SetSizer(self.box2)
        self.dic['A'].Show()
        self.binder()
        self.Show(True)
        self.Centre()
        self.SetSize((300, 225))
        box.Add(self.panel, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(box)

    def frames(self):
        def dic_make():
            self.dic = {}
            self.dic['A'] = self.dnainput
            self.dic['B'] = self.dnaoutput

        self.dnainput = GUI_DNAtranslate_Input(self.panel)
        self.dnaoutput = GUI_DNAtranslate_Output(self.panel)
        dic_make()
        self.box2 = wx.BoxSizer()
        for x in self.dic:
            self.box2.Add(self.dic[x], 1, wx.ALL | wx.EXPAND)

    def hiding(self):
        for x in self.dic:
            self.dic[x].Hide()

    def binder(self):
        def stop_buttons():
            for x in self.dic:
                self.dic[x].stop.Bind(wx.EVT_BUTTON, self.quitting)

        def other_buttons():
            self.dnainput.next.Bind(wx.EVT_BUTTON, self.next_frame)
            self.dnaoutput.prev.Bind(wx.EVT_BUTTON, self.prev_frame)

        stop_buttons()
        other_buttons()

    def quitting(self, event):
        sys.exit()

    def next_frame(self, event):
        def get_seq():
            with open(self.dnainput.filename.GetPath(), "r") as f:
                seq = f.readline().strip()
            return seq
        
        def set_seqs(seq):
            seqs = ESC_DNAtranslate(seq)
            self.dnaoutput.fdna.SetValue(seqs.get_fdna())
            self.dnaoutput.cdna.SetValue(seqs.get_cdna())
            self.dnaoutput.frna.SetValue(seqs.get_frna())
            self.dnaoutput.crna.SetValue(seqs.get_crna())
            self.dnaoutput.fpro.SetValue(seqs.get_fpro())
            self.dnaoutput.cpro.SetValue(seqs.get_cpro())
        
        set_seqs(get_seq())
        self.hiding()
        self.SetSize((300, 500))
        self.Refresh()
        self.dic['B'].Show()
        self.Layout()
        self.Centre()
    
    def prev_frame(self, event):
        self.rfinput.filename.SetPath("")
        self.hiding()
        self.SetSize((300, 225))
        self.Refresh()
        self.dic['A'].Show()
        self.Layout()
        self.Centre()


# Is called when this script is used as the MAIN.
if __name__ == "__main__":
    class MyApp(wx.App):
        def OnInit(self):
            frame = RFSeq(None)
            frame.Show(True)
            frame.Centre()
            self.SetTopWindow(frame)
            return True

    # The application-loop
    app = MyApp(0)
app.MainLoop()