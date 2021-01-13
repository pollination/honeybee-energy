from dataclasses import dataclass
from queenbee_dsl.function import Inputs, Outputs, Function, command


@dataclass
class _SimulateBase(Function):
    """Base class for simulating models in EnergyPlus."""

    epw = Inputs.file(
        description='Weather file.', path='weather.epw', extensions=['epw']
    )

    osm = Outputs.file(
        description='The OpenStudio model used in the simulation.',
        path='output/run/in.osm'
    )

    idf = Outputs.file(
        description='The IDF model used in the simulation.',
        path='output/run/in.idf'
    )

    sql = Outputs.file(
        description='The result SQL file output by the simulation.',
        path='output/run/eplusout.sql'
    )

    zsz = Outputs.file(
        description='The result CSV with the zone loads over the design day output '
        'by the simulation.', path='output/run/epluszsz.csv'
    )

    html = Outputs.file(
        description='The result HTML page with summary reports output by the '
        'simulation.', path='output/run/eplustbl.htm'
    )

    err = Outputs.file(
        description='The error report output by the simulation.',
        path='output/run/eplusout.err'
    )


@dataclass
class SimulateModel(_SimulateBase):
    """Simulate a Model JSON file in EnergyPlus."""

    model = Inputs.file(
        description='Honeybee model in JSON format.', path='model.json',
        extensions=['hbjson', 'json']
    )

    sim_par = Inputs.file(
        description='SimulationParameter JSON that describes the settings for the '
        'simulation.', path='sim-par.json', extensions=['json']
    )

    @command
    def simulate_model(self):
        return 'honeybee-energy simulate model model.json weather.epw ' \
            '--sim-par-json sim-par.json --folder output ' \
            '--log-file output/output_paths.json'


@dataclass
class SimulateOsm(_SimulateBase):
    """Simulate an OSM file in EnergyPlus."""

    osm = Inputs.file(
        description='Path to a simulate-able OSM file.', path='model.osm',
        extensions=['osm']
    )

    @command
    def simulate_model(self):
        return 'honeybee-energy simulate osm model.osm weather.epw ' \
            '--folder output --log-file output/output_paths.json'


@dataclass
class SimulateIdf(_SimulateBase):
    """Simulate an IDF file in EnergyPlus."""

    idf = Inputs.file(
        description='Path to a simulate-able IDF file.', path='model.idf',
        extensions=['idf']
    )

    @command
    def simulate_model(self):
        return 'honeybee-energy simulate idf model.idf weather.epw ' \
            '--folder output/run --log-file output/run/output_paths.json'
