# Program Name: 
# Programmer: 
# Purpose:1: 
# Modules:  
#Functions: 
# Input: 
# Output: 
#######################################################################################################
import pygame
from PyQt4 import QtCore, QtGui
done = False
#Initialize pygame
pygame.init()

#Load sounds
click_sound = pygame.mixer.Sound("laser5.ogg")
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(600, 765)
        Form.setMinimumSize(QtCore.QSize(600, 765))
        Form.setMaximumSize(QtCore.QSize(600, 765))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("FlyingMonkeyRedSmall.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)

# Styles and Formatting

        # Styles For Entry Boxes & Drop Downs
        font1 = QtGui.QFont()
        font1.setFamily(_fromUtf8("Helvetica"))
        font1.setPointSize(12)
        font1.setWeight(60)

        # Styles For Labels
        font2 = QtGui.QFont()
        font2.setFamily(_fromUtf8("Helvetica"))
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)

# Drop Down List Items
        salutationList = ["Mr." , "Mrs." ,"'Ms."]

        stateList = ["AL" , "AK" ,"AZ" ,"AR" ,"CA" ,"CO" ,"CT" ,"DE" ,"DC" ,"FL" ,"GA" ,"HI" ,"ID" ,"IL" ,"IN"
                     ,"IA" ,"KS" ,"KY","LA" ,"ME" ,"MT" ,"NE" ,"NV" ,"NH" ,"NJ" ,"NM" ,"NY" ,"NC" ,"ND" ,"OH"
                     ,"OK" ,"OR" ,"MD" ,"MA" ,"MI" ,"MN" ,"MS" ,"MO" ,"PA" ,"RI" ,"SC" ,"SD" ,"TN" ,"TX" ,"UT"
                     ,"VT" ,"VA" ,"WA" ,"WV" ,"WI","WY"]

        monthList = ["January" , "February" , "March" , "April" , "May" , "June"
                 , "July" , "August" , "September" , "October" , "November" , "December"]

        dayList =["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"
                  ,"16","17","18","19","20","21","22","23","24","25","26","27","28"
                  ,"29","30","31"]

        serviceLevelList = ["Ecomomy Class" , "Business Class" , "First Class"]
                            
