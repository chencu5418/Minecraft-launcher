import tkinter as tk
import os
import subprocess
window = tk.Tk()
window.title('Launcher')
window.geometry('300x100')
beg = False
def begin():
    global beg
    if beg == False:
        beg = True
        subprocess.Popen("C:\Program Files\WindowsApps\Microsoft.MinecraftUWP_1.19.4002.0_x64__8wekyb3d8bbwe\Minecraft.Windows.exe")
killer = False
def kill():
    global killer
    if killer == False:
        killer = True
        pro = 'taskkill /f /im Minecraft.Windows.exe'
        os.system(pro)
b1 = tk.Button(window,text='minecraft BE begin',width=15,height=2,command=begin)
b2 = tk.Button(window,text='minecraft BE killer',width=15,height=2,command=kill)
b1.pack()
b2.pack()
window.mainloop()
