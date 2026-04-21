from models.user_model import UserModel
from PySide6.QtWidgets import QMessageBox
from views.register_view import Ui_MainWindow as RegisterUI
from controllers.register_controller import RegisterController
from views.dashboard_view import DashboardView
from controllers.dashboard_controller import DashboardController

from PySide6.QtWidgets import QMessageBox
from models.user_model import UserModel


class LoginController:
    def __init__(self, ui, app, window):
        self.ui = ui
        self.app = app
        self.window = window  
        self.ui.pushButton.clicked.connect(self.login)  
        self.ui.label_5.linkActivated.connect(self.open_register)  

    def login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        def show_message(title, text, icon=QMessageBox.Information):
            msg = QMessageBox(self.window)
            msg.setWindowTitle(title)
            msg.setText(text)
            msg.setIcon(icon)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white;
                    border-radius: 10px;
                }
                QLabel {
                    color: black;
                    font-size: 13px;
                }
                QPushButton {
                    background-color: #5E5EFF;
                    color: white;
                    border-radius: 5px;
                    padding: 5px 12px;
                }
                QPushButton:hover {
                    background-color: #3a3aff;
                }
            """)
            msg.exec()

        if UserModel.validate_user(username, password):
            show_message("Success", "✅ Login successful!", QMessageBox.Information)
            self.window.close()           
            self.app.show_dashboard()     
        else:
            show_message("Error", "❌ Invalid username or password", QMessageBox.Warning)


    def open_register(self):
        self.window.close()           
        self.app.show_register()      