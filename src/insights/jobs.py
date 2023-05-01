from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')

        all_jobs = []
        for job in jobs_reader:
            all_jobs.append(job)

    return all_jobs


def get_unique_job_types(path: str) -> List[str]:
    jobs_data = read(path)

    all_job_types = []
    for type in jobs_data:
        row = type["job_type"]
        if row not in all_job_types:
            all_job_types.append(type["job_type"])

    return all_job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs
