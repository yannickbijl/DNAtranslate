# DNAtranslate
DNAtranslate uses an input DNA sequence to generate the complement sequence, and from both the forward and complement sequences translate the RNA and protein sequences.

The program uses the module sys and the third-party module wx-python 4.0 (Phoenix) WxPython

The executable was made using pyinstaller on Windows 10 Home-edition 64-bit.

In the project folder open the cmd and use the command: **pyinstaller -F --icon=DNAtranslate.ico -w DNAtranslate.py**

The icon was made in Adobe Illustrator

DNAtranslate.py is the main file, GUI_DNAtranslate_Input.py and GUI_DNAtranslate_Output.py are used to generate the user interface, and ESC_DNAtranslate.py does the trnaslation of DNA to RNA and protein sequences.
