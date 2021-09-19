#создай тут фоторедактор Easy Editor!
#создай приложение для запоминания информации#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter, ImageEnhance
import os

app = QApplication([])
main_win = QWidget()
main_win.resize(750, 500)

class ImageEd():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modified/'
    def LoadI(self, dir, filename):
        self.dir = dir
        self.filename = filename
        ImageP = os.path.join(dir, filename)
        self.image = Image.open(ImageP)
    def ShowI(self, path):
        p.hide()
        pixmapI = QPixmap(path)
        w, h = p.width(), p.height()
        pixmapI = pixmapI.scaled(w, h, Qt.KeepAspectRatio)
        p.setPixmap(pixmapI)
        p.show()
    def SaveI(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        ImageP = os.path.join(path, self.filename)
        self.image.save(ImageP)
    def ImageBW(self):
        self.image = self.image.convert('L')
        self.SaveI()
        ImageP = os.path.join(self.dir, self.save_dir, self.filename)
        self.ShowI(ImageP)   
    def ImageBL(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.SaveI()
        ImageP = os.path.join(self.dir, self.save_dir, self.filename)
        self.ShowI(ImageP) 
    def ImageM(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.SaveI()
        ImageP = os.path.join(self.dir, self.save_dir, self.filename)
        self.ShowI(ImageP)
    def ImageL(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.SaveI()
        ImageP = os.path.join(self.dir, self.save_dir, self.filename)
        self.ShowI(ImageP)
    def ImageR(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.SaveI()
        ImageP = os.path.join(self.dir, self.save_dir, self.filename)
        self.ShowI(ImageP)
    def ImageK(self):
        k = ImageEnhance.Contrast(self.image)
        self.image = k.enhance(1.5)
        self.SaveI()
        ImageP = os.path.join(self.dir, self.save_dir, self.filename)
        self.ShowI(ImageP)




#pic_contrast = pic_contrast.enhance(1.5)
#pic_contrast = ImageEnhance.Contrast(image)

#создание приложения и главного окна
l = QPushButton('Лево')
r = QPushButton('Право')
m = QPushButton('Зеркало')
z = QPushButton('Резкость')
w = QPushButton('Ч/Б')
k = QPushButton('Контраст')
b = QPushButton('Папка')
p = QLabel('Картинка')
n = QListWidget()
#создание виджетов главного окна
v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QVBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
#расположение виджетов по лэйаутам
v1.addWidget(b)
v1.addWidget(n)
h1.addWidget(p)
h2.addWidget(l)
h2.addWidget(r)
h2.addWidget(m)
h2.addWidget(z)
h2.addWidget(w)
h2.addWidget(k)
v2.addLayout(h1)
v2.addLayout(h2)
h3.addLayout(v1)
h3.addLayout(v2)

workdir = ''

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def chooseworkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def List():
    extensions = ['.jpg', '.png', '.jpeg', '.gif']
    chooseworkdir()
    filenames = filter(os.listdir(workdir), extensions)
    n.clear()
    for filename in filenames:
        n.addItem(filename)

def ShowI():
    filename = n.currentItem().text()
    WorkI.LoadI(workdir, filename)
    ImageP = os.path.join(WorkI.dir, WorkI.filename)
    WorkI.ShowI(ImageP)

WorkI = ImageEd()

b.clicked.connect(List)
n.currentRowChanged.connect(ShowI)
w.clicked.connect(WorkI.ImageBW)
z.clicked.connect(WorkI.ImageBL)
m.clicked.connect(WorkI.ImageM)
l.clicked.connect(WorkI.ImageL)
r.clicked.connect(WorkI.ImageR)
k.clicked.connect(WorkI.ImageK)

main_win.setLayout(h3) 
main_win.show()
app.exec_()