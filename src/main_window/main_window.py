from src.postgres_database import Database
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.views import TransactionFormView, AllTransactionsView, SettingsView, TestView
from src.utils import Logger
from config.settings import load_toml_settings
from src.setters import TextSetter, ProfitLossColorPicker, TextColorSetter
from src.generators import QPushButtonGenerator


class MainWindowWidget(QWidget):
    """A class used to build widget for main window

    Arguments
    ---------
    QWidget (class): Class used to create widgets

    Attributes
    ----------
    currency: str
        a main currency chosen in settings
    database: Database
        a database contains all transactions created in application
    language: str
        an application language chosen in settings
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
        self.text_setter = TextSetter(self.language)
        self.qpush_button_generator = QPushButtonGenerator(self, self.main_window.toml_data['settings']['primary_color'], self.text_setter)

        # Create version label
        self.version_label = QLabel(self, objectName='version-label')
        self.version_label.setText(f"Version: {self.main_window.toml_data['project']['version']}")
        self.version_label.move(700, 570)
        self.version_label.setAlignment(Qt.AlignCenter)
        self.main_window.logger.logger.info('Version label generated.')

        # Show profile/loss information
        self.show_profit_loss_info()

        # Load buttons
        self.load_buttons()
        self.load_text()

        # Check if show window in full screen
        if self.main_window.toml_data['settings']['fullscreen']:
            self.main_window.showFullScreen()
        else:
            self.main_window.setGeometry(550, 200, 800, 800)

    def load_buttons(self):
        self.settings_btn = self.qpush_button_generator.generate_element('settings-btn', '', 750, 50)
        self.settings_btn.setIcon(QIcon('static/images/settings_icon.png'))
        self.settings_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.transaction_btn = self.qpush_button_generator.generate_element('transaction-btn', 'Dodaj transakcję', 50, 140)
        self.all_transactions_btn = self.qpush_button_generator.generate_element('all-transactions-btn', 'Wszystkie transakcje', 50, 200)
        self.test_btn = self.qpush_button_generator.generate_element('test-btn', 'Test', 50, 260)
        self.exit_btn = self.qpush_button_generator.generate_element('exit-btn', 'Wyjdź', 50, 320)
        self.main_window.logger.logger.info('Buttons loaded.')

    def load_text(self):
        """Load texts for all elements in main window"""

        self.text_setter.set_text(self.profit_loss_label, 'Z/S: ')
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
            code of language chosen in settings

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
    def __init__(self):
        """Initializes the instance based on parent window."""

        super(MainWindow, self).__init__()

        # Initiate all used attributes
        self.logger = Logger(__name__)
        self.toml_data = load_toml_settings()
        self.language = self.toml_data['settings']['language']

        # Set window settings
        self.setWindowIcon(QIcon('static/images/favicon.jpg'))
        self.logger.logger.info("Main window generated.")
        self.setGeometry(550, 250, 800, 600)

        # Generate main window UI
        self.start_main_window_UI()

    def start_main_window_UI(self):
        """Load main window UI"""

        # Create MainWindowWidget class instance
        self.main_tab = MainWindowWidget(self)
        self.logger.logger.info("Main window widget generated.")
        self.setCentralWidget(self.main_tab)

        # Connect all buttons in UI into class methods
        self.main_tab.settings_btn.clicked.connect(self.settings_UI)
        self.main_tab.transaction_btn.clicked.connect(self.add_new_transaction_UI)
        self.main_tab.all_transactions_btn.clicked.connect(self.show_all_transactions_UI)
        self.main_tab.test_btn.clicked.connect(self.test_view_UI)
        self.main_tab.exit_btn.clicked.connect(self.close)

        #Show UI
        self.show()

    def add_new_transaction_UI(self):
        """Load new transaction form UI"""

        # Create TransactionFormView class instance
        self.transaction_tab = TransactionFormView(self)
        self.logger.logger.info("Transaction form view generated.")
        self.setCentralWidget(self.transaction_tab)

        # Connect "Back to menu" button into start_main_window_UI method
        self.transaction_tab.menu_btn.clicked.connect(self.start_main_window_UI)

        # Show UI
        self.show()
        
    def show_all_transactions_UI(self):
        """Load all transactions table UI"""

        # Create AllTransactionsView class instance
        self.all_transactions_tab = AllTransactionsView(self)
        self.logger.logger.info("All transactions view generated.")
        self.setCentralWidget(self.all_transactions_tab)

        # Connect "Back to menu" button into start_main_window_UI method
        self.all_transactions_tab.menu_btn.clicked.connect(self.start_main_window_UI)
        
        # Show UI
        self.show()

    def settings_UI(self):
        """Load settings panel UI"""

        # Create SettingsView class instance
        self.settings_tab = SettingsView(self)
        self.logger.logger.info('Settings view generated.')
        self.setCentralWidget(self.settings_tab)

        # Connect "Back to menu" button into start_main_window_UI method
        self.settings_tab.menu_btn.clicked.connect(self.start_main_window_UI)

        # Show UI
        self.show()

    def test_view_UI(self):
        """Load test form UI"""

        # Create TestView class instance
        self.test_tab = TestView(self)
        self.logger.logger.info('Test view generated.')
        self.setCentralWidget(self.test_tab)

        # Connect "Back to menu" button into start_main_window_UI method
        self.test_tab.menu_btn.clicked.connect(self.start_main_window_UI)

        # Show UI
        self.show()
