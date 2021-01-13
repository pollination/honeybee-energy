from pollination_honeybee_energy.settings import SimParDefault, SimParLoadBalance, \
    SimParComfort
from queenbee.plugin.function import Function


def test_sim_par_default():
    function = SimParDefault().queenbee
    assert function.name == 'sim-par-default'
    assert isinstance(function, Function)


def test_sim_par_load_balance():
    function = SimParLoadBalance().queenbee
    assert function.name == 'sim-par-load-balance'
    assert isinstance(function, Function)


def test_sim_par_comfort():
    function = SimParComfort().queenbee
    assert function.name == 'sim-par-comfort'
    assert isinstance(function, Function)
