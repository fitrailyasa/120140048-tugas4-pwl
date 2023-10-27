# Tugas Individu 4 - Pemrograman Web Lanjut
# 120140048 - Fitra Ilyasa
from be_tugas4_pwl_120140048 import models

def test_my_view_success(testapp, dbsession):
    model = models.MyModel(name='one', value=55)
    dbsession.add(model)
    dbsession.flush()

    res = testapp.get('/', status=200)
    assert res.body

def test_notfound(testapp):
    res = testapp.get('/badurl', status=404)
    assert res.status_code == 404
