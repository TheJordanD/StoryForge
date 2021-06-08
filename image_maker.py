import PyQt5.QtWidgets as qtw
from PIL import Image
item_name = 'toaster'


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(qtw.QVBoxLayout())

        self.show()

        def generate_image():
            background = Image.open('images/{}.jpg'.format(item_name))
            foreground = Image.open('images/water.jpg')
            mask = Image.open('images/50mask.png')

            background.paste(foreground, (0, 0), mask)
            background.show()

            # image_lbl = qtw.QLabel()
            # pixmap = qtg.QPixmap('images/toaster.jpg')
            # image_lbl.setPixmap(pixmap)
            # self.layout().addWidget(image_lbl)

        generate_image()


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
