# -*- coding: utf8 -*-
########################################################################################
# This file is part of exhale.  Copyright (c) 2017-2024, Stephen McDowell.             #
# Full BSD 3-Clause license available here:                                            #
#                                                                                      #
#                https://github.com/svenevs/exhale/blob/master/LICENSE                 #
########################################################################################
"""
Global ``pytest`` configurations that are used / executed for every test.

See ``pytest`` documentation on `Package/Directory-level fixtures (setups)`__.

__ https://docs.pytest.org/en/latest/example/simple.html#package-directory-level-fixtures-setups
"""

pytest_plugins = [
    "sphinx.testing.fixtures",
    "testing.fixtures"
]
"""Signals to ``pytest`` which plugins are needed for all tests."""


def pytest_configure(config):
    """Register ``@pytest.mark.exhale`` with PyTest."""
    config.addinivalue_line(
        "markers", "exhale: internal marker for testing metaclass."
    )
    # TODO: upstream this if not fixed already.
    config.addinivalue_line(
        "markers", "sphinx: register sphinx test."
    )


def pytest_runtest_setup(item):
    """.. todo:: stop reloading configs module in 1.x."""
    from importlib import reload
    from exhale import configs
    reload(configs)
