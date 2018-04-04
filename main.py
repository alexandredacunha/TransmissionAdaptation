# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiProject.ui'
#
# Created: Tue Apr  3 23:30:02 2018
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1148, 810)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 329, 1111, 421))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Visualization = QtGui.QTabWidget(self.gridLayoutWidget)
        self.Visualization.setObjectName(_fromUtf8("Visualization"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.Visualization.addTab(self.tab, _fromUtf8(""))
        self.genetic_algorithm = QtGui.QWidget()
        self.genetic_algorithm.setObjectName(_fromUtf8("genetic_algorithm"))
        self.graphicsView_ga1 = QtGui.QGraphicsView(self.genetic_algorithm)
        self.graphicsView_ga1.setGeometry(QtCore.QRect(10, 10, 201, 361))
        self.graphicsView_ga1.setObjectName(_fromUtf8("graphicsView_ga1"))
        self.graphicsView_ga3 = QtGui.QGraphicsView(self.genetic_algorithm)
        self.graphicsView_ga3.setGeometry(QtCore.QRect(430, 10, 411, 361))
        self.graphicsView_ga3.setObjectName(_fromUtf8("graphicsView_ga3"))
        self.graphicsView_ga4 = QtGui.QGraphicsView(self.genetic_algorithm)
        self.graphicsView_ga4.setGeometry(QtCore.QRect(850, 10, 241, 121))
        self.graphicsView_ga4.setObjectName(_fromUtf8("graphicsView_ga4"))
        self.graphicsView_ga5 = QtGui.QGraphicsView(self.genetic_algorithm)
        self.graphicsView_ga5.setGeometry(QtCore.QRect(850, 140, 241, 111))
        self.graphicsView_ga5.setObjectName(_fromUtf8("graphicsView_ga5"))
        self.graphicsView_ga6 = QtGui.QGraphicsView(self.genetic_algorithm)
        self.graphicsView_ga6.setGeometry(QtCore.QRect(850, 260, 241, 111))
        self.graphicsView_ga6.setObjectName(_fromUtf8("graphicsView_ga6"))
        self.graphicsView_ga2 = QtGui.QGraphicsView(self.genetic_algorithm)
        self.graphicsView_ga2.setGeometry(QtCore.QRect(220, 10, 201, 361))
        self.graphicsView_ga2.setObjectName(_fromUtf8("graphicsView_ga2"))
        self.Visualization.addTab(self.genetic_algorithm, _fromUtf8(""))
        self.gridLayout.addWidget(self.Visualization, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(429, 9, 691, 311))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        
        self.Estimator_configuration = QtGui.QTabWidget(self.gridLayoutWidget_2)
        self.Estimator_configuration.setObjectName(_fromUtf8("Estimator_configuration"))
        
        self.mlp_tf = QtGui.QWidget()
        self.mlp_tf.setObjectName(_fromUtf8("mlp_tf"))
        self.label_6 = QtGui.QLabel(self.mlp_tf)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 171, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.mlp_tf)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 131, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.number_of_hidden_layers = QtGui.QSpinBox(self.mlp_tf)
        self.number_of_hidden_layers.setGeometry(QtCore.QRect(190, 10, 60, 31))
        self.number_of_hidden_layers.setObjectName(_fromUtf8("number_of_hidden_layers"))
        self.label_8 = QtGui.QLabel(self.mlp_tf)
        self.label_8.setGeometry(QtCore.QRect(20, 100, 161, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.number_of_hidden_layers_2 = QtGui.QSpinBox(self.mlp_tf)
        self.number_of_hidden_layers_2.setGeometry(QtCore.QRect(190, 90, 60, 31))
        self.number_of_hidden_layers_2.setObjectName(_fromUtf8("number_of_hidden_layers_2"))
        self.activation_function = QtGui.QLineEdit(self.mlp_tf)
        self.activation_function.setGeometry(QtCore.QRect(160, 50, 91, 31))
        self.activation_function.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.activation_function.setObjectName(_fromUtf8("activation_function"))
        self.Estimator_configuration.addTab(self.mlp_tf, _fromUtf8(""))
        self.mlp_tf_training = QtGui.QWidget()
        self.mlp_tf_training.setObjectName(_fromUtf8("mlp_tf_training"))
        self.start_trainning = QtGui.QPushButton(self.mlp_tf_training)
        self.start_trainning.setGeometry(QtCore.QRect(20, 50, 98, 27))
        self.start_trainning.setObjectName(_fromUtf8("start_trainning"))
        self.label_9 = QtGui.QLabel(self.mlp_tf_training)
        self.label_9.setGeometry(QtCore.QRect(20, 20, 131, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.number_of_seasons = QtGui.QLineEdit(self.mlp_tf_training)
        self.number_of_seasons.setGeometry(QtCore.QRect(160, 10, 61, 31))
        self.number_of_seasons.setObjectName(_fromUtf8("number_of_seasons"))
        self.Estimator_configuration.addTab(self.mlp_tf_training, _fromUtf8(""))
        self.genetic_algorithm1 = QtGui.QWidget()
        self.genetic_algorithm1.setObjectName(_fromUtf8("genetic_algorithm1"))
        self.start_trainning_2 = QtGui.QPushButton(self.genetic_algorithm1)
        self.start_trainning_2.setGeometry(QtCore.QRect(30, 20, 98, 27))
        self.start_trainning_2.setObjectName(_fromUtf8("start_trainning_2"))
        self.Estimator_configuration.addTab(self.genetic_algorithm1, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.Estimator_configuration, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(9, 9, 411, 311))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.general_settings = QtGui.QTabWidget(self.gridLayoutWidget_3)
        self.general_settings.setObjectName(_fromUtf8("general_settings"))
        self.simulation_parameters = QtGui.QWidget()
        self.simulation_parameters.setObjectName(_fromUtf8("simulation_parameters"))
        self.max_packet_size = QtGui.QLineEdit(self.simulation_parameters)
        self.max_packet_size.setGeometry(QtCore.QRect(330, 20, 61, 31))
        self.max_packet_size.setObjectName(_fromUtf8("max_packet_size"))
        self.label = QtGui.QLabel(self.simulation_parameters)
        self.label.setGeometry(QtCore.QRect(220, 30, 111, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.min_packet_size = QtGui.QLineEdit(self.simulation_parameters)
        self.min_packet_size.setGeometry(QtCore.QRect(130, 20, 61, 31))
        self.min_packet_size.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.min_packet_size.setObjectName(_fromUtf8("min_packet_size"))
        self.label_2 = QtGui.QLabel(self.simulation_parameters)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 111, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.simulation_lenth = QtGui.QLineEdit(self.simulation_parameters)
        self.simulation_lenth.setGeometry(QtCore.QRect(150, 60, 91, 31))
        self.simulation_lenth.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.simulation_lenth.setObjectName(_fromUtf8("simulation_lenth"))
        self.label_3 = QtGui.QLabel(self.simulation_parameters)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 121, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.general_settings.addTab(self.simulation_parameters, _fromUtf8(""))
        self.channel_model = QtGui.QWidget()
        self.channel_model.setObjectName(_fromUtf8("channel_model"))
        self.pushButton = QtGui.QPushButton(self.channel_model)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 161, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.channel_model)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 60, 161, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.graphicsView = QtGui.QGraphicsView(self.channel_model)
        self.graphicsView.setGeometry(QtCore.QRect(20, 100, 361, 161))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.min_packet_size_2 = QtGui.QLineEdit(self.channel_model)
        self.min_packet_size_2.setGeometry(QtCore.QRect(330, 20, 51, 31))
        self.min_packet_size_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.min_packet_size_2.setObjectName(_fromUtf8("min_packet_size_2"))
        self.label_5 = QtGui.QLabel(self.channel_model)
        self.label_5.setGeometry(QtCore.QRect(210, 30, 111, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.general_settings.addTab(self.channel_model, _fromUtf8(""))
        self.log_control = QtGui.QWidget()
        self.log_control.setObjectName(_fromUtf8("log_control"))
        self.checkBox = QtGui.QCheckBox(self.log_control)
        self.checkBox.setGeometry(QtCore.QRect(30, 20, 111, 22))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.log_control)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 50, 111, 22))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.log_control)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 80, 111, 22))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_4 = QtGui.QCheckBox(self.log_control)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 110, 121, 22))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.general_settings.addTab(self.log_control, _fromUtf8(""))
        self.size_estimator = QtGui.QWidget()
        self.size_estimator.setObjectName(_fromUtf8("size_estimator"))
        self.radioButton = QtGui.QRadioButton(self.size_estimator)
        self.radioButton.setGeometry(QtCore.QRect(30, 40, 116, 22))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.size_estimator)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 70, 211, 22))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.size_estimator)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 100, 231, 22))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.label_4 = QtGui.QLabel(self.size_estimator)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 121, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.radioButton_4 = QtGui.QRadioButton(self.size_estimator)
        self.radioButton_4.setGeometry(QtCore.QRect(30, 130, 231, 22))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.general_settings.addTab(self.size_estimator, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.general_settings, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1148, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Visualization.setCurrentIndex(1)
        self.Estimator_configuration.setCurrentIndex(0)
        self.general_settings.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Transmition Adaptation Game", None))
        self.Visualization.setTabText(self.Visualization.indexOf(self.tab), _translate("MainWindow", "MLP TF visualization", None))
        self.Visualization.setTabText(self.Visualization.indexOf(self.genetic_algorithm), _translate("MainWindow", "Genetic Algorithm", None))
        self.label_6.setText(_translate("MainWindow", "Number of hidden layers", None))
        self.label_7.setText(_translate("MainWindow", "Activation function", None))
        self.label_8.setText(_translate("MainWindow", "Nr of perceptrons/layer", None))
        self.Estimator_configuration.setTabText(self.Estimator_configuration.indexOf(self.mlp_tf), _translate("MainWindow", "MLP TF", None))
        self.start_trainning.setText(_translate("MainWindow", "Start", None))
        self.label_9.setText(_translate("MainWindow", "Number of seasons", None))
        self.Estimator_configuration.setTabText(self.Estimator_configuration.indexOf(self.mlp_tf_training), _translate("MainWindow", "MLP TF training", None))
        self.start_trainning_2.setText(_translate("MainWindow", "Start", None))
        self.Estimator_configuration.setTabText(self.Estimator_configuration.indexOf(self.genetic_algorithm1), _translate("MainWindow", "Genetic Algorithm", None))
        self.label.setText(_translate("MainWindow", "Max packet size", None))
        self.label_2.setText(_translate("MainWindow", "Min packet size", None))
        self.label_3.setText(_translate("MainWindow", "Simulation Lenth", None))
        self.general_settings.setTabText(self.general_settings.indexOf(self.simulation_parameters), _translate("MainWindow", "Main Parameters", None))
        self.pushButton.setText(_translate("MainWindow", "Show channel model", None))
        self.pushButton_2.setText(_translate("MainWindow", "Generate noise", None))
        self.label_5.setText(_translate("MainWindow", "Set fixed quality", None))
        self.general_settings.setTabText(self.general_settings.indexOf(self.channel_model), _translate("MainWindow", "Channel Model", None))
        self.checkBox.setText(_translate("MainWindow", "sender logs", None))
        self.checkBox_2.setText(_translate("MainWindow", "receiver logs", None))
        self.checkBox_3.setText(_translate("MainWindow", "channel logs", None))
        self.checkBox_4.setText(_translate("MainWindow", "trainning logs", None))
        self.general_settings.setTabText(self.general_settings.indexOf(self.log_control), _translate("MainWindow", "Logs", None))
        self.radioButton.setText(_translate("MainWindow", "Fixed size", None))
        self.radioButton_2.setText(_translate("MainWindow", "Neural Network - Keras", None))
        self.radioButton_3.setText(_translate("MainWindow", "Neural Network - Tensor Flow", None))
        self.label_4.setText(_translate("MainWindow", "Estimator in Use", None))
        self.radioButton_4.setText(_translate("MainWindow", "Genetic Algorithm 1", None))
        self.general_settings.setTabText(self.general_settings.indexOf(self.size_estimator), _translate("MainWindow", "Estimator", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

