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
    namerdos = {}
    for autores in publicacoes:
        if 'erdos' in autores:
            namerdos['erdos'] = 0

    return namerdos


def test_erdos_sozinho():
    publicacoes = [['erdos']]
    assert erdos(publicacoes) == {'erdos': 0}