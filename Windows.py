import MainWindow as m
import Web as w
import Cert as c
import CertDetails as cd
import DBWorker as d
from PyQt5.QtWidgets import QTableWidgetItem
import HTMLWorker as h


# Окно просмотра веб страниц
class WebWindow(w.QtWidgets.QMainWindow):
    resized = w.QtCore.pyqtSignal()
    html = []

    def __init__(self, parent=None):
        w.QtWidgets.QWidget.__init__(self, parent)
        self.ui = w.Ui_Form()
        self.ui.setupUi(self)
        self.resized.connect(self.adjust)
        self.adjustSize()

        self.load_html()
        self.set_slider_params()
        self.slider_listing()

        self.ui.horizontalSlider.valueChanged.connect(self.slider_listing)

    def load_html(self):
        worker = h.HTMLWorker('c_2.csv')
        self.html = worker.get_html()

    def set_slider_params(self):
        self.ui.horizontalSlider.setMinimum(0)
        self.ui.horizontalSlider.setMaximum(len(self.html) - 1)
        self.ui.horizontalSlider.setSingleStep(1)
        self.ui.horizontalSlider.setValue(0)

    def slider_listing(self):
        self.set_html_value(self.html[self.ui.horizontalSlider.value()])

    def resizeEvent(self, event):
        self.resized.emit()
        return super(WebWindow, self).resizeEvent(event)

    def adjust(self):
        self.ui.scrollArea.setGeometry(10, 40, 10, 10)
        self.ui.horizontalSlider.setGeometry(10, 10, self.size().width() - 21, 20)
        self.ui.widget.resize(self.size().width() - 21, self.size().height() - 61)
        self.ui.scrollArea.resize(self.size().width() - 21, self.size().height() - 61)
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
    data = []

    def __init__(self, parent=None):
        c.QtWidgets.QWidget.__init__(self, parent)
        self.ui = c.Ui_Form()
        self.ui.setupUi(self)
        self.det_info = CertDetailWindow()
        self.worker = d.DBWorker('config.xml')
        self.save_data()
        self.convert_data()
        self.ui.pushButton.clicked.connect(self.on_click)

        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setRowCount(len(self.data))
        for key in self.data:
            self.ui.tableWidget.setItem(key, 0, QTableWidgetItem(self.data[key][0]))

    def on_click(self):
        for idx in self.ui.tableWidget.selectionModel().selectedRows():
            self.det_info.set_info_value(self.data[idx.row()][1])
        if self.browser_exists == 0:
            self.det_info.show()
            self.browser_exists = 1
        else:
            self.det_info.hide()
            self.browser_exists = 0

    def save_data(self):
        self.worker.init_keys_connection()
        self.data = self.worker.get_key()

    def convert_data(self):
        storage = dict()
        i = 0
        for cert in self.data:
            if type([s for s in str(cert[0]).split('\n') if 'Subject:' in s]) == 'list':
                storage[i] = [[s for s in str(cert[0]).split('\n') if 'Subject:' in s][0].strip(), cert[0]]
                i = i + 1
        self.data = storage


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

    def init_dates(self):
        pass

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
