class YourName:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def calculate_course(self, current_year=2025):
        if self.birth_year:
            age = current_year - self.birth_year
            if age < 15 or self.birth_year == 2005:
                return None
            return min(max(1, age - 15), 4)
        return None

    def get_name_list(self):
        return [self.first_name, self.last_name] if self.first_name and self.last_name else []


class Student(YourName):
    def __init__(self, first_name=None, last_name=None, birth_year=None, student_id=None, specialty=None,
                 average_grade=None):
        super().__init__(first_name, last_name, birth_year)
        self.student_id = student_id
        self.specialty = specialty
        self.average_grade = average_grade
        self._scholarship = self.__calculate_scholarship()

    def __calculate_scholarship(self):
        return self.average_grade >= 8 if self.average_grade is not None else False

    def get_scholarship_status(self):
        return "Отримує стипендію" if self._scholarship else "Не отримує стипендію"

    def student_info(self):
        return {
            "Ім'я": self.first_name,
            "Прізвище": self.last_name,
            "Рік народження": self.birth_year,
            "ID студента": self.student_id,
            "Спеціальність": self.specialty,
            "Середній бал": self.average_grade
        }


student = Student("Іван", "Петров", 2005, "12345", "Інформатика", 8.5)
print(student.calculate_course())
print(student.get_name_list())
print(student.get_scholarship_status())
print(student.student_info())
