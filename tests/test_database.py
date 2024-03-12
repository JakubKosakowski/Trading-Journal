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
    assert test_inst.select(conditions="id = 1") == [(1, 'Jakub', 24, 0)]
    with pytest.raises(psycopg2.errors.UndefinedColumn):
        test_inst.select(columns=['price'])
    with pytest.raises(psycopg2.errors.InFailedSqlTransaction):
        test_inst.select(conditions="age == 24")

def test_insert():
    test_inst = Database()
    assert test_inst.insert(table="test", values=["Krzysztof", 27, 21]) == 21
    # assert test_inst.insert(table="test", values=['Mateusz'])
    with pytest.raises(psycopg2.errors.SyntaxError):
        test_inst.insert(table="test", values=['Mateusz'])
        test_inst.insert(table="not_existed")
        test_inst.insert(table="not_existed", values=["Michal", 22, 12])

# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()