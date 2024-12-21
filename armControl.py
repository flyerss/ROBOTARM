# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'armControl.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, ImageLabel, LineEdit, PushButton,
    RadioButton, Slider, StrongBodyLabel, SwitchButton,
    TextEdit, TitleLabel)

class Ui_ControlUi(object):
    def setupUi(self, ControlUi):
        if not ControlUi.objectName():
            ControlUi.setObjectName(u"ControlUi")
        ControlUi.setEnabled(True)
        ControlUi.resize(1012, 899)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ControlUi.sizePolicy().hasHeightForWidth())
        ControlUi.setSizePolicy(sizePolicy)
        ControlUi.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        ControlUi.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.layoutWidget = QWidget(ControlUi)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(520, 40, 461, 821))
        self.verticalLayout_right = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_right.setObjectName(u"verticalLayout_right")
        self.verticalLayout_right.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_videoInfo = QHBoxLayout()
        self.horizontalLayout_videoInfo.setObjectName(u"horizontalLayout_videoInfo")
        self.video_switch_label = BodyLabel(self.layoutWidget)
        self.video_switch_label.setObjectName(u"video_switch_label")

        self.horizontalLayout_videoInfo.addWidget(self.video_switch_label)

        self.video_switch = SwitchButton(self.layoutWidget)
        self.video_switch.setObjectName(u"video_switch")

        self.horizontalLayout_videoInfo.addWidget(self.video_switch)


        self.verticalLayout_right.addLayout(self.horizontalLayout_videoInfo)

        self.horizontalLayout_initInfo = QHBoxLayout()
        self.horizontalLayout_initInfo.setObjectName(u"horizontalLayout_initInfo")
        self.verticalLayout_labels = QVBoxLayout()
        self.verticalLayout_labels.setObjectName(u"verticalLayout_labels")
        self.maxspeed_label = BodyLabel(self.layoutWidget)
        self.maxspeed_label.setObjectName(u"maxspeed_label")

        self.verticalLayout_labels.addWidget(self.maxspeed_label)

        self.accel_label = BodyLabel(self.layoutWidget)
        self.accel_label.setObjectName(u"accel_label")

        self.verticalLayout_labels.addWidget(self.accel_label)

        self.speed_label = BodyLabel(self.layoutWidget)
        self.speed_label.setObjectName(u"speed_label")

        self.verticalLayout_labels.addWidget(self.speed_label)


        self.horizontalLayout_initInfo.addLayout(self.verticalLayout_labels)

        self.verticalLayout_sliders = QVBoxLayout()
        self.verticalLayout_sliders.setObjectName(u"verticalLayout_sliders")
        self.maxspeed_slider = Slider(self.layoutWidget)
        self.maxspeed_slider.setObjectName(u"maxspeed_slider")
        self.maxspeed_slider.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.maxspeed_slider.sizePolicy().hasHeightForWidth())
        self.maxspeed_slider.setSizePolicy(sizePolicy1)
        self.maxspeed_slider.setMinimumSize(QSize(0, 0))
        self.maxspeed_slider.setMouseTracking(False)
        self.maxspeed_slider.setTabletTracking(False)
        self.maxspeed_slider.setAutoFillBackground(False)
        self.maxspeed_slider.setSliderPosition(0)
        self.maxspeed_slider.setTracking(True)
        self.maxspeed_slider.setOrientation(Qt.Orientation.Horizontal)
        self.maxspeed_slider.setInvertedAppearance(True)
        self.maxspeed_slider.setInvertedControls(True)
        self.maxspeed_slider.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.verticalLayout_sliders.addWidget(self.maxspeed_slider)

        self.accel_slider = Slider(self.layoutWidget)
        self.accel_slider.setObjectName(u"accel_slider")
        self.accel_slider.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.accel_slider.sizePolicy().hasHeightForWidth())
        self.accel_slider.setSizePolicy(sizePolicy1)
        self.accel_slider.setMinimumSize(QSize(0, 0))
        self.accel_slider.setAutoFillBackground(False)
        self.accel_slider.setSliderPosition(0)
        self.accel_slider.setTracking(True)
        self.accel_slider.setOrientation(Qt.Orientation.Horizontal)
        self.accel_slider.setInvertedAppearance(True)
        self.accel_slider.setInvertedControls(True)
        self.accel_slider.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.verticalLayout_sliders.addWidget(self.accel_slider)

        self.speed_slider = Slider(self.layoutWidget)
        self.speed_slider.setObjectName(u"speed_slider")
        self.speed_slider.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.speed_slider.sizePolicy().hasHeightForWidth())
        self.speed_slider.setSizePolicy(sizePolicy1)
        self.speed_slider.setMinimumSize(QSize(0, 0))
        self.speed_slider.setAutoFillBackground(False)
        self.speed_slider.setSliderPosition(0)
        self.speed_slider.setTracking(True)
        self.speed_slider.setOrientation(Qt.Orientation.Horizontal)
        self.speed_slider.setInvertedAppearance(True)
        self.speed_slider.setInvertedControls(True)
        self.speed_slider.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.verticalLayout_sliders.addWidget(self.speed_slider)


        self.horizontalLayout_initInfo.addLayout(self.verticalLayout_sliders)


        self.verticalLayout_right.addLayout(self.horizontalLayout_initInfo)

        self.verticalLayout_move = QVBoxLayout()
        self.verticalLayout_move.setObjectName(u"verticalLayout_move")
        self.horizontalLayout_move_start = QHBoxLayout()
        self.horizontalLayout_move_start.setObjectName(u"horizontalLayout_move_start")
        self.stratpoint_label = StrongBodyLabel(self.layoutWidget)
        self.stratpoint_label.setObjectName(u"stratpoint_label")

        self.horizontalLayout_move_start.addWidget(self.stratpoint_label)

        self.startpoint_x_label = BodyLabel(self.layoutWidget)
        self.startpoint_x_label.setObjectName(u"startpoint_x_label")

        self.horizontalLayout_move_start.addWidget(self.startpoint_x_label)

        self.startpoint_x_LineEdit = LineEdit(self.layoutWidget)
        self.startpoint_x_LineEdit.setObjectName(u"startpoint_x_LineEdit")

        self.horizontalLayout_move_start.addWidget(self.startpoint_x_LineEdit)

        self.startpoint_y_label = BodyLabel(self.layoutWidget)
        self.startpoint_y_label.setObjectName(u"startpoint_y_label")

        self.horizontalLayout_move_start.addWidget(self.startpoint_y_label)

        self.startpoint_y_LineEdit = LineEdit(self.layoutWidget)
        self.startpoint_y_LineEdit.setObjectName(u"startpoint_y_LineEdit")

        self.horizontalLayout_move_start.addWidget(self.startpoint_y_LineEdit)

        self.startpoint_z_label = BodyLabel(self.layoutWidget)
        self.startpoint_z_label.setObjectName(u"startpoint_z_label")

        self.horizontalLayout_move_start.addWidget(self.startpoint_z_label)

        self.startpoint_z_LineEdit = LineEdit(self.layoutWidget)
        self.startpoint_z_LineEdit.setObjectName(u"startpoint_z_LineEdit")

        self.horizontalLayout_move_start.addWidget(self.startpoint_z_LineEdit)


        self.verticalLayout_move.addLayout(self.horizontalLayout_move_start)

        self.horizontalLayout_move_end = QHBoxLayout()
        self.horizontalLayout_move_end.setObjectName(u"horizontalLayout_move_end")
        self.endpoint_label = StrongBodyLabel(self.layoutWidget)
        self.endpoint_label.setObjectName(u"endpoint_label")

        self.horizontalLayout_move_end.addWidget(self.endpoint_label)

        self.endpoint_x_label = BodyLabel(self.layoutWidget)
        self.endpoint_x_label.setObjectName(u"endpoint_x_label")

        self.horizontalLayout_move_end.addWidget(self.endpoint_x_label)

        self.endpoint_x_lineEdit = LineEdit(self.layoutWidget)
        self.endpoint_x_lineEdit.setObjectName(u"endpoint_x_lineEdit")

        self.horizontalLayout_move_end.addWidget(self.endpoint_x_lineEdit)

        self.endpoint_y_label = BodyLabel(self.layoutWidget)
        self.endpoint_y_label.setObjectName(u"endpoint_y_label")

        self.horizontalLayout_move_end.addWidget(self.endpoint_y_label)

        self.endpoint_y_lineEdit = LineEdit(self.layoutWidget)
        self.endpoint_y_lineEdit.setObjectName(u"endpoint_y_lineEdit")

        self.horizontalLayout_move_end.addWidget(self.endpoint_y_lineEdit)

        self.endpoint_z_label = BodyLabel(self.layoutWidget)
        self.endpoint_z_label.setObjectName(u"endpoint_z_label")

        self.horizontalLayout_move_end.addWidget(self.endpoint_z_label)

        self.endpoint_z_lineEdit = LineEdit(self.layoutWidget)
        self.endpoint_z_lineEdit.setObjectName(u"endpoint_z_lineEdit")

        self.horizontalLayout_move_end.addWidget(self.endpoint_z_lineEdit)


        self.verticalLayout_move.addLayout(self.horizontalLayout_move_end)

        self.horizontalLayout_move_buttons = QHBoxLayout()
        self.horizontalLayout_move_buttons.setObjectName(u"horizontalLayout_move_buttons")
        self.reset_button = PushButton(self.layoutWidget)
        self.reset_button.setObjectName(u"reset_button")

        self.horizontalLayout_move_buttons.addWidget(self.reset_button)

        self.move_button = PushButton(self.layoutWidget)
        self.move_button.setObjectName(u"move_button")

        self.horizontalLayout_move_buttons.addWidget(self.move_button)

        self.loopRadioButton = RadioButton(self.layoutWidget)
        self.loopRadioButton.setObjectName(u"loopRadioButton")
        self.loopRadioButton.setMaximumSize(QSize(100, 24))

        self.horizontalLayout_move_buttons.addWidget(self.loopRadioButton)

        self.loopTimes_lineEdit = LineEdit(self.layoutWidget)
        self.loopTimes_lineEdit.setObjectName(u"loopTimes_lineEdit")
        self.loopTimes_lineEdit.setMaximumSize(QSize(50, 33))

        self.horizontalLayout_move_buttons.addWidget(self.loopTimes_lineEdit)


        self.verticalLayout_move.addLayout(self.horizontalLayout_move_buttons)


        self.verticalLayout_right.addLayout(self.verticalLayout_move)

        self.verticalLayout_work = QVBoxLayout()
        self.verticalLayout_work.setObjectName(u"verticalLayout_work")
        self.horizontalLayout_work_objInfo = QHBoxLayout()
        self.horizontalLayout_work_objInfo.setObjectName(u"horizontalLayout_work_objInfo")
        self.objinfo_label = StrongBodyLabel(self.layoutWidget)
        self.objinfo_label.setObjectName(u"objinfo_label")

        self.horizontalLayout_work_objInfo.addWidget(self.objinfo_label)

        self.objinfo_length_label = BodyLabel(self.layoutWidget)
        self.objinfo_length_label.setObjectName(u"objinfo_length_label")

        self.horizontalLayout_work_objInfo.addWidget(self.objinfo_length_label)

        self.objinfo_length_lineEdit = LineEdit(self.layoutWidget)
        self.objinfo_length_lineEdit.setObjectName(u"objinfo_length_lineEdit")

        self.horizontalLayout_work_objInfo.addWidget(self.objinfo_length_lineEdit)

        self.objinfo_width_label = BodyLabel(self.layoutWidget)
        self.objinfo_width_label.setObjectName(u"objinfo_width_label")

        self.horizontalLayout_work_objInfo.addWidget(self.objinfo_width_label)

        self.objinfo_width_lineEdit = LineEdit(self.layoutWidget)
        self.objinfo_width_lineEdit.setObjectName(u"objinfo_width_lineEdit")

        self.horizontalLayout_work_objInfo.addWidget(self.objinfo_width_lineEdit)

        self.objinfo_height_label = BodyLabel(self.layoutWidget)
        self.objinfo_height_label.setObjectName(u"objinfo_height_label")

        self.horizontalLayout_work_objInfo.addWidget(self.objinfo_height_label)

        self.objinfo_height_lineEdit = LineEdit(self.layoutWidget)
        self.objinfo_height_lineEdit.setObjectName(u"objinfo_height_lineEdit")

        self.horizontalLayout_work_objInfo.addWidget(self.objinfo_height_lineEdit)


        self.verticalLayout_work.addLayout(self.horizontalLayout_work_objInfo)

        self.horizontalLayout_work_stackInfo = QHBoxLayout()
        self.horizontalLayout_work_stackInfo.setObjectName(u"horizontalLayout_work_stackInfo")
        self.stackinfo_label = StrongBodyLabel(self.layoutWidget)
        self.stackinfo_label.setObjectName(u"stackinfo_label")

        self.horizontalLayout_work_stackInfo.addWidget(self.stackinfo_label)

        self.stackinfo_row_label = BodyLabel(self.layoutWidget)
        self.stackinfo_row_label.setObjectName(u"stackinfo_row_label")

        self.horizontalLayout_work_stackInfo.addWidget(self.stackinfo_row_label)

        self.stackinfo_row_lineEdit = LineEdit(self.layoutWidget)
        self.stackinfo_row_lineEdit.setObjectName(u"stackinfo_row_lineEdit")

        self.horizontalLayout_work_stackInfo.addWidget(self.stackinfo_row_lineEdit)

        self.stackinfo_col_label = BodyLabel(self.layoutWidget)
        self.stackinfo_col_label.setObjectName(u"stackinfo_col_label")

        self.horizontalLayout_work_stackInfo.addWidget(self.stackinfo_col_label)

        self.stackinfo_col_lineEdit = LineEdit(self.layoutWidget)
        self.stackinfo_col_lineEdit.setObjectName(u"stackinfo_col_lineEdit")

        self.horizontalLayout_work_stackInfo.addWidget(self.stackinfo_col_lineEdit)

        self.stackinfo_layer_label = BodyLabel(self.layoutWidget)
        self.stackinfo_layer_label.setObjectName(u"stackinfo_layer_label")

        self.horizontalLayout_work_stackInfo.addWidget(self.stackinfo_layer_label)

        self.stackinfo_layer_lineEdit = LineEdit(self.layoutWidget)
        self.stackinfo_layer_lineEdit.setObjectName(u"stackinfo_layer_lineEdit")

        self.horizontalLayout_work_stackInfo.addWidget(self.stackinfo_layer_lineEdit)


        self.verticalLayout_work.addLayout(self.horizontalLayout_work_stackInfo)

        self.horizontalLayout_work_start = QHBoxLayout()
        self.horizontalLayout_work_start.setObjectName(u"horizontalLayout_work_start")
        self.work_startpoint_label = StrongBodyLabel(self.layoutWidget)
        self.work_startpoint_label.setObjectName(u"work_startpoint_label")

        self.horizontalLayout_work_start.addWidget(self.work_startpoint_label)

        self.work_startpoint_x_label = BodyLabel(self.layoutWidget)
        self.work_startpoint_x_label.setObjectName(u"work_startpoint_x_label")

        self.horizontalLayout_work_start.addWidget(self.work_startpoint_x_label)

        self.work_startpoint_x_lineEdit = LineEdit(self.layoutWidget)
        self.work_startpoint_x_lineEdit.setObjectName(u"work_startpoint_x_lineEdit")

        self.horizontalLayout_work_start.addWidget(self.work_startpoint_x_lineEdit)

        self.work_startpoint_y_label = BodyLabel(self.layoutWidget)
        self.work_startpoint_y_label.setObjectName(u"work_startpoint_y_label")

        self.horizontalLayout_work_start.addWidget(self.work_startpoint_y_label)

        self.work_startpoint_y_lineEdit = LineEdit(self.layoutWidget)
        self.work_startpoint_y_lineEdit.setObjectName(u"work_startpoint_y_lineEdit")

        self.horizontalLayout_work_start.addWidget(self.work_startpoint_y_lineEdit)

        self.work_startpoint_z_label = BodyLabel(self.layoutWidget)
        self.work_startpoint_z_label.setObjectName(u"work_startpoint_z_label")

        self.horizontalLayout_work_start.addWidget(self.work_startpoint_z_label)

        self.work_startpoint_z_lineEdit = LineEdit(self.layoutWidget)
        self.work_startpoint_z_lineEdit.setObjectName(u"work_startpoint_z_lineEdit")

        self.horizontalLayout_work_start.addWidget(self.work_startpoint_z_lineEdit)


        self.verticalLayout_work.addLayout(self.horizontalLayout_work_start)

        self.horizontalLayout_work_putInfo = QHBoxLayout()
        self.horizontalLayout_work_putInfo.setObjectName(u"horizontalLayout_work_putInfo")
        self.putinfo_label = StrongBodyLabel(self.layoutWidget)
        self.putinfo_label.setObjectName(u"putinfo_label")

        self.horizontalLayout_work_putInfo.addWidget(self.putinfo_label)

        self.putinfo_row_label = BodyLabel(self.layoutWidget)
        self.putinfo_row_label.setObjectName(u"putinfo_row_label")

        self.horizontalLayout_work_putInfo.addWidget(self.putinfo_row_label)

        self.putinfo_row_lineEdit = LineEdit(self.layoutWidget)
        self.putinfo_row_lineEdit.setObjectName(u"putinfo_row_lineEdit")

        self.horizontalLayout_work_putInfo.addWidget(self.putinfo_row_lineEdit)

        self.putinfo_col_label = BodyLabel(self.layoutWidget)
        self.putinfo_col_label.setObjectName(u"putinfo_col_label")

        self.horizontalLayout_work_putInfo.addWidget(self.putinfo_col_label)

        self.putinfo_col_lineEdit = LineEdit(self.layoutWidget)
        self.putinfo_col_lineEdit.setObjectName(u"putinfo_col_lineEdit")

        self.horizontalLayout_work_putInfo.addWidget(self.putinfo_col_lineEdit)

        self.putinfo_layer_label = BodyLabel(self.layoutWidget)
        self.putinfo_layer_label.setObjectName(u"putinfo_layer_label")

        self.horizontalLayout_work_putInfo.addWidget(self.putinfo_layer_label)

        self.putinfo_layer_lineEdit = LineEdit(self.layoutWidget)
        self.putinfo_layer_lineEdit.setObjectName(u"putinfo_layer_lineEdit")

        self.horizontalLayout_work_putInfo.addWidget(self.putinfo_layer_lineEdit)


        self.verticalLayout_work.addLayout(self.horizontalLayout_work_putInfo)

        self.horizontalLayout_work_end = QHBoxLayout()
        self.horizontalLayout_work_end.setObjectName(u"horizontalLayout_work_end")
        self.work_endtpoint_label = StrongBodyLabel(self.layoutWidget)
        self.work_endtpoint_label.setObjectName(u"work_endtpoint_label")

        self.horizontalLayout_work_end.addWidget(self.work_endtpoint_label)

        self.work_endtpoint_x_label = BodyLabel(self.layoutWidget)
        self.work_endtpoint_x_label.setObjectName(u"work_endtpoint_x_label")

        self.horizontalLayout_work_end.addWidget(self.work_endtpoint_x_label)

        self.work_endtpoint_x_lineEdit = LineEdit(self.layoutWidget)
        self.work_endtpoint_x_lineEdit.setObjectName(u"work_endtpoint_x_lineEdit")

        self.horizontalLayout_work_end.addWidget(self.work_endtpoint_x_lineEdit)

        self.work_endtpoint_y_label = BodyLabel(self.layoutWidget)
        self.work_endtpoint_y_label.setObjectName(u"work_endtpoint_y_label")

        self.horizontalLayout_work_end.addWidget(self.work_endtpoint_y_label)

        self.work_endtpoint_y_lineEdit = LineEdit(self.layoutWidget)
        self.work_endtpoint_y_lineEdit.setObjectName(u"work_endtpoint_y_lineEdit")

        self.horizontalLayout_work_end.addWidget(self.work_endtpoint_y_lineEdit)

        self.work_endtpoint_z_label = BodyLabel(self.layoutWidget)
        self.work_endtpoint_z_label.setObjectName(u"work_endtpoint_z_label")

        self.horizontalLayout_work_end.addWidget(self.work_endtpoint_z_label)

        self.work_endtpoint_z_lineEdit = LineEdit(self.layoutWidget)
        self.work_endtpoint_z_lineEdit.setObjectName(u"work_endtpoint_z_lineEdit")

        self.horizontalLayout_work_end.addWidget(self.work_endtpoint_z_lineEdit)


        self.verticalLayout_work.addLayout(self.horizontalLayout_work_end)

        self.horizontalLayout_work_buttons = QHBoxLayout()
        self.horizontalLayout_work_buttons.setObjectName(u"horizontalLayout_work_buttons")
        self.move_reset_button = PushButton(self.layoutWidget)
        self.move_reset_button.setObjectName(u"move_reset_button")
        self.move_reset_button.setAutoFillBackground(False)
        self.move_reset_button.setStyleSheet(u"PushButton, ToolButton, ToggleButton, ToggleToolButton {\n"
"    color: black;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 0.073);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"    border-radius: 5px;\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    padding: 5px 12px 6px 12px;\n"
"    outline: none;\n"
"}\n"
"\n"
"ToolButton {\n"
"    padding: 5px 9px 6px 8px;\n"
"}\n"
"\n"
"PushButton[isPlaceholderText=true] {\n"
"    color: rgba(0, 0, 0, 0.6063);\n"
"}\n"
"\n"
"PushButton[hasIcon=false] {\n"
"    padding: 5px 12px 6px 12px;\n"
"}\n"
"\n"
"PushButton[hasIcon=true] {\n"
"    padding: 5px 12px 6px 36px;\n"
"}\n"
"\n"
"DropDownToolButton, PrimaryDropDownToolButton {\n"
"    padding: 5px 31px 6px 8px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=false],\n"
"PrimaryDropDownPushButton[hasIcon=false] {\n"
"    padding: 5px 31px 6px 12px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=true],\n"
"PrimaryDropDownPushButton[hasIcon=true] {\n"
"    padding: 5p"
                        "x 31px 6px 36px;\n"
"}\n"
"\n"
"PushButton:hover, ToolButton:hover, ToggleButton:hover, ToggleToolButton:hover {\n"
"    background: rgba(249, 249, 249, 0.5);\n"
"}\n"
"\n"
"PushButton:pressed, ToolButton:pressed, ToggleButton:pressed, ToggleToolButton:pressed {\n"
"    color: rgba(0, 0, 0, 0.63);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"}\n"
"\n"
"PushButton:disabled, ToolButton:disabled, ToggleButton:disabled, ToggleToolButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 0.06);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
"}\n"
"\n"
"\n"
"PrimaryPushButton,\n"
"PrimaryToolButton,\n"
"ToggleButton:checked,\n"
"ToggleToolButton:checked {\n"
"    color: white;\n"
"    background-color: #009faa;\n"
"    border: 1px solid #00a7b3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:hover,\n"
"PrimaryToolButton:hover,\n"
"ToggleBu"
                        "tton:checked:hover,\n"
