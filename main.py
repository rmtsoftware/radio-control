import os
import serial
from PySide6.QtWidgets import QMainWindow, QApplication
from mainwindow import Ui_MainWindow
from dotenv import load_dotenv
from PySide6.QtCore import QThread, Signal, QTimer, Qt
import sys
from enum import Enum

load_dotenv()


class ControlMode(Enum):
    MANUAL = 'Manual'
    REMOTE = 'Remote'
    AUTO = 'Autonomous'
    UNDEFINED = 'Not Selected'


class Base(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set window title
        self.setWindowTitle("Связь УКВ")

        # Set fixed window size
        self.setFixedSize(477, 622)

        self.lb_latitude_val = self.ui.lb_latitude_val_2
        self.lb_NS_val = self.ui.lb_NS_val_2
        self.lb_longitude_val = self.ui.lb_longitude_val_2
        self.lb_EW_val = self.ui.lb_EW_val_2
        self.lb_altitude_val = self.ui.lb_altitude_val_2
        self.lb_grndspeed_val = self.ui.lb_grndspeed_val_2
        self.lb_axl_x_val = self.ui.lb_axl_x_val_2
        self.lb_axl_y_val = self.ui.lb_axl_y_val_2
        self.lb_axl_z_val = self.ui.lb_axl_z_val_2
        self.set_zero_values()

    def set_zero_values(self):
        zero_labels = [self.lb_latitude_val, self.lb_NS_val, self.lb_longitude_val, self.lb_EW_val,
                       self.lb_altitude_val, self.lb_grndspeed_val, self.lb_axl_x_val, self.lb_axl_y_val,
                       self.lb_axl_z_val]
        for label in zero_labels:
            label.setText('0')


class UiButtons(Base):
    def __init__(self):
        super().__init__()
        self.ui.btn_gps.clicked.connect(self.get_gps)
        self.ui.btn_imu.clicked.connect(self.get_imu)
        self.ui.btn_motor_start.clicked.connect(self.motor_start)
        self.ui.btn_motor_stop.clicked.connect(self.motor_stop)
        self.ui.btn_mnl_mode.clicked.connect(self.mnl_mode)
        self.ui.btn_rmt_mode.clicked.connect(self.rmt_mode)
        self.ui.btn_mnl_cmd.clicked.connect(self.send_mnl_cmd)

    def get_gps(self): pass
    def get_imu(self): pass
    def motor_start(self): pass
    def motor_stop(self): pass
    def mnl_mode(self): pass
    def rmt_mode(self): pass
    def send_mnl_cmd(self): pass


class SerialReader(QThread):

    receive_data_signal = Signal(str)

    def __init__(self, port):
        QThread.__init__(self)
        self.serial = port

    def run(self):
        while True:
            data = self.serial.readline().decode('utf-8').strip()
            if data.startswith == "D,s,5,RC":
                self._add_to_terminal('Управление с пульта')
            self.receive_data_signal.emit(data)


class SerialWritter(UiButtons):
    def __init__(self):
        super().__init__()
        self.port = os.getenv('PORT')
        self.baudrate = int(os.getenv('BAUDRATE'))
        try:
            self.serial = serial.Serial(port=self.port,
                                        baudrate=self.baudrate,
                                        timeout=5)
            self.thread = SerialReader(self.serial)
            self.thread.receive_data_signal.connect(self.process_data)
            self.thread.start()
            print(f"Подключено устройство {self.port}")
        except serial.SerialException:
            print("Порт не доступен")
            self.serial = None

    def process_data(self, data):

        if data.startswith("D,s,1,1"):
            self.parse_msg_gps(data)

        elif data.startswith("D,s,1,3"):
            self.parse_msg_imu(data)

    def parse_msg_gps(self, data):
        # D,s,1,1,0.0000,N,0.0000,E,0.0,000000,0.000,0.000,*122
        data = data.split(',')
        latitude = data[4]
        NS = data[5]
        longitude = data[6]
        EW = data[7]
        altitude = data[8]
        grndspeed = data[9]
        self.lb_latitude_val.setText(latitude)
        self.lb_NS_val.setText(NS)
        self.lb_longitude_val.setText(longitude)
        self.lb_EW_val.setText(EW)
        self.lb_altitude_val.setText(altitude)
        self.lb_grndspeed_val.setText(grndspeed)
        

    def parse_msg_imu(self, data):
        # D,s,1,3,-0.244,0.097,-101.182*116
        data = data.split(',')
        axl_x = data[4]
        axl_y = data[5]
        axl_z = data[6].split('*')[0]
        self.lb_axl_x_val.setText(str(axl_x))
        self.lb_axl_y_val.setText(str(axl_y))
        self.lb_axl_z_val.setText(str(axl_z))


class TerminalViewer(SerialWritter):
    def __init__(self):
        super().__init__()
        self.current_text = ''

        self.terminal_cleaner = QTimer()  # таймер очистки содержимого терминала
        self.terminal_cleaner.timeout.connect(self._clean_by_timer)
        self.terminal_cleaner.start(300)

    def _add_to_terminal(self, message):
        if message == '':
            return
        self.current_text = f'{message}' + '\n' + self.current_text
        self.ui.terminal_window.setText(self.current_text)

    def _clean_by_timer(self):
        if len(self.current_text) > 2000:
            self.current_text = ''

    def process_data(self, data):

        self._add_to_terminal(data)

        if data.startswith("D,s,1,1"):
            self.parse_msg_gps(data)

        elif data.startswith("D,s,1,3"):
            self.parse_msg_imu(data)


class Actions(TerminalViewer):
    def __init__(self):
        super().__init__()
        self.mode = ControlMode.MANUAL

    def get_gps(self):
        if self.serial:
            self.serial.write(b'D,s,4,GPS,*,\r\n')
            self._add_to_terminal('D,s,4,GPS,*,')
        else:
            print('Порт не доступен')

    def get_imu(self):
        if self.serial:
            self.serial.write(b'D,s,4,IMU,*,\r\n')
            self._add_to_terminal('D,s,4,IMU,*,')
        else:
            print('Порт не доступен')

    def motor_start(self):
        if self.serial:
            self.serial.write(b'D,s,ESTART,*,\r\n')
            self._add_to_terminal('D,s,ESTART,*,')
        else:
            print('Порт не доступен')

    def motor_stop(self):
        if self.serial:
            self.serial.write(b'D,s,ESTOP,*,\r\n')
            self._add_to_terminal('D,s,ESTOP,*,')
        else:
            print('Порт не доступен')
    
    def mnl_mode(self):
        if self.serial:
            self.mode = ControlMode.MANUAL
            self._add_to_terminal('Ручной режим')
        else:
            print('Порт не доступен')

    def rmt_mode(self):
        if self.serial:
            self.serial.write(b'D,s,5,RC,*,\r\n')
            self._add_to_terminal('D,s,5,RC,*,')
            self._add_to_terminal('Дистанционный режим')
            self.mode = ControlMode.REMOTE
        else:
            print('Порт не доступен')

    # Override closeEvent to close serial port when main window is closed
    def closeEvent(self, event):
        if self.serial:
            self.serial.close()
            print('Порт закрыт')

        event.accept()


class AutoTelemetryGetter(Actions):
    def __init__(self):
        super().__init__()
        self._auto_state = {'gps': 0, 'imu': 0}
        self.ui.cb_auto_gps.stateChanged.connect(lambda _: self.update_auto_state('gps'))
        self.ui.cb_auto_imu.stateChanged.connect(lambda _: self.update_auto_state('imu'))
        self.auto_request_timer = QTimer()  # таймер автозапроса телеметрии
        self.auto_request_timer.timeout.connect(self.auto_request_telemetry)
        self.auto_request_timer.start(300)

    def update_auto_state(self, telemetrytype):
        if self.ui.__dict__[f'cb_auto_{telemetrytype}'].checkState() == Qt.CheckState.Unchecked:
            self._auto_state[telemetrytype] -= 1
        elif self.ui.__dict__[f'cb_auto_{telemetrytype}'].checkState() == Qt.CheckState.Checked:
            self._auto_state[telemetrytype] += 1
            

    def auto_request_telemetry(self):
        for telemetrytype in ['gps', 'imu']:
            if self._auto_state[telemetrytype] == 1:
                self.ui.__dict__[f'btn_{telemetrytype}'].setEnabled(False)
                self.request_telemetry(telemetrytype)
            elif self._auto_state[telemetrytype] == 0:
                self.ui.__dict__[f'btn_{telemetrytype}'].setEnabled(True)

    def request_telemetry(self, telemetrytype):
        if telemetrytype == 'gps':
            self.get_gps()
        if telemetrytype == 'imu':
            self.get_imu()


class PowerEngineLine(AutoTelemetryGetter):
    def __init__(self):
        super().__init__()
        self.pwr_mnl: int = 0
        self.reset_input_to_zero()
        self.ui.le_pwr_mnl.editingFinished.connect(self._handle_line_edit)

    def _handle_line_edit(self):
        """ Действия по окончанию изменения значения в lineEdit 'Задание мощности' """

        # Получение текста из области
        user_input = self.ui.le_pwr_mnl.text()

        if self._is_input_empty(user_input):
            self.reset_input_to_zero()
            return

        try:
            self.pwr_mnl = self._check_valid_range(int(user_input))
        except ValueError as _:
            self.reset_input_to_zero()
            return

        self.ui.le_pwr_mnl.setText(str(self.pwr_mnl))

    @staticmethod
    def _is_input_empty(user_input):
        return user_input == ''

    def reset_input_to_zero(self):
        self.pwr_mnl = 0
        self.ui.le_pwr_mnl.setText(str(self.pwr_mnl))

    @staticmethod
    def _check_valid_range(value):
        if value > 100 or value < 0:
            # Reset out of bound values to maximum or minimum limit respectively.
            return 100 if value > 100 else 0
        return value


class ManualKeysControl(PowerEngineLine):
    def __init__(self):
        super().__init__()
        self._add_to_terminal('Ручной режим')

    def emit_server_signal(self, cmds_character):
        cmd = cmds_character + str(self.pwr_mnl)
        if self.serial:
            _cmd = f'D,s,3,{cmd[0]},{cmd[1:]},*,\r\n'
            self._add_to_terminal(_cmd[:-4])
            self.serial.write(_cmd.encode("utf-8"))

    def keyPressEvent(self, event):
        
        if self.serial is None:
            return

        if self.mode != ControlMode.MANUAL:
            return
        
        key_press = event.key()
        if key_press == Qt.Key.Key_W:
            self.emit_server_signal('F')
        elif key_press == Qt.Key.Key_S:
            self.emit_server_signal('B')
        elif key_press == Qt.Key.Key_A:
            self.emit_server_signal('L')
        elif key_press == Qt.Key.Key_D:
            self.emit_server_signal('R')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window =  ManualKeysControl()
    window.show()
    app.exec()