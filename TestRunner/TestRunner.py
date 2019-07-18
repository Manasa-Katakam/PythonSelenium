import Tests.HomeInsuranceForContentWithCoOwner
import Tests.HomeInsuranceForStructureAndContentWithCorrespondenceAddress
import Tests.HomeInsuranceForStructureWithAdditionalCoverage
import Tests.TenantInsuranceForContentWithFinancierDetails
import HtmlTestRunner
import unittest
import os

direct = os.getcwd()

class TestRunner(unittest.TestCase):

    def test_Runner(self):

        test_Suite = unittest.TestSuite()
        test_Suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Tests.TenantInsuranceForContentWithFinancierDetails.TenantInsuranceForContent)

        ])

        outfile = open(direct + "\\TestSuite.html", "w")

        runner1 = HtmlTestRunner.HTMLTestRunner(
            report_title = "HDFC Ergo Test Suite",
            stream=outfile
        )

        runner1.run(test_Suite)

if __name__ == '__main__':
    unittest.main()