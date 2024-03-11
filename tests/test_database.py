import pytest
import psycopg2
from src.postgres_database import Database

# def f():
#     raise SystemExit(1)

def test_select():
    test_inst = Database()
    assert test_inst.select(columns=['age']) == [(24,), (28,), (32,)]
    assert test_inst.select(columns="name, age") == [('Jakub', 24,), ('Pawel', 28,), ('Michal', 32)]
    assert test_inst.select(columns="name age") == [('Jakub', 24,), ('Pawel', 28,), ('Michal', 32)]
    assert test_inst.select(conditions="id = 1") == [(1, 'Jakub', 24,)]
    with pytest.raises(psycopg2.errors.UndefinedColumn):
        test_inst.select(columns=['price'])
    with pytest.raises(psycopg2.errors.UndefinedFunction):
        test_inst.select(conditions="age == 24")

# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()