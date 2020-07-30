import os
import shutil

os.chdir('D:\VIDEOS\YOUTUBE\CODING\Python')
for f in os.listdir():
    if "Classes" in f:
        shutil.move(f'{os.getcwd()}\\{f}', f'{os.getcwd()}\\Python-class\\{f}')
