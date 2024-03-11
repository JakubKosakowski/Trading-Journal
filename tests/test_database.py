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
    with pytest.raises(psycopg2.errors.UndefinedColumn):
        test_inst.select(columns=['price'])

# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()