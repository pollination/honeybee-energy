# Pollination Honeybee Energy plugin.

The honeybee-energy plugin adds daylight simulation functions to Pollination.

## Dependencies:

- `honeybee-energy` Python package. [PyPI](https://pypi.org/project/honeybee-energy/), [source](https://github.com/ladybug-tools/honeybee-energy)
- `honeybee-openstudio-gem` Ruby gem. [Rubygems](https://rubygems.org/gems/honeybee-openstudio), [source](https://github.com/ladybug-tools/honeybee-openstudio-gem)
- `OpenStudio` ([source](https://github.com/NREL/OpenStudio/releases)).


## Load as Queenbee plugin

Install the package using `pip install .`. Then you can use `queenbee_dsl` to load the
package as a Queenbee Plugin.

```python
from queenbee_dsl.package import load

plugin = load(python_package)
print(plugin.yaml())
```
