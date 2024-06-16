from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.utils import Logger, Utils
from src.postgres_database import Database
from src.setters import ButtonColorSetter, TextSetter, BackgroundColorSetter, TextColorSetter, ButtonTextColorPicker
from src.abstract import ViewClass
from src.meta import MetaClass


class AllTransactionsView(QWidget, ViewClass, metaclass=MetaClass):
    """A class used to build all transactions table widget for window

    Arguments
    ---------
        QWidget (class): Class used to create widgets
        ViewClass (class): Abstract class used to override methods for view type classes
        metaclass (class, optional): Class used to inherit by two classes. Defaults to MetaClass.

    Attributes
    ----------
    language: str
        Language code
    main_window: object
        Main window object

    database: Database
        Database object
    logger: Logger
        Logger object

    layout: QVBoxLayout
        Layout for adding other PyQt elements
    menu_btn: QPushButton
        Button moving user into main window
    order_method_cb: QComboBox
        Combo box used to setting method of order (ASC, DESC)
    sort_cb: QComboBox
        Combo box used to setting column, which app will sort

    Methods
    -------
    create_table()
        Create table widget with loaded database datas
    sort_records()
        Sort entire table by choosen column
    load_colors()
        Load colors for widget
    load_text()
        Load text in choosen language for widget and window
    load_menu_button_color()
        Load choosen primary color for 'Go back to menu' button
    load_background_color()
        Load choosen secondary color for database records table
    """

    def __init__(self, parent=None):
        """Initializes the instance based on parent window.

        Arguments:
            parent (QMainWindow, optional): window, which show this widget. Defaults to None.
        """

        super(AllTransactionsView, self).__init__(parent)
    
         # Initiate all used attributes
        self.main_window = parent
        self.language = self.main_window.toml_data['settings']['language']
        self.logger = Logger(__name__)
        self.database = Database()
        self.logger.logger.info("Database loaded.")

        # Create 'Go back to menu' button
        self.menu_btn = QPushButton("", self)
        self.menu_btn.move(100, 350)
        self.menu_btn.setObjectName('menu-btn')
        self.logger.logger.info('Go back to menu button generated.')

        # Create table widget
        self.create_table()
        self.logger.logger.info('Table widget generated.')

        # Create sort column ComboBox
        columns = ["", "name", "age"]
        self.sort_cb = QComboBox(self)
        self.sort_cb.addItems(columns)
        self.sort_cb.move(100, 200)
        self.sort_cb.setCurrentIndex(0)
        self.sort_cb.currentIndexChanged.connect(self.sort_records)
        self.logger.logger.info('Sort column ComboBox generated.')

        # Create order method ComboBox
        order_method = ['ASC', 'DESC']
        self.order_method_cb = QComboBox(self)
        self.order_method_cb.addItems(order_method)
        self.order_method_cb.move(100, 200)
        self.order_method_cb.setCurrentIndex(0)
        self.order_method_cb.currentIndexChanged.connect(self.sort_records)
        self.logger.logger.info('Order method ComboBox generated.')

        # Create layout for all PyQt elements and set them as main layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.sort_cb)
        self.layout.addWidget(self.order_method_cb)
        self.layout.addWidget(self.table_widget)
        self.layout.addWidget(self.menu_btn)
        self.setLayout(self.layout)
        self.logger.logger.info("Table layout set up.")

        # Load colors
        self.load_colors()

        # Load text
        self.load_text()

    def create_table(self):
        """Load data from database and show them in table"""

        self.table_widget = QTableWidget()
        self.table_widget.setShowGrid(False) # Disable clickable headers
        self.records = self.database.select() # Select all columns from test table

        # Set table sizes
        self.table_widget.setRowCount(len(self.records))
        self.table_widget.setColumnCount(2)

        self.table_widget.setHorizontalHeaderLabels(["name", "age"]) # Set header labels
        for ind, record in enumerate(self.records): # Set items in table widget
            self.table_widget.setItem(ind,0, QTableWidgetItem(record[1]))
            self.table_widget.setItem(ind,1, QTableWidgetItem(str(record[2])))

    def sort_records(self):
        """Method is triggered when value in any ComboBox is changed"""

        if self.sort_cb.currentText() != "":
            self.records = self.database.select(order_by=f'{self.sort_cb.currentText()} {self.order_method_cb.currentText()}')
            for ind, record in enumerate(self.records):
                self.table_widget.setItem(ind,0, QTableWidgetItem(record[1]))
                self.table_widget.setItem(ind,1, QTableWidgetItem(str(record[2])))

    def load_colors(self):
        """Method used to load all colors for widget"""
        
        self.load_menu_button_color()
        self.load_background_color()
        self.logger.logger.info("All view colors loaded.")

    def load_menu_button_color(self):
        """Method used to load menu button background and text color"""

        button_text_color_picker = ButtonTextColorPicker()
        text_color_setter = TextColorSetter(['white', 'black'], button_text_color_picker)
        button_text_color_picker.check_pick_condiditon(self.main_window.toml_data['settings']['primary_color'])
        button_color_setter = ButtonColorSetter(self.main_window.toml_data['settings']['primary_color'], text_color_setter)
        button_color_setter.set_color(self.menu_btn)
        self.logger.logger.info('Menu button color set.')
        
    def load_background_color(self):
        """Method used to load table background color"""

        background_color_setter = BackgroundColorSetter(self.main_window.toml_data['settings']['secondary_color'])
        background_color_setter.set_color(self.table_widget)
        self.logger.logger.info('Table background color set.')

    def load_text(self):
        """Method used to load widget text in chosen language"""
        
        text_setter = TextSetter(self.language)
        text_setter.set_title(self.main_window, 'Wszystkie transakcje')
        text_setter.set_text(self.menu_btn, "Wróć do menu")
        self.logger.logger.info('View text set.')