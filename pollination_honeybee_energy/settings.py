from dataclasses import dataclass
from queenbee_dsl.function import Inputs, Outputs, Function, command


@dataclass
class SimParDefault(Function):
    """Get a SimulationParameter JSON with default outputs for energy use only"""

    filter_des_days = Inputs.bool(
        description='Boolean for whether the ddy-file should be filtered to only include'
        ' 99.6 and 0.4 design days', default=True
    )

    ddy = Inputs.file(
        description='A DDY file with design days to be included in the SimulationParameter',
        path='input.ddy', extensions=['ddy']
    )

    @command
    def create_sim_param(self):
        return 'honeybee-energy settings default-sim-par input.ddy --filter-des-days ' \
            '{{self.filter_des_days}} --output-file sim_par.json'

    sim_par_json = Outputs.file(
        description='SimulationParameter JSON with default outputs for energy use',
        path='sim_par.json'
    )


@dataclass
class SimParLoadBalance(SimParDefault):
    """Get a SimulationParameter JSON with all outputs needed to construct thermal load balances"""

    load_type = Inputs.str(
        description='Text to indicate the type of load. Choose from (Total, Sensible, Latent, All)',
        default='Total',
        spec={'type': 'string', 'enum': ['Total', 'Sensible', 'Latent', 'All']}
    )

    @command
    def create_sim_param(self):
        return 'honeybee-energy settings load-balance-sim-par input.ddy --load-type ' \
            '{{self.load_type}} --filter-des-days {{self.filter_des_days}} ' \
            '--output-file sim_par.json'
