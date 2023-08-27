from grada import graphs as g
import numpy as np

# disable logging
g.Functions.activate_logging(status=False)


def test_addensa_equal_elements():
    _ = np.array([-5, -2, 0, 1, 1, 4, 6])
    res = g.Functions.addensa(_, 2)

    assert np.array_equal(_, res)


def test_addensa():
    _ = np.linspace(-5, 5, num=20)
    res = g.Functions.addensa(_, 10)

    assert len(res) > len(_)


def test_allarga_campo_extremes():
    _ = np.array([-5, -2, 0, 1, 4, 6])
    res = g.Functions.allarga_campo(_, 0, 0, 2)

    assert res[0] == _[0] and res[-1] == _[-1]

    res = g.Functions.allarga_campo(_, 0, 0.1, 2)

    assert res[0] != res[1]

    res = g.Functions.allarga_campo(_, 0.1, 0, 2)

    assert res[-1] != res[-2]


def test_allarga_campo():
    _ = np.array([-5, -2, 0, 1, 4, 6])
    res = g.Functions.allarga_campo(_, 0.1, 0.2, 2)

    print(res)

    assert len(res) > len(_) and res[0] < _[0] and res[-1] > _[-1]


def test_get_titolo():
    text = g.Text("text/text.txt")
    titolo = text.get_titolo()

    assert titolo == "titolo"


def test_get_ascisse():
    text = g.Text("text/text.txt")
    ascisse = text.get_ascisse()

    assert ascisse == "ascisse"


def test_get_ordinate():
    text = g.Text("text/text.txt")
    ordinate = text.get_ordinate()

    assert ordinate == "ordinate"


def test_get_dati():
    text = g.Text("text/text.txt")
    dati1 = text.get_dati(1)
    dati2 = text.get_dati(2)

    assert dati1 == "dati 1" and dati2 == "dati 2"


def test_get_funzione():
    text = g.Text("text/text.txt")
    funzione1 = text.get_funzione(1)
    funzione2 = text.get_funzione(2)

    assert funzione1 == "funzione 1" and funzione2 == "funzione 2"
