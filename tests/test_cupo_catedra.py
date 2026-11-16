from arandu.cupo import hay_cupo


def test_comision_sin_inscriptos_tiene_cupo():
    assert hay_cupo(30, []) is True


def test_comision_llena_no_tiene_cupo():
    assert hay_cupo(2, ["activa", "activa"]) is False


def test_cupo_cero_rechaza_siempre():
    assert hay_cupo(0, []) is False


def test_una_baja_no_ocupa_lugar():
    assert hay_cupo(2, ["activa", "baja"]) is True


def test_ultimo_lugar_disponible():
    assert hay_cupo(3, ["activa", "activa"]) is True
