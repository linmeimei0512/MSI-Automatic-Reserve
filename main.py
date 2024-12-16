import itertools
import sys
import os
import traceback
from enum import Enum

from PyQt5.QtWidgets import QMainWindow, QFrame, QLabel, QDialog, QDesktopWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTime, QTimer
from PyQt5.QtGui import QIcon
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from ui.ui_main_windows import Ui_MainWindow
from ui import img_rc
from ui.waiting_animation import add_waiting_animation
from ui.success_frame import SuccessFrame
from ui.fail_frame import FailFrame
from ui.string_dialog import Ui_Dialog
import version


##########  Python Library Version ##########
recommend_package_dict = {'onnxruntime': '==1.18.0',
                          'onnxruntime-gpu': '==1.18.0',
                          'opencv-python': '>=4.5.2.52',
                          'colorama': '>=0.4.6',
                          'selenium': '==4.21.0',
                          'webdriver-manager': '==4.0.1',
                          'PyQt5': '==5.15.10'}
#############################################


class UpgradeDialog(QDialog):
    def __init__(self):
        super(UpgradeDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.__init_message()

    def __init_message(self):
        self.ui.label.setText('Have new version [1.0.1.1811]'
                              '\nDo you want to upgrade?')


class MainWindow(QMainWindow):
    # account
    __account_save_file_path = 'account.txt'

    # state
    class STATE(Enum):
        STOP = 1
        WAITING_START_TIME = 2
        RESERVING = 3
    __state = STATE.STOP

    # device
    # __device_xpath = '//*[@id="ctl00_ContentPlaceHolder1_DataList1"]/span[15]/li/div'
    __device_xpath = '//*[@id="ctl00_ContentPlaceHolder1_DataList1"]/span[13]/li/div'

    # waiting animation
    __waiting_animation_frame: QFrame = None
    __waiting_animation_label: QLabel = None
    __waiting_animation_timer: QTimer = None

    # success / fail animation
    __success_animation_frame = None
    __fail_animation_frame = None

    # start thread
    __start_thread = None

    # retry
    __retry_times = 0

    # input value
    __account = None
    __password = None
    __chamber_number = None
    __date_time = None
    __project = None
    __test_plan = None

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.activateWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFocus()
        self.setWindowIcon(QIcon('./ui/icon/icon-310.png'))
        self.__center()

        self.__init_version()
        self.__add_waiting_animation()
        self.__add_success_animation()
        self.__add_fail_animation()
        self.__init_account()
        self.__init_date_time()
        self.__init_start_time()
        self.__set_btn_listener()

    def __center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def __init_version(self):
        self.ui.label_version.setText('Version: {}'.format(version.version))

    def __add_waiting_animation(self):
        self.__waiting_animation_frame, self.__waiting_animation_label = add_waiting_animation(self.ui.centralwidget)
        self.__hide_waiting_animation()

    def __add_success_animation(self):
        self.__success_animation_frame = SuccessFrame(self)
        self.__success_animation_frame.move(
            (self.width() - self.__success_animation_frame._width) // 2,
            (self.height() - self.__success_animation_frame._height) // 2)
        self.__success_animation_frame.hide()
        # self.__success_animation_frame.start()

    def __add_fail_animation(self):
        self.__fail_animation_frame = FailFrame(self)
        self.__fail_animation_frame.move(
            (self.width() - self.__fail_animation_frame._width) // 2,
            (self.height() - self.__fail_animation_frame._height) // 2)
        self.__fail_animation_frame.hide()
        # self.__fail_animation_frame.start()

    def __show_waiting_animation(self, waiting_text):
        self.__waiting_animation_frame.show()
        self.__waiting_animation_label.setText(waiting_text)
        progress_text_list = ['.', '..', '...']
        cycle_progress = itertools.cycle(progress_text_list)
        self.__waiting_animation_timer = QTimer(self)
        self.__waiting_animation_timer.timeout.connect(lambda: self.__waiting_animation_label.setText(waiting_text + next(cycle_progress)))
        self.__waiting_animation_timer.start(1000)

    def __hide_waiting_animation(self):
        if self.__waiting_animation_timer is not None:
            self.__waiting_animation_timer.stop()
        self.__waiting_animation_frame.hide()

    def __init_account(self):
        try:
            if os.path.exists(self.__account_save_file_path):
                self.__log('Initialize account by [{}]... '.format(self.__account_save_file_path), end='', show_on_ui=True)
                self.ui.checkBox_save_account.click()
                with open(self.__account_save_file_path, 'r') as file:
                    lines = file.readlines()
                    if len(lines) >= 2:
                        account = lines[0].replace('\n', '')
                        password = lines[1].replace('\n', '')
                        self.ui.lineEdit_account.setText(account)
                        self.ui.lineEdit_password.setText(password)
                        # self.__log('Account: {}'.format(account))
                        # self.__log('Password: {}\n'.format(password))
                        self.__log('OK', new_line=False, show_on_ui=True)
                    else:
                        raise Exception('Account or password is incomplete in [{}].'.format(self.__account_save_file_path))

        except Exception as ex:
            self.__log('Fail.', new_line=False, show_on_ui=True)
            self.__log(str(ex), show_on_ui=True)
            traceback.format_exc()

    def __init_date_time(self):
        self.__log('Initialize date time by current time... ', end='', show_on_ui=True)
        current_date_time = QtCore.QDateTime.currentDateTime()
        # current_date_time.setTime(QTime(current_date_time.time().hour(), current_date_time.time().minute(), 0))
        current_date_time.setTime(QTime(8, 0, 0))
        self.ui.dateTimeEdit_start.setDisplayFormat('yyyy/MM/dd HH:mm')
        self.ui.dateTimeEdit_start.setDateTime(current_date_time)
        current_date_time.setTime(QTime(23, 30, 0))
        self.ui.dateTimeEdit_end.setDisplayFormat('yyyy/MM/dd HH:mm')
        self.ui.dateTimeEdit_end.setDateTime(current_date_time)
        self.__log('OK.', new_line=False, show_on_ui=True)

    def __init_start_time(self):
        self.__log('Initialize start time by current time... ', end='', show_on_ui=True)
        current_date_time = QtCore.QDateTime.currentDateTime()
        current_date_time.setTime(QTime(current_date_time.time().hour(), current_date_time.time().minute(), 0))
        self.ui.dateTimeEdit_start_date_time.setDisplayFormat('yyyy/MM/dd HH:mm')
        self.ui.dateTimeEdit_start_date_time.setDateTime(current_date_time)
        self.__log('OK.', new_line=False, show_on_ui=True)

    def __set_btn_listener(self):
        self.ui.pushButton_start.clicked.connect(self.__start)
        self.ui.pushButton_hidden_password.clicked.connect(self.__show_password)

    def __show_password(self):
        if self.ui.pushButton_hidden_password.isChecked():
            self.ui.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.ui.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)

    def __check_value(self) -> bool:
        self.__log('Checking value... ', end='', show_on_ui=True)

        # account
        self.__account = self.ui.lineEdit_account.text()
        if self.__account == '':
            self.__log('Fail', new_line=False, show_on_ui=True)
            self.__log('Account is empty.', show_on_ui=True)
            return False

        # password
        self.__password = self.ui.lineEdit_password.text()
        if self.__password == '':
            self.__log('Fail', new_line=False, show_on_ui=True)
            self.__log('Password is empty.', show_on_ui=True)
            return False

        # chamber number
        self.__chamber_number = self.ui.lineEdit_chamber_no.text()
        if self.__chamber_number == '':
            self.__log('Fail', new_line=False, show_on_ui=True)
            self.__log('Chamber number is empty.', show_on_ui=True)
            return False
        if not self.__can_convert_to_int(self.__chamber_number):
            self.__log('Fail', new_line=False, show_on_ui=True)
            self.__log('Chamber number need to be a integer.', show_on_ui=True)
            return False

        # project
        self.__project = self.ui.lineEdit_project.text()
        if self.__project == '':
            self.__log('Fail', new_line=False, show_on_ui=True)
            self.__log('Project is empty.', show_on_ui=True)
            return False

        # test plan
        self.__test_plan = self.ui.lineEdit_test_plan.text()
        if self.__test_plan == '':
            self.__log('Fail', new_line=False, show_on_ui=True)
            self.__log('Test plan is empty.', show_on_ui=True)
            return False

        # retry times
        self.__retry_times = self.ui.lineEdit_retry_times.text()
        if self.__retry_times == '':
            self.__retry_times = 0
        else:
            if not self.__can_convert_to_int(self.__retry_times):
                self.__log('Fail', new_line=False, show_on_ui=True)
                self.__log('Retry times need to be a integer.', show_on_ui=True)
                return False
            else:
                self.__retry_times = int(self.__retry_times)

        self.__log('OK', new_line=False, show_on_ui=True)
        return True


    def __save_account(self):
        self.__log('Save account and password.', show_on_ui=True)
        with open('account.txt', 'w') as file:
            file.write(self.ui.lineEdit_account.text() + '\n')
            file.write(self.ui.lineEdit_password.text() + '\n')
            file.close()

    def __wait_start_date_time(self):
        self.__log('Waiting for the set start datetime ({})...'.format(self.ui.dateTimeEdit_start_date_time.dateTime().toString('yyyy/MM/dd HH:mm')), show_on_ui=True)
        self.__state = MainWindow.STATE.WAITING_START_TIME
        self.ui.pushButton_start.setText('Stop')
        self.__show_waiting_animation(waiting_text='Waiting')

        self.__log('Set start date time: {}'.format(self.ui.dateTimeEdit_start_date_time.dateTime().toString('yyyy/MM/dd HH:mm')))

        progress_text_list = ['|', '/', '-', '\\']
        cycle_progress = itertools.cycle(progress_text_list)
        self.__wait_start_datatime_timer = QTimer(self)
        self.__wait_start_datatime_timer.timeout.connect(
            lambda:
            self.__start_reserve() if self.ui.dateTimeEdit_start_date_time.dateTime().toSecsSinceEpoch() <= QtCore.QDateTime.currentDateTime().toSecsSinceEpoch()
            else print(f"\r{'Waiting for the set start datetime...'} {next(cycle_progress)}", flush=True, end=''))
        self.__wait_start_datatime_timer.start(100)

    def __stop_wait_start_date_time(self):
        if self.__wait_start_datatime_timer is not None:
            self.__wait_start_datatime_timer.stop()

    def __start_reserve(self):
        self.__state = MainWindow.STATE.RESERVING
        self.__stop_wait_start_date_time()
        self.__hide_waiting_animation()
        self.__show_waiting_animation(waiting_text='Reserving')

        self.__log('\nStart reserve...', show_on_ui=True)
        self.__start_thread = StartThread(account=self.__account,
                                          password=self.__password,
                                          device_xpath='//*[@id="ctl00_ContentPlaceHolder1_DataList1"]/span[{}]/li/div'.format(self.ui.lineEdit_chamber_no.text()),
                                          project=self.__project,
                                          test_plan=self.__test_plan,
                                          date_time='{} - {}'.format(self.ui.dateTimeEdit_start.dateTime().toString('yyyy/MM/dd HH:mm'), self.ui.dateTimeEdit_end.dateTime().toString('yyyy/MM/dd HH:mm')),
                                          retry_times=self.__retry_times)
        self.__start_thread._result_message.connect(self.__get_result_message_by_thread)
        self.__start_thread._result_state.connect(self.__get_result_state_by_thread)
        self.__start_thread.start()

    def __stop_reserve(self):
        if self.__start_thread is not None:
            self.__start_thread.stop()

    def __get_result_message_by_thread(self, message, end, new_line):
        self.__log(message, end=end, new_line=new_line, show_on_ui=True)

    def __get_result_state_by_thread(self, state):
        self.__state = MainWindow.STATE.STOP
        self.__waiting_animation_frame.hide()
        self.ui.pushButton_start.setText('Start')
        if state == "SUCCESS":
            self.__success_animation_frame.show()
            self.__success_animation_frame.start()
        else:
            self.__fail_animation_frame.show()
            self.__fail_animation_frame.start()


    def __start(self):
        if self.__state == MainWindow.STATE.STOP:
            # clean result message
            self.ui.textEdit_result_message.setText('')

            if not self.__check_value(): return
            if self.ui.checkBox_save_account.isChecked():
                self.__save_account()
            self.__wait_start_date_time()

        else:
            self.__stop()

    def __stop(self):
        self.__log('\n\nStopping... ', end='', show_on_ui=True)
        self.__state = MainWindow.STATE.STOP
        self.ui.pushButton_start.setText('Start')
        self.__stop_wait_start_date_time()
        self.__stop_reserve()
        self.__hide_waiting_animation()
        self.__log('Done.', end='\n', new_line=False, show_on_ui=True)

    def __can_convert_to_int(self, string: str):
        try:
            int(string)
            return True
        except ValueError:
            return False

    def __log(self, message, end='\n', new_line=True, show_on_ui=False):
        print(message, end=end)
        if show_on_ui:
            _message = '' + message \
                if self.ui.textEdit_result_message.toPlainText() == '' \
                else self.ui.textEdit_result_message.toPlainText() + ('\n' if new_line else '') + message
            self.ui.textEdit_result_message.setText(_message)
            self.ui.textEdit_result_message.moveCursor(QtGui.QTextCursor.End)



class StartThread(QThread):
    # stop thread flag
    __stop = False

    # browser driver
    __driver = None

    # retry
    __retry_count = 0

    # result message
    _result_message = pyqtSignal(str, str, bool)

    # result state
    _result_state = pyqtSignal(str)

    def __init__(self, account, password, device_xpath, project, test_plan, date_time, retry_times):
        self.__account = account
        self.__password = password
        self.__device_xpath = device_xpath
        self.__project = project
        self.__test_plan = test_plan
        self.__date_time = date_time
        self.__retry_times = retry_times
        super().__init__()

    def run(self):
        try:
            self.__show_value()
            self.__init_yolov5_model()
            self.__init_browser()
            self.__login()
            self.__choose_device()
            self.__crack_captcha()
            self.__key_in_reserve_data()
            self.__create_reserve()
            self.__check_reserve_state()

        except Exception as ex:
            self._result_message.emit(str(ex), '\n', True)
            traceback.format_exc()

    def retry(self):
        try:
            self.__crack_captcha()
            self.__key_in_reserve_data()
            self.__create_reserve()
            self.__check_reserve_state()

        except Exception as ex:
            self._result_message.emit(str(ex), '\n', True)
            traceback.format_exc()

    def stop(self):
        self.__stop = True
        if self.__driver is not None:
            self.__driver.close()

    def __show_value(self):
        self._result_message.emit('\n'
                                  'Account: {}\n'
                                  'Password: {}\n'
                                  'Device XPATH: {}\n'
                                  'Project: {}\n'
                                  'Date time: {}\n'
                                  'Test plan: {}\n'
                                  'Retry times: {}\n'.format(self.__account, self.__password, self.__device_xpath, self.__project, self.__date_time, self.__test_plan, self.__retry_times), '\n', True)

    def __init_yolov5_model(self):
        self._result_message.emit('Initialzie detect captcha model... ', '', True)
        sys.path.append('./YOLO_v5/')
        from YOLO_v5.detect_onnx import DetectONNX
        self.__detect_captcha = DetectONNX(model_path='./best.onnx',
                                           warm_up_image_path='./captcha/images/000.png',
                                           confidence_threshold=0.3,
                                           iou_threshold=0.5)
        self._result_message.emit('OK.', '\n', False)

    def __init_browser(self):
        self._result_message.emit('Initialzie browser... ', '', True)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_experimental_option('detach', True)  # disable auto quit
        prefs = {
            'credentials_enable_service': False,
            'profile.password_mamnger_enabled': False
        }
        chrome_options.add_experimental_option('prefs', prefs)

        platform = sys.platform
        if platform == 'linux':
            self.__driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                             options=chrome_options)
        else:
            import os
            from subprocess import CREATE_NO_WINDOW

            chrome_install = ChromeDriverManager().install()
            folder = os.path.dirname(chrome_install)
            chromedriver_path = os.path.join(folder, 'chromedriver.exe')
            chrome_service = ChromeService(chromedriver_path)
            chrome_service.creation_flags = CREATE_NO_WINDOW
            self.__driver = webdriver.Chrome(service=chrome_service,
                                      options=chrome_options)

        self.__driver.set_window_position(0, 0)
        self.__driver.get('https://rdraid5.msi.com.tw/DQA/Code/NewLabCenter/NewLab_ReserveHomePage.aspx?index=1&Labs=Reliability')
        self.__driver.maximize_window()
        self._result_message.emit('OK', '\n', False)

    def __login(self):
        self._result_message.emit('Login account... ', '', True)

        # login button
        login_btn = self.__driver.find_element(by=By.XPATH, value='//*[@id="ctl00_linkLog"]')
        login_btn.click()

        # key in account and passowrd
        account_edit = self.__driver.find_element(by=By.XPATH, value='//*[@id="ctl00_pcLogin_LoginView1_Login1_UserName_I"]')
        account_edit.send_keys(self.__account)
        password_edit = self.__driver.find_element(by=By.XPATH, value='//*[@id="ctl00_pcLogin_LoginView1_Login1_Password_I"]')
        password_edit.send_keys(self.__password)
        login_btn = self.__driver.find_element(By.XPATH, value='//*[@id="ctl00_pcLogin_LoginView1_Login1_LoginButton_CD"]/span')
        login_btn.click()
        self._result_message.emit('OK. ', '\n', False)

    def __choose_device(self):
        self._result_message.emit('Choose device... ', '', True)

        # device
        device_btn = self.__driver.find_element(by=By.XPATH, value=self.__device_xpath)
        device_btn.click()

        # reserve button
        reserve_btn = self.__driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ContentPlaceHolder1_ReserveDetailed_Modal_LBtn_reserve"]')
        reserve_btn.click()
        self._result_message.emit('OK.',  '\n', False)

    def __crack_captcha(self):
        self._result_message.emit('Crack captcha... ', '', True)
        import cv2

        # get captcha image
        captcha_image = self.__driver.find_element(By.XPATH, value='//*[@id="captcha"]/canvas[1]')
        x, y = captcha_image.location['x'], captcha_image.location['y']
        width, height = captcha_image.size['width'], captcha_image.size['height']
        screenshot_path = 'screenshot.png'
        self.__driver.save_screenshot(screenshot_path)
        captcha_image = cv2.imread(screenshot_path)[y:y + height, x:x + width]

        # detect captcha
        result = self.__detect_captcha.detect(captcha_image)

        # crack
        slider = self.__driver.find_element(By.XPATH, value='//*[@id="captcha"]/div[3]/div')
        move = ActionChains(self.__driver)
        move.click_and_hold(slider).perform()
        move.move_by_offset(int(result[0]['box'][0] + 15), 0).perform()

        import pyautogui
        pyautogui.moveTo(x, y)
        pyautogui.moveTo(x + int(result[0]['box'][0] + 15), y)
        move.release().perform()
        self._result_message.emit('OK', '\n', False)

    def __key_in_reserve_data(self):
        self._result_message.emit('Key in reserve data... ', '', True)

        # project
        project_edit = self.__driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ContentPlaceHolder1_Txt_Model_I"]')
        project_edit.clear()
        project_edit.send_keys(self.__project)

        # date
        date_edit = self.__driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ContentPlaceHolder1_datetimes_pickers"]')
        date_edit.clear()
        date_edit.send_keys(self.__date_time)

        # test plan
        test_plan_edit = self.__driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ContentPlaceHolder1_TxtDescription"]')
        test_plan_edit.clear()
        test_plan_edit.send_keys(self.__test_plan)
        self._result_message.emit('OK.', '\n', False)

    def __create_reserve(self):
        self._result_message.emit('Create reserve... ', '', True)

        # create button
        create_btn = self.__driver.find_element(by=By.XPATH, value='//*[@id="ctl00_ContentPlaceHolder1_BtnReal_JustNew"]')
        create_btn.click()
        self._result_message.emit('OK.', '\n', False)

    def __check_reserve_state(self):
        self._result_message.emit('Check reserve state... ', '', True)
        try:
            alert = self.__driver.switch_to.alert
            self._result_message.emit(alert.text, '\n', False)
            if alert.text == '您已預約成功！':
                self._result_state.emit('SUCCESS')

            else:
                if self.__retry_count < self.__retry_times:
                    alert.accept()
                    self.__retry_count += 1
                    self._result_message.emit('\n==> Retry [ {} ] '.format(self.__retry_count), '\n', True)
                    self.retry()
                else:
                    self._result_state.emit('FAIL')

        except Exception as ex:
            # print('Can not found alert.')
            self._result_message.emit('Reserve failed. Ex: {}'.format(ex), '\n', False)




if __name__ == '__main__':
    from utils.python_package_utils import show_recommend_version
    show_recommend_version(recommend_package_dict)

    app = QtWidgets.QApplication([])

    # from utils.upgrade_utils import check_have_new_version
    # if check_have_new_version():
    #     upgrade_dialog = UpgradeDialog()
    #     upgrade_dialog.show()

    msi_automatic_reserve = MainWindow()
    msi_automatic_reserve.show()

    sys.exit(app.exec())

