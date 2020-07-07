import os

os.chdir('F:\SERIES\All American\Season 1')
for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    if f_ext == '.mkv':
        new_name = f'{f_name}.mp4'
        print(new_name)
        os.rename(f, new_name)


