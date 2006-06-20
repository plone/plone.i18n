"""
    Normalizer tests.
"""

from unittest import TestSuite
from zope.testing.doctestunit import DocTestSuite

def test_suite():
    return TestSuite((
        DocTestSuite('plone.i18n.normalizer'),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")