"ToggleToolButton:checked:hover {\n"
"    background-color: #00a7b3;\n"
"    border: 1px solid #2daab3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:pressed,\n"
"PrimaryToolButton:pressed,\n"
"ToggleButton:checked:pressed,\n"
"ToggleToolButton:checked:pressed {\n"
"    color: rgba(255, 255, 255, 0.63);\n"
"    background-color: #3eabb3;\n"
"    border: 1px solid #3eabb3;\n"
"}\n"
"\n"
"PrimaryPushButton:disabled,\n"
"PrimaryToolButton:disabled,\n"
"ToggleButton:checked:disabled,\n"
"ToggleToolButton:checked:disabled {\n"
"    color: rgba(255, 255, 255, 0.9);\n"
"    background-color: rgb(205, 205, 205);\n"
"    border: 1px solid rgb(205, 205, 205);\n"
"}\n"
"\n"
"SplitDropButton,\n"
"PrimarySplitDropButton {\n"
"    border-left: none;\n"
"    border-top-left-radius: 0;\n"
"    border-bottom-left-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton,\n"
"#splitToolButton,\n"
"#primarySplitPushButton,\n"
"#primarySplitToolButton {\n"
"    border-top-right-radius: 0;\n"
""
                        "    border-bottom-right-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton:pressed,\n"
