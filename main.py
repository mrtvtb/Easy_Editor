from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog,
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL import ImageEnhance
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


class ImageProcessor():
   def __init__(self):
      self.filename = None
      self.directory = None
      self.full = None
      self.save_dir = 'modified/'
      self.image = None

   def loadImage(self, dir, filename):
      self.filename = filename
      self.directory = dir
      self.full = os.path.join(workdir, filename)
      self.image = Image.open(os.path.join(workdir, filename))

   def showImage(self, path):
      lb_image.hide()
      pic = QPixmap(path)
      w, h = lb_image.width(), lb_image.height()
      pic = pic.scaled(w, h, Qt.KeepAspectRatio)
      lb_image.setPixmap(pic)
      lb_image.show()

   def saveImage(self):
      save_path = os.path.join(self.directory, self.save_dir)
      if not(os.path.exists(save_path) or os.path.isdir(save_path)):
         os.mkdir(save_path)
      self.image.save(os.path.join(save_path, self.filename))

   def doBW(self):
      self.image = self.image.convert('L')
      self.saveImage()
      image_path = os.path.join(self.directory, self.save_dir, self.filename)
      self.showImage(image_path)

   def doMirror(self):
      self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
      self.saveImage()
      image_path = os.path.join(self.directory, self.save_dir, self.filename)
      self.showImage(image_path)

   def doSharpness(self):
      enhancer = ImageEnhance.Sharpness(self.image)
      self.image = enhancer.enhance(2.0)  
      self.saveImage()
      image_path = os.path.join(self.directory, self.save_dir, self.filename)
      self.showImage(image_path)

   def doLeft(self):
      self.image = self.image.transpose(Image.ROTATE_90)
      self.saveImage()
      image_path = os.path.join(self.directory, self.save_dir, self.filename)
      self.showImage(image_path)

   def doRight(self):
      self.image = self.image.transpose(Image.ROTATE_270)
      self.saveImage()
      image_path = os.path.join(self.directory, self.save_dir, self.filename)
      self.showImage(image_path)


workImage = ImageProcessor()

def showChosenImage():
   if lw_files.currentRow() >= 0:
      filename = lw_files.currentItem().text()
      workImage.loadImage(workdir, filename)
      workImage.showImage(os.path.join(workdir, filename))

lw_files.currentRowChanged.connect(showChosenImage)
btn_bw.clicked.connect(workImage.doBW)
btn_flip.clicked.connect(workImage.doMirror)
btn_left.clicked.connect(workImage.doLeft)
btn_right.clicked.connect(workImage.doRight)
btn_sharp.clicked.connect(workImage.doSharpness)

win.show()
app.exec_()