# 1491. Average Salary Excluding the Minimum and Maximum Salary

def average(1salaries):
    """
    :type salary: List[int]
    :rtype: float
    """
    maximum_salary = salaries[0]
    minimum_salary = salaries[0]
    sum = 0
    for salary in salaries:
        sum += salary
        if salary >= maximum_salary:
            maximum_salary = salary
        if salary <= minimum_salary:
            minimum_salary = salary
    sum -= (minimum_salary + maximum_salary)
    
    return sum / (len(salaries) - 2)