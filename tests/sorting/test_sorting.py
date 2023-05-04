from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    def test_sort_by_min_salary():
        jobs = [
            {
                "title": "job1",
                "min_salary": 5000,
                "max_salary": 7000,
                "date_posted": "2023-04-21"
            },
            {
                "title": "job2",
                "min_salary": 7500,
                "max_salary": 8000,
                "date_posted": "2023-04-29"
            },
            {
                "title": "job3",
            },
        ]
        sort_by(jobs, "min_salary")
        assert jobs == [
            {
                "title": "job1",
                "min_salary": 5000,
                "max_salary": 7000,
                "date_posted": "2023-04-21"
            },
            {
                "title": "job2",
                "min_salary": 7500,
                "max_salary": 8000,
                "date_posted": "2023-04-29"
            },
            {
                "title": "job3",
            },
        ]
        pass
    pass
