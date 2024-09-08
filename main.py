import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QComboBox, QSpinBox, QWidget
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Movie Billing System")
        self.setGeometry(0, 0, 800, 600)

        # Create central widget
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        # Create UI elements
        self.label_title = QLabel("MOVIE BILLING SYSTEM", self.centralwidget)
        self.label_title.setGeometry(220, 0, 361, 41)
        self.label_title.setFont(QFont("MS Shell Dlg 2", 20))

        self.label_name = QLabel("NAME", self.centralwidget)
        self.label_name.setGeometry(40, 70, 81, 31)
        self.lineEdit_name = QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(30, 110, 113, 22)

        self.label_phone = QLabel("PHONE NO", self.centralwidget)
        self.label_phone.setGeometry(600, 70, 81, 31)
        self.lineEdit_phone = QLineEdit(self.centralwidget)
        self.lineEdit_phone.setGeometry(600, 110, 113, 22)

        self.label_movie_selector = QLabel("MOVIE SELECTOR", self.centralwidget)
        self.label_movie_selector.setGeometry(290, 150, 271, 41)
        self.label_movie_selector.setFont(QFont("MS Shell Dlg 2", 20))
        self.comboBox_movies = QComboBox(self.centralwidget)
        self.comboBox_movies.setGeometry(140, 200, 511, 22)
        self.comboBox_movies.addItems(["MOVIE-1", "MOVIE-2", "MOVIE-3", "MOVIE-4"])

        self.label_no_of_tickets = QLabel("NO OF TICKET", self.centralwidget)
        self.label_no_of_tickets.setGeometry(340, 240, 121, 41)
        self.spinBox_tickets = QSpinBox(self.centralwidget)
        self.spinBox_tickets.setGeometry(480, 250, 42, 22)

        self.label_price_per_ticket = QLabel("PRICE PER TICKET", self.centralwidget)
        self.label_price_per_ticket.setGeometry(310, 290, 141, 41)
        self.label_price_per_ticket_value = QLabel("TextLabel", self.centralwidget)
        self.label_price_per_ticket_value.setGeometry(480, 290, 101, 41)

        self.label_total_price = QLabel("TOTAL PRICE", self.centralwidget)
        self.label_total_price.setGeometry(340, 350, 141, 41)
        self.label_total_price_value = QLabel("TextLabel", self.centralwidget)
        self.label_total_price_value.setGeometry(480, 350, 101, 41)

        self.button_submit = QPushButton("SUBMIT", self.centralwidget)
        self.button_submit.setGeometry(340, 490, 151, 31)
        self.button_submit.clicked.connect(self.calculate_total)

    def calculate_total(self):
        # Implement your calculation logic here
        # Get selected movie and number of tickets
        selected_movie = self.comboBox_movies.currentText()
        num_tickets = self.spinBox_tickets.value()

        # Determine price per ticket based on selected movie
        price_per_ticket = 0  # Replace with actual pricing logic
        if selected_movie == "MOVIE-1":
            price_per_ticket = 100
        elif selected_movie == "MOVIE-2":
            price_per_ticket = 150
        # ... add more movie pricing conditions

        # Calculate total price
        total_price = price_per_ticket * num_tickets

        # Update labels
        self.label_price_per_ticket_value.setText(f"{price_per_ticket}")
        self.label_total_price_value.setText(f"{total_price}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
