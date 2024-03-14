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
        test_inst.select(table="not_existed")     

def test_insert():
    test_inst = Database()
    assert test_inst.insert(table="test", values=["Krzysztof", 27, 21]) == 21
    # assert test_inst.insert(table="test", values=['Mateusz'])
    with pytest.raises(psycopg2.errors.SyntaxError):
        test_inst.insert(table="test", values=['Mateusz'])
        test_inst.insert(table="not_existed")
        test_inst.insert(table="not_existed", values=["Michal", 22, 12])

def test_update():
    test_inst = Database()
    assert test_inst.update(table="test", ident_column="id" , ident_value="1", columns=["age"], new_values=[21]) == 21
    assert test_inst.update(table="test", ident_column="id" , ident_value="2", columns=["name", "age"], new_values=["Bozydar", 45]) == "Bozydar"
    with pytest.raises(TypeError):
        test_inst.update(table="not_existed")
    with pytest.raises(psycopg2.errors.SyntaxError):
        test_inst.update(table="test", ident_column="id", ident_value="10", columns=["name"], new_values=["Czeslaw"])
    #     test_inst.update(table="test", ident_column="id", ident_value="2", columns=["price"], new_values=[12])
    #     test_inst.update(table="test", ident_column="id", ident_value="2", columns=["name"], new_valuse=[12])

def test_delete():
    test_inst = Database()
    assert test_inst.delete(table="test", condition="id = 1") == 1
    with pytest.raises(TypeError):
        test_inst.delete()
        test_inst.delete(table="test")
        test_inst.delete(condition="id = 2")
        test_inst.delete(table="test", condition="id = 21")
    with pytest.raises(psycopg2.errors.UndefinedTable):
        test_inst.delete(table="not_existed", condition="id = 2")
    

# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()