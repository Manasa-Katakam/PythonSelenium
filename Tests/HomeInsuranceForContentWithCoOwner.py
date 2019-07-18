from selenium import webdriver
import unittest
from Pages.HomeInsurancePage import HomeInsurancePage
from Pages.StructureDetailsPage import StructureDetailsPage
from Pages.CustomizeQuotePage import CustomizeQuotePage
from Pages.DetailsPage import DetailPage


class HomeInsuranceForContent(unittest.TestCase):
    baseURL = "https://www.hdfcergo.com/home-insurance-policy/"
    driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
    amount = "60,000"
    name = "jupiter"
    email = "jupiter@planets.com"
    phone = "8888888888"
    coOwner = "mk jupiters"

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(60)

    def test_AOpenContentDetails(self):
        hip = HomeInsurancePage(self.driver)
        hip.navigateToHomeInsurance()
        hip.launchContentCoverForHomeOwner()

    def test_BEnterContentDetails(self):
        sdp = StructureDetailsPage(self.driver)
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
        qde.setCoOwner(self.coOwner)
        print("The Content value is:", qde.getContentValue())
        assert (qde.getContentValue() == self.amount)
        print("The Final Premium value is: ", qde.getPremiunmValue())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("HomeInsuranceForContent Test is completed!")

    if __name__ == "__main__":
        unittest.main()