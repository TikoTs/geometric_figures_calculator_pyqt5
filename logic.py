# main_logic.py
import math
from PyQt5.QtWidgets import QMessageBox


def square(side):
    p = side * 4
    area = side ** 2
    return [area, p]


def trapezoid(base1, base2, side):
    p = base1 + base2 + side * 2
    packet = (base2 - base1) / 2
    height = math.sqrt(side ** 2 - packet ** 2)
    area = (base1 + base2) / 2 * height
    return [area, p]


class MainLogic:
    def __init__(self, ui):
        self.ui = ui

    # change events
    # setting calculate button state for each shapes
    def select_shape(self):
        return self.ui.shape_group.checkedButton().text()

    # circle
    def radius(self):
        return self.ui.radiusi.text()

    # triangle
    def triangle_side1(self):
        side1 = self.ui.samkutxedi_gverdi1.text()
        return side1

    def triangle_side2(self):
        side2 = self.ui.samkutxedi_gverdi2.text()
        return side2

    def triangle_side3(self):
        side3 = self.ui.samkutxedi_gverdi3.text()
        return side3

    def is_triangle(self, side1, side2, side3):
        return (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1)

    # square
    def square_size(self):
        return self.ui.kvadrati_sigrdze.text()

    # trapezoid
    def trapezoid_upper_length(self):
        return self.ui.zeda_fudze.text()

    def trapezoid_lower_length(self):
        return self.ui.qveda_fudze.text()

    def trapezoid_side_length(self):
        return self.ui.trapecia_ferdi.text()

    def calculate(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            return
        elif self.select_shape() == "სამკუთხედი":
            side1 = float(self.triangle_side1())
            side2 = float(self.triangle_side2())
            side3 = float(self.triangle_side3())
            if side1 == 0 or side2 == 0 or side3 == 0:
                warning_message = QMessageBox()
                warning_message.setIcon(QMessageBox.Warning)
                warning_message.setText("გვერდი უდრის 0-ს")
                warning_message.setWindowTitle("Warning")
                warning_message.exec_()
            elif self.is_triangle(side1, side2, side3) == False:
                warning_message = QMessageBox()
                warning_message.setIcon(QMessageBox.Warning)
                warning_message.setText("ნებისმიერი 2 გვერდის ჯამი უნდა აღემატებოდეს მესამეს")
                warning_message.setWindowTitle("Warning")
                warning_message.exec_()
            else:
                p = side1 + side2 + side3
                area = pow(p / 2 * (p / 2 - side1) * (p / 2 - side2) * (p / 2 - side3), 1 / 2)
                self.ui.samkutxedi_perimeter.display(p)
                self.ui.samkutxedi_fartobi.display(area)
        elif self.select_shape() == "წრე":
            r = float(self.radius())
            if r == 0:
                warning_message = QMessageBox()
                warning_message.setIcon(QMessageBox.Warning)
                warning_message.setText("რადიუსი უდრის 0-ს")
                warning_message.setWindowTitle("Warning")
                warning_message.exec_()
            else:
                length = 2 * r
                area = r ** 2
                if int(length) == length:
                    length = int(length)
                if int(area) == area:
                    area = int(area)
                length = str(length) + 'π'
                area = str(area) + 'π'
                self.ui.wre_fartobi.display(area)
                self.ui.wre_sigrdze.display(length)
        elif self.select_shape() == "კვადრატი":
            length = float(self.square_size())
            if length == 0:
                warning_message = QMessageBox()
                warning_message.setIcon(QMessageBox.Warning)
                warning_message.setText("გვერდი უდრის 0-ს")
                warning_message.setWindowTitle("Warning")
                warning_message.exec_()
            else:
                p = length * 4
                area = length ** 2
                self.ui.kvadrati_area_3.display(area)
                self.ui.kvadrati_area_2.display(p)
        elif self.select_shape() == "ტოლფერდა ტრაპეცია":
            upper_length = float(self.trapezoid_upper_length())
            lower_length = float(self.trapezoid_lower_length())
            side = float(self.trapezoid_side_length())
            if lower_length == 0 or side == 0 or upper_length == 0:
                warning_message = QMessageBox()
                warning_message.setIcon(QMessageBox.Warning)
                warning_message.setText("გვერდი უდრის 0-ს")
                warning_message.setWindowTitle("Warning")
                warning_message.exec_()
            elif lower_length < upper_length:
                warning_message = QMessageBox()
                warning_message.setIcon(QMessageBox.Warning)
                warning_message.setText("დიდი ფუძე უფრო მეტი უნდა იყოს, ვიდრე პატარა")
                warning_message.setWindowTitle("Warning")
                warning_message.exec_()
            else:
                trapezoid_base_part = (lower_length - upper_length) // 2
                trapezoid_height = (side ** 2 - trapezoid_base_part ** 2) ** (1 / 2)
                area = (upper_length + lower_length) / 2 * trapezoid_height
                p = upper_length + lower_length + side * 2
                self.ui.trapeci_area.display(area)
                self.ui.trapecia_perimeter.display(p)
