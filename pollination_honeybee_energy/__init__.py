
__queenbee__ = {
    'name': 'honeybee-energy',
    'description': 'Honeybee energy plugin for Pollination.',
    'icon': 'https://raw.githubusercontent.com/ladybug-tools/artwork/master/icons_bugs/grasshopper_tabs/HB-energy.png',
    'home': 'https://ladybug.tools/honeybee-energy/docs',
    'sources': [
        'https://github.com/ladybug-tools/honeybee-energy'
    ],
    'tag': '0.1.6',  # tag for honeybee-energy plugin on Pollination
    'keywords': ['ladybug-tools', 'honeybee', 'energyplus', 'openstudio', 'energy'],
    'maintainers': [
        {'name': 'chris', 'email': 'chris@ladybug.tools'}
    ],
    'license': {
        'name': 'PolyForm Shield License 1.0.0',
        'url': 'https://polyformproject.org/wp-content/uploads/2020/06/PolyForm-Shield-1.0.0.txt'
    },
    'config': {
        'docker': {
            'image': 'ladybugtools/honeybee-energy:1.66.1',
            'workdir': '/home/ladybugbot/run'
        }
    }
}
