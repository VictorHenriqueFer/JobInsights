from src.pre_built.counter import count_ocurrences


def test_counter():
    'Retorna corretamente a contagem de ocorrências de uma palavra'
    assert count_ocurrences(path='data/jobs.csv', word='javascript') == 122
