import cv2
from PySide6.QtCore import Slot, QTimer, Qt
from PySide6.QtGui import QImage, QPixmap, QColor
from PySide6.QtWidgets import QMessageBox

from qfluentwidgets.components.widgets.frameless_window import FramelessWindow


from armControl import Ui_ControlUi
from utils import generate_instruction

class ControlUiWidget(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ControlUi()
        self.ui.setupUi(self)
        self.init_black_placeholder()
        # 连接按钮点击信号与对应的槽函数（这里只是示例，你可以根据实际需求定义具体函数逻辑）
        self.ui.reset_button.clicked.connect(self.on_reset_button_clicked)
        self.ui.move_button.clicked.connect(self.on_move_button_clicked)
        self.ui.move_reset_button.clicked.connect(self.on_move_reset_button_clicked)
        self.ui.work_button.clicked.connect(self.on_work_button_clicked)
        self.ui.video_switch.checkedChanged.connect(self.on_video_switch_clicked)

        # 连接滑块值改变信号与对应的槽函数（同样示例，可按需扩展逻辑）
        self.ui.maxspeed_slider.valueChanged.connect(self.on_maxspeed_slider_changed)
        self.ui.accel_slider.valueChanged.connect(self.on_accel_slider_changed)
        self.ui.speed_slider.valueChanged.connect(self.on_speed_slider_changed)

        # 用于控制视频更新的定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_video_frame)

        # 用于存储摄像头对象
        self.cap = None
    # 以下是各个按钮点击对应的槽函数示例，你可以根据具体需求编写功能逻辑

    def init_black_placeholder(self):
        # 获取QLabel当前的尺寸
        size = self.ui.video_view.size()
        width = size.width()
        height = size.height()
        # 创建对应尺寸的黑色Pixmap
        black_pixmap = QPixmap(width, height)
        black_pixmap.fill(QColor(Qt.black))
        self.ui.video_view.setPixmap(black_pixmap)


    def display_serial_info(self, message):
        """
        此方法用于将指定信息显示到串口信息区域

        参数:
        message (str): 要显示的信息字符串
        """
        # 获取当前串口信息
        current_text = self.ui.serial_text.toPlainText() | ''
        new_text=current_text
        if isinstance(message, list):
            for msg in message:
                new_text = new_text + msg + '\n'
        else:
            new_text = current_text + message + '\n'
        # 将更新后的信息设置到串口信息区域
        self.ui.serial_text.setPlainText(new_text)
    @Slot()
    def on_reset_button_clicked(self):
        print("复位按钮被点击了")
        # 在这里添加复位相关的具体业务逻辑代码

    @Slot()
    def on_move_button_clicked(self):
        is_loop = self.ui.loopRadioButton.isChecked()
        loop_times = 1
        if is_loop:
            try:
                loop_times = int(self.ui.loopTimes_lineEdit.text())
                if loop_times <= 0:
                    QMessageBox.warning(self, "输入错误", "循环次数必须为正整数")
                    return
            except ValueError:
                QMessageBox.warning(self, "输入错误", "请输入有效的循环次数")
                return

        # 获取起始点坐标，并尝试将其转换为 float 类型
        try:
            start_x = float(self.ui.startpoint_x_LineEdit.text() if self.ui.startpoint_x_LineEdit.text()!='' else 0)
            start_y = float(self.ui.startpoint_y_LineEdit.text() if self.ui.startpoint_y_LineEdit.text()!='' else 0)
            start_z = float(self.ui.startpoint_z_LineEdit.text() if self.ui.startpoint_z_LineEdit.text()!='' else 0)
        except ValueError:
            # 如果无法将输入转换为 float 类型，显示错误消息
            QMessageBox.warning(self, "输入错误", "请输入有效的浮点数作为起始点坐标")
            return

        # 获取终点坐标，并尝试将其转换为 float 类型
        try:
            end_x = float(self.ui.endpoint_x_lineEdit.text())
            end_y = float(self.ui.endpoint_y_lineEdit.text())
            end_z = float(self.ui.endpoint_z_lineEdit.text())
        except ValueError:
            # 如果无法将输入转换为 float 类型，显示错误消息
            QMessageBox.warning(self, "输入错误", "请输入有效的浮点数作为终点坐标")
            return
        if is_loop:
            instructions=loop_times*generate_instruction('move',(start_x, start_y, start_z),(end_x, end_y, end_z))
        else:
            instructions=generate_instruction('move',[],(end_x, end_y, end_z))
        print(instructions)
        self.display_serial_info(instructions)


    @Slot()
    def on_move_reset_button_clicked(self):
        print("移动复位按钮被点击了")
        # 移动复位相关的业务逻辑

    @Slot()
    def on_work_button_clicked(self):
        print("工作按钮被点击了")
        # 处理工作按钮点击后的操作逻辑

    @Slot(bool)
    def on_video_switch_clicked(self, checked):
        print("视频开关按钮被点击了")
        if checked:
            print("视频开关已打开")
            if self.cap is None:
                # 尝试打开摄像头，这里假设使用默认摄像头（索引为0），如果有多个摄像头可以修改参数
                self.cap = cv2.VideoCapture(0)
                if not self.cap.isOpened():
                    print("无法打开摄像头")
                    return
                # 启动定时器，定时更新视频画面，这里设置每30毫秒更新一次，可根据需要调整
                self.timer.start(30)
            else:
                print("摄像头已打开，无需重复打开")
        else:
            print("视频开关已关闭")
            self.init_black_placeholder()
            if self.cap is not None:
                # 停止定时器，不再更新视频画面
                self.timer.stop()
                # 释放摄像头资源
                self.cap.release()
                self.cap = None


    # 用于更新视频画面的函数，由定时器触发
    def update_video_frame(self):
        ret, frame = self.cap.read()
        size = self.ui.video_view.size()
        if ret:
            # 将OpenCV读取到的BGR格式图像转换为RGB格式，因为Qt使用RGB格式显示图像
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # 获取图像的尺寸信息
            h, w, ch = frame.shape
            # 创建QImage对象用于在Qt中显示图像
            q_image = QImage(frame.data, size.width(),size.height(), ch * w, QImage.Format_RGB888)
            # 将QImage转换为QPixmap，方便在QLabel或者QOpenGLWidget等控件上显示
            pixmap = QPixmap.fromImage(q_image)
            # 将视频画面显示在video_view控件上，根据你的界面设计，可能需要调整显示的尺寸等以适配控件大小
            self.ui.video_view.setPixmap(pixmap)

    # 以下是滑块值改变对应的槽函数示例，用于获取并处理滑块新值
    @Slot(int)
    def on_maxspeed_slider_changed(self, value):
        print(f"最大速度滑块值改变为: {value}")
        # 根据新值可以进行速度相关的设置、计算等操作

    @Slot(int)
    def on_accel_slider_changed(self, value):
        print(f"加速度滑块值改变为: {value}")
        # 处理加速度值改变后的逻辑

    @Slot(int)
    def on_speed_slider_changed(self, value):
        print(f"速度滑块值改变为: {value}")
        # 比如根据速度滑块新值更新显示或者执行相关速度调整操作