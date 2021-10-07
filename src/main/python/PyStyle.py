# StyleSheet class returns CSS stylesheets for QWidgets

class StyleSheet(object):
  def __init__(self, arg):
    super(ClassName, self).__init__()
    self.arg = arg

  def css(widget, color="rgb(255,255,255)"):

    if ("temp" == widget):
        css = \
        "QLabel {" + \
        "font-size:32pt;" + \
        "font-family:Montserrat;" + \
        "color:" + color + ";" + \
        "}"

    elif ("gpu" == widget):
        css = \
        "QLabel {" + \
        "font-size:18pt;" + \
        "font-weight:bold;" + \
        "font-family:Montserrat;" + \
        "color:" + color + ";" + \
        "}"

    return css
