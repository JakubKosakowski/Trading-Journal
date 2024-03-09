from src.postgres_database import Database

def test_select():
    test_inst = Database()
    assert test_inst.select(columns=['age']) == [(24,), (28,), (32,)]