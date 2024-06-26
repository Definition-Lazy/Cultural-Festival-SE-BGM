import os
import glob
import pygame
import tkinter as tk
import configparser as cfg
from functools import partial
class Application(tk.Frame):
    def __init__(self, master=None,cfg=None):
        super().__init__(master,width=int(cfg["SYSTEM"]["width"]), height=int(cfg["SYSTEM"]["height"]))
        self.pack()
        self.cfg = cfg
        self.load_sound()
        self.set_button()
        self.master.title("Acoustic")
        self.master.geometry("640x400")
    def load_sound(self):
        self.files = glob.glob("./sound/*")
    def play_sound(self,num):
        pygame.mixer.init()
        sound = pygame.mixer.Sound(self.files[num])
        sound.play()
    def set_button(self):
        try:
            for y in range(int(self.cfg["BUTTON"]["HEIGHT"])):
                for x in range(int(self.cfg["BUTTON"]["WIDTH"])):
                    self.button = tk.Button(self, text=os.path.splitext(os.path.basename(self.files[x+y*8]))[0],command=partial(self.play_sound,x+y*8)).place(x=x*int(self.cfg["BUTTON"]["x"]),y=y*int(self.cfg["BUTTON"]["y"]),width=int(self.cfg["BUTTON"]["x"]),height=int(self.cfg["BUTTON"]["y"]))
        except IndexError:
            pass
        
if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap(default="icon.ico")
    cfg = cfg.ConfigParser()
    cfg.read("config.ini")
    app = Application(master=root,cfg=cfg)
    app.mainloop()