# Form Header

        # Flight Reservation System Label
        self.label1 = QtGui.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(10, 0, 241, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName(_fromUtf8("label1"))

        # Book Your Flight Label
        self.label2 = QtGui.QLabel(Form)
        self.label2.setGeometry(QtCore.QRect(260, 10, 171, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setObjectName(_fromUtf8("label2"))

# Customer Information
        # Customer Information Label
        self.CustomerInformationLabel = QtGui.QLabel(Form)
        self.CustomerInformationLabel.setGeometry(QtCore.QRect(10, 30, 181, 31))
        
        self.CustomerInformationLabel.setFont(font2)
        self.CustomerInformationLabel.setObjectName(_fromUtf8("CustomerInformationLabel"))

        # Salutation Drop Down         
        self.salutationDrop = QtGui.QComboBox(Form)
        self.salutationDrop.setGeometry(QtCore.QRect(10, 60, 69, 31))
        self.salutationDrop.setObjectName(_fromUtf8("salutationDrop"))
        self.salutationDrop.addItems(salutationList)

        self.salutationDrop.setFont(font1)
        self.salutationDrop.setStyleSheet("color: #7b7b7b;")

        # First Name Entry Box
        self.firstNameEntry = QtGui.QTextEdit(Form)
        self.firstNameEntry.setGeometry(QtCore.QRect(90, 60, 201, 31))
        self.firstNameEntry.setObjectName(_fromUtf8("firstNameEntry"))

        self.firstNameEntry.setText("First Name")
        self.firstNameEntry.setFont(font1)
        self.firstNameEntry.setStyleSheet("color: #7b7b7b;")

        # Middle Initial Entry Box
        self.middleInitialEntry = QtGui.QTextEdit(Form)
        self.middleInitialEntry.setGeometry(QtCore.QRect(300, 60, 81, 31))
        self.middleInitialEntry.setObjectName(_fromUtf8("middleInitialEntry"))

        self.middleInitialEntry.setText("M.I.")
        self.middleInitialEntry.setFont(font1)
        self.middleInitialEntry.setStyleSheet("color: #7b7b7b;")

        # Last Name Entry Box
        self.lastNameEntry = QtGui.QTextEdit(Form)
        self.lastNameEntry.setGeometry(QtCore.QRect(390, 60, 201, 31))
        self.lastNameEntry.setObjectName(_fromUtf8("lastNameEntry"))

        self.lastNameEntry.setText("Last Name")
        self.lastNameEntry.setFont(font1)
        self.lastNameEntry.setStyleSheet("color: #7b7b7b;")

        # Street Address Entry Box
        self.streetEntry = QtGui.QTextEdit(Form)
        self.streetEntry.setGeometry(QtCore.QRect(10, 100, 581, 31))
        self.streetEntry.setObjectName(_fromUtf8("streetEntry"))

        self.streetEntry.setText("Street Address")
        self.streetEntry.setFont(font1)
        self.streetEntry.setStyleSheet("color: #7b7b7b;")

        # City Entry Box
        self.cityEntry = QtGui.QTextEdit(Form)
        self.cityEntry.setGeometry(QtCore.QRect(10, 140, 311, 31))
        self.cityEntry.setObjectName(_fromUtf8("cityEntry"))

        self.cityEntry.setText("City")
        self.cityEntry.setFont(font1)
        self.cityEntry.setStyleSheet("color: #7b7b7b;")

        #State Drop Down Box
        self.stateDrop = QtGui.QComboBox(Form)
        self.stateDrop.setGeometry(QtCore.QRect(330, 140, 91, 31))
        self.stateDrop.setObjectName(_fromUtf8("stateDrop"))
        self.stateDrop.addItems(stateList)

        self.stateDrop.setFont(font1)
        self.stateDrop.setStyleSheet("color: #7b7b7b;")

        # Zip Code Entry Box
        self.zipCodeEntry = QtGui.QTextEdit(Form)
        self.zipCodeEntry.setGeometry(QtCore.QRect(430, 140, 161, 31))
        self.zipCodeEntry.setObjectName(_fromUtf8("zipCodeEntry"))
        
        self.zipCodeEntry.setText("Zip Code")
        self.zipCodeEntry.setFont(font1)
        self.zipCodeEntry.setStyleSheet("color: #7b7b7b;")

        # Email Entry Box
        self.emailEntry = QtGui.QTextEdit(Form)
        self.emailEntry.setGeometry(QtCore.QRect(10, 180, 411, 31))
        self.emailEntry.setObjectName(_fromUtf8("emailEntry"))

        self.emailEntry.setText("Email Address")
        self.emailEntry.setFont(font1)
        self.emailEntry.setStyleSheet("color: #7b7b7b;")

        # Phone Entry Box
        self.phoneEntry = QtGui.QTextEdit(Form)
        self.phoneEntry.setGeometry(QtCore.QRect(430, 180, 161, 31))
        self.phoneEntry.setObjectName(_fromUtf8("phoneEntry"))

        self.phoneEntry.setText("Phone Number")
        self.phoneEntry.setFont(font1)
        self.phoneEntry.setStyleSheet("color: #7b7b7b;")

        # Number of Passengers Label
        self.label3 = QtGui.QLabel(Form)
        self.label3.setGeometry(QtCore.QRect(10, 220, 181, 31))

        self.label3.setFont(font2)
        self.label3.setObjectName(_fromUtf8("label3"))

        # Number of Passengers Entry Box
        self.numberPassentersEntry = QtGui.QTextEdit(Form)
        self.numberPassentersEntry.setGeometry(QtCore.QRect(200, 220, 71, 31))
        self.numberPassentersEntry.setObjectName(_fromUtf8("numberPassentersEntry"))

        # Passenger List Entry Box
        self.passengerListEntry = QtGui.QTextEdit(Form)
        self.passengerListEntry.setGeometry(QtCore.QRect(280, 220, 311, 31))
        self.passengerListEntry.setObjectName(_fromUtf8("passengerListEntry"))

        self.passengerListEntry.setText("Enter in passenger Names")
        self.passengerListEntry.setFont(font1)
        self.passengerListEntry.setStyleSheet("color: #7b7b7b;")

        ## Separator Line
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 260, 581, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

# Departure Information

        # Departure Information Label
        self.label4 = QtGui.QLabel(Form)
        self.label4.setGeometry(QtCore.QRect(10, 280, 181, 31))

        self.label4.setFont(font2)
        self.label4.setObjectName(_fromUtf8("label4"))

        # Departure City Entry Box
        self.departureCityEntry = QtGui.QTextEdit(Form)
        self.departureCityEntry.setGeometry(QtCore.QRect(10, 310, 201, 31))
        self.departureCityEntry.setObjectName(_fromUtf8("departureCityEntry"))

        self.departureCityEntry.setText("Departure City")
        self.departureCityEntry.setFont(font1)
        self.departureCityEntry.setStyleSheet("color: #7b7b7b;")

        # Departure State Drop Down Box
        self.departureStateDrop = QtGui.QComboBox(Form)
        self.departureStateDrop.setGeometry(QtCore.QRect(220, 310, 69, 31))
        self.departureStateDrop.setObjectName(_fromUtf8("departureStateDrop"))
        self.departureStateDrop.addItems(stateList)

        self.departureStateDrop.setFont(font1)
        self.departureStateDrop.setStyleSheet("color: #7b7b7b;")

        # Departure Month Drop Down Box
        self.departureMonthDrop = QtGui.QComboBox(Form)
        self.departureMonthDrop.setGeometry(QtCore.QRect(10, 350, 101, 31))
        self.departureMonthDrop.setObjectName(_fromUtf8("departureMonthDrop"))
        self.departureMonthDrop.addItems(monthList)

        self.departureMonthDrop.setFont(font1)
        self.departureMonthDrop.setStyleSheet("color: #7b7b7b;")

        # Departure Day Drop Down Box
        self.departureDayDrop = QtGui.QComboBox(Form)
        self.departureDayDrop.setGeometry(QtCore.QRect(120, 350, 61, 31))
        self.departureDayDrop.setObjectName(_fromUtf8("departureDayDrop"))
        self.departureDayDrop.addItems(dayList)

        self.departureDayDrop.setFont(font1)
        self.departureDayDrop.setStyleSheet("color: #7b7b7b;")

        # Departure Year Drop Down Box
        self.departureYearDrop = QtGui.QComboBox(Form)
        self.departureYearDrop.setGeometry(QtCore.QRect(190, 350, 101, 31))
        self.departureYearDrop.setObjectName(_fromUtf8("departureYearDrop"))

# Destination Information

        # Destination Information Label
        self.label5 = QtGui.QLabel(Form)
        self.label5.setGeometry(QtCore.QRect(310, 280, 181, 31))
        self.label5.setFont(font2)
        self.label5.setObjectName(_fromUtf8("label5"))

        # Destination City Entry Box
        self.destinationCityEntry = QtGui.QTextEdit(Form)
        self.destinationCityEntry.setGeometry(QtCore.QRect(310, 310, 201, 31))
        self.destinationCityEntry.setObjectName(_fromUtf8("destinationCityEntry"))

        self.destinationCityEntry.setText("Destination City")
        self.destinationCityEntry.setFont(font1)
        self.destinationCityEntry.setStyleSheet("color: #7b7b7b;")

        # Destination State Drop Down Box
        self.destinationStateDrop = QtGui.QComboBox(Form)
        self.destinationStateDrop.setGeometry(QtCore.QRect(520, 310, 69, 31))
        self.destinationStateDrop.setObjectName(_fromUtf8("destinationStateDrop"))
        self.destinationStateDrop.addItems(stateList)

        self.destinationStateDrop.setFont(font1)
        self.destinationStateDrop.setStyleSheet("color: #7b7b7b;")

        # Destination Month Drop Down Box
        self.destinationMonthDrop = QtGui.QComboBox(Form)
        self.destinationMonthDrop.setGeometry(QtCore.QRect(310, 350, 101, 31))
        self.destinationMonthDrop.setObjectName(_fromUtf8("destinationMonthDrop"))
        self.destinationMonthDrop.addItems(monthList)

        self.destinationMonthDrop.setFont(font1)
        self.destinationMonthDrop.setStyleSheet("color: #7b7b7b;")

        # Destination Day Drop Down Box
        self.destinationDayDrop = QtGui.QComboBox(Form)
        self.destinationDayDrop.setGeometry(QtCore.QRect(420, 350, 61, 31))
        self.destinationDayDrop.setObjectName(_fromUtf8("destinationDayDrop"))
        self.destinationDayDrop.addItems(dayList)

        self.destinationDayDrop.setFont(font1)
        self.destinationDayDrop.setStyleSheet("color: #7b7b7b;")

        # Destination Year Drop Down Box
        self.destinationYearDrop = QtGui.QComboBox(Form)
        self.destinationYearDrop.setGeometry(QtCore.QRect(490, 350, 101, 31))
        self.destinationYearDrop.setObjectName(_fromUtf8("destinationYearDrop"))
        
        ## Separator Line
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(10, 390, 581, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))

# Direct / Non Stop, Round Trip / One Way

        # Direct Flight Check Box
        self.directFlightCheck = QtGui.QCheckBox(Form)
        self.directFlightCheck.setGeometry(QtCore.QRect(30, 420, 201, 21))

        self.directFlightCheck.setFont(font2)
        self.directFlightCheck.setObjectName(_fromUtf8("directFlightCheck"))

        # Round Trip / One Way Group Box
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(310, 410, 281, 41))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        # Round Trip Radio Button
        self.roundTripRadio = QtGui.QRadioButton(self.groupBox)
        self.roundTripRadio.setGeometry(QtCore.QRect(20, 10, 121, 21))
       
        self.roundTripRadio.setFont(font2)
        self.roundTripRadio.setObjectName(_fromUtf8("roundTripRadio"))

        # One Way Radio Button
        self.oneWayRadio = QtGui.QRadioButton(self.groupBox)
        self.oneWayRadio.setGeometry(QtCore.QRect(170, 10, 91, 21))
       
        self.oneWayRadio.setFont(font2)
        self.oneWayRadio.setObjectName(_fromUtf8("oneWayRadio"))

        ## Separator line
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(10, 460, 581, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))

