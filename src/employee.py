import csv


class Employee(object):
    __slots__ = ["name", "age", "job", "salary"]

    def __init__(self, name, age, job, salary):
        self.job = job
        self.name = name
        self.age = age
        self.salary = salary

    def profile(self):
        for attr in self.__slots__:
            print(f"{attr.capitalize()}: {getattr(self, attr)}")


def from_csv_file(file_path):
    with open(file_path) as file:
        reader = csv.DictReader(file)
        employees = []
        for row in reader:
            employees.append(
                Employee(
                    name=row["name"],
                    age=int(row["age"]),
                    job=row["job"],
                    salary=float(row["salary"]),
                )
            )
        return employees
