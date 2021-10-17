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
        for pos, autor in enumerate(autores):  # iteramos os autores de cada publicação
            if autor == 'erdos':
                continue  # erdos já está no dicionário
            if 'erdos' in autores:
                namerdos[autor] = 1  # se erdos é um dos autores, os demais são 1
            else:
                # aqui entra uma lista de autores em que erdos não está incluída, daí entendemos se tratar
                # de uma lista sem nenhum colaborador (uma publicação individual)
                if len(autores) == 1:
                    namerdos[autor] = float('inf')
                else:
                    outros_autores = autores[:]
                    del(outros_autores[pos])  # elimina o autor atual da lista de autores da publicação

                    # essa lista receberá o índice dos demais autores da publicação, mais o 'inf'
                    # isto é necessário para incluir no dicionário autor que não tenha nenhuma colaboração,
                    # direta ou indireta, com Erdos
                    indice_autores = [namerdos[outro] for outro in outros_autores if outro in namerdos] + [float('inf')]

                    # determina o menor índice erdos entre os colaboradores do artigo e adiciona 1
                    if len(indice_autores) > 0:
                        indice_min = min(indice_autores)
                        if indice_min <= namerdos.get(autor, float('inf')):
                            namerdos[autor] = indice_min + 1

    return namerdos

def test_autores_sem_erdos_3_autores():
    publicacoes = [['erdos', 'a'], ['a', 'b'], ['c', 'd', 'e']]
    assert erdos(publicacoes) == {'erdos': 0, 'a': 1, 'b': 2, 'c': float('inf'), 'd': float('inf'), 'e': float('inf')}

def test_autores_sem_erdos():
    publicacoes = [['a', 'b'], ['c', 'b']]
    assert erdos(publicacoes) == {'erdos': 0, 'a': float('inf'), 'b': float('inf'), 'c': float('inf')}

def test_autores_sem_erdos():
    publicacoes =[['erdos', 'a'], ['a', 'b'], ['c', 'b']]
    assert erdos(publicacoes) == {'erdos': 0, 'a': 1, 'b': 2, 'c': 3}

def test_autor_sem_erdos():
    publicacoes = [['a']]
    assert erdos(publicacoes) == {'erdos': 0, 'a': float('inf')}

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