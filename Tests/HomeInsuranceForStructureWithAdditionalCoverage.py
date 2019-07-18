from selenium import webdriver
import unittest
from Pages.HomeInsurancePage import HomeInsurancePage
from Pages.StructureDetailsPage import StructureDetailsPage
from Pages.CustomizeQuotePage import CustomizeQuotePage
from Pages.DetailsPage import DetailPage


class HomeInsuranceForStructure(unittest.TestCase):
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
    addOnFlag = True
    addOnValue = "2,00,000"

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(60)

    def test_AOpenStructureDetails(self):
        hip = HomeInsurancePage(self.driver)
        hip.navigateToHomeInsurance()
        hip.launchStructureCoverForHomeOwner()

    def test_BEnterStructureDetails(self):
        sdp = StructureDetailsPage(self.driver)
        sdp.setStructureValue(self.propertyValuation, self.structureValue, self.area, self.age, self.propertyType)
        sdp.setSecurityMeasures()
        sdp.clickNext()
        sdp.setPersonalDetails(self.name, self.email, self.phone)
        sdp.clickGetQuote()

    def test_CCustomizeQuote(self):
        cq = CustomizeQuotePage(self.driver)
        cq.setTenure()
        cq.clickProceed()
        if(self.addOnFlag):
            cq.setAddOnCover(self.addOnValue)
        else:
            print("Add-on flag is false, hence no add-on cover is added!")
        cq.clickBuyNow()

    def test_DQuoteDetails(self):
        qde = DetailPage(self.driver)
        print("The Structure value is:", qde.getStructureValue())
        assert (qde.getStructureValue() == self.structureValue)
        print("The Final Premium value is: ", qde.getPremiunmValue())
        if (self.addOnFlag):
            assert (qde.getAddOnValue() == self.addOnValue)
            print("The Add-On value is:", qde.getAddOnValue())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("TenantInsuranceForContent Test is completed!")

    if __name__ == "__main__":
        unittest.main()


