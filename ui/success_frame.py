from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QFont
from PyQt5.QtCore import Qt, QTimer
import sys

class SuccessFrame(QFrame):
    __x, __y, _width, _height = 50, 50, 170, 170

    # success image
    __image_label: QLabel = None
    __image_x, __image_y, __image_width, __image_height = 0, -15, 170, 170
    __image_color = QColor("green")
    __image_line_size = 7
    __image_animation_timer: QTimer = None

    # success image (circle)
    __image_circle_full_circle = 5760
    __image_circle_add_angele_once = 240
    __image_circle_current_angle = 0
    __image_circle_animation_completed = False

    # success image (mask)
    __image_mask_step = 0
    __image_mask_start_x, __image_mask_start_y = 60, 85
    __image_mask_middle_x, __image_mask_middle_y = __image_mask_start_x, __image_mask_start_y
    __image_mask_end_x, __image_mask_end_y = 0, 0

    # success text
    __text_label: QLabel = None
    __text = 'Success'
    __text_font = 'Arial'
    __text_size = 14
    __text_color = 'color: green;'
    __text_y = 130

    def __init__(self, parent=None):
        super().__init__(parent)
        # set frame size
        self.setGeometry(self.__x, self.__y, self._width, self._height)
        self.setObjectName('bg_frame')
        self.setStyleSheet(
            '#bg_frame{'
            'border-radius: 5px;'
            'background-color: rgba(0, 0, 0, 200);'
            '}')
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(100)
        shadow_effect.setOffset(0, 10)
        shadow_effect.setColor(QColor(0, 0, 0))
        self.setGraphicsEffect(shadow_effect)

        # success image
        self.__image_label = QLabel(self)
        self.__image_label.setGeometry(self.__image_x, self.__image_y, self.__image_width, self.__image_height)

        # success text
        self.__text_label = QLabel(self.__text, self)
        self.__text_label.setFont(QFont(self.__text_font, self.__text_size, QFont.Bold))
        self.__text_label.setStyleSheet(self.__text_color)
        self.__text_label.adjustSize()
        self.__text_label.move((self.width() - self.__text_label.width()) // 2, self.__text_y)

    def start(self):
        # draw image animation timer
        self.__image_animation_timer = QTimer(self)
        self.__image_animation_timer.timeout.connect(self.__draw_image_animation)
        self.__image_animation_timer.start(30)

    def __draw_image_animation(self):
        stop = False
        if not self.__image_circle_animation_completed:
            if self.__image_circle_current_angle < self.__image_circle_full_circle:
                self.__image_circle_current_angle += self.__image_circle_add_angele_once
            else:
                self.__image_circle_animation_completed = True

        else:
            self.__image_mask_step += 1

        pixmap = QPixmap(self._width, self._height)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        pen = QPen(self.__image_color, self.__image_line_size)
        pen.setCapStyle(Qt.RoundCap)
        painter.setPen(pen)

        rect = pixmap.rect().adjusted(40, 40, -40, -40)
        painter.drawArc(rect, 0, self.__image_circle_current_angle)

        if self.__image_circle_animation_completed:
            if self.__image_mask_step <= 8:
                self.__image_mask_middle_x += 2
                self.__image_mask_middle_y += 2
                self.__image_mask_end_x = self.__image_mask_middle_x
                self.__image_mask_end_y = self.__image_mask_middle_y
                painter.drawLine(self.__image_mask_start_x, self.__image_mask_start_y,
                                 self.__image_mask_middle_x, self.__image_mask_middle_y)

            elif self.__image_mask_step <= 22:
                self.__image_mask_end_x += 2
                self.__image_mask_end_y -= 2
                painter.drawLine(self.__image_mask_start_x, self.__image_mask_start_y,
                                 self.__image_mask_middle_x, self.__image_mask_middle_y)
                painter.drawLine(self.__image_mask_middle_x, self.__image_mask_middle_y,
                                 self.__image_mask_end_x, self.__image_mask_end_y)

            else:
                painter.drawLine(self.__image_mask_start_x, self.__image_mask_start_y,
                                 self.__image_mask_middle_x, self.__image_mask_middle_y)
                painter.drawLine(self.__image_mask_middle_x, self.__image_mask_middle_y,
                                 self.__image_mask_end_x, self.__image_mask_end_y)
                stop = True

        painter.end()
        self.__image_label.setPixmap(pixmap)

        if stop:
            self.__image_animation_timer.stop()


class CircleMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(2000, 200, 300, 300)

        frame_width, frame_height = 170, 170
        center_x = (300 - frame_width) // 2
        center_y = (300 - frame_height) // 2

        self.success_frame = SuccessFrame(self)
        self.success_frame.move(center_x, center_y)
        self.success_frame.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleMainWindow()
    window.show()
    sys.exit(app.exec_())