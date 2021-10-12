import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])

"""
  e a b c d f
e   T 
a T   T     T
b   T   T
c     T
d
f   T

d['e'] = ['a']
d['a'] = ['e', 'b', 'f']
d['b'] = ['a', 'c']
d['c'] = ['b']
d['d'] = []
d['f'] = ['a']

p['e'] = 0
p['a'] = 1
p['b'] = 2
p['c'] = 3
p['f'] = 2

p['d'] = inf
"""


def erdos(publicacoes):
    d = {}

    for p in publicacoes:
        for autor in p:
            if autor not in d:
                d[autor] = []
                p2 = p[:]
                d[autor] = p2.remove(autor)

    d2 = {}

    d2['erdos'] = 0
    
    for coautor in d['erdos']:
        if not coautor in d2:
            d2[coautor] += 1

    return d

def test_3():
    publicacoes = [['erdos', 'a'], ['a', 'b'], ['a', 'f'], ['c', 'b'],['d']]
    assert erdos(publicacoes) == {'erdos': 0, 'a': 1, 'b': 2, 'c': 3}

def test_():
    publicacoes = [['erdos', 'a'], ['a', 'b']]
    assert erdos(publicacoes) == {'erdos': 0, 'a': 1, 'b': 2}

def test_a_erdos():
    publicacoes = [['a', 'erdos']]
    assert erdos(publicacoes) == {'erdos': 0, 'a': 1}

def test_erdos_a():
    publicacoes = [['erdos', 'a']]
    assert erdos(publicacoes) == {'erdos': 0, 'a': 1}

def test_erdos():
    publicacoes = [['erdos']]
    assert erdos(publicacoes) == {'erdos': 0}



# Problema: https://dojopuzzles.com/problems/numero-de-erdos/

# -> repl.it: https://replit.com/join/jkuyxwujar-claudioberrondo 

"""
FILA:
Vinícius Bôscoa
Maurício Fagundes
Cláudio Berrondo
Cássio Augusto
Wesley Mendes
Henrique Bastos

"""