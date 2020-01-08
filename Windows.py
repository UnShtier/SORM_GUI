import MainWindow as m
import Web as w
import Cert as c
import CertDetails as cd


# Окно просмотра веб страниц
class WebWindow(w.QtWidgets.QMainWindow):
    resized = w.QtCore.pyqtSignal()

    def __init__(self, parent=None):
        w.QtWidgets.QWidget.__init__(self, parent)
        self.ui = w.Ui_Form()
        self.ui.setupUi(self)
        self.resized.connect(self.adjust)
        self.adjustSize()

    def resizeEvent(self, event):
        self.resized.emit()
        return super(WebWindow, self).resizeEvent(event)

    def adjust(self):
        self.ui.widget.resize(self.size().width(), self.size().height())
        self.ui.scrollArea.resize(self.size().width(), self.size().height())
        self.ui.scrollAreaWidgetContents_4.adjustSize()

    def set_html_value(self, html):
        self.ui.widget.setHtml(html)
        self.resize(1024, 720)
        self.adjust()


# Окно просмотра детализации о сертификате
class CertDetailWindow(cd.QtWidgets.QMainWindow):
    resized = cd.QtCore.pyqtSignal()

    def __init__(self, parent=None):
        cd.QtWidgets.QWidget.__init__(self, parent)
        self.ui = cd.Ui_Form()
        self.ui.setupUi(self)
        self.resized.connect(self.adjust)
        self.adjustSize()

    def resizeEvent(self, event):
        self.resized.emit()
        return super(CertDetailWindow, self).resizeEvent(event)

    def adjust(self):
        self.ui.info.resize(self.size().width(), self.size().height())

    def set_info_value(self, info):
        self.ui.info.setText(info)


# Окно выбора сертификата для просмотра
class CertWindow(c.QtWidgets.QMainWindow):
    browser_exists = 0

    def __init__(self, parent=None):
        c.QtWidgets.QWidget.__init__(self, parent)
        self.ui = c.Ui_Form()
        self.ui.setupUi(self)
        self.det_info = CertDetailWindow()

    def on_click(self):
        if self.browser_exists == 0:
            self.det_info.show()
            self.browser_exists = 1
        else:
            self.det_info.hide()
            self.browser_exists = 0


# Основное окно программы
class MWindow(m.QtWidgets.QMainWindow):
    html_browser_exists = 0
    cert_browser_exists = 0

    def __init__(self, parent=None):
        m.QtWidgets.QWidget.__init__(self, parent)
        self.ui = m.Ui_MainWindow()
        self.web = WebWindow()
        self.cert = CertWindow()
        self.ui.setupUi(self)
        self.ui.browse_html.clicked.connect(self.on_html_click)
        self.ui.browse_cert.clicked.connect(self.on_cert_click)

    def on_html_click(self):
        if self.html_browser_exists == 0:
            self.web.show()
            self.html_browser_exists = 1
        else:
            self.web.hide()
            self.html_browser_exists = 0

    def on_cert_click(self):
        if self.cert_browser_exists == 0:
            self.cert.show()
            self.cert_browser_exists = 1
        else:
            self.cert.hide()
            self.cert_browser_exists = 0
