from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def __get_salaries(self, st) -> Union[int, str]:
        recibo = [
            float(job.get(st))
            for job in self.jobs_list
            if job.get(st).isdigit()
        ]
        return recibo

    def get_max_salary(self) -> int:
        recebo = self.__get_salaries("max_salary")
        return max(recebo, default=0)

    def get_min_salary(self) -> int:
        recebo = self.__get_salaries("min_salary")
        return min(recebo, default=0)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        maximo = job.get("max_salary")
        minimo = job.get("min_salary")
        if maximo is None or minimo is None:
            raise ValueError("salary range is not specified")
        try:
            minimo = int(minimo)
            maximo = int(maximo)
            salary = int(salary)
        except (ValueError, TypeError):
            raise ValueError("salary is not a number")
        if maximo < minimo:
            raise ValueError("minimum salary is greater than maximum salary")
        return maximo >= salary >= minimo

    def try_matches_salary_range(
        self, trabalho: Dict, sa: Union[int, str]
    ) -> bool:
        try:
            return self.matches_salary_range(trabalho, sa)
        except ValueError:
            return False

    def filter_by_salary_range(
        self, trabalhos: List[dict], sa: Union[str, int]
    ) -> List[Dict]:
        return [
            job for job in trabalhos if self.try_matches_salary_range(job, sa)
        ]
