from selenium import webdriver
import time
import unittest
import sys
import HtmlTestRunner
from Pages.HomeInsurancePage import HomeInsurancePage
from Pages.StructureDetailsPage import StructureDetailsPage
from Pages.CustomizeQuotePage import CustomizeQuotePage
from Pages.DetailsPage import DetailPage


class HomeInsuranceForStructureAndContent(unittest.TestCase):
    baseURL = "https://www.hdfcergo.com/home-insurance-policy/"
    driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
    propertyValuation = "Reasonable Current Market Value"
    structureValue = "30,00,000"
    area = "1500"
    age = "Less than 25 Years"
    propertyType = "Flat above Ground floor"
    name = "Manasa"
    email = "e004007@cigniti.com"
    phone = "8888888888"
    amount = "50,000"
    propertyPincode = "500050"
    faltNo = "409"
    propertyArea = "Madhavapuri Hills"
    cpdFlatNo = "C3/38"
    cpdArea = "Huda Colony"

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(60)

    def test_AOpenStructureDetails(self):
        hip = HomeInsurancePage(self.driver)
        hip.navigateToHomeInsurance()
        hip.launchStructureAndContentCoverForHomeOwner()

    def test_BEnterStructureDetails(self):
        sdp = StructureDetailsPage(self.driver)
        sdp.setStructureValue(self.propertyValuation, self.structureValue, self.area, self.age, self.propertyType)
        sdp.setContentValue(self.amount)
        sdp.setSecurityMeasures()
        sdp.clickNext()
        sdp.setPersonalDetails(self.name, self.email, self.phone)
        sdp.clickGetQuote()

    def test_CCustomizeQuote(self):
        cq = CustomizeQuotePage(self.driver)
        cq.setTenure()
        cq.clickProceed()
        cq.clickBuyNow()

    def test_DQuoteDetails(self):
        qde = DetailPage(self.driver)
        print("The Structure value is:", qde.getStructureValue())
        assert (qde.getStructureValue() == self.structureValue)
        print("The Content value is:", qde.getContentValue())
        assert (qde.getContentValue() == self.amount)
        print("The Final Premium value is: ", qde.getPremiunmValue())
        qde.setPropertyAddress(self.propertyPincode, self.faltNo, self.propertyArea)
        qde.setCorrespondenceAddress(self.propertyPincode, self.cpdFlatNo, self.cpdArea)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("HomeInsuranceForStructure Test is completed!")

    if __name__ == "__main__":
        unittest.main()


