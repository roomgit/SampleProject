import sys

from PySide2.QtWidgets import QApplication, QPushButton, QLCDNumber



# Create the Qt Application

app = QApplication(sys.argv)

# Create a button

button = QPushButton()

#button.display(123)

# Show the button

button.show()

# Run the main Qt loop

app.exec_()


