from PySide6 import QtWidgets
from datetime import datetime
from calculateur import DevisesLogic 

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.logic = DevisesLogic()
        self.setWindowTitle("convertisseur de devises")
        self.setup_ui()
        self.c = self.logic.c
        self.set_default_value()
        self.setup_connections()
        
    def setup_ui(self):
        self.Layout = QtWidgets.QHBoxLayout(self)
        self.cbb_deviseFrom = QtWidgets.QComboBox()
        self.spn_montant = QtWidgets.QDoubleSpinBox()
        self.cbb_deviseTo = QtWidgets.QComboBox()
        self.spn_montantConverti = QtWidgets.QDoubleSpinBox()
        self.spn_montantConverti.setReadOnly(True)

        self.btn_inverser = QtWidgets.QPushButton("Inverser devises")
        self.Layout.addWidget(self.cbb_deviseFrom)
        self.Layout.addWidget(self.spn_montant)
        self.Layout.addWidget(self.cbb_deviseTo)
        self.Layout.addWidget(self.spn_montantConverti)
        self.Layout.addWidget(self.btn_inverser)
        

    def set_default_value(self):
        if self.c.currencies:
            self.cbb_deviseFrom.addItems(sorted(self.c.currencies))
            self.cbb_deviseTo.addItems(sorted(self.c.currencies))
            self.cbb_deviseFrom.setCurrentText("EUR")
            self.cbb_deviseTo.setCurrentText("CHF")
            self.spn_montant.setRange(0, 1000000)
            self.spn_montant.setDecimals(2)
            self.spn_montantConverti.setRange(0, 1000000)
            self.spn_montantConverti.setDecimals(2)

           

    def setup_connections(self):
        self.cbb_deviseFrom.activated.connect(self.compute)
        self.cbb_deviseTo.activated.connect(self.compute)
        self.spn_montant.valueChanged.connect(self.compute)
        self.btn_inverser.clicked.connect(self.inverser_devise)

    def compute(self):
        montant = self.spn_montant.value()
        print(montant)
        devise_from = self.cbb_deviseFrom.currentText()
        devise_to = self.cbb_deviseTo.currentText()
        resultat = self.logic.convertir(montant, devise_from, devise_to)
        print(resultat)
        self.spn_montantConverti.setValue(resultat)



    def inverser_devise(self):
        devise_from = self.cbb_deviseFrom.currentText()
        devise_to = self.cbb_deviseTo.currentText()
        self.cbb_deviseFrom.setCurrentText(devise_to)
        self.cbb_deviseTo.setCurrentText(devise_from)
        self.compute()

app = QtWidgets.QApplication()
app.setStyle("Fusion")
win = App()
win.show()



app.exec()