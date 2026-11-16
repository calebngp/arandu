from arandu.cupo import hay_cupo


def test_sin_inscriptos_hay_cupo():
    assert hay_cupo(30, []) is True


def test_comision_llena_no_hay_cupo():
    assert hay_cupo(2, ["activa", "activa"]) is False


def test_cupo_cero_no_acepta():
    assert hay_cupo(0, []) is False


def test_baja_no_ocupa_lugar():
    assert hay_cupo(2, ["activa", "baja"]) is True


def test_ultimo_lugar_libre():
    assert hay_cupo(3, ["activa", "activa"]) is True


def test_solo_bajas_no_ocupan():
    assert hay_cupo(1, ["baja", "baja"]) is True
