from src.postgres_database import Database
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.views import TransactionFormView, AllTransactionsView, SettingsView, TestView
from src.utils import Logger, Utils
from config.settings import load_toml_settings
from src.setters import ButtonColorSetter, TextSetter, ProfitLossColorPicker, TextColorSetter, ButtonTextColorPicker
from src.abstract import ViewClass
from src.meta import MetaClass


class MainWindowWidget(QWidget, ViewClass, metaclass=MetaClass):
    """A class used to build widget for main window

    Arguments
    ---------
    QWidget (class): Class used to create widgets
    ViewClass (class): Abstract class used to override methods for view type classes
    metaclass (class, optional): Class used to inherit by two classes. Defaults to MetaClass.

    Attributes
    ----------
    currency: str
        a main currency choosen in settings
    database: Database
        a database contains all transactions created in application
    language: str
        an application language choosen in settings
    main_window: QMainWindow
        an object represents whole main window

    all_transactions_btn: QPushButton
        button moves user into all transactions table
    exit_btn: QPushButton
        button to close application
    settings_btn: QPushButton
        button moves user into settings
    test_btn: QPushButton
        button moves user into test view
    transaction_btn: QPushButton
        button moves user into add transaction form
        
    version_label: QLabel
        label shows version on application


    Methods
    -------
    count_profit_loss_value()
        Count values for all transactions added to application    
    load_colors()
        Load colors for all elements in main window
    load_text()
        Load text for all elements in main window
    show_profit_loss_info()
        Display information about profit or loss in transactions account
    """

    def __init__(self, parent=None):
        """Initializes the instance based on parent window.

        Arguments:
            parent (QMainWindow, optional): window, which show this widget. Defaults to None.
        """

        super(MainWindowWidget, self).__init__(parent)

        # Initiate all used attributes
        self.main_window = parent
        self.database = Database()
        self.language = self.main_window.toml_data['settings']['language']
        self.currency = self.main_window.toml_data['settings']['user_currency']

        # Create settings button
        self.settings_btn = QPushButton("", self, objectName='settings-btn')
        self.settings_btn.move(750, 50)
        self.settings_btn.setIcon(QIcon('static/images/settings_icon.png'))
        self.settings_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.main_window.logger.logger.info('Settings button generated.')

        # Create trasnsactions button
        self.transaction_btn = QPushButton("", self, objectName='transaction-btn')
        self.transaction_btn.move(50, 140)
        self.main_window.logger.logger.info("Add transaction button generated")

        # Create all transactions button
        self.all_transactions_btn = QPushButton("", self, objectName='all-transactions-btn')
        self.all_transactions_btn.move(50, 200)
        self.main_window.logger.logger.info("Show all transactions button generated")
        
        # Create exit button
        self.exit_btn = QPushButton("", self, objectName='exit-btn')
        self.exit_btn.move(50, 320)
        self.main_window.logger.logger.info("Exit button generated")

        # Create test button
        self.test_btn = QPushButton("", self, objectName='test-btn')
        self.test_btn.move(50, 260)
        self.main_window.logger.logger.info("Test view button generated")

        # Create version label
        self.version_label = QLabel(self, objectName='version-label')
        self.version_label.setText(f"Version: {self.main_window.toml_data['project']['version']}")
        self.version_label.move(700, 570)
        self.version_label.setAlignment(Qt.AlignCenter)
        self.main_window.logger.logger.info('Version label generated.')

        # Show profile/loss information
        self.show_profit_loss_info()

        # Check if show window in full screen
        if self.main_window.toml_data['settings']['fullscreen']:
            self.main_window.showFullScreen()
        else:
            self.main_window.setGeometry(550, 250, 800, 600)

        # Load colors and texts
        self.load_colors()
        self.load_text()

    def load_colors(self):
        """Load colors for all elements in main window"""

        # Initiate ButtonTextColorPicker and TextColorSetter
        button_text_color_picker = ButtonTextColorPicker()
        text_color_setter = TextColorSetter(['white', 'black'], button_text_color_picker)

        # Check if primary color is not enough bright for white text color
        button_text_color_picker.check_pick_condiditon(self.main_window.toml_data['settings']['primary_color'])

        # Initiate ButtonColorSetter 
        button_color_setter = ButtonColorSetter(self.main_window.toml_data['settings']['primary_color'], text_color_setter)

        # Set colors for all buttons in main window
        button_color_setter.set_color(self.transaction_btn)
        button_color_setter.set_color(self.all_transactions_btn)
        button_color_setter.set_color(self.exit_btn)
        button_color_setter.set_color(self.test_btn)
        self.main_window.logger.logger.info("All window styles set.")

    def load_text(self):
        """Load texts for all elements in main window"""

        # Initiate TextSetter
        text_setter = TextSetter(self.language, self.main_window.toml_data)

        # Set text for window title and all buttons in main window 
        text_setter.set_title(self.main_window, 'Dziennik transakcji')
        text_setter.set_text(self.transaction_btn, "Dodaj transakcję")
        text_setter.set_text(self.exit_btn, "Wyjdź")
        text_setter.set_text(self.all_transactions_btn, "Wszystkie transakcje")
        text_setter.set_text(self.test_btn, "Test")
        text_setter.set_text(self.profit_loss_label, 'Z/S: ')
        self.main_window.logger.logger.info('View text set.')

    def show_profit_loss_info(self):
        """Display information about profit or loss in transactions account"""

        # Create Profit/Loss information label
        self.profit_loss_label = QLabel(self, objectName='profit-loss-label')
        self.profit_loss_label.move(50, 20)
        self.profit_loss_label.setStyleSheet(f"border-style: none;")
        self.main_window.logger.logger.info('Profit/Loss label generated.')

        # Create all transactions value label
        self.profit_loss_value = QLabel(self, objectName='profit-loss-label')
        self.profit_loss_value.move(80, 20)
        self.profit_loss_value.setText(f'{str(self.count_profit_loss_value())} {self.currency}')

        # Initiate ProfitLossColorPicker and TextColorSetter
        self.picker = ProfitLossColorPicker()
        self.text_color_setter = TextColorSetter(['red', 'green'], self.picker)

        # Check if value of all transactions if negative or positive
        self.picker.check_pick_condiditon(self.profit_loss_value.text())

        # Set color for value of all transactions
        self.text_color_setter.set_color(self.profit_loss_value)

        self.main_window.logger.logger.info('Profit/Loss value generated.')

    def count_profit_loss_value(self):
        values = self.database.select(columns='test_ident')
        return sum([x[0] for x in values])


