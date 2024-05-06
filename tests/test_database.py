import pytest
import psycopg2
from src.postgres_database import Database

# def f():
#     raise SystemExit(1)

def test_select(caplog):
    test_inst = Database()
    assert test_inst.select(columns=['age']) == [(24,), (28,), (32,)]
    assert test_inst.select(columns="name, age") == [('Jakub', 24,), ('Pawel', 28,), ('Michal', 32)]
    assert test_inst.select(columns="name age") == [('Jakub', 24,), ('Pawel', 28,), ('Michal', 32)]
    assert test_inst.select(conditions="id = 1") == [(1, 'Jakub', 24, 0)]
    
    test_inst.select(columns=['price'])
    assert 'An error occurred: column "price" does not exist' in caplog.records[0].msg
    
    test_inst.select(conditions="age == 24")
    assert 'An error occurred: operator does not exist: integer == integer' in caplog.records[1].msg

def test_insert(caplog):
    test_inst = Database()
    assert test_inst.insert(table="test", values=["Krzysztof", 27, 21]) == 21

    test_inst.insert(table="test", values=['Mateusz'])
    assert 'An error occurred: syntax error at or near ")"' in caplog.records[0].msg


def test_update(caplog):
    test_inst = Database()
    assert test_inst.update(table="test", ident_column="id" , ident_value="1", columns=["age"], new_values=[21]) == 21
    assert test_inst.update(table="test", ident_column="id" , ident_value="2", columns=["name", "age"], new_values=["Bozydar", 45]) == "Bozydar"
    
    test_inst.update(table="not_existed")
    assert 'An error occurred: One of parameters is None!' in caplog.records[0].msg

    test_inst.update(table="test", ident_column="id", ident_value="10", columns=["name"], new_values=["Czeslaw"])
    assert "An error occurred: 'NoneType' object is not subscriptable" in caplog.records[1].msg
    # test_inst.update(table="test", ident_column="id", ident_value="2", columns=["price"], new_values=[12])
    # test_inst.update(table="test", ident_column="id", ident_value="2", columns=["name"], new_valuse=[12])


def test_delete(caplog):
    test_inst = Database()
    assert test_inst.delete(table="test", condition="id = 1") == 1


    test_inst.delete()
    assert 'An error occurred: One of parameters is None!' in caplog.records[0].msg

    test_inst.delete(table="test")
    assert 'An error occurred: One of parameters is None!' in caplog.records[1].msg

    test_inst.delete(condition="id = 2")
    assert 'An error occurred: One of parameters is None!' in caplog.records[2].msg

    # test_inst.delete(table="test", condition="id = 21")
    # test_inst.delete(table="not_existed", condition="id = 2")
    

# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()