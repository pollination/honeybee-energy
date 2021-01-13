from pollination_honeybee_energy.result import AvailableResultsInfo, DataByOutput, \
    ResultCsvQueryable
from queenbee.plugin.function import Function


def test_available_results_info():
    function = AvailableResultsInfo().queenbee
    assert function.name == 'available-results-info'
    assert isinstance(function, Function)


def test_data_by_output():
    function = DataByOutput().queenbee
    assert function.name == 'data-by-output'
    assert isinstance(function, Function)


def test_result_csv_queryable():
    function = ResultCsvQueryable().queenbee
    assert function.name == 'result-csv-queryable'
    assert isinstance(function, Function)
