import os


if __name__ == '__main__':
    os.system(f"start /wait cmd /c pip3 install pygame")
    os.system(f"start /wait cmd /c pyinstaller --onefile src/game.py --windowed")
