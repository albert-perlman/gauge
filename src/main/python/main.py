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
  resized = pyqtSignal()
  focusIn = pyqtSignal()
  focusOut = pyqtSignal()

  def __init__(self, *args, **kwargs):
    super(MainWindow, self).__init__(*args, **kwargs)

    self.appctxt = ApplicationContext()

    # Main Widget Container
    MainWidgetContainer = QWidget()
    QFontDatabase.addApplicationFont(self.appctxt.get_resource('fonts/Montserrat-Thin.ttf'))
    # MainWidgetContainer.setStyleSheet(StyleSheet.css("window"))
    self.setCentralWidget(MainWidgetContainer)

    windowPosX = 3600
    windowPosY = -500
    windowWidth = 160
    windowHeight = 180

    timer = QTimer(self)                 # create a timer object
    timer.timeout.connect(self.update)   # add action to the timer, update the whole code
    timer.start(0)                    # update cycle in milliseconds

    self.setGeometry(windowPosX, windowPosY, windowWidth, windowHeight)       # window location and size
    self.setAttribute(Qt.WA_TranslucentBackground)
    self.setWindowFlags(Qt.FramelessWindowHint)

    #############
    #  WIDGETS  #
    #############
    # # close button
    # self.closeBtn = QPushButton(MainWidgetContainer)
    # self.closeBtn.setFixedSize(40,40)
    # self.closeBtn.setText('X')
    # self.closeBtn.setStyleSheet(StyleSheet.css("closeFocusIn"))
    # self.closeBtn.clicked.connect(lambda: self.close())
    # pos = QPoint(windowWidth-30,-10)
    # self.closeBtn.move(pos)

    spacerTop = QLabel()
    spacerTop.setFixedSize(0,15)

    # temp display
    self.tempDisplay = QLabel(str(self.getGpuTemp()))
    self.tempDisplay.setAlignment(Qt.AlignCenter)
    self.tempDisplay.setStyleSheet(StyleSheet.css("temp"))

    spacerBottom = QLabel()
    spacerBottom.setFixedSize(0,2.5)

    # GPU label
    gpuLabel = QLabel("GPU")
    gpuLabel.setAlignment(Qt.AlignCenter)
    gpuLabel.setStyleSheet(StyleSheet.css("gpu"))

    #############
    #  LAYOUTS  #
    #############
    MainVLayout = QVBoxLayout()
    MainVLayout.setAlignment(Qt.AlignCenter)
    MainVLayout.addWidget(spacerTop)
    MainVLayout.addWidget(self.tempDisplay)
    MainVLayout.addWidget(spacerBottom)
    MainVLayout.addWidget(gpuLabel)
    MainWidgetContainer.setLayout(MainVLayout)

    ####################
    #  SIGNAL / SLOTS  #
    ####################
    self.focusIn.connect(self.SLOT_focusIn)
    self.focusOut.connect(self.SLOT_focusOut)

    ####################
    #     START-UP     #
    ####################
    self.updateTitle()
    self.show()
    self.setFocusPolicy(Qt.ClickFocus)

### end MainWindow init() #####################################################################

  def getGpuTemp(self):
    clr.AddReference(r"D:\util\OpenHardwareMonitor\OpenHardwareMonitorLib.dll")
    from OpenHardwareMonitor.Hardware import Computer
    c = Computer()
    c.CPUEnabled = True # get the Info about CPU
    c.GPUEnabled = True # get the Info about GPU
    c.Open()
    for a in range(0, len(c.Hardware[1].Sensors)):
      # print(c.Hardware[1].Sensors[a].Identifier)
      if "/nvidiagpu/0/temperature/0" in str(c.Hardware[1].Sensors[a].Identifier):
        c.Hardware[1].Update()
        return int(c.Hardware[1].Sensors[a].get_Value())

  def paintEvent(self, event):
    canvasHeight = 150
    canvasWidth = canvasHeight

    gaugeSize = 270
    gaugeWidth = 5
    gaugeOutlineWidth = 0.2

    gaugeValuePainter = QPainter(self)
    gaugeValuePainter.setRenderHint(QPainter.Antialiasing)
    gaugeValuePainter.setPen(QPen(Qt.white, gaugeWidth, cap=Qt.SquareCap))

    # # ---------- the following lines simulate sensor reading. -----------
    # gaugeValue = 0
    # adder = 0.1
    # if gaugeValue > gaugeSize or gaugeValue < 0:  # variable to make arc move
    #     adder = -adder  # gaugeValue corresponds to the
    #     # value to be indicated by the arc.
    # gaugeValue = gaugeValue + adder
    # # --------------------- end simulation ------------------------------

    minTemp = 20
    maxTemp = 100
    gpuTemp = self.getGpuTemp()

    # map temp range [20-100] to gauge range [0-270]
    gaugeValue = (((gpuTemp - minTemp) * (gaugeSize)) / (maxTemp - minTemp))
    self.tempDisplay.setText(str(gpuTemp))

    # drawArc syntax:
    #       drawArc(canvas_origin_x, canvas_origin_y, canvas_width, canvas_height, startAngle, spanAngle)
    gaugeValuePainter.drawArc( gaugeWidth/2, gaugeWidth/2,
                     canvasHeight + gaugeWidth, canvasWidth + gaugeWidth,
                     int((gaugeSize + (180 - gaugeSize) / 2)*16), int(-gaugeValue*16) )


    gaugeOutlinePainter = QPainter(self)    # create a painter object
    gaugeOutlinePainter.setRenderHint(QPainter.Antialiasing)  # tune up painter
    gaugeOutlinePainter.setPen(QPen(Qt.white, gaugeOutlineWidth, cap=Qt.FlatCap))

    gaugeOutlinePainter.drawArc(gaugeWidth/2, gaugeWidth/2,   # binding box: x0, y0, pixels
              canvasHeight + gaugeWidth, # binding box: height
              canvasWidth + gaugeWidth,  # binding box: width
              int((gaugeSize + (180 - gaugeSize) / 2)*16),  # arc start point, degrees (?)
              int(-270*16))         # arc span

    gaugeValuePainter.end()
    gaugeOutlinePainter.end()

  # SLOT: Main Window has been resized
  def SLOT_focusIn(self):
    self.closeBtn.setStyleSheet(StyleSheet.css("closeFocusIn"))
    print("focus in")

  # SLOT: Main Window has been resized
  def SLOT_focusOut(self):
    self.closeBtn.setStyleSheet(StyleSheet.css("closeFocusOut"))
    print("focus out")


  # critical dialog pop-up
  def dialogCritical(self, s):
    dlg = QMessageBox(self)
    dlg.setText(s)
    dlg.setIcon(QMessageBox.Critical)
    dlg.show()

  # delete all widgets in a layout
  def clearLayout(self, layout):
    while layout.count():
      child = layout.takeAt(0)
      if child.widget():
        child.widget().deleteLater()

  # update main window title
  def updateTitle(self, str=""):
    self.setWindowTitle(""+ str)

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

  # overload Main Window resizeEvent to emit signal
  def resizeEvent(self, event):
    self.resized.emit()
    return super(MainWindow, self).resizeEvent(event)

  # overload Main Window focusInEvent to emit signal
  def focusInEvent(self, event):
    print("focus in")
    self.focusIn.emit()
    return super(MainWindow, self).focusInEvent(event)

  # overload Main Window focusOutEvent to emit signal
  def focusOutEvent(self, event):
    print("focus out")
    self.focusOut.emit()
    return super(MainWindow, self).focusOutEvent(event)

def changedFocusSlot(old, now):
    if (now==None and QApplication.activeWindow()!=None):
        print("set focus to the active window")
        QApplication.activeWindow().setFocus()

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    # QMainWindow.connect(appctxt, SIGNAL("focusChanged(QWidget *, QWidget *)"), changedFocusSlot)
    Window = MainWindow()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)



# class MainWindow(QMainWindow):
#   focusIn = pyqtSignal()
#   focusOut = pyqtSignal()
#   def focusInEvent(self, event):
#     print("focus in")
#     self.focusIn.emit()
#   def focusOutEvent(self, event):
#     print("focus out")
#     self.focusOut.emit()
