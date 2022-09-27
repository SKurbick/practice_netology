from application.db.people import get_employees
from application.salary import calculate_salary
import datetime

now = datetime.datetime.now()
if __name__ == '__main__':
    print(str(now.date()))
    get_employees()
    calculate_salary()

