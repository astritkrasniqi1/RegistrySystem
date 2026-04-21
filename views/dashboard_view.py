from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QFormLayout,
    QHBoxLayout, QDialog, QMessageBox
)


# -------------------------------
# Add Citizen Popup Window
# -------------------------------
class AddCitizenView(QDialog):
    def __init__(self, controller, edit_mode=False, citizen_id=None):
        super().__init__()
        self.controller = controller
        self.edit_mode = edit_mode
        self.citizen_id = citizen_id
        self.setWindowTitle("Add Citizen")
        self.resize(400, 250)

        self.setStyleSheet("""
        QWidget {
                background-color: white;
            }
                           
        QLabel {
                color: black;
                font-size:15px;
                padding-bottom:7px;
            }
                           
        QLineEdit {
                 border: 1px solid rgb(0, 170, 255);
                 color: black;
                border-radius: 5px;
                padding-bottom:7px;
                min-height:16px;
                line-height:12px;
            }
        QPushButton {
                background-color: rgb(0, 170, 255);
                color: white;
                margin-top:10px;
                padding: 7px 0;
        }

    """)

        layout = QFormLayout()

        self.input_personal_id = QLineEdit()
        self.input_emri = QLineEdit()
        self.input_mbiemri = QLineEdit()
        self.input_email = QLineEdit()
        self.input_city = QLineEdit()

        btn_add = QPushButton("Save")
        btn_add.clicked.connect(self.save_citizen)

        layout.addRow("Personal ID:", self.input_personal_id)
        layout.addRow("First Name:", self.input_emri)
        layout.addRow("Last Name:", self.input_mbiemri)
        layout.addRow("Email:", self.input_email)
        layout.addRow("City:", self.input_city)
        layout.addRow(btn_add)

        self.setLayout(layout)

    def save_citizen(self):
        if self.edit_mode:  # Edit existing citizen
            data = {
                "personal_id": self.input_personal_id.text(),
                "emri": self.input_emri.text(),
                "mbiemri": self.input_mbiemri.text(),
                "email": self.input_email.text(),
                "city": self.input_city.text()
            }
            try:
                self.controller.update_citizen(self.citizen_id, data)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to update citizen:\n{str(e)}")
        else:  # Add new citizen
            try:
                self.controller.add_citizen(
                    self.input_personal_id.text(),
                    self.input_emri.text(),
                    self.input_mbiemri.text(),
                    self.input_email.text(),
                    self.input_city.text()
                )
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to add citizen:\n{str(e)}")
        self.accept()



