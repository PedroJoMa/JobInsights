from src.pre_built.brazilian_jobs import read_brazilian_file

mock = {'title': 'Maquinista', 'salary': '2000', 'type': 'trainee'}


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"
    assert read_brazilian_file(path)[0] == mock
    pass