"#splitToolButton:pressed,\n"
"SplitDropButton:pressed {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"}\n"
"\n"
"PrimarySplitDropButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"#primarySplitPushButton, #primarySplitToolButton {\n"
"    border-right: 1px solid #3eabb3;\n"
"}\n"
"\n"
"#primarySplitPushButton:pressed, #primarySplitToolButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"HyperlinkButton {\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    padding: 6px 12px 6px 12px;\n"
"    color: #009faa;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"HyperlinkButton[hasIcon=false] {\n"
"    padding: 6px 12px 6px 12px;\n"
"}\n"
"\n"
"HyperlinkButton[hasIcon=true] {\n"
"    padding: 6px 12px 6px 36px;\n"
"}\n"
"\n"
"HyperlinkButton:hover {\n"
"    color: #009faa;\n"
"    background-color: rgba(0, 0, 0, 10);\n"
""
                        "    border: none;\n"
"}\n"
"\n"
"HyperlinkButton:pressed {\n"
"    color: #009faa;\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"    border: none;\n"
"}\n"
"\n"
"HyperlinkButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.43);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"RadioButton {\n"
"    min-height: 24px;\n"
"    max-height: 24px;\n"
"    background-color: transparent;\n"
"    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
"    color: black;\n"
"}\n"
"\n"
"RadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 11px;\n"
"    border: 2px solid #999999;\n"
"    background-color: rgba(0, 0, 0, 5);\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"RadioButton::indicator:hover {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"RadioButton::indicator:pressed {\n"
"    border: 2px solid #bbbbbb;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255,"
                        " 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 rgb(225, 224, 223),\n"
"            stop:1 rgb(225, 224, 223));\n"
"}\n"
"\n"
"RadioButton::indicator:checked {\n"
"    height: 22px;\n"
"    width: 22px;\n"
"    border: none;\n"
"    border-radius: 11px;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:hover {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.6 rgb(255, 255, 255),\n"
"            stop:0.7 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(2"
                        "55, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton:disabled {\n"
"    color: rgba(0, 0, 0, 110);\n"
"}\n"
"\n"
"RadioButton::indicator:disabled {\n"
"    border: 2px solid #bbbbbb;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"RadioButton::indicator:disabled:checked {\n"
"    border: none;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 rgba(0, 0, 0, 0.2169),\n"
"            stop:1 rgba(0, 0, 0, 0.2169));\n"
"}\n"
"\n"
"TransparentToolButton,\n"
"TransparentToggleToolButton,\n"
"TransparentDropDownToolButton,\n"
"TransparentPushButton,\n"
"TransparentDropDownPushButton,\n"
"TransparentTogglePushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"TransparentToolBu"
                        "tton:hover,\n"
"TransparentToggleToolButton:hover,\n"
"TransparentDropDownToolButton:hover,\n"
"TransparentPushButton:hover,\n"
"TransparentDropDownPushButton:hover,\n"
"TransparentTogglePushButton:hover {\n"
"    background-color: rgba(0, 0, 0, 9);\n"
"    border: none;\n"
"}\n"
"\n"
"TransparentToolButton:pressed,\n"
"TransparentToggleToolButton:pressed,\n"
"TransparentDropDownToolButton:pressed,\n"
"TransparentPushButton:pressed,\n"
"TransparentDropDownPushButton:pressed,\n"
"TransparentTogglePushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"    border: none;\n"
"}\n"
"\n"
"TransparentToolButton:disabled,\n"
"TransparentToggleToolButton:disabled,\n"
"TransparentDropDownToolButton:disabled,\n"
"TransprentPushButton:disabled,\n"
"TransparentDropDownPushButton:disabled,\n"
"TransprentTogglePushButton:disabled {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"PillPushButton,\n"
"PillPushButton:hover,\n"
"PillPushButton:pressed,\n"
"PillPushButton:disabled,\n"
""
                        "PillPushButton:checked,\n"
"PillPushButton:checked:hover,\n"
"PillPushButton:checked:pressed,\n"
"PillPushButton:disabled:checked,\n"
"PillToolButton,\n"
"PillToolButton:hover,\n"
"PillToolButton:pressed,\n"
"PillToolButton:disabled,\n"
"PillToolButton:checked,\n"
"PillToolButton:checked:hover,\n"
"PillToolButton:checked:pressed,\n"
"PillToolButton:disabled:checked {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"")

        self.horizontalLayout_work_buttons.addWidget(self.move_reset_button)

        self.work_button = PushButton(self.layoutWidget)
        self.work_button.setObjectName(u"work_button")

        self.horizontalLayout_work_buttons.addWidget(self.work_button)


        self.verticalLayout_work.addLayout(self.horizontalLayout_work_buttons)


        self.verticalLayout_right.addLayout(self.verticalLayout_work)

        self.verticalLayout_move_list = QVBoxLayout()
        self.verticalLayout_move_list.setObjectName(u"verticalLayout_move_list")
        self.put_list_label = StrongBodyLabel(self.layoutWidget)
        self.put_list_label.setObjectName(u"put_list_label")

        self.verticalLayout_move_list.addWidget(self.put_list_label)

        self.put_list_starts_textEdit = TextEdit(self.layoutWidget)
        self.put_list_starts_textEdit.setObjectName(u"put_list_starts_textEdit")

        self.verticalLayout_move_list.addWidget(self.put_list_starts_textEdit)

        self.endpoint_list_label = StrongBodyLabel(self.layoutWidget)
        self.endpoint_list_label.setObjectName(u"endpoint_list_label")

        self.verticalLayout_move_list.addWidget(self.endpoint_list_label)

        self.put_list_ends_textEdit = TextEdit(self.layoutWidget)
        self.put_list_ends_textEdit.setObjectName(u"put_list_ends_textEdit")

        self.verticalLayout_move_list.addWidget(self.put_list_ends_textEdit)

        self.horizontalLayout_move_list_buttons = QHBoxLayout()
        self.horizontalLayout_move_list_buttons.setObjectName(u"horizontalLayout_move_list_buttons")
        self.reset_list_button = PushButton(self.layoutWidget)
        self.reset_list_button.setObjectName(u"reset_list_button")

        self.horizontalLayout_move_list_buttons.addWidget(self.reset_list_button)

        self.move_list_button = PushButton(self.layoutWidget)
        self.move_list_button.setObjectName(u"move_list_button")

        self.horizontalLayout_move_list_buttons.addWidget(self.move_list_button)


        self.verticalLayout_move_list.addLayout(self.horizontalLayout_move_list_buttons)


        self.verticalLayout_right.addLayout(self.verticalLayout_move_list)

        self.layoutWidget1 = QWidget(ControlUi)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 40, 481, 841))
        self.verticalLayout_left = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_left.setObjectName(u"verticalLayout_left")
        self.verticalLayout_left.setContentsMargins(0, 0, 0, 0)
        self.video_view = ImageLabel(self.layoutWidget1)
        self.video_view.setObjectName(u"video_view")
        sizePolicy1.setHeightForWidth(self.video_view.sizePolicy().hasHeightForWidth())
        self.video_view.setSizePolicy(sizePolicy1)
        self.video_view.setMinimumSize(QSize(479, 327))
        self.video_view.setMaximumSize(QSize(479, 327))

        self.verticalLayout_left.addWidget(self.video_view)

        self.serial_label = TitleLabel(self.layoutWidget1)
        self.serial_label.setObjectName(u"serial_label")
        self.serial_label.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.serial_label.sizePolicy().hasHeightForWidth())
        self.serial_label.setSizePolicy(sizePolicy2)
        self.serial_label.setMinimumSize(QSize(75, 16))
        self.serial_label.setMaximumSize(QSize(75, 16))
        self.serial_label.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(11)
        font.setBold(False)
        self.serial_label.setFont(font)

        self.verticalLayout_left.addWidget(self.serial_label)

        self.serial_text = TextEdit(self.layoutWidget1)
        self.serial_text.setObjectName(u"serial_text")

        self.verticalLayout_left.addWidget(self.serial_text)


        self.retranslateUi(ControlUi)

        QMetaObject.connectSlotsByName(ControlUi)
    # setupUi

    def retranslateUi(self, ControlUi):
        ControlUi.setWindowTitle(QCoreApplication.translate("ControlUi", u"Form", None))
        self.video_switch_label.setText(QCoreApplication.translate("ControlUi", u"\u6444\u50cf\u5934\uff1a", None))
        self.video_switch.setProperty(u"onText", "")
        self.video_switch.setProperty(u"offText", "")
        self.maxspeed_label.setText(QCoreApplication.translate("ControlUi", u"\u6700\u5927\u901f\u5ea6\uff1a", None))
        self.accel_label.setText(QCoreApplication.translate("ControlUi", u"\u52a0\u901f\u5ea6\uff1a", None))
        self.speed_label.setText(QCoreApplication.translate("ControlUi", u"\u901f\u5ea6\uff1a", None))
#if QT_CONFIG(tooltip)
        self.maxspeed_slider.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.maxspeed_slider.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.stratpoint_label.setText(QCoreApplication.translate("ControlUi", u"\u8d77\u70b9\uff1a", None))
        self.startpoint_x_label.setText(QCoreApplication.translate("ControlUi", u"X\u5750\u6807:", None))
        self.startpoint_y_label.setText(QCoreApplication.translate("ControlUi", u"Y\u5750\u6807:", None))
        self.startpoint_z_label.setText(QCoreApplication.translate("ControlUi", u"Z\u5750\u6807:", None))
        self.endpoint_label.setText(QCoreApplication.translate("ControlUi", u"\u7ec8\u70b9\uff1a", None))
        self.endpoint_x_label.setText(QCoreApplication.translate("ControlUi", u"X\u5750\u6807:", None))
        self.endpoint_y_label.setText(QCoreApplication.translate("ControlUi", u"Y\u5750\u6807:", None))
        self.endpoint_z_label.setText(QCoreApplication.translate("ControlUi", u"Z\u5750\u6807:", None))
        self.reset_button.setText(QCoreApplication.translate("ControlUi", u"\u590d\u4f4d", None))
        self.move_button.setText(QCoreApplication.translate("ControlUi", u"\u8fd0\u52a8", None))
        self.loopRadioButton.setText(QCoreApplication.translate("ControlUi", u"\u5f80\u590d\u8fd0\u52a8", None))
        self.objinfo_label.setText(QCoreApplication.translate("ControlUi", u"\u7269\u4f53\u4fe1\u606f(mm):", None))
        self.objinfo_length_label.setText(QCoreApplication.translate("ControlUi", u"\u957f:", None))
        self.objinfo_width_label.setText(QCoreApplication.translate("ControlUi", u"\u5bbd:", None))
        self.objinfo_height_label.setText(QCoreApplication.translate("ControlUi", u"\u9ad8:", None))
        self.stackinfo_label.setText(QCoreApplication.translate("ControlUi", u"\u5806\u653e\u4fe1\u606f:", None))
        self.stackinfo_row_label.setText(QCoreApplication.translate("ControlUi", u"\u884c\u6570:", None))
        self.stackinfo_col_label.setText(QCoreApplication.translate("ControlUi", u"\u5217\u6570:", None))
        self.stackinfo_layer_label.setText(QCoreApplication.translate("ControlUi", u"\u5c42\u6570:", None))
        self.work_startpoint_label.setText(QCoreApplication.translate("ControlUi", u"\u8d77\u59cb\u70b9(\u5de6\u4e0a):", None))
        self.work_startpoint_x_label.setText(QCoreApplication.translate("ControlUi", u"X:", None))
        self.work_startpoint_y_label.setText(QCoreApplication.translate("ControlUi", u"Y:", None))
        self.work_startpoint_z_label.setText(QCoreApplication.translate("ControlUi", u"Z:", None))
        self.putinfo_label.setText(QCoreApplication.translate("ControlUi", u"\u653e\u7f6e\u4fe1\u606f:", None))
        self.putinfo_row_label.setText(QCoreApplication.translate("ControlUi", u"\u884c\u6570:", None))
        self.putinfo_col_label.setText(QCoreApplication.translate("ControlUi", u"\u5217\u6570:", None))
        self.putinfo_layer_label.setText(QCoreApplication.translate("ControlUi", u"\u5c42\u6570:", None))
        self.work_endtpoint_label.setText(QCoreApplication.translate("ControlUi", u"\u653e\u7f6e\u70b9(\u5de6\u4e0a)", None))
        self.work_endtpoint_x_label.setText(QCoreApplication.translate("ControlUi", u"X:", None))
        self.work_endtpoint_y_label.setText(QCoreApplication.translate("ControlUi", u"Y:", None))
        self.work_endtpoint_z_label.setText(QCoreApplication.translate("ControlUi", u"Z:", None))
        self.move_reset_button.setText(QCoreApplication.translate("ControlUi", u"\u590d\u4f4d", None))
        self.work_button.setText(QCoreApplication.translate("ControlUi", u"\u5f00\u59cb\u7801\u579b", None))
        self.put_list_label.setText(QCoreApplication.translate("ControlUi", u"\u8d77\u59cb\u5750\u6807\u6570\u7ec4(\u6bcf\u884c\u4e00\u6761\u5750\u6807\u4fe1\u606f\uff0c\u6362\u884c\u7b26\u9694\u5f00)\uff1a", None))
        self.endpoint_list_label.setText(QCoreApplication.translate("ControlUi", u"\u7ec8\u70b9\u5750\u6807\u6570\u7ec4(\u6bcf\u884c\u4e00\u6761\u5750\u6807\u4fe1\u606f\uff0c\u6362\u884c\u7b26\u9694\u5f00)", None))
        self.reset_list_button.setText(QCoreApplication.translate("ControlUi", u"\u590d\u4f4d", None))
        self.move_list_button.setText(QCoreApplication.translate("ControlUi", u"\u4e0a\u6599", None))
        self.video_view.setText("")
        self.serial_label.setText(QCoreApplication.translate("ControlUi", u"\u4e32\u53e3\u4fe1\u606f\uff1a", None))
    # retranslateUi

