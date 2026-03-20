from aprovado1 import aprovado

def test1():
    assert aprovado(10, 80, 0) == 'Aprovado'

def test2():
    assert aprovado(7, 80, 80) == 'Reprovado por faltas'
def test3():
    assert aprovado(6, 80, 0) == 'Aprovado'
def test4():
    assert aprovado (6.1, 80, 0) == 'Aprovado'
def test5():
    assert aprovado (8, 80, 19) == 'Aprovado'
def test6():
    assert aprovado (6, 60, 79) == 'Reprovado por faltas'
def test7():
    assert aprovado (5, 60, 10) == 'Precisa fazer a prova final'

    