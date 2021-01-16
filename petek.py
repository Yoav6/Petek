import sys
from SQLper import *
#from PyQt5 import uic
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from stylesheet import styleSheet
from main_window import Ui_MainWindow
from homepage_layout import Ui_homepage_layout
from tab_window import Ui_TabWindow
from add_person import Ui_add_person_popup

print('finished importing\nInitiating app...')

def set_search_box(parent):
    parent.addWidget(searchbox.search_box)

def open_add_person_popup(first_name='', last_name='', parent=None):
    popup = addPersonPopup(parent)
    popup.show()
    if parent:
        popup.ui.type_cbox.setCurrentIndex(1)
    if first_name:
        popup.ui.first_name_field.setText(first_name)
    if last_name:
        popup.ui.last_name_field.setText(last_name)
    popup.exec()

def check_name_and_add_person(first_name, last_name, **kwargs):
    instances = check_if_name_exists(first_name, last_name)
    print(3)
    if instances:
        full_name = first_name + ' ' + last_name
        messagebox = \
            qtw.QMessageBox.question(None, 'נמצא אדם נוסף במערכת עם אותו השם',
                                 f'נמצאו {len(instances)} מופעים של השם {full_name}. האם להוסיף אדם נוסף עם אותו השם?'
                                 f'', qtw.QMessageBox.No | qtw.QMessageBox.Yes, qtw.QMessageBox.Yes)
        print(4)
        if messagebox == qtw.QMessageBox.Yes:
            instances = False
    if not instances:
        print(4)
        return insert_row_to_table('people', first_name=first_name, last_name=last_name, **kwargs)

def split_full_name(name: str):
    try:
        first_name, last_name = name.split(' ', 1)
    except:
        first_name, last_name = name, ''
    return first_name, last_name

class appWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.setCentralWidget(homepage)
        #homepage.setParent(self.ui.window_frame)
        self.home_btn = qtw.QAction(qtg.QIcon('home_btn.png'), 'דף בית', self)
        self.ui.toolBar.addAction(self.home_btn)
        self.home_btn.triggered.connect(self.go_to_home_page)
        self.setStyleSheet(stylesheet.stylesheet)

    def go_to_home_page(self):
        print(homepage)
        self.setCentralWidget(homepage)

