import pytest
import operacions

def test_suma_cero():
  assert operacions.suma_enteros(0,0) == 0


def test_suma_positivos():
  assert operacions.suma_enteros(5,5) == 10


def test_suma_positivos_negativos():
  assert operacions.suma_enteros(-5,5) == 0


def test_suma_nagativo():
  assert operacions.suma_enteros(-5,-5) == -10


def test_suma_excepcion_sumando1():
   with pytest.raises(TypeError):
       operacions.suma_enteros(5.0,5) == 0


def test_suma_excepcion_sumando2():
   with pytest.raises(TypeError):
       operacions.suma_enteros(5.0,'a') == 0


def test_suma_excepcion_sumandos():
   with pytest.raises(TypeError):
       operacions.suma_enteros(True,'a') == 0