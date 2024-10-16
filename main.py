import sys
import io

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Файловая статистика</string>
  </property>
  <widget class="QLineEdit" name="filenameEdit">
   <property name="geometry">
    <rect>
     <x>90</x>
     <y>20</y>
     <width>171</width>
     <height>20</height>
    </rect>
   </property>
  </widget>
  <widget class="QPushButton" name="button">
   <property name="geometry">
    <rect>
     <x>300</x>
     <y>20</y>
     <width>75</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Рассчитать</string>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>20</y>
     <width>61</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>Имя файла</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_2">
   <property name="enabled">
    <bool>true</bool>
   </property>
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>80</y>
     <width>86</width>
     <height>32</height>
    </rect>
   </property>
   <property name="sizePolicy">
    <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
     <horstretch>0</horstretch>
     <verstretch>0</verstretch>
    </sizepolicy>
   </property>
   <property name="focusPolicy">
    <enum>Qt::WheelFocus</enum>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Максимальное&lt;br&gt;значение&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_3">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>140</y>
     <width>81</width>
     <height>32</height>
    </rect>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Минимальное&lt;br&gt;значение:&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
   <property name="indent">
    <number>-1</number>
   </property>
  </widget>
  <widget class="QLabel" name="label_4">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>200</y>
     <width>55</width>
     <height>32</height>
    </rect>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;
    Среднее&lt;br/&gt; значение&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="maxEdit">
   <property name="geometry">
    <rect>
     <x>140</x>
     <y>90</y>
     <width>113</width>
     <height>22</height>
    </rect>
   </property>
   <property name="readOnly">
    <bool>true</bool>
   </property>
  </widget>
  <widget class="QLineEdit" name="minEdit">
   <property name="geometry">
    <rect>
     <x>140</x>
     <y>150</y>
     <width>113</width>
     <height>22</height>
    </rect>
   </property>
   <property name="readOnly">
    <bool>true</bool>
   </property>
  </widget>
  <widget class="QLineEdit" name="avgEdit">
   <property name="geometry">
    <rect>
     <x>140</x>
     <y>200</y>
     <width>113</width>
     <height>22</height>
    </rect>
   </property>
   <property name="readOnly">
    <bool>true</bool>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui> """


class FileStat(QMainWindow):
    def __init__(self):
        super().__init__()
        ff = io.StringIO(template)
        uic.loadUi(ff, self)
        self.button.clicked.connect(self.run)
        self.status_bar = self.statusBar()

    def run(self):
        txt = self.filenameEdit.text()
        try:
            with open(txt, 'r', encoding='utf-8') as f:
                try:
                    data = f.read()
                    data = data.replace(r"\t", "")
                    data = data.replace(r"\n", "")
                    data = ' '.join(data.split())
                    data = list(map(int, data.split()))
                except ValueError:
                    self.status_bar.showMessage('Файл содержит некорректные данные')
                else:
                    try:
                        maxx = str(max(data))
                        minn = str(min(data))
                        avgg = str("{:.2f}".format(sum(data) / len(data)))
                        self.maxEdit.setText(maxx)
                        self.minEdit.setText(minn)
                        self.avgEdit.setText(avgg)
                    except ValueError:
                        self.status_bar.showMessage('Указанный файл пуст')
        except FileNotFoundError:
            self.status_bar.showMessage('Указанный файл не существует')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    a = FileStat()
    a.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
