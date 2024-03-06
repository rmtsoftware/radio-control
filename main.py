import os
import serial
from PySide6.QtWidgets import QMainWindow, QApplication
from mainwindow import Ui_MainWindow
from dotenv import load_dotenv
from PySide6.QtCore import QThread, Signal
import sys

load_dotenv()


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
        print(latitude, NS, longitude, EW, altitude, grndspeed)

    def parse_msg_imu(self, data):
        # D,s,1,3,-0.244,0.097,-101.182*116
        data = data.split(',')
        axl_x = data[4]
        axl_y = data[5]
        axl_z = data[6]
        print(axl_x, axl_y, axl_z)


class Actions(SerialWritter):
    def __init__(self):
        super().__init__()

    def get_gps(self):
        if self.serial:
            self.serial.write(b'D,s,4,GPS,*,\r\n')
        else:
            print('Порт не доступен')

    def get_imu(self):
        if self.serial:
            self.serial.write(b'D,s,4,IMU,*,\r\n')
        else:
            print('Порт не доступен')

    def motor_start(self):
        if self.serial:
            self.serial.write(b'D,s,ESTART,*,\r\n')
        else:
            print('Порт не доступен')

    def motor_stop(self):
        if self.serial:
            self.serial.write(b'D,s,ESTOP,*,\r\n')
        else:
            print('Порт не доступен')

    def rmt_mode(self):
        if self.serial:
            self.serial.write(b'D,s,5,RC,*,\r\n')
        else:
            print('Порт не доступен')

    # Override closeEvent to close serial port when main window is closed
    def closeEvent(self, event):
        if self.serial:
            self.serial.close()
            print('Порт закрыт')

        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Actions()
    window.show()
    app.exec()