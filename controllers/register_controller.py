from models.user_model import UserModel
from PySide6.QtWidgets import QMessageBox, QWidget


class RegisterController:
    def __init__(self, view, window: QWidget, app):
        self.view = view
        self.window = window   
        self.app = app

        self.view.pushButton.clicked.connect(self.register)
        self.view.label_10.linkActivated.connect(self.back_to_login)

    def register(self):
        nrpersonal = self.view.lineEdit_3.text()
        emri = self.view.lineEdit.text()
        mbiemri = self.view.lineEdit_2.text()
        email = self.view.lineEdit_4.text()
        username = self.view.lineEdit_5.text()
        password = self.view.lineEdit_6.text()

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

        if not username or not password:
            show_message("Error", "❌ Fill all fields!", QMessageBox.Warning)
            return

        # Check if personal_id already exists
        if UserModel.personal_id_exists(nrpersonal):
            show_message("Error", "❌ This personal ID already exists!", QMessageBox.Warning)
            return

        try:
            UserModel.create_user(username, password, email, emri, mbiemri, nrpersonal)
            show_message("Success", "✅ User registered!", QMessageBox.Information)

            self.window.close()
            self.app.show_login()

        except Exception as e:
            show_message("Error", str(e), QMessageBox.Critical)


    def back_to_login(self):
        self.app.show_login()
