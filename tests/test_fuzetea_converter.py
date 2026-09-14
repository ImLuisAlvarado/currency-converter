from fuzetea_converter import *


def test_pesos_a_fuze(capsys):
    pesos_a_fuze(100)

    captured = capsys.readouterr()

    assert captured.out == (
        "$100 equivalen a 5.26 Fuze Teas\n"
        "Puedes comprar 5 Fuze Teas completos\n"
        "Te sobran $5\n"
    )

