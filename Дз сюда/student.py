class Student:

    name = ""
    birth_year = 2000
    group = ""
    gpa = 10

    def __init__(self, name="Anonim", birth_year=2000, group="###", gpa=10):
        self.name = name
        self.birth_year = birth_year
        self.group = group
        self.gpa = gpa

    def __str__(self):
        return \
            f"Name: {self.name}\n" \
            f"Birth year: {self.birth_year}\n" \
            f"Group: {self.group}\n" \
            f"GPA: {self.gpa}\n"

    def get_age(self):
        import datetime
        this_year = datetime.date.today().year
        age = this_year - self.birth_year
        print("Age:", age)