class searchBox(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.search_box = qtw.QComboBox(self)
        self.search_box.setObjectName('search_box')
        size_policy = qtw.QSizePolicy(qtw.QSizePolicy.Preferred, qtw.QSizePolicy.Preferred)
        self.search_box.setSizePolicy(size_policy)
        self.list = [""]
        self.edit = qtw.QLineEdit(self)
        self.search_box.setLineEdit(self.edit)
        self.line = self.search_box.lineEdit()
        self.edit.setPlaceholderText('חיפוש')
        self.search_box.setLayoutDirection(qtc.Qt.RightToLeft)
        #self.line.setFocusPolicy(qtc.Qt.StrongFocus)
        self.search_box.setInsertPolicy(self.search_box.NoInsert)
        self.search_box.completer().setCompletionMode(qtw.QCompleter.PopupCompletion)
        #self.search_box.currentIndexChanged.connect(self.match_id)

    def match_id(self):
        index = self.search_box.currentIndex()
        if index:
            id_ = self.id_list[index - 1]
            return id_

    def add_items(self, item_list):
        def sort_first(val):
            return val[0]
        item_list.sort(key=sort_first)
        item_list, self.id_list = map(list, zip(*item_list))  # splits list of tuples into 2 lists
        self.item_list = self.list + item_list
        self.search_box.addItems(self.item_list)

    def set_list(self, func):
        person_list = func()
        self.add_items(person_list)


class homepage_layout(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_homepage_layout()
        self.ui.setupUi(self)
        self.ui.searchbox_container.addWidget(searchbox.search_box)
        searchbox.set_list(get_all_people)
        searchbox.search_box.currentIndexChanged.connect(self.search_item_selected)
        self.ui.new_person_btn.clicked.connect(open_add_person_popup)

    def search_item_selected(self):
        id_ = searchbox.match_id()
        if id_:
            name = searchbox.edit.text()
            searchbox.search_box.clearFocus()
            searchbox.search_box.clearEditText()
            searchbox.search_box.setEditText('')
            searchbox.search_box.setCurrentIndex(0)
            window.setCentralWidget(profile_page_layout)
            set_search_box(profile_page_layout.ui.searchbox_container)
            profile_page_layout.add_tab(id_, name)

class profilePageLayout(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TabWindow()
        self.ui.setupUi(self)
        self.open_tabs = []  # IDs
        searchbox.search_box.currentIndexChanged.connect(self.search_item_selected)
        self.ui.tab_widget.tabCloseRequested.connect(self.close_tab)

    def add_tab(self, id_, title):
        print('id: ', id_)  # gets full name using id_
        self.open_tabs.append(id_)
        print(self.open_tabs)
        tab = qtw.QWidget()
        tab.setObjectName(str(id_))
        self.ui.tab_widget.addTab(tab, title)
        self.ui.tab_widget.setCurrentWidget(tab)
        #setting tab layout
        tab.setContentsMargins(0, 5, 0, 0)
        tab.setLayout(qtw.QGridLayout())
        tab.font().setPointSize(10)
        #setup inner tab
        inner_tab_widget = qtw.QTabWidget()
        inner_tab_widget.setParent(tab)
        inner_tab = qtw.QWidget()
        inner_tab_widget.addTab(inner_tab, 'ראשי')
        inner_tab_widget.setTabBarAutoHide(False)
        self.setup_profile(inner_tab_widget, id_)
        tab = inner_tab_widget = inner_tab = None

    def setup_profile(self, tab_widget, id_):
        #tab = qtw.QWidget()
        #tab_widget.addTab(tab, 'ראשי')
        print(tab_widget, '| id: ', id_)


    def search_item_selected(self):
        id_ = searchbox.match_id()
        if id_:
            if id_ not in self.open_tabs:
                name = searchbox.edit.text()
                self.add_tab(id_, name)
            else:
                target_tab = self.ui.tab_widget.findChild(qtw.QWidget, str(id_))
                self.ui.tab_widget.setCurrentWidget(target_tab)
            searchbox.search_box.clearFocus()
            searchbox.search_box.clearEditText()
            searchbox.search_box.setCurrentIndex(0)


    def close_tab(self, tab_index):
        tab_object = self.ui.tab_widget.widget(tab_index)
        id_ = tab_object.objectName()
        #print('id: ', id_)
        self.open_tabs.remove(int(id_))
        #print(self.open_tabs)
        self.ui.tab_widget.removeTab(tab_index)

class addPersonPopup(qtw.QDialog):  # , qtc.Qt
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_add_person_popup()
        self.ui.setupUi(self)
        #self.AA_DisableWindowContextHelpButton(True)
        self.mode = 'student'
        self.set_type()
        plus_icon = qtg.QIcon()
        plus_icon.addPixmap(qtg.QPixmap('plus_btn.png'))
        self.ui.new_mentor_btn.setIcon(plus_icon)
        self.ui.new_mentor_btn.clicked.connect(self.new_mentor)
        self.ui.ok_btn.clicked.connect(self.ok)
        self.ui.cancel_btn.clicked.connect(self.cancel)
        self.ui.type_cbox.currentIndexChanged.connect(self.set_type)
        """self.phone_field = qtw.QLineEdit()
        self.phone_field.setParent(self.ui.mentor_cbox_container)"""
        if parent:
            self.ui.type_cbox.setDisabled(True)
        self.mentor_field = searchBox()
        self.mentor_field.search_box.setParent(self.ui.mentor_cbox_container)
        self.mentor_field.set_list(get_all_staff)
        # self.mentor_field.search_box.setSizePolicy(
        # qtw.QSizePolicy(qtw.QSizePolicy.Preferred, qtw.QSizePolicy.Preferred))
        self.mentor_field.edit.setPlaceholderText('')

    def set_type(self):
        if self.ui.type_cbox.currentIndex() == 0:
            self.mode = 'student'
            self.ui.mentor_label.setText('חונך')
            self.ui.new_mentor_btn.setDisabled(False)
            self.ui.mentor_label.setDisabled(False)
            self.ui.mentor_field.setDisabled(False)
        elif self.ui.type_cbox.currentIndex() == 1:
            self.mode = 'staff'
            self.mentor_field = qtw.QLineEdit()
            self.mentor_field.setParent(self.ui.mentor_cbox_container)
            self.ui.mentor_label.setText('טלפון')
            self.ui.mentor_field.setDisabled(False)
            self.ui.new_mentor_btn.setDisabled(True)
            self.ui.mentor_label.setDisabled(False)
        else:
            self.mode = 'other'
            self.ui.mentor_label.setText('חונך')
            self.ui.mentor_label.setDisabled(True)
            self.ui.mentor_field.setDisabled(True)
            self.ui.new_mentor_btn.setDisabled(True)

    def ok(self):
        first_name = self.ui.first_name_field.text()
        last_name = self.ui.last_name_field.text()
        if self.mode == 'student':
            if self.mentor_field.search_box.currentIndex() != 0:
                mentor_id = self.mentor_field.match_id()
                student_id = check_name_and_add_person(first_name, last_name, student=1, current_mentor=mentor_id)
                if student_id:
                    add_student_mentor_relation(student_id, mentor_id)
            else:
                pass  # announce it
        elif self.mode == 'staff':
            check_name_and_add_person(first_name, last_name, staff=1, phone=self.mentor_field.edit.text())
        else:
            check_name_and_add_person(first_name, last_name)

    def cancel(self):
        self.close()

    def new_mentor(self):
        first_name, last_name = split_full_name(self.mentor_field.edit.text())
        open_add_person_popup(first_name=first_name, last_name=last_name, parent=self)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    stylesheet = styleSheet()
    searchbox = searchBox()
    homepage = homepage_layout()
    print('building main window...')
    window = appWindow()
    window.setCentralWidget(homepage)
    print('loading main window...')
    window.showMaximized()
    profile_page_layout = profilePageLayout()
    socket_main_thread = threading.Thread(target=activate_socket, daemon=True)
    socket_main_thread.start()
    app.exec()
    conn.close()
    sys.exit()
