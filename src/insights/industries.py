from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    all_jobs = read(path)

    all_industries = []

    for industry in all_jobs:
        row = industry["industry"]
        if row not in all_industries:
            if row != "":
                all_industries.append(row)

    return all_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_jobs = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_jobs.append(job)
    return filtered_jobs