class MainWindow(QMainWindow):
    """A class used to show all widgets in application

        Arguments
        ---------
        QMainWindow (class): Class used to generate application main window

        Attributes
        ----------
        logger: Logger
            object used to show appication's logs
        toml_data: dict
            datas from .toml file
        language: str
            code of language choosen in settings

        all_transactions_tab: AllTransactionsView
            widget contains all transactions table
        main_tab: MainWindowWidget
            widget contains main window view
        settings_tab: SettingsView
            widget contains settings view
        test_tab: TestView
            widget contains test view
        transaction_tab: TransactionFormView
            widget contains new transaction form

        
        Methods
        -------
        add_new_transaction_UI():
            Loads new transaction form
        settings_UI():
            Loads widget with application's settings
        show_all_transactions_UI():
            Loads widget with all transactions in database
        start_main_window_UI():
            Loads MainWindowWidget with all buttons
        test_view_UI():
            Loads test widget
    """
    def __init__(self, parent=None):
        self.logger = Logger(__name__)
        self.toml_data = load_toml_settings()
        self.language = self.toml_data['settings']['language']
        super(MainWindow, self).__init__(parent)
        self.setWindowIcon(QIcon('static/images/favicon.jpg'))
        self.logger.logger.info("Main window generated.")
        self.setGeometry(550, 250, 800, 600)
        self.start_main_window_UI()

    def start_main_window_UI(self):
        self.main_tab = MainWindowWidget(self)
        self.logger.logger.info("Main window widget generated.")
        self.setCentralWidget(self.main_tab)
        self.main_tab.settings_btn.clicked.connect(self.settings_UI)
        self.main_tab.transaction_btn.clicked.connect(self.add_new_transaction_UI)
        self.main_tab.all_transactions_btn.clicked.connect(self.show_all_transactions_UI)
        self.main_tab.test_btn.clicked.connect(self.test_view_UI)
        self.main_tab.exit_btn.clicked.connect(self.close)
        self.show()

    def add_new_transaction_UI(self):
        self.transaction_tab = TransactionFormView(self)
        self.logger.logger.info("Transaction form view generated.")
        self.setCentralWidget(self.transaction_tab)
        self.transaction_tab.menu_btn.clicked.connect(self.start_main_window_UI)
        self.show()
        
    def show_all_transactions_UI(self):
        self.all_transactions_tab = AllTransactionsView(self)
        self.logger.logger.info("All transactions view generated.")
        self.setCentralWidget(self.all_transactions_tab)
        self.all_transactions_tab.menu_btn.clicked.connect(self.start_main_window_UI)
        self.show()

    def settings_UI(self):
        self.settings_tab = SettingsView(self)
        self.logger.logger.info('Settings view generated.')
        self.setCentralWidget(self.settings_tab)
        self.settings_tab.menu_btn.clicked.connect(self.start_main_window_UI)
        self.show()

    def test_view_UI(self):
        self.test_tab = TestView(self)
        self.setCentralWidget(self.test_tab)
        self.test_tab.menu_btn.clicked.connect(self.start_main_window_UI)
        self.show()
