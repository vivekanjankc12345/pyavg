company = {
    'employees': {
        'John': {'age': 35, 'job_title': 'Manager'},
        'Emma': {'age': 28, 'job_title': 'Software Engineer'},
        'Kelly': {'age': 41, 'job_title': 'Senior Developer'},
        'Sam': {'age': 30, 'job_title': 'Software Engineer'},
        'Mark': {'age': 37, 'job_title': 'Senior Manager'},
        'Sara': {'age': 32, 'job_title': 'Software Engineer'},
    }
}

def averages(company):
    employees=[employee for employee,details in company['employees'].items() if details['job_title'].startswith("s")]
    if not employees:
        return 0
    totalage=sum(company["employees"][employees]['age'] for employees in employees) 
    average=totalage/len(employees)
    return average
averageage=averages(company)
print(averageage)   

