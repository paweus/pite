# encoding=utf8
# Created by: PyQt4 UI code generator 4.11.4

from PyQt4 import QtCore, QtGui
import sys
import os
import csv
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg

from FlightSimulator import FlightSimulator
from Reader import Reader
from Plotter import Plotter
from Statistics import Statistics
from Operations import Operations

reload(sys)
sys.setdefaultencoding('utf8')

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


#Głowna klasa odpowiadajaca za gui
#Zawiera buttony, ktore wywoluja poszczegolne funkcje, stanowiace funkcjonalnosc programu

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.plotHolder = Plotter()
        self.layout = QtGui.QVBoxLayout()
        self.data = 0
        self.dataStr = 0
        self.filePath = None
        self.filePath2 = 0
        self.setWindowTitle("FlightMadness")
        self.setWindowIcon(QtGui.QIcon('phyton.ico'))
        self.setupUi(self)

    #Funkcja, ktora otwiera okno dialogowe i pozwala wybrac plik .CSV potrzebny do symulacji danych
    def openFileForSimulation(self):
        print '---------------------------'
        print 'Opening file for simulation'
        filter = "CSV (*.csv)"
        filename = QtGui.QFileDialog.getOpenFileNameAndFilter(self,"Open File",'',filter)
        self.filePath = filename[0]
        if str(self.filePath) != "":
            self.dataLoad_label.setText("<b>OK</b>")
            self.start_Button.setEnabled(True)
            self.start_label.setText("OCZEKIWANIE")
            print 'File loaded'
        else:
            print 'Opening  aborted'

    #Funkcja, ktora otwiera okno dialogowe i pozwala wybrac plik .CSV potrzebny do wizualizacji danych
    def openFileForVisualisation(self):
        print '---------------------------'
        print 'Opening file for visualisation'
        filter = "CSV (*.csv)"
        filename = QtGui.QFileDialog.getOpenFileNameAndFilter(self,"Open File",'',filter)
        self.filePath2 = filename[0]
        if str(self.filePath2) != "":
            self.dataLoad_label_2.setText("<b>OK</b>")
            self.start_Button_2.setEnabled(True)
            self.start_label_2.setText("OCZEKIWANIE")
            print 'File loaded'
        else:
            print 'Opening  aborted'

    #Funkcja inicjalizujaca symulacje danych
    def StartFlight(self):
        print '---------------------------'
        print 'Starting simulation'
        temp = FlightSimulator(self.filePath)
        temp.openDataSimulation()
        self.start_label.setText("<b>OK</b>")
        self.start_Button.setEnabled(False)

    #Funkcja inicjalizujaca prztwarzanie danych do wizualizacji
    #Dane sa wczytywane do zmiennych, a na ich podstawie aktualizowane jest GUI oraz tworzone statystyki lotu
    def LoadDataForVisualisation(self):
        print 'Loading data for visualisation...'
        Reader.read(self.filePath2)
        self.data = Reader.load
        self.dataStr = Reader.load2 #data i czas
        self.data = Operations.CalculateToMetrics(self.data)
        stat = Statistics(self.data,self.dataStr)
        stat.makeStats()
        self.UpdateStatsGUI(stat)
        print 'All done.'

    #Funkcja aktualizujaca statystyki w GUI po pobraniu danych do wizualizacji
    def UpdateStatsGUI(self,obj):
        self.stats = obj
        self.spinBox_max.setValue(obj.timeFlight)
        self.spinBox_min.setValue(0)
        self.start_label_2.setText("<b>OK</b>")
        self.start_Button_2.setEnabled(False)
        self.plotHolder.addData(self.data)
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.label_visualisation_state.show()

        #Stats
        self.value_dateStart.setText(str(obj.dateStart) +'   ' + str(obj.timeStart))
        self.value_dateStart.adjustSize()
        self.value_dateLand.setText(str(obj.dateLand) +'   ' + str(obj.timeLand))
        self.value_dateLand.adjustSize()
        self.value_timeFlight.setText(str(obj.timeFlight))
        self.value_startCoords.setText(str(obj.latitudeStart) + '   ' + str(obj.longitudeStart))
        self.value_startCoords.adjustSize()
        self.value_landCords.setText(str(obj.latitudeLand) + '   ' + str(obj.longitudeLand))
        self.value_landCords.adjustSize()
        self.value_maxHeight.setText(str(round(obj.maxAltitude,3)))
        self.value_maxSpeed.setText(str(round(obj.maxSpeed,3)))
        self.value_maxAcceleration.setText(str(round(obj.maxAcceleration,3)))
        self.value_averageSpeed.setText(str(round(obj.averageSpeed,3)))
        self.value_averageHeight.setText(str(round(obj.averageHeight,3)))
        self.value_endPoint.setText(str(round(obj.endPoint,3)))
        self.value_startPoint.setText(str(round(obj.startPoint,3)))
        self.tabWidget.setCurrentIndex(1)


    #Funkcja inicjalizujaca rysowanie wykresu
    #argumenty: tytyl wykresu, tytul osi x, tylul osi y, wartosci odpowiadajaca indeksowi w tablicy data dla osi x y
    #argumenty sa podawane do funkcji
    def DrawPlot(self,title,title_x,title_y,valuex,valuey):
        print 'Creating plot...'
        Plotter.checkbox_min = self.spinBox_min.value()
        Plotter.checkbox_max = self.spinBox_max.value()
        self.tabWidget.removeTab(0)
        self.newTab = QtGui.QWidget()
        self.newTab.setObjectName(_fromUtf8("plot"))
        self.tabWidget.insertTab(0,self.newTab, _fromUtf8("Wykres"))
        self.tabWidget.setCurrentWidget(self.newTab)
        layout = QtGui.QVBoxLayout()
        fig = self.plotHolder.PlotCreator(title,title_x,title_y,valuex,valuey)
        layout.addWidget(FigureCanvasQTAgg(fig))
        self.newTab.setLayout(layout)
        print 'Plot created.'

    #Funkcja informujaca w konsuli o zamknieciu aplikacji
    def closeEvent(self, event):
        print 'Application closed.'
        event.accept()

    #Funkcja tworzaca GUI
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setFixedSize(978, 630)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.loadData_button = QtGui.QPushButton(self.centralwidget)
        self.loadData_button.setGeometry(QtCore.QRect(40, 100, 91, 31))
        self.loadData_button.setObjectName(_fromUtf8("loadData_button"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(280, 40, 661, 461))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.stats_dateStart = QtGui.QLabel(self.tab_2)
        self.stats_dateStart.setGeometry(QtCore.QRect(30, 60, 121, 21))
        self.stats_dateStart.setObjectName(_fromUtf8("stats"))
        self.stats_dateLand = QtGui.QLabel(self.tab_2)
        self.stats_dateLand.setGeometry(QtCore.QRect(30, 80, 131, 21))
        self.stats_dateLand.setObjectName(_fromUtf8("stats_dateLand"))
        self.stats_flightTime = QtGui.QLabel(self.tab_2)
        self.stats_flightTime.setGeometry(QtCore.QRect(30, 110, 131, 21))
        self.stats_flightTime.setObjectName(_fromUtf8("stats_flightTime"))
        self.stats_startCords = QtGui.QLabel(self.tab_2)
        self.stats_startCords.setGeometry(QtCore.QRect(30, 130, 131, 21))
        self.stats_startCords.setObjectName(_fromUtf8("stats_startCords"))
        self.stats_landCoords = QtGui.QLabel(self.tab_2)
        self.stats_landCoords.setGeometry(QtCore.QRect(30, 150, 131, 21))
        self.stats_landCoords.setObjectName(_fromUtf8("stats_landCoords"))
        self.stats_maxAltitude = QtGui.QLabel(self.tab_2)
        self.stats_maxAltitude.setGeometry(QtCore.QRect(30, 240, 181, 21))
        self.stats_maxAltitude.setObjectName(_fromUtf8("stats_maxAltitude"))
        self.stats_maxSpeed = QtGui.QLabel(self.tab_2)
        self.stats_maxSpeed.setGeometry(QtCore.QRect(30, 280, 121, 21))
        self.stats_maxSpeed.setObjectName(_fromUtf8("stats_maxSpeed"))
        self.stats_maxAcceleration = QtGui.QLabel(self.tab_2)
        self.stats_maxAcceleration.setGeometry(QtCore.QRect(30, 260, 181, 21))
        self.stats_maxAcceleration.setObjectName(_fromUtf8("stats_maxAcceleration"))
        self.value_dateStart = QtGui.QLabel(self.tab_2)
        self.value_dateStart.setGeometry(QtCore.QRect(310, 60, 61, 21))
        self.value_dateStart.setTextFormat(QtCore.Qt.LogText)
        self.value_dateStart.setObjectName(_fromUtf8("value_label"))
        self.value_dateLand = QtGui.QLabel(self.tab_2)
        self.value_dateLand.setGeometry(QtCore.QRect(310, 80, 61, 20))
        self.value_dateLand.setObjectName(_fromUtf8("value_dateLand"))
        self.value_timeFlight = QtGui.QLabel(self.tab_2)
        self.value_timeFlight.setGeometry(QtCore.QRect(310, 110, 61, 21))
        self.value_timeFlight.setObjectName(_fromUtf8("value_timeFlight"))
        self.value_startCoords = QtGui.QLabel(self.tab_2)
        self.value_startCoords.setGeometry(QtCore.QRect(310, 130, 61, 21))
        self.value_startCoords.setObjectName(_fromUtf8("value_startCoords"))
        self.value_landCords = QtGui.QLabel(self.tab_2)
        self.value_landCords.setGeometry(QtCore.QRect(310, 150, 61, 21))
        self.value_landCords.setObjectName(_fromUtf8("value_landCords"))
        self.value_maxHeight = QtGui.QLabel(self.tab_2)
        self.value_maxHeight.setGeometry(QtCore.QRect(310, 240, 61, 21))
        self.value_maxHeight.setObjectName(_fromUtf8("value_maxHeight"))
        self.value_maxSpeed = QtGui.QLabel(self.tab_2)
        self.value_maxSpeed.setGeometry(QtCore.QRect(310, 280, 61, 21))
        self.value_maxSpeed.setObjectName(_fromUtf8("value_maxSpeed"))
        self.value_maxAcceleration = QtGui.QLabel(self.tab_2)
        self.value_maxAcceleration.setGeometry(QtCore.QRect(310, 260, 61, 21))
        self.value_maxAcceleration.setObjectName(_fromUtf8("value_maxAcceleration"))
        self.stats_startPoint = QtGui.QLabel(self.tab_2)
        self.stats_startPoint.setGeometry(QtCore.QRect(30, 180, 191, 21))
        self.stats_startPoint.setObjectName(_fromUtf8("stats_startPoint"))
        self.stats_endPoint = QtGui.QLabel(self.tab_2)
        self.stats_endPoint.setGeometry(QtCore.QRect(30, 200, 181, 21))
        self.stats_endPoint.setObjectName(_fromUtf8("stats_endPoint"))
        self.value_averageHeight = QtGui.QLabel(self.tab_2)
        self.value_averageHeight.setGeometry(QtCore.QRect(310, 340, 61, 21))
        self.value_averageHeight.setObjectName(_fromUtf8("value_averageHeight"))
        self.stats_averageHeightASM = QtGui.QLabel(self.tab_2)
        self.stats_averageHeightASM.setGeometry(QtCore.QRect(30, 340, 181, 21))
        self.stats_averageHeightASM.setObjectName(_fromUtf8("stats_averageHeightASM"))
        self.value_averageSpeed = QtGui.QLabel(self.tab_2)
        self.value_averageSpeed.setGeometry(QtCore.QRect(310, 320, 61, 21))
        self.value_averageSpeed.setObjectName(_fromUtf8("value_averageSpeed"))
        self.stats_avarageHeight = QtGui.QLabel(self.tab_2)
        self.stats_avarageHeight.setGeometry(QtCore.QRect(30, 360, 181, 21))
        self.stats_avarageHeight.setObjectName(_fromUtf8("stats_avarageHeight"))
        self.stats_avarageSpeed = QtGui.QLabel(self.tab_2)
        self.stats_avarageSpeed.setGeometry(QtCore.QRect(30, 320, 181, 21))
        self.stats_avarageSpeed.setObjectName(_fromUtf8("stats_avarageSpeed"))
        self.value_startPoint = QtGui.QLabel(self.tab_2)
        self.value_startPoint.setGeometry(QtCore.QRect(310, 180, 61, 21))
        self.value_startPoint.setObjectName(_fromUtf8("value_startPoint"))
        self.value_endPoint = QtGui.QLabel(self.tab_2)
        self.value_endPoint.setGeometry(QtCore.QRect(310, 200, 61, 21))
        self.value_endPoint.setObjectName(_fromUtf8("value_endPoint"))
        self.stats_header = QtGui.QLabel(self.tab_2)
        self.stats_header.setGeometry(QtCore.QRect(30, 30, 231, 16))
        self.stats_header.setObjectName(_fromUtf8("stats_header"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.label_info2 = QtGui.QLabel(self.tab_5)
        self.label_info2.setGeometry(QtCore.QRect(30, 80, 571, 21))
        self.label_info2.setWordWrap(True)
        self.label_info2.setObjectName(_fromUtf8("label_info2"))
        self.label_info_header = QtGui.QLabel(self.tab_5)
        self.label_info_header.setGeometry(QtCore.QRect(30, 30, 141, 16))
        self.label_info_header.setObjectName(_fromUtf8("label_info_header"))
        self.label_info1 = QtGui.QLabel(self.tab_5)
        self.label_info1.setGeometry(QtCore.QRect(30, 60, 411, 21))
        self.label_info1.setTextFormat(QtCore.Qt.PlainText)
        self.label_info1.setWordWrap(True)
        self.label_info1.setObjectName(_fromUtf8("label_info1"))
        self.label_info3 = QtGui.QLabel(self.tab_5)
        self.label_info3.setGeometry(QtCore.QRect(30, 100, 531, 16))
        self.label_info3.setWordWrap(True)
        self.label_info3.setObjectName(_fromUtf8("label_info3"))
        self.label_info4 = QtGui.QLabel(self.tab_5)
        self.label_info4.setGeometry(QtCore.QRect(30, 120, 531, 16))
        self.label_info4.setWordWrap(True)
        self.label_info4.setObjectName(_fromUtf8("label_info4"))
        self.label_info5 = QtGui.QLabel(self.tab_5)
        self.label_info5.setGeometry(QtCore.QRect(30, 160, 511, 16))
        self.label_info5.setWordWrap(True)
        self.label_info5.setObjectName(_fromUtf8("label_info5"))
        self.label_info6 = QtGui.QLabel(self.tab_5)
        self.label_info6.setGeometry(QtCore.QRect(30, 140, 571, 16))
        self.label_info6.setWordWrap(True)
        self.label_info6.setObjectName(_fromUtf8("label_info6"))
        self.label_info7 = QtGui.QLabel(self.tab_5)
        self.label_info7.setGeometry(QtCore.QRect(30, 200, 511, 16))
        self.label_info7.setWordWrap(True)
        self.label_info7.setObjectName(_fromUtf8("label_info7"))
        self.label_info8 = QtGui.QLabel(self.tab_5)
        self.label_info8.setGeometry(QtCore.QRect(30, 270, 511, 16))
        self.label_info8.setWordWrap(True)
        self.label_info8.setObjectName(_fromUtf8("label_info8"))
        self.label_info9 = QtGui.QLabel(self.tab_5)
        self.label_info9.setGeometry(QtCore.QRect(30, 290, 561, 16))
        self.label_info9.setTextFormat(QtCore.Qt.LogText)
        self.label_info9.setObjectName(_fromUtf8("label_info9"))
        self.line = QtGui.QFrame(self.tab_5)
        self.line.setGeometry(QtCore.QRect(30, 180, 571, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_info10 = QtGui.QLabel(self.tab_5)
        self.label_info10.setGeometry(QtCore.QRect(30, 220, 491, 16))
        self.label_info10.setObjectName(_fromUtf8("label_info10"))
        self.line_2 = QtGui.QFrame(self.tab_5)
        self.line_2.setGeometry(QtCore.QRect(30, 250, 571, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.dataLoad_label = QtGui.QLabel(self.centralwidget)
        self.dataLoad_label.setGeometry(QtCore.QRect(140, 100, 81, 31))
        self.dataLoad_label.setObjectName(_fromUtf8("dataLoad_label"))
        self.label_simulation = QtGui.QLabel(self.centralwidget)
        self.label_simulation.setGeometry(QtCore.QRect(70, 70, 121, 21))
        self.label_simulation.setObjectName(_fromUtf8("label_simulation"))
        self.start_Button = QtGui.QPushButton(self.centralwidget)
        self.start_Button.setGeometry(QtCore.QRect(40, 140, 91, 31))
        self.start_Button.setObjectName(_fromUtf8("start_Button"))
        self.start_label = QtGui.QLabel(self.centralwidget)
        self.start_label.setGeometry(QtCore.QRect(140, 140, 81, 31))
        self.start_label.setObjectName(_fromUtf8("start_label"))
        self.dataLoad_button2 = QtGui.QPushButton(self.centralwidget)
        self.dataLoad_button2.setGeometry(QtCore.QRect(40, 240, 91, 31))
        self.dataLoad_button2.setObjectName(_fromUtf8("dataLoad_button2"))
        self.label_loadToVisualisation = QtGui.QLabel(self.centralwidget)
        self.label_loadToVisualisation.setGeometry(QtCore.QRect(60, 210, 141, 21))
        self.label_loadToVisualisation.setObjectName(_fromUtf8("label_loadToVisualisation"))
        self.dataLoad_label_2 = QtGui.QLabel(self.centralwidget)
        self.dataLoad_label_2.setGeometry(QtCore.QRect(140, 240, 81, 31))
        self.dataLoad_label_2.setObjectName(_fromUtf8("dataLoad_label_2"))
        self.start_label_2 = QtGui.QLabel(self.centralwidget)
        self.start_label_2.setGeometry(QtCore.QRect(140, 280, 81, 31))
        self.start_label_2.setObjectName(_fromUtf8("start_label_2"))
        self.start_Button_2 = QtGui.QPushButton(self.centralwidget)
        self.start_Button_2.setGeometry(QtCore.QRect(40, 280, 91, 31))
        self.start_Button_2.setObjectName(_fromUtf8("start_Button_2"))
        self.label_visualisation_state = QtGui.QLabel(self.centralwidget)
        self.label_visualisation_state.setGeometry(QtCore.QRect(60, 310, 151, 31))
        self.label_visualisation_state.setObjectName(_fromUtf8("label_visualisation_state"))
        self.label_visualisation = QtGui.QLabel(self.centralwidget)
        self.label_visualisation.setGeometry(QtCore.QRect(280, 510, 121, 21))
        self.label_visualisation.setObjectName(_fromUtf8("label_visualisation"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 540, 91, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 540, 101, 21))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 540, 91, 21))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(620, 540, 101, 21))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(740, 540, 101, 21))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(860, 540, 81, 21))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.spinBox_botValue = QtGui.QLabel(self.centralwidget)
        self.spinBox_botValue.setGeometry(QtCore.QRect(50, 390, 91, 21))
        self.spinBox_botValue.setObjectName(_fromUtf8("spinBox_botValue"))
        self.spinBox_max = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_max.setGeometry(QtCore.QRect(150, 420, 61, 22))
        self.spinBox_max.setObjectName(_fromUtf8("spinBox_max"))
        self.spinBox_min = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_min.setGeometry(QtCore.QRect(150, 390, 61, 22))
        self.spinBox_min.setObjectName(_fromUtf8("spinBox_min"))
        self.spinBox_topValue = QtGui.QLabel(self.centralwidget)
        self.spinBox_topValue.setGeometry(QtCore.QRect(50, 415, 91, 31))
        self.spinBox_topValue.setObjectName(_fromUtf8("spinBox_topValue"))
        self.slider_value1_2 = QtGui.QLabel(self.centralwidget)
        self.slider_value1_2.setGeometry(QtCore.QRect(90, 370, 121, 16))
        self.slider_value1_2.setObjectName(_fromUtf8("slider_value1_2"))

        self.dataLoad_button2.clicked.connect(self.openFileForVisualisation)
        self.start_Button.clicked.connect(self.StartFlight)
        self.start_Button.setEnabled(False)
        self.loadData_button.clicked.connect(self.openFileForSimulation)
        self.start_Button_2.clicked.connect(self.LoadDataForVisualisation)
        self.start_Button_2.setEnabled(False)
        #Ustawienie wartosci ograniczajacych spinbuxa
        self.spinBox_min.setMinimum(0)
        self.spinBox_min.setMaximum(3000)
        self.spinBox_max.setMinimum(0)
        self.spinBox_max.setMaximum(3000)

        #Przypisywanie przyciskom tworzenia odpowiednich wykresow
        self.pushButton.clicked.connect(lambda: self.DrawPlot('Predkosc od czasu','czas(s)','predkosc(m)',0,4))
        self.pushButton_2.clicked.connect(lambda: self.DrawPlot('Przyspieszenie od czasu','czas(s)','przyspieszenie',0,5))
        self.pushButton_3.clicked.connect(lambda: self.DrawPlot('Wysokosc od czasu','czas(s)','wysokosc(m)',0,3))
        self.pushButton_4.clicked.connect(lambda: self.DrawPlot('Pochylenie w czasie','czas(s)',"pochylenie(kat)",0,7))
        self.pushButton_5.clicked.connect(lambda: self.DrawPlot('Przechylenie w czasie','czas(s)','przechylenie(kat)',0,6))
        self.pushButton_6.clicked.connect(lambda: self.DrawPlot('Kurs','czas(s)','kurs',0,8))

        #Poczatkowo buttony do tworzenia wykresow sa nieaktywne
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)

        self.label_visualisation_state.hide()

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #Dane tekstowe GUI
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Flight recorder symulator", None))
        self.loadData_button.setText(_translate("MainWindow", "Wczytaj dane", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Wykres", None))
        self.stats_dateStart.setText(_translate("MainWindow", "Data startu:", None))
        self.stats_dateLand.setText(_translate("MainWindow", "Data lądowania:", None))
        self.stats_flightTime.setText(_translate("MainWindow", "Całkowity czas lotu:", None))
        self.stats_startCords.setText(_translate("MainWindow", "Współrzędne startu:", None))
        self.stats_landCoords.setText(_translate("MainWindow", "Współrzędne lądowania:", None))
        self.stats_maxAltitude.setText(_translate("MainWindow", "Maksymalna wysokość (bezwzględna):", None))
        self.stats_maxSpeed.setText(_translate("MainWindow", "Maksymalna prędkosc:", None))
        self.stats_maxAcceleration.setText(_translate("MainWindow", "Maksymalne przyśpieszenie:", None))
        self.stats_startPoint.setText(_translate("MainWindow", "Położenie punktu startowego (n.p.m):", None))
        self.stats_endPoint.setText(_translate("MainWindow", "Położenie punktu końcowego (n.p.m):", None))
        self.stats_averageHeightASM.setText(_translate("MainWindow", "Średnia wysokość (bezwzględna):", None))
        self.stats_avarageSpeed.setText(_translate("MainWindow", "Średnia prędkość:", None))

        self.value_dateStart.setText(_translate("MainWindow", "NULL", None))
        self.value_dateLand.setText(_translate("MainWindow", "NULL", None))
        self.value_timeFlight.setText(_translate("MainWindow", "NULL", None))
        self.value_startCoords.setText(_translate("MainWindow", "NULL", None))
        self.value_landCords.setText(_translate("MainWindow", "NULL", None))
        self.value_maxHeight.setText(_translate("MainWindow", "NULL", None))
        self.value_maxSpeed.setText(_translate("MainWindow", "NULL", None))
        self.value_maxAcceleration.setText(_translate("MainWindow", "NULL", None))
        self.value_startPoint.setText(_translate("MainWindow", "NULL", None))
        self.value_endPoint.setText(_translate("MainWindow", "NULL", None))
        self.value_averageHeight.setText(_translate("MainWindow", "NULL", None))
        self.value_averageSpeed.setText(_translate("MainWindow", "NULL", None))

        self.stats_header.setText(_translate("MainWindow", "Statystki z przebiegu lotu", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Statystyki lotu", None))
        self.label_info_header.setText(_translate("MainWindow", "Informacje o programie", None))
        self.label_info1.setText(_translate("MainWindow", "- Statystyki generowane są po wczytaniu danych do wizualizacji.", None))
        self.label_info2.setText(_translate("MainWindow", "- Dane z symulacji lotu samolotu zapisywane sa w folderze, z którego zostal uruchomiony program.", None))
        self.label_info3.setText(_translate("MainWindow", "- Po wczytaniu danych do wizualizacji odblokowywana zostaje opcja rysowania wykresów (na dole). ", None))
        self.label_info4.setText(_translate("MainWindow", "- Po wczytaniu danych do wizualizacji odblokowywana zostaje opcja rysowania wykresów (na dole). ", None))
        self.label_info5.setText(_translate("MainWindow", "- Wykresy są automatycznie zapisywane w folderze, w ktorym znajduje sie program.", None))
        self.label_info6.setText(_translate("MainWindow", "- Spinboxy, w których można ustawić przedział czasu, zmieniają zakres czasowy na wykresie.", None))
        self.label_info7.setText(_translate("MainWindow", "- Dane obsługiwane przez program pochodzą z programu FlightGear.", None))
        self.label_info8.setText(_translate("MainWindow", "Kolejnosc danych w pliku .CSV obsługiwanych przez program:", None))
        self.label_info9.setText(_translate("MainWindow", "Time,Latitude,Longitude,Altitude,Speed,Acceleration,Roll,Pitch,Heading,date,time", None))
        self.label_info10.setText(_translate("MainWindow", "- Dane przykładowe zostały zebrane poprzez latanie samolotem \"Viggen\" (military jet)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Informacje o programie", None))
        self.dataLoad_label.setText(_translate("MainWindow", "OCZEKIWANIE", None))
        self.label_simulation.setText(_translate("MainWindow", "Symulacja lotu samolotu", None))
        self.start_Button.setText(_translate("MainWindow", "Start", None))
        self.start_label.setText(_translate("MainWindow", "OCZEKIWANIE", None))
        self.dataLoad_button2.setText(_translate("MainWindow", "Wczytaj dane", None))
        self.label_loadToVisualisation.setText(_translate("MainWindow", "Wczytaj dane do wizualizacji", None))
        self.dataLoad_label_2.setText(_translate("MainWindow", "OCZEKIWANIE", None))
        self.start_label_2.setText(_translate("MainWindow", "OCZEKIWANIE", None))
        self.start_Button_2.setText(_translate("MainWindow", "Start", None))
        self.label_visualisation_state.setText(_translate("MainWindow", "Dane gotowe do wizualizacji", None))
        self.label_visualisation.setText(_translate("MainWindow", "Wizualizacja wykresow", None))
        self.pushButton.setText(_translate("MainWindow", "Prędkość", None))
        self.pushButton_2.setText(_translate("MainWindow", "Przyśpieszenie", None))
        self.pushButton_3.setText(_translate("MainWindow", "Wysokosć", None))
        self.pushButton_4.setText(_translate("MainWindow", "Pochylenie", None))
        self.pushButton_5.setText(_translate("MainWindow", "Przechylenie", None))
        self.pushButton_6.setText(_translate("MainWindow", "Kurs", None))
        self.spinBox_botValue.setText(_translate("MainWindow", "Wartosc dolna", None))
        self.spinBox_topValue.setText(_translate("MainWindow", "Wartosc górna", None))
        self.slider_value1_2.setText(_translate("MainWindow", "Przedział czasu", None))


if __name__ == '__main__':
    print "Starting application"
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())
