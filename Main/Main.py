import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from StarWars.StarWars import StarWars

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('Main.ui', self)

        self.btnStarWars.clicked.connect(self.play_Star_Wars)
        # self.btnRacing.clicked.connect(self.play_Racing)
        # self.btnSpaceTravel.clicked.connect(self.play_Space_Travel)

        self.main_window = None

    def play_Star_Wars(self):
        if not self.main_window:
            self.main_window = StarWars()
        self.main_window.run()
        self.hide()

    # def play_Racing(self):
    #     if not self.main_window:
    #         self.main_window = Racing()
    #     self.main_window.run()
    #     self.hide()

    # def play_Space_Travel(self):
    #     if not self.main_window:
    #         self.main_window = SpaceTravel()
    #     self.main_window.run()
    #     self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
