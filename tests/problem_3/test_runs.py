# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 08 (Fix as many bugs as possible!)
# PROBLEM NUMBER: 3

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_output, assert_python3

FILENAME = 'bug_03.py'
POINTS = 1

def test_python3():
    assert_python3()

def test_runs():
    return _test_output(FILENAME,
                        r""".*""",
                        input_values=[1],
                        regex=True)

