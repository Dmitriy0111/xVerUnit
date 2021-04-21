#
# File          : TestCase.py
# Autor         : Vlasov D.V.
# Data          : 16.04.2021
# Language      : Python
# Description   : Main class for tests
# Copyright(c)  : 2021 Vlasov D.V.
#

class TestCase:
    def __init__(self,args = [""]):
        self.Name = ""
        self.TestResult = -1
        self.ReportPath = ""
    def Setup(self):
        pass
    def Exercise(self):
        pass
    def Verify(self):
        pass
    def Teardown(self):
        pass
