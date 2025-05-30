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


person = YourName("Іван", "Петров", 2007)
print(person.calculate_course())
print(person.get_name_list())
