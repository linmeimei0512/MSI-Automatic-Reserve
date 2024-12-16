from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTime, QTimer, QSize
from PyQt5.QtGui import QMovie, QFont, QColor, QIcon, QPainter, QPen, QBrush
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QFrame, QLabel, QHBoxLayout, QGraphicsDropShadowEffect

def add_waiting_animation(centralwidget: QtWidgets):
    root_vertical_layout = QVBoxLayout(centralwidget)
    root_vertical_layout.setAlignment(Qt.AlignCenter)

    # background
    __waiting_animation_frame = QFrame()
    __waiting_animation_frame.setObjectName('bg_frame')
    __waiting_animation_frame.setFixedSize(170, 170)
    __waiting_animation_frame.setStyleSheet(
        '#bg_frame{'
        'border-radius: 5px;'
        'background-color: rgba(0, 0, 0, 200);'
        '}')
    shadow_effect = QGraphicsDropShadowEffect()
    shadow_effect.setBlurRadius(100)
    shadow_effect.setOffset(0, 10)
    shadow_effect.setColor(QColor(0, 0, 0))
    __waiting_animation_frame.setGraphicsEffect(shadow_effect)
    root_vertical_layout.addWidget(__waiting_animation_frame)

    # vertical layout
    vertical_layout = QVBoxLayout()
    vertical_layout.setAlignment(Qt.AlignCenter)
    vertical_layout.setContentsMargins(0, 0, 0, 0)
    __waiting_animation_frame.setLayout(vertical_layout)

    # loading animation gif
    loading_animation_label = QLabel()
    loading_animation_label.setFixedSize(150, 100)
    loading_animation_label.setAlignment(Qt.AlignCenter)
    vertical_layout.addWidget(loading_animation_label)

    __loading_movie = QMovie('ui/images/loading.gif')
    __loading_movie.setScaledSize(QSize(100, 100))
    __loading_movie.start()
    loading_animation_label.setMovie(__loading_movie)

    # loading text
    __waiting_animation_label = QLabel()
    __waiting_animation_label.setFixedSize(150, 50)
    __waiting_animation_label.setAlignment(Qt.AlignCenter)
    __waiting_animation_label.setStyleSheet('color: rgb(255, 255, 255);')
    __waiting_animation_label.setText('waiting...')
    font = QFont()
    font.setFamily("Arial")
    font.setBold(True)
    font.setPointSize(10)
    __waiting_animation_label.setFont(font)
    vertical_layout.addWidget(__waiting_animation_label)

    return __waiting_animation_frame, __waiting_animation_label