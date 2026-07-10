import json
from pathlib import Path


class SchoolAdmission:
    database = "school.json"
    data = []

    # Load data from file
    if Path(database).exists():
        with open(database, "r") as myfile:
            data = json.load(myfile)

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as myfile:
            json.dump(cls.data, myfile, indent=4)

    def add_school(self):
        school = {
            "school_name": input("Enter school name: "),
            "available_seats": int(input("Enter total seats: "))
        }

        SchoolAdmission.data.append(school)
        SchoolAdmission.__update()

        print("School added successfully!")

    def admission_seat(self):
        school_name = input("Enter school name: ")

        school = [
            i for i in SchoolAdmission.data
            if i["school_name"].lower() == school_name.lower()
        ]

        if not school:
            print("School not found!")
            return

        seats = int(input("How many seats do you want to admit? "))

        if seats > school[0]["available_seats"]:
            print("Not enough seats available!")
        else:
            school[0]["available_seats"] -= seats
            SchoolAdmission.__update()

            print(f"{seats} seat(s) admitted successfully!")

    def cancel_admission(self):
        school_name = input("Enter school name: ")

        school = [
            i for i in SchoolAdmission.data
            if i["school_name"].lower() == school_name.lower()
        ]

        if not school:
            print("School not found!")
            return

        seats = int(input("How many admissions cancel? "))

        school[0]["available_seats"] += seats
        SchoolAdmission.__update()

        print("Admission cancelled successfully!")

    def show_school(self):
        if not SchoolAdmission.data:
            print("No schools found!")
            return

        for school in SchoolAdmission.data:
            print("\nSchool Name:", school["school_name"])
            print("Available Seats:", school["available_seats"])


# Main Program
admission = SchoolAdmission()

while True:
    print("\n===== School Admission System =====")
    print("1. Add School")
    print("2. Admit Student")
    print("3. Cancel Admission")
    print("4. Show Schools")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        admission.add_school()

    elif choice == 2:
        admission.admission_seat()

    elif choice == 3:
        admission.cancel_admission()

    elif choice == 4:
        admission.show_school()

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")