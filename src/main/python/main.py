from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtMultimedia  import *

import sys
import clr

from PyStyle import *

class MainWindow(QMainWindow):

  def __init__(self, *args, **kwargs):
    super(MainWindow, self).__init__(*args, **kwargs)

    self.appctxt = ApplicationContext()

    MainWidgetContainer = QWidget()
    QFontDatabase.addApplicationFont(self.appctxt.get_resource('fonts/Montserrat-Thin.ttf'))
    self.setCentralWidget(MainWidgetContainer)

    # configure application window
    self.setFixedSize(160, 180)
    self.setAttribute(Qt.WA_TranslucentBackground)
    self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)

    # gauge refresh rate (queues self.paintEvent every 500ms)
    refreshTimer = QTimer(self)
    refreshTimer.timeout.connect(self.update)
    refreshTimer.start(1000)

    # identify gpu sensor
    self.gpuSensor = self.getGpuSensor()

    #############
    #  WIDGETS  #
    #############
    spacerTop = QWidget()
    spacerTop.setFixedSize(0,15)
    spacerBottom = QWidget()
    spacerBottom.setFixedSize(0,2.5)

    # temp display
    self.tempDisplay = QLabel(str(self.getGpuTemp()))
    self.tempDisplay.setAlignment(Qt.AlignCenter)
    self.tempDisplay.setStyleSheet(StyleSheet.css("temp"))

    # GPU label
    self.gpuLabel = QLabel("GPU")
    self.gpuLabel.setAlignment(Qt.AlignCenter)
    self.gpuLabel.setStyleSheet(StyleSheet.css("gpu"))

    #############
    #  LAYOUTS  #
    #############
    MainVLayout = QVBoxLayout()
    MainVLayout.setAlignment(Qt.AlignCenter)
    MainVLayout.addWidget(spacerTop)
    MainVLayout.addWidget(self.tempDisplay)
    MainVLayout.addWidget(spacerBottom)
    MainVLayout.addWidget(self.gpuLabel)
    MainWidgetContainer.setLayout(MainVLayout)

    ####################
    #  SIGNAL / SLOTS  #
    ####################

    ####################
    #     START-UP     #
    ####################
    self.show()


  # draw gauge, update temp display, and set window position
  def paintEvent(self, event):

    # set display temperature
    gpuTemp = self.getGpuTemp()
    self.tempDisplay.setText(str(gpuTemp))

    # update window position and colors from user config
    self.getUserConfig()
    self.setWindowPos()
    self.tempDisplay.setStyleSheet(StyleSheet.css("temp", self.gaugeColorStr))
    self.gpuLabel.setStyleSheet(StyleSheet.css("gpu", self.gaugeColorStr))

    # gauge painter canvas size
    canvasHeight = 150
    canvasWidth = canvasHeight

    # gauge arc range: [0-270] degrees
    gaugeSize = 270
    gaugeWidth = 5
    gaugeOutlineWidth = 0.3

    # temp range: [20 - 100] C
    minTemp = 20
    maxTemp = 100

    if gpuTemp < 20: gpuTemp = 20
    if gpuTemp > 100: gpuTemp = 100

    # map hardware temp reading from temp range [20-100] to gauge range [0-270]
    gaugeValue = (((gpuTemp - minTemp) * (gaugeSize)) / (maxTemp - minTemp))

    # paint gauge value
    gaugeValuePainter = QPainter(self)
    gaugeValuePainter.setRenderHint(QPainter.Antialiasing)
    gaugeValuePainter.setPen(QPen(self.gaugeColor, gaugeWidth, cap=Qt.SquareCap))

    # drawArc( canvas_origin_x, canvas_origin_y, canvas_width, canvas_height, start_angle, span_angle )
    gaugeValuePainter.drawArc( gaugeWidth/2, gaugeWidth/2,
                               canvasHeight + gaugeWidth, canvasWidth + gaugeWidth,
                               int((gaugeSize + (180 - gaugeSize) / 2)*16), int(-gaugeValue*16) )
    gaugeValuePainter.end()

    # paint gauge outline
    gaugeOutlinePainter = QPainter(self)
    gaugeOutlinePainter.setRenderHint(QPainter.Antialiasing)
    gaugeOutlinePainter.setPen(QPen(self.gaugeColor, gaugeOutlineWidth, cap=Qt.FlatCap))

    gaugeOutlinePainter.drawArc( gaugeWidth/2, gaugeWidth/2,
                                 canvasHeight + gaugeWidth, canvasWidth + gaugeWidth,
                                 int((gaugeSize + (180 - gaugeSize) / 2)*16), int(-270*16) )
    gaugeOutlinePainter.end()


  def getGpuTemp(self):
    self.computer.Hardware[1].Update()
    return int(self.gpuSensor.get_Value())


  # identify OpenHardwareMonitor gpu temperature sensor
  def getGpuSensor(self):
    clr.AddReference(self.appctxt.get_resource("OpenHardwareMonitorLib.dll"))
    from OpenHardwareMonitor.Hardware import Computer
    self.computer = Computer()
    self.computer.CPUEnabled = True # get the Info about CPU
    self.computer.GPUEnabled = True # get the Info about GPU
    self.computer.Open()
    for i in range(0, len(self.computer.Hardware[1].Sensors)):
      if "/nvidiagpu/0/temperature/0" in str(self.computer.Hardware[1].Sensors[i].Identifier):
        return self.computer.Hardware[1].Sensors[i]


  # read gauge.config
  def getUserConfig(self):
    configFile = open(self.appctxt.get_resource('gauge.config'), 'r')
    self.windowPos = list( map(int, configFile.readline().split(',')) )
    rgba = list( map(int, configFile.readline().split(',')) )
    self.gaugeColor = QColor(rgba[0], rgba[1], rgba[2], rgba[3])
    self.gaugeColorStr = "rgba({0},{1},{2},{3})".format(rgba[0], rgba[1], rgba[2], rgba[3])
    self.alarmTemp = configFile.readline()

  def setWindowPos(self):
    self.move(self.windowPos[0], self.windowPos[1])

  # map key press events to gallery navigation
  def keyPressEvent(self, event):

    keyCode = event.key()

    # map left / right arrow keys
    if (16777234 == keyCode):   # left arrow
      pass
    elif (16777236 == keyCode): # right arrow
      pass

    try: # map 0-9 key press
      if (49 == keyCode):   # 1
        pass
      elif (50 == keyCode): # 2
        pass
      elif (51 == keyCode): # 3
        pass
      elif (52 == keyCode): # 4
        pass
      elif (53 == keyCode): # 5
        pass
      elif (54 == keyCode): # 6
        pass
      elif (55 == keyCode): # 7
        pass
      elif (56 == keyCode): # 8
        pass
      elif (57 == keyCode): # 9
        pass
      elif (48 == keyCode): # 0
        pass
    except:
      pass


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    Window = MainWindow()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
