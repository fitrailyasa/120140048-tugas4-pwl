# Tugas Individu 4 - Pemrograman Web Lanjut
# 120140048 - Fitra Ilyasa
from . import models


def setup(env):
    request = env['request']

    # start a transaction
    request.tm.begin()

    # inject some vars into the shell builtins
    env['tm'] = request.tm
    env['dbsession'] = request.dbsession
    env['models'] = models
