#
# File          : TestRunner.py
# Autor         : Vlasov D.V.
# Data          : 16.04.2021
# Language      : Python
# Description   : Class for running tests
# Copyright(c)  : 2021 Vlasov D.V.
#

from xVerUnit.TestCase import TestCase

class TestRunner(TestCase):
    def __init__(self):
        self.TestCases = []
    def add_TestCase(self, TestCase_, args = [""]):
        Test = TestCase_(args)
        self.TestCases.append(Test)
    def Run(self):
        for TestCase_ in self.TestCases:
            TestCase_.Setup()
            TestCase_.Exercise()
            TestCase_.Verify()
            TestCase_.Teardown()
