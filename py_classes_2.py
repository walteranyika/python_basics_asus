from datetime import datetime, date


class Person:
    def __init__(self, name, email, dob, gender, favourite_teams):
        self.name = name
        self.email = email
        self.dob = dob
        self.gender = gender
        self.teams = favourite_teams

    def print_details(self):
        print(self.name)
        print(self.gender)
        print(self.email)
        print("-----TEAMS-----")
        for team in self.teams:
            print(team)
        print("----------------")
        # "10-09-2001"

    def calc_age(self):
        today = datetime.now()
        dob = datetime.strptime(self.dob, "%d-%m-%Y")
        delta = today - dob
        print(delta.days // 365, "Years Old")


p1 = Person("June", "june@test.com", "03-09-1999", "Female", ["Newcastle", "Girona"])
p1.print_details()
p1.calc_age()