# -------------------------------
# Dashboard Main Window
# -------------------------------
class DashboardView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Dashboard")
        self.resize(900, 600)

        # Apply styles
        self.setStyleSheet("""
                           


            QPushButton#btnEdit {
                background-color: rgb(0, 170, 255);
                color: white;
                font-weight: bold;
                border-radius: 4px;
                padding: 4px 8px;
            }

            QPushButton#btnEdit:hover {
                background-color: rgb(0, 140, 220);
            }

            QPushButton#btnDelete {
                background-color: rgb(200, 0, 0);
                color: white;
                font-weight: bold;
                border-radius: 4px;
                padding: 4px 8px;
            }

            QPushButton#btnDelete:hover {
                background-color: rgb(255, 0, 0);
            }
                           


            QWidget {
                background-color: white;
            }

            /* --- Table --- */
            QTableWidget {
                padding-top: 30px;
                gridline-color: #0078d7;  /* Blue gridlines */
                border: 1px solid #0078d7;
                border:none;
                color:black;
                min-width:400px;
            }

            QHeaderView::section {
                background-color: #f0f8ff;
                color: #0078d7;
                font-weight: bold;
                border: 1px solid #0078d7;
                padding: 4px;
                
            }

            /* Remove item border to avoid double-lines */
            QTableWidget::item {
                border: none;
            }

            QTableWidget::item:selected {
                background-color: #cce6ff;
                color: black;
            }

            /* --- Filter inputs --- */
            QLineEdit {
                border: 1px solid rgb(0, 170, 255);
                padding: 5px;
                border-radius: 5px;
                color:black;
            }
            QLineEdit::placeholder {
                color: black;
            }

            /* --- Search button --- */
            QPushButton#btnSearch {
                background-color: rgb(0, 170, 255);
                color: white;
                font-weight: bold;
                padding: 6px 12px;
                border-radius: 4px;
            }

            QPushButton#btnSearch:hover {
                background-color: rgb(0, 140, 220);
            }

            /* --- Add Citizen button --- */
            QPushButton#btnAddCitizen {
                background-color: rgb(100, 226, 0);
                color: white;
                font-weight: bold;
                padding: 6px 12px;
                border-radius: 4px;
            }

            QPushButton#btnAddCitizen:hover {
                background-color: rgb(80, 200, 0);
            }

            QPushButton#btnLogout {
                background-color: rgb(180,0,0);
                color: white;
                font-weight: bold;
                padding: 6px 12px;
                border-radius: 4px;
            }
                           
            QPushButton#btnLogout:hover {
                 background-color: rgb(255,0,0);       
            }
        """)

        layout = QVBoxLayout()

        # -------- Filters --------
        filter_layout = QHBoxLayout()
        self.filter_personal_id = QLineEdit()
        self.filter_personal_id.setPlaceholderText("Filter by Personal ID")

        self.filter_name = QLineEdit()
        self.filter_name.setPlaceholderText("Filter by Name")

        self.filter_city = QLineEdit()
        self.filter_city.setPlaceholderText("Filter by City")

        btn_filter = QPushButton("Search")
        btn_filter.setObjectName("btnSearch")  # For CSS styling
        btn_filter.clicked.connect(self.load_data)

        filter_layout.addWidget(self.filter_personal_id)
        filter_layout.addWidget(self.filter_name)
        filter_layout.addWidget(self.filter_city)
        filter_layout.addWidget(btn_filter)
        layout.addLayout(filter_layout)

        # -------- Table --------
        self.table = QTableWidget()
        layout.addWidget(self.table)

        # -------- Add Citizen Button --------
        btn_open_add = QPushButton("Add Citizen")
        btn_open_add.setObjectName("btnAddCitizen")  # For CSS styling
        btn_open_add.clicked.connect(self.open_add_citizen)
        layout.addWidget(btn_open_add)

        btn_logout = QPushButton("Logout")
        btn_logout.setObjectName("btnLogout")  # For CSS styling
        btn_logout.clicked.connect(self.logout)
        layout.addWidget(btn_logout)

        self.setLayout(layout)
        self.load_data()


    def load_data(self):
        personal_id_filter = self.filter_personal_id.text() if hasattr(self, 'filter_personal_id') else ""
        name_filter = self.filter_name.text() if hasattr(self, 'filter_name') else ""
        city_filter = self.filter_city.text() if hasattr(self, 'filter_city') else ""

        citizens = self.controller.get_citizens(personal_id_filter, name_filter, city_filter)

        self.table.setRowCount(len(citizens))
        self.table.setColumnCount(6)  # 5 data columns + 1 for actions
        self.table.setHorizontalHeaderLabels(
            ["Personal ID", "First Name", "Last Name", "Email", "City", "Actions"]
        )

        for row, c in enumerate(citizens):
            # c is a single tuple: (id, personal_id, emri, mbiemri, email, city)

            # Fill table cells
            self.table.setItem(row, 0, QTableWidgetItem(c[1]))  # personal_id
            self.table.setItem(row, 1, QTableWidgetItem(c[2]))  # emri
            self.table.setItem(row, 2, QTableWidgetItem(c[3]))  # mbiemri
            self.table.setItem(row, 3, QTableWidgetItem(c[4]))  # email
            self.table.setItem(row, 4, QTableWidgetItem(c[5] if c[5] else ""))  # city

            # --- Action buttons ---
            btn_edit = QPushButton("Edit")
            btn_edit.setObjectName("btnEdit")

            btn_delete = QPushButton("Delete")
            btn_delete.setObjectName("btnDelete")

            btn_edit.clicked.connect(lambda checked, cid=c[0]: self.controller.edit_citizen(cid))
            btn_delete.clicked.connect(lambda checked, cid=c[0]: self.controller.delete_citizen(cid))

            action_widget = QWidget()
            layout = QHBoxLayout()
            layout.addWidget(btn_edit)
            layout.addWidget(btn_delete)
            layout.setContentsMargins(0, 0, 0, 0)
            action_widget.setLayout(layout)

            self.table.setCellWidget(row, 5, action_widget)



    def open_add_citizen(self):
        dialog = AddCitizenView(self.controller)
        if dialog.exec():  
            self.load_data()  

    def logout(self):
        self.close()
        self.controller.app.show_login()  # now works!`

