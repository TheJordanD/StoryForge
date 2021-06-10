import os
from pathlib import Path
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from PIL import Image
item_name = 'toaster'
crime_name = 'drowning'


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(qtw.QVBoxLayout())

        self.show()

        def generate_image():
            image_path = Path('images/{}.jpg'.format(item_name))
            crime_path = Path('images/{}.jpg'.format(crime_name))
            if image_path.exists():
                item_image = Image.open('images/{}.jpg'.format(item_name))
                print('Image found')
            else:
                item_image = Image.open('images/noitem.png')
            if crime_path.exists():
                crime_image = Image.open('images/{}.jpg'.format(crime_name))
            else:
                crime_image = Image.open('images/nocrime.png')

            mask = Image.open('images/50mask.png')

            item_image.paste(crime_image, (0, 0), mask)
            item_image.save('images/result.png')

            image_lbl = qtw.QLabel()
            pixmap = qtg.QPixmap('images/result.png')
            image_lbl.setPixmap(pixmap)
            self.layout().addWidget(image_lbl)

            os.remove('images/result.png')

        generate_image()


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
