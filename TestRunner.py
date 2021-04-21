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
    def __init__(self, Name):
        self.TestCases = []
        self.Name = Name
    def add_TestCase(self, TestCase_, args = [""]):
        Test = TestCase_(args)
        self.TestCases.append(Test)
    def Run(self):
        for TestCase_ in self.TestCases:
            TestCase_.Setup()
            TestCase_.Exercise()
            TestCase_.Verify()
            TestCase_.Teardown()

        self.WriteReport()

    def WriteReport(self):
        fd = open(self.Name+".html","w")

        fd.write("<table border=\"1\">\n")
        fd.write("    <tr>\n")
        fd.write("        <td> TestName </td>\n")
        fd.write("        <td> TestStatus </td>\n")
        fd.write("    </tr>\n")

        for TestCase_ in self.TestCases:
            fd.write("    <tr>\n")
            fd.write("        <td><a href=\"{:s}\"> {:s} </a></td>\n".format(
                    TestCase_.ReportPath,
                    TestCase_.Name
                    ))
            fd.write("        <td bgcolor = {:s}> {:s} </td>\n".format(
                    "\"green\"" if TestCase_.TestResult == 0 else "\"red\"",
                    "PASS" if TestCase_.TestResult == 0 else "FAIL"
                    ))
            fd.write("    </tr>\n")
        fd.write("</table>\n")
        fd.close()
