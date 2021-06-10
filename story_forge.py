import random
import os
from pathlib import Path
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from PIL import Image

names = ['Jordan', 'Preston', 'Jarel', 'Kenobi', 'Kael', 'Aidan', 'Rush', 'Sam', 'Rhema', 'Hannah', 'Anna', 'Alee', 'Chandler', 'Razi']
roles = ['Judge', 'Accused', 'Victim', 'Defendant', 'Plaintiff', 'Juror1',
         'Witness1', 'Bailiff', 'Juror2', 'Witness2', 'Foreperson', 'Juror3',
         'Witness3', 'Reporter']
personalities = ['a germophobe', 'chill', 'forgetful', 'crazy', 'awkward',
                 'quiet', 'loud', 'bored', 'lazy', 'tired', 'generous',
                 'forgiving']
descriptor = ['hatred for', 'love for', 'addiction to', 'diet of',
              'obsession with']
crimes = ['vandalizing', 'causing emotional harm to', 'stealing',
          'drowning']
items = ['rubber chicken', 'forklift', 'sock', 'toilet', 'elk', 'toaster', 'anime', 'NF beanie', 'artwork', 'money', 'v-bucks', 'dogecoin', 'aardvark']
places = ['sandwich', 'hunting ground', 'cave', 'cousin', 'planet',
          'favorite restaurant', 'school', 'computer', 'mailbox',
          'minecraft house']
adjectives = ['pink', 'pet', 'wild']


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Story Forge')
        self.setLayout(qtw.QVBoxLayout())

        roles_lbl = qtw.QLabel('')
        roles_lbl.setFont(qtg.QFont('Helvetica', 20))
        self.layout().addWidget(roles_lbl)

        story_lbl = qtw.QLabel('')
        story_lbl.setFont(qtg.QFont('Helvetica', 30))
        self.layout().addWidget(story_lbl)

        image_lbl = qtw.QLabel()
        pixmap = qtg.QPixmap('images/blank.png')
        image_lbl.setPixmap(pixmap)
        self.layout().addWidget(image_lbl)

        generate_btn = qtw.QPushButton('Generate Case', clicked=lambda: generate())
        generate_btn.setFont(qtg.QFont('Helvetica', 30))
        generate_btn.setMinimumHeight(100)
        self.layout().addWidget(generate_btn)

        self.show()

        def generate():
            random.seed(os.urandom(1), 2)
            print('There are ' + str(len(names)) + ' Players')

            random.shuffle(names)

            roles_statement = ''
            role = {}
            idx = 0
            roles_statements = ''
            for name in names:
                role[roles[idx]] = names[idx]
                rand_personality = random.randint(0, len(personalities) - 1)
                rand_descriptor = random.randint(0, len(descriptor) - 1)
                rand_item = random.randint(0, len(items) - 1)
                statement = '{} {} is {} and has a {} {}s'.format(roles[idx],
                                                              names[idx],
                                                              personalities[
                                                                  rand_personality],
                                                              descriptor[
                                                                  rand_descriptor],
                                                              items[
                                                                  rand_item])

                roles_statements = roles_statements + '\n' + statement
                print(statement)

                idx += 1

            rand_crime = random.randint(0, len(crimes) - 1)
            rand_item = random.randint(0, len(items) - 1)
            rand_place = random.randint(0, len(places) - 1)
            rand_adj = random.randint(0, len(adjectives) - 1)
            story = '{} is being accused of {} {}\'s {} {} from their {}'.format(
                role['Accused'], crimes[rand_crime], role['Victim'],
                adjectives[rand_adj],
                items[rand_item],
                places[rand_place])
            print(story)

            roles_lbl.setText(roles_statements)
            story_lbl.setText(story)

            # Image generation
            image_path = Path('images/{}.png'.format(items[rand_item]))
            adjective_path = Path('images/{}.png'.format(adjectives[rand_adj]))
            crime_path = Path('images/{}.png'.format(crimes[rand_crime]))
            if image_path.exists():
                item_image = Image.open('images/{}.png'.format(items[rand_item]))
                print('Image found')
            else:
                item_image = Image.open('images/noitem.png')
            if adjective_path.exists():
                adjective_image = Image.open('images/{}.png'.format(adjectives[rand_adj]))
            else:
                adjective_image = Image.open('images/noadjective.png')
            if crime_path.exists():
                crime_image = Image.open('images/{}.png'.format(crimes[rand_crime]))
            else:
                crime_image = Image.open('images/nocrime.png')

            comp1 = Image.alpha_composite(item_image, adjective_image)
            comp2 = Image.alpha_composite(comp1, crime_image)
            comp2.save('images/result.png')

            pixmap = qtg.QPixmap('images/result.png')
            image_lbl.setPixmap(pixmap)

            os.remove('images/result.png')


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
