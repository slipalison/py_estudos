import pytest
from cliente import Cliente

def test_cliente_valido():
    c = Cliente(1, "Ana")
    c.validar()

def test_cliente_sem_nome():
    with pytest.raises(ValueError):
        Cliente(1, "").validar()