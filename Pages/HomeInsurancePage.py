import time
class HomeInsurancePage():
    # Locators from the current page
    btnBuyNow_Xpath = "//button[contains(text(),'Buy Now')]"
    spnHomeCoverFor_ID = "HomeCoverSpan"
    spnHomeOwner_Xpath = "//span[contains(text(),'Owner')]"
    spnTenant_Xpath = "//span[contains(text(),'Tenant')]"
    spnCoverage_ID = "RiskCoverSpan"
    lblStructureCover_Xpath = "//label[contains(text(),'Structure')]"
    lblContentCover_Xpath = "//label[contains(text(),'Content')]"
    lblStrunctureAndContentCover_Xpath = "//label[contains(text(),'Structure & Content')]"
    btnContinue_Xpath = "//button[contains(text(),'Continue')]"


    def __init__(self,driver):
        self.driver = driver

    def navigateToHomeInsurance(self):
        self.driver.find_element_by_xpath(self.btnBuyNow_Xpath).click()
        time.sleep(5)
        handles = self.driver.window_handles
        for h in handles:
            self.driver.switch_to.window(h)
        print(self.driver.title)

    def launchStructureCoverForHomeOwner(self):
        self.driver.find_element_by_id(self.spnHomeCoverFor_ID).click()
        self.driver.find_element_by_xpath(self.spnHomeOwner_Xpath).click()
        self.driver.find_element_by_id(self.spnCoverage_ID).click()
        self.driver.find_element_by_xpath(self.lblStructureCover_Xpath).click()
        self.driver.find_element_by_xpath(self.btnContinue_Xpath).click()

    def launchContentCoverForHomeOwner(self):
        self.driver.find_element_by_id(self.spnHomeCoverFor_ID).click()
        self.driver.find_element_by_xpath(self.spnHomeOwner_Xpath).click()
        self.driver.find_element_by_id(self.spnCoverage_ID).click()
        self.driver.find_element_by_xpath(self.lblContentCover_Xpath).click()
        self.driver.find_element_by_xpath(self.btnContinue_Xpath).click()

    def launchStructureAndContentCoverForHomeOwner(self):
        self.driver.find_element_by_id(self.spnHomeCoverFor_ID).click()
        self.driver.find_element_by_xpath(self.spnHomeOwner_Xpath).click()
        self.driver.find_element_by_id(self.spnCoverage_ID).click()
        self.driver.find_element_by_xpath(self.lblStrunctureAndContentCover_Xpath).click()
        self.driver.find_element_by_xpath(self.btnContinue_Xpath).click()

    def launchContentCoverForTenant(self):
        self.driver.find_element_by_id(self.spnHomeCoverFor_ID).click()
        self.driver.find_element_by_xpath(self.spnTenant_Xpath).click()
        self.driver.find_element_by_xpath(self.btnContinue_Xpath).click()