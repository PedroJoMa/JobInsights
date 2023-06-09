from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    all_jobs = read(path)

    salaries = set()

    for salary in all_jobs:
        row = salary["max_salary"]
        if row.isnumeric():
            salaries.add(int(row))

    return max(salaries)


def get_min_salary(path: str) -> int:
    all_jobs = read(path)

    salaries = set()

    for salary in all_jobs:
        row = salary["min_salary"]
        if row.isnumeric():
            salaries.add(int(row))
    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        max_salary = int(job["max_salary"])
        min_salary = int(job["min_salary"])
        value = int(salary)
    except (TypeError, KeyError, ValueError):
        raise ValueError
    if min_salary > max_salary:
        raise ValueError
    return value in range(min_salary, max_salary + 1)


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    valid_jobs = []
    for j in jobs:
        try:
            if matches_salary_range(j, salary):
                valid_jobs.append(j)
        except ValueError:
            ValueError
    return valid_jobs