# Flight Options

        # Flight Options Label
        self.label6 = QtGui.QLabel(Form)
        self.label6.setGeometry(QtCore.QRect(10, 470, 181, 31))

        self.label6.setFont(font2)
        self.label6.setObjectName(_fromUtf8("label6"))
        
       # Service Level Drop Down Box
        self.serviceLevelDrop = QtGui.QComboBox(Form)
        self.serviceLevelDrop.setGeometry(QtCore.QRect(10, 500, 211, 31))
        self.serviceLevelDrop.setObjectName(_fromUtf8("serviceLevelDrop"))
        self.serviceLevelDrop.addItems(serviceLevelList)

        self.serviceLevelDrop.setFont(font1)
        self.serviceLevelDrop.setStyleSheet("color: #7b7b7b;")

        # Number of Check Bags Label                       
        self.label7 = QtGui.QLabel(Form)
        self.label7.setGeometry(QtCore.QRect(310, 500, 201, 31))
        
        self.label7.setFont(font2)
        self.label7.setObjectName(_fromUtf8("label7"))
        
        # Number of Checked Bags Entry Box
        self.checkedBagsEntry = QtGui.QTextEdit(Form)
        self.checkedBagsEntry.setGeometry(QtCore.QRect(520, 500, 71, 31))
        self.checkedBagsEntry.setObjectName(_fromUtf8("checkedBagsEntry"))

        # Special Accomodations Check Box
        self.specialAccomodationsCheck = QtGui.QCheckBox(Form)
        self.specialAccomodationsCheck.setGeometry(QtCore.QRect(10, 540, 201, 21))
      
        self.specialAccomodationsCheck.setFont(font2)
        self.specialAccomodationsCheck.setObjectName(_fromUtf8("specialAccomodationsCheck"))

        # Special Accomodations Entry Box
        self.specialAccomodationsEntry = QtGui.QTextEdit(Form)
        self.specialAccomodationsEntry.setGeometry(QtCore.QRect(10, 570, 281, 61))
        self.specialAccomodationsEntry.setObjectName(_fromUtf8("specialAccomodationsEntry"))

        # Meal Servie Check Box
        self.mealServiceCheck = QtGui.QCheckBox(Form)
        self.mealServiceCheck.setGeometry(QtCore.QRect(310, 540, 201, 21))
       
        self.mealServiceCheck.setFont(font2)
        self.mealServiceCheck.setObjectName(_fromUtf8("mealServiceCheck"))

        # Meal Service Entry Box
        self.mealServiceEntry = QtGui.QTextEdit(Form)
        self.mealServiceEntry.setGeometry(QtCore.QRect(310, 570, 281, 61))
        self.mealServiceEntry.setObjectName(_fromUtf8("mealServiceEntry"))

        # Comments Label
        self.label8 = QtGui.QLabel(Form)
        self.label8.setGeometry(QtCore.QRect(10, 640, 181, 31))
       
        self.label8.setFont(font2)
        self.label8.setObjectName(_fromUtf8("label7"))

        # Comments Entry Box
        self.commentsEntry = QtGui.QTextEdit(Form)
        self.commentsEntry.setGeometry(QtCore.QRect(10, 670, 581, 51))
        self.commentsEntry.setObjectName(_fromUtf8("commentsEntry"))

        # Submit Button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play()
        self.submitButton = QtGui.QPushButton(Form)
        self.submitButton.setGeometry(QtCore.QRect(480, 730, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Myriad Pro"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.submitButton.setStyleSheet("background-color: #841414; color: white;")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Flying Monkey Airlines", None))
        self.label1.setText(_translate("Form", "Flight Reservation System", None))
        self.label2.setText(_translate("Form", "- Book Your Flight", None))
        self.label3.setText(_translate("Form", "Number of Passengers:", None))
        self.directFlightCheck.setText(_translate("Form", "Direct / Non Stop Flight", None))
        self.roundTripRadio.setText(_translate("Form", "Round Trip", None))
        self.oneWayRadio.setText(_translate("Form", "One Way", None))
        self.label6.setText(_translate("Form", "Flight Options:", None))
        self.label4.setText(_translate("Form", "Departure Information:", None))
        self.label5.setText(_translate("Form", "Destination Information:", None))
        self.label7.setText(_translate("Form", "Number of  Checked Bags:", None))
        self.specialAccomodationsCheck.setText(_translate("Form", "Special Accomodations", None))
        self.mealServiceCheck.setText(_translate("Form", "Meal Service", None))
        self.label8.setText(_translate("Form", "Comments:", None))
        self.submitButton.setText(_translate("Form", "Submit", None))
        self.CustomerInformationLabel.setText(_translate("Form", "Customer Information:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    pygame.quit()

