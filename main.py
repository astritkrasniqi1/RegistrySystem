import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from views.dashboard_view import DashboardView
from views.login_view import Ui_MainWindow as LoginUI
from views.register_view import Ui_MainWindow as RegisterUI
from controllers.register_controller import RegisterController
from controllers.dashboard_controller import DashboardController
from controllers.login_controller import LoginController



class App:
    def __init__(self):
        self.qt_app = QApplication(sys.argv)
        self.login_window = None
        self.register_window = None
        self.dashboard_window = None

    def show_login(self):
        if self.login_window is None:
            self.login_window = QMainWindow()
            ui = LoginUI()
            ui.setupUi(self.login_window)
            # Keep a reference to the controller to prevent garbage collection
            self.login_controller = LoginController(ui, self, self.login_window)
        self.login_window.show()

        # Hide other windows if they exist
        if self.register_window:
            self.register_window.hide()
        if self.dashboard_window:
            self.dashboard_window.hide()

    def show_register(self):
        if self.register_window is None:
            self.register_window = QMainWindow()
            ui = RegisterUI()
            ui.setupUi(self.register_window)
            self.register_controller = RegisterController(ui, self.register_window, self)
        self.register_window.show()
        if self.login_window:
            self.login_window.hide()
        if self.dashboard_window:
            self.dashboard_window.hide()



    def show_dashboard(self):
        if self.dashboard_window is None:
            # Create the controller first
            self.dashboard_controller = DashboardController(self)

            # Create the view, passing the controller
            self.dashboard_window = DashboardView(self.dashboard_controller)

            # Link them both
            self.dashboard_controller.view = self.dashboard_window

        self.dashboard_window.show()

        if self.login_window:
            self.login_window.hide()
        if self.register_window:
            self.register_window.hide()




    def run(self):
        self.show_login()
        sys.exit(self.qt_app.exec())

if __name__ == "__main__":
    App().run()
