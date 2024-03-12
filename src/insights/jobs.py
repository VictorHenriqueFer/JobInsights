import csv
from typing import List


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, xx: str):
        with open(xx, 'r') as file:
            read_data = csv.DictReader(file)
            self.jobs_list = list(read_data)

    def get_unique_job_types(self) -> List[str]:
        jobs = set()
        for job_info in self.jobs_list:
            job_type = job_info.get('job_type')
            jobs.add(job_type)
        return jobs

    def filter_by_multiple_criteria(self, jobs, FCx) -> List[dict]:
        if not isinstance(jobs, list):
            raise TypeError('jobs must be a list')
        if not isinstance(FCx, dict):
            raise TypeError('criteria must be a dict')
        procura_trabalho = [
            job
            for job in jobs
            if all(job[key] == value for key, value in FCx.items())
        ]
        return procura_trabalho
