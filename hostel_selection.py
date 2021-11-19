class Student:
    # def __init__(self, name, year_of_study, dist_to_home, cgpa, reservation_status):
    #     self.name = name
    #     self.year_of_study = year_of_study
    #     self.dist_to_home = dist_to_home
    #     self.cgpa = cgpa
    #     self.reservation_status = reservation_status

    def hostel_checker(self, name, year_of_study, dist_to_home, cgpa, reservation_status):
        dist_score = dist_to_home/30
        year_score = year_of_study*1.25
        final_score = cgpa+dist_score+year_score
        if(reservation_status == "y"):
            final_score = final_score + 5
        if(final_score >= 20):
            print("You are eligible to hostel")
        else:
            print("You are not eligible to hostel")


name = str(input("Enter student name: "))
year_of_study = int(input("Enter year of study(1/2/3/4): "))
dist_to_home = int(input("Enter distance to home: "))
cgpa = float(input("Enter cgpa: "))
reservation_status = str(input("Enter reservation status(y/n): "))

s = Student()
s.hostel_checker(name, year_of_study, dist_to_home, cgpa, reservation_status)
