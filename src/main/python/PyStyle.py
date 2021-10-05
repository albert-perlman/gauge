# StyleSheet class returns CSS stylesheets for QWidgets

class StyleSheet(object):
  def __init__(self, arg):
    super(ClassName, self).__init__()
    self.arg = arg

  def css(widget=None):

    if ("window" == widget):

        css = \
        "QWidget {" + \
        "font-family:Montserrat;" + \
        "color:rgb(255,255,255);" + \
        "background-color:" + \
        "qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1," + \
        "stop: 0.0 rgb(35,35,35)" + \
        "stop: 0.2 rgb(50,50,50)" + \
        "stop: 0.7 rgb(50,50,50)," + \
        "stop: 1.0 rgb(25,25,25));" + \
        "}"

        return css

    elif ("temp" == widget):

        css = \
        "QLabel {" + \
        "font-size:32pt;" + \
        "font-family:Montserrat;" + \
        "color:rgb(255,255,255);" + \
        "}"

        return css

    elif ("gpu" == widget):

        css = \
        "QLabel {" + \
        "font-size:18pt;" + \
        "font-weight:bold;" + \
        "font-family:Montserrat;" + \
        "color:rgb(255,255,255);" + \
        "}"

        return css

    elif ("closeFocusIn" == widget):

        css = \
        "QPushButton {" + \
        "font-size:12pt;" + \
        "font-family:Montserrat;" + \
        "color:rgb(55,55,55);" + \
        "background:transparent;" + \
        "}"

        return css

    elif ("closeFocusOut" == widget):

        css = \
        "QLabel {" + \
        "font-size:18pt;" + \
        "font-family:Montserrat;" + \
        "color:rgb(255,255,255,0);" + \
        "background-color:rgb(255,255,255,0);" + \
        "}"

        return css
