#!/usr/bin/env python2

import os
import sys
import unittest

source_dir = os.path.join(os.path.dirname(__file__), 'source')
sys.path.insert(0, source_dir)

from tests.test_main import MainTestCase
from tests.test_auth import AuthTestCase


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(MainTestCase),
        unittest.makeSuite(AuthTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
