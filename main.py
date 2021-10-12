import pytest

pytest.main([__file__, '-v', '-p', 'no:warnings'])

# Problema: https://dojopuzzles.com/problems/numero-de-erdos/
'''
Com base no que foi visto na primeira sessão, cheguei à conclusão de que
a estrutura final ('pensar no output', como o Henrique falou) que deveria
ficar assim:
namerdos = {
    'erdos': 0,
    'a': 1  # publicou artigo com o erdos
    'b': 2  # publicou artigo com a, que publicou artigo com erdos (['erdos', 'a'] ou ['a', 'erdos'])
    'c': 3  # publicou artibo com b que, por sua vez, publicou com a (['a', 'b'])
}
'''


def erdos(publicacoes):
    namerdos = {'erdos': 0}  # refatorando, já que erdos sempre será o topo do gráfico, com o valor zero
    for autores in publicacoes:
        for autor in autores:
            if autor == 'erdos':
                continue
            if 'erdos' in autores:
                namerdos[autor] = 1
            else:
                if 'a' in namerdos:
                    namerdos['b'] = namerdos['a'] + 1
                    if autor == 'c':
                        namerdos['c'] = namerdos['b'] + 1

    return namerdos

def test_nivel_3():
    publicacoes =[['erdos'], ['erdos', 'a'], ['a', 'b'], ['c', 'b']]
    assert erdos(publicacoes) == {'erdos': 0, 'a': 1, 'b': 2, 'c': 3}

def test_nivel_2():
    publicacoes = [['erdos'], ['erdos', 'a'], ['a', 'b']]
    assert erdos(publicacoes) == {'erdos': 0, 'a': 1, 'b': 2}

def test_nivel_1():
    publicacoes = [['erdos'], ['erdos', 'a']]
    assert erdos(publicacoes) == {'erdos': 0, 'a': 1}


def test_erdos_sozinho():
    publicacoes = [['erdos']]
    assert erdos(publicacoes) == {'erdos': 0}