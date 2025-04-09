class Staff:
    def __init__(self, name, initial_grade):
        self.name = name
        self.grade = initial_grade

    def tardy(self):
        self.grade -= 3
        print(f'{self.name} was tardy. New grade: {self.grade}')

    def absent(self):
        self.grade -= 10
        print(f'{self.name} was absent. New grade: {self.grade}')

    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"{self.name}'s grade updated. New grade: {self.grade}")


def main():
    Staffs = [
        Staff("Evan", 100),
        Staff('Maddie', 97),
        Staff("Eddie", 95),
        Staff("Andrew", 90),
        Staff('Gregory', 86),
        Staff("Jake", 85),
        Staff("Kyle", 70),
        Staff("Kieran", 65)
    ]
    for staff in Staffs:
        status = input(f"Enter the attendance status for {staff.name} (tardy/absent/present): ").strip().lower()
        if status == 'tardy':
            staff.tardy()
        elif status == 'absent':
            staff.absent()
        elif status == 'present':
            print(f'{staff.name} is present. No changes to grade.')
        else:
            print("Invalid status")

        update = input(f"Do you want to make any additional alterations to the grade of {staff.name}? (yes/no): ").strip().lower()
        if update == 'yes':
            change = float(input(f"Enter the amount to change the grade for {staff.name}(positive or negative): "))
            staff.update_grade(change)

    print("\nFinal grades: ")
    for staff in Staffs:
        print(f"{staff.name}: {staff.grade}")


if __name__ == '__main__':
    main()
