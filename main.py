from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog,
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)

import os

app = QApplication([])
win = QWidget()
win.setWindowTitle("Easy Editor")
win.resize(700,500)

lb_image = QLabel("Картинка")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()

btn_left = QPushButton("Вліво") 
btn_right = QPushButton("Вправо")
btn_flip = QPushButton("Дзеркало")
btn_sharp = QPushButton("Різкість")
btn_bw = QPushButton("Ч/Б")

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image, 95)
row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)

win.setLayout(row)


workdir = ''

def chooseWorkdir():
   global workdir
   workdir = QFileDialog.getExistingDirectory()


def filter(files, extension):
   result = []
   for filename in files:
      for ext in extension:
         if filename.endswith(ext):
            result.append(filename)
   return result



def showFilenamesList():
   chooseWorkdir()
   filenames = os.listdir(workdir)
   extension = ["png", "jpg", "gif", "bmp", "tiff"]
   pics = filter(filenames, extension)
   lw_files.clear()
   for pic in pics:
      lw_files.addItem(pic)


btn_dir.clicked.connect(showFilenamesList)



win.show()
app.exec_()