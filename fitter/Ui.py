# -*- coding: utf-8 -*-
# Created by: PyQt4 UI code generator 4.11.4

from PyQt4 import QtCore, QtGui
import sys
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
from Stats import Stats
from Fitter import Fitter
from Plotter import Plotter
from Generator import Generator

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        plott = Plotter()
        QtGui.QMainWindow.__init__(self)
        self.setWindowIcon(QtGui.QIcon('phyton.ico'))
        self.setupUi(self)
        self.fit = Fitter()
        self.gen = Generator()
        self.plot = Plotter()
        self.popt = []
        self.chi2 = None

    def DrawPlot(self):
        print 'Creating plot...'
        Plotter.dopasowana = self.checkBox_dopasowana.isChecked()
        Plotter.poczatkowa = self.checkBox_poczatkowa.isChecked()
        Plotter.dane = self.checkBox_dane.isChecked()
        Plotter.xlim_min = self.spinbox_zakresOd.value()
        Plotter.xlim_max = self.spinbox_zakresDo.value()

        self.tabWidget.removeTab(0)
        self.newTab = QtGui.QWidget()
        self.newTab.setObjectName(_fromUtf8("plot"))
        self.tabWidget.insertTab(0,self.newTab, _fromUtf8("Wykres"))
        self.tabWidget.setCurrentWidget(self.newTab)
        layout = QtGui.QVBoxLayout()
        fig = self.plot.plot(self.gen.returnX(),self.gen.returnY(),self.gen.returnYn(),self.fit.returnFittedData())
        layout.addWidget(FigureCanvasQTAgg(fig))
        self.newTab.setLayout(layout)
        print 'Plot created.'

    def start(self):
        print 'test'
        print self.checkBox_poczatkowa.isChecked()
        self.gen.getData(self.spinbox_amp.value(),self.spinbox_freq.value(),self.spinbox_ilePkt.value(),self.spinbox_rozrzut.value(),self.spinbox_przesuniecie.value(),self.spinbox_zakresOd.value(),self.spinbox_zakresDo.value())
        # #uruchamianie kreatora
        self.gen.creator()
        # #tworzenie fittera
        self.fit.getData(self.gen.returnX(),self.gen.returnYn())
        # #fittowanie
        chio = None
        oneMoreGuess = 0
        while ((chio == None) or (chio > 0.2)) and (oneMoreGuess < self.spinbox_freq.maximum()):
            self.fit.fit(self.gen.guess(oneMoreGuess))
            chio = Stats.chi(self.gen.returnY(),self.fit.returnFittedData())
            oneMoreGuess += 0.1
        self.chi2 = chio
        # #wydrukowanie zfitowanych wartosci
        self.popt = self.fit.printPopt()
        # #tworzenie plottera
        self.DrawPlot()
        self.UpdateGui()
        # #pobieranie danych do plottera

    def UpdateGui(self):
        self.chi_value.setText(str(round(self.chi2,6)))
        self.amp_value.setText(str(round(self.popt[0],6)))
        self.freq_value.setText(str(round(self.popt[1],6)))
        self.przes_value.setText(str(round(self.popt[2],6)))

    def initSpinBox(self):
        self.spinbox_amp.setValue(1)
        self.spinbox_freq.setValue(1)
        self.spinbox_rozrzut.setValue(0.1)
        self.spinbox_ilePkt.setValue(500)
        self.spinbox_zakresOd.setValue(0)
        self.spinbox_zakresDo.setValue(10)
        self.spinbox_przesuniecie.setValue(0)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setFixedSize(914, 523)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(350, 30, 531, 371))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.spinbox_rozrzut = QtGui.QDoubleSpinBox(self.centralwidget)
        self.spinbox_rozrzut.setGeometry(QtCore.QRect(190, 230, 62, 22))
        self.spinbox_rozrzut.setObjectName(_fromUtf8("spinbox_rozrzut"))
        self.iloscPkt_label = QtGui.QLabel(self.centralwidget)
        self.iloscPkt_label.setGeometry(QtCore.QRect(70, 200, 81, 21))
        self.iloscPkt_label.setObjectName(_fromUtf8("iloscPkt_label"))
        self.rozrzutPkt_label = QtGui.QLabel(self.centralwidget)
        self.rozrzutPkt_label.setGeometry(QtCore.QRect(70, 230, 101, 21))
        self.rozrzutPkt_label.setObjectName(_fromUtf8("rozrzutPkt_label"))
        self.zakresOd_label = QtGui.QLabel(self.centralwidget)
        self.zakresOd_label.setGeometry(QtCore.QRect(70, 260, 71, 21))
        self.zakresOd_label.setObjectName(_fromUtf8("zakresOd_label"))
        self.zakresDo_label = QtGui.QLabel(self.centralwidget)
        self.zakresDo_label.setGeometry(QtCore.QRect(230, 260, 21, 21))
        self.zakresDo_label.setObjectName(_fromUtf8("zakresDo_label"))
        self.spinbox_zakresOd = QtGui.QDoubleSpinBox(self.centralwidget)
        self.spinbox_zakresOd.setGeometry(QtCore.QRect(160, 260, 62, 22))
        self.spinbox_zakresOd.setObjectName(_fromUtf8("spinbox_zakresOd"))
        self.spinbox_zakresDo = QtGui.QDoubleSpinBox(self.centralwidget)
        self.spinbox_zakresDo.setGeometry(QtCore.QRect(250, 260, 62, 22))
        self.spinbox_zakresDo.setObjectName(_fromUtf8("spinbox_zakresDo"))
        self.spinbox_ilePkt = QtGui.QSpinBox(self.centralwidget)
        self.spinbox_ilePkt.setGeometry(QtCore.QRect(190, 200, 61, 22))
        self.spinbox_ilePkt.setObjectName(_fromUtf8("spinbox_ilePkt"))
        self.rozklad_label = QtGui.QLabel(self.centralwidget)
        self.rozklad_label.setGeometry(QtCore.QRect(70, 170, 161, 21))
        self.rozklad_label.setObjectName(_fromUtf8("rozklad_label"))
        self.funkcja_label = QtGui.QLabel(self.centralwidget)
        self.funkcja_label.setGeometry(QtCore.QRect(70, 30, 161, 21))
        self.funkcja_label.setObjectName(_fromUtf8("funkcja_label"))
        self.amplituda_label = QtGui.QLabel(self.centralwidget)
        self.amplituda_label.setGeometry(QtCore.QRect(70, 60, 61, 21))
        self.amplituda_label.setObjectName(_fromUtf8("amplituda_label"))
        self.spinbox_amp = QtGui.QDoubleSpinBox(self.centralwidget)
        self.spinbox_amp.setGeometry(QtCore.QRect(190, 60, 62, 22))
        self.spinbox_amp.setObjectName(_fromUtf8("spinbox_amp"))
        self.frekwencja_label = QtGui.QLabel(self.centralwidget)
        self.frekwencja_label.setGeometry(QtCore.QRect(70, 90, 61, 21))
        self.frekwencja_label.setObjectName(_fromUtf8("frekwencja_label"))
        self.spinbox_freq = QtGui.QDoubleSpinBox(self.centralwidget)
        self.spinbox_freq.setGeometry(QtCore.QRect(190, 90, 62, 22))
        self.spinbox_freq.setObjectName(_fromUtf8("spinbox_freq"))
        self.przesuniecie_label = QtGui.QLabel(self.centralwidget)
        self.przesuniecie_label.setGeometry(QtCore.QRect(70, 120, 61, 21))
        self.przesuniecie_label.setObjectName(_fromUtf8("przesuniecie_label"))
        self.spinbox_przesuniecie = QtGui.QDoubleSpinBox(self.centralwidget)
        self.spinbox_przesuniecie.setGeometry(QtCore.QRect(190, 120, 62, 22))
        self.spinbox_przesuniecie.setObjectName(_fromUtf8("spinbox_przesuniecie"))
        self.checkBox_poczatkowa = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_poczatkowa.setGeometry(QtCore.QRect(70, 330, 131, 21))
        self.checkBox_poczatkowa.setChecked(True)
        self.checkBox_poczatkowa.setObjectName(_fromUtf8("checkBox_poczatkowa"))
        self.checkBox_dopasowana = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_dopasowana.setGeometry(QtCore.QRect(70, 350, 131, 21))
        self.checkBox_dopasowana.setChecked(True)
        self.checkBox_dopasowana.setObjectName(_fromUtf8("checkBox_dopasowana"))
        self.checkBox_dane = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_dane.setGeometry(QtCore.QRect(70, 370, 131, 21))
        self.checkBox_dane.setChecked(True)
        self.checkBox_dane.setObjectName(_fromUtf8("checkBox_dane"))
        self.rysuj_label = QtGui.QLabel(self.centralwidget)
        self.rysuj_label.setGeometry(QtCore.QRect(70, 310, 161, 21))
        self.rysuj_label.setObjectName(_fromUtf8("rysuj_label"))
        self.rysuj_button = QtGui.QPushButton(self.centralwidget)
        self.rysuj_button.setGeometry(QtCore.QRect(160, 400, 75, 23))
        self.rysuj_button.setObjectName(_fromUtf8("rysuj_button"))
        self.dopasowane_label = QtGui.QLabel(self.centralwidget)
        self.dopasowane_label.setGeometry(QtCore.QRect(350, 400, 111, 21))
        self.dopasowane_label.setObjectName(_fromUtf8("dopasowane_label"))
        self.amp_dopasowane_label = QtGui.QLabel(self.centralwidget)
        self.amp_dopasowane_label.setGeometry(QtCore.QRect(350, 420, 61, 21))
        self.amp_dopasowane_label.setObjectName(_fromUtf8("amp_dopasowane_label"))
        self.freq_dopasowane_label = QtGui.QLabel(self.centralwidget)
        self.freq_dopasowane_label.setGeometry(QtCore.QRect(350, 440, 61, 21))
        self.freq_dopasowane_label.setObjectName(_fromUtf8("freq_dopasowane_label"))
        self.przez_dopasowane_label = QtGui.QLabel(self.centralwidget)
        self.przez_dopasowane_label.setGeometry(QtCore.QRect(350, 460, 61, 21))
        self.przez_dopasowane_label.setObjectName(_fromUtf8("przez_dopasowane_label"))
        self.chi_label = QtGui.QLabel(self.centralwidget)
        self.chi_label.setGeometry(QtCore.QRect(610, 420, 61, 21))
        self.chi_label.setObjectName(_fromUtf8("chi_label"))
        self.amp_value = QtGui.QLabel(self.centralwidget)
        self.amp_value.setGeometry(QtCore.QRect(470, 420, 111, 21))
        self.amp_value.setObjectName(_fromUtf8("amp_value"))
        self.freq_value = QtGui.QLabel(self.centralwidget)
        self.freq_value.setGeometry(QtCore.QRect(470, 440, 111, 21))
        self.freq_value.setObjectName(_fromUtf8("freq_value"))
        self.przes_value = QtGui.QLabel(self.centralwidget)
        self.przes_value.setGeometry(QtCore.QRect(470, 460, 111, 21))
        self.przes_value.setObjectName(_fromUtf8("przes_value"))
        self.chi_value = QtGui.QLabel(self.centralwidget)
        self.chi_value.setGeometry(QtCore.QRect(690, 420, 101, 21))
        self.chi_value.setObjectName(_fromUtf8("chi_value"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.spinbox_amp.setMaximum(10)
        self.spinbox_amp.setMinimum(0.1)
        self.spinbox_freq.setMaximum(10)
        self.spinbox_ilePkt.setMaximum(10000)
        self.spinbox_ilePkt.setMinimum(100)
        self.spinbox_przesuniecie.setMinimum(1)
        self.spinbox_przesuniecie.setMaximum(10)



        self.rysuj_button.clicked.connect(self.start)
        self.initSpinBox()
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Fitter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Wykres", None))
        self.iloscPkt_label.setText(_translate("MainWindow", "Ilosc punktow", None))
        self.rozrzutPkt_label.setText(_translate("MainWindow", "Rozrzut punktow", None))
        self.zakresOd_label.setText(_translate("MainWindow", "Zakres x od", None))
        self.zakresDo_label.setText(_translate("MainWindow", "do", None))
        self.rozklad_label.setText(_translate("MainWindow", "Rozklad punktow:", None))
        self.funkcja_label.setText(_translate("MainWindow", "Funkcja: sinus", None))
        self.amplituda_label.setText(_translate("MainWindow", "Amplituda:", None))
        self.frekwencja_label.setText(_translate("MainWindow", "Frekwencja:", None))
        self.przesuniecie_label.setText(_translate("MainWindow", "Przesuniecie:", None))
        self.checkBox_poczatkowa.setText(_translate("MainWindow", "Funkcja poczatkowa", None))
        self.checkBox_dopasowana.setText(_translate("MainWindow", "Funkcja dopasowana", None))
        self.checkBox_dane.setText(_translate("MainWindow", "Dane", None))
        self.rysuj_label.setText(_translate("MainWindow", "Rysuj na wykresie:", None))
        self.rysuj_button.setText(_translate("MainWindow", "Rysuj", None))
        self.dopasowane_label.setText(_translate("MainWindow", "Dopasowane dane:", None))
        self.amp_dopasowane_label.setText(_translate("MainWindow", "Amplituda:", None))
        self.freq_dopasowane_label.setText(_translate("MainWindow", "frekwencja:", None))
        self.przez_dopasowane_label.setText(_translate("MainWindow", "Przesuniecie:", None))
        self.chi_label.setText(_translate("MainWindow", "Chi square:", None))
        self.amp_value.setText(_translate("MainWindow", "x", None))
        self.freq_value.setText(_translate("MainWindow", "x", None))
        self.przes_value.setText(_translate("MainWindow", "x", None))
        self.chi_value.setText(_translate("MainWindow", "x", None))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())
