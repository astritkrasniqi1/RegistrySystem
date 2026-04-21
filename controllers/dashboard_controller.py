from models.citizen_model import CitizenModel
from views.dashboard_view import AddCitizenView
from PySide6.QtWidgets import QMessageBox

class DashboardController:
    def __init__(self, app, view = None):
        self.view = view
        self.app = app
        self.model = CitizenModel()
        

    def get_citizens(self, personal_id_filter= "", name_filter= "", city_filter=""):
        return CitizenModel.get_citizens(personal_id_filter, name_filter, city_filter)
    

    
    def add_citizen(self, personal_id, emri, mbiemri, email, city):
        existing = CitizenModel.get_citizens(personal_id_filter=personal_id)
        if existing:
            
            msg = QMessageBox(self.view)
            msg.setWindowTitle("Warning")
            msg.setText(f"This citizen with ID {personal_id} already exists!")
            msg.setIcon(QMessageBox.Warning)
            msg.setStyleSheet("QLabel{min-width: 200px; color: black;} QMessageBox{background-color: white;}")
            msg.exec()
            return

        CitizenModel.AddCitizen(personal_id, emri, mbiemri, email, city)
        self.view.load_data()

    def edit_citizen(self, citizen_id):
        citizen = CitizenModel.get_citizen_by_id(citizen_id)
        if not citizen:
            return

        dialog = AddCitizenView(self, edit_mode=True, citizen_id=citizen_id)

        
        dialog.input_personal_id.setText(citizen[5])   
        dialog.input_emri.setText(citizen[1])
        dialog.input_mbiemri.setText(citizen[2])
        dialog.input_email.setText(citizen[3])
        dialog.input_city.setText(citizen[4])

        dialog.exec()



    def update_citizen(self, citizen_id, data):
        CitizenModel.update_citizen(citizen_id, data)
        self.view.load_data()



    def delete_citizen(self, citizen_id):
        from PySide6.QtWidgets import QMessageBox

        msg = QMessageBox(self.view)  # set parent to your view
        msg.setWindowTitle("Confirm Delete")
        msg.setText("Are you sure you want to delete this citizen?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)

        # Apply custom CSS
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

        ret = msg.exec()

        if ret == QMessageBox.Yes:
            CitizenModel.delete_citizen(citizen_id)
            self.view.load_data()
