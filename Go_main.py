from PyQt5.QtWidgets import QApplication
import game
from window import GomokuWindow
from game import Gomoku
import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget, QApplication


def main():

    app = QApplication(sys.argv)
    w = QWidget()
    from game import jingshou
    from game import nandu
    ex = GomokuWindow()
    reply = QMessageBox.question(w, '设置', '是否开启禁手？', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                 QMessageBox.Cancel)
    if reply == QMessageBox.Yes:
        game.jingshou =1
        print('禁手开启')
    if reply == QMessageBox.No:
        game.jingshou =0
        print('禁手关闭')
    else:
        print('窗口关闭')
    reply = QMessageBox.question(w, '设置', '是否要降低难度？', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                 QMessageBox.Cancel)
    if reply ==  QMessageBox.Yes:
        game.nandu =1
        print('难度：简单')
        sys.exit(app.exec_())
    if reply == QMessageBox.No:
        game.nandu =2
        print('难度：中等')
        sys.exit(app.exec_())
    else:
        game.nandu=3
        print('难度：地狱')
        sys.exit(app.exec_())

    # 创建一个问答框，注意是Question


if __name__ == '__main__':
    main()

