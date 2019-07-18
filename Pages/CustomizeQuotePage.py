from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
class CustomizeQuotePage():
    lblPlanQuote_ID = "PlanSetup"
    lnkTenure_Xpath = "//div[@id='PlanSetup']//a[@data-policytenure='1']"
    iconAdditionalCoverage_Xpath = "//div[contains(text(),'Public liability')]/../.."
    txtAdditionalCoverageValue_Xpath  = "//input[@id='PublicLiabilitySumInsured']"
    btnProceed_Xpath = "//a[contains(text(),'Proceed')]"
    btnBuyNow_Xpath = "//a[contains(@class,'BuyNow')]"

    def __init__(self,driver):
        self.driver=driver

    def setTenure(self):
        time.sleep(3)
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.lnkTenure_Xpath)))
        self.driver.find_element_by_xpath(self.lnkTenure_Xpath).click()

    def clickProceed(self):
        time.sleep(3)
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.btnProceed_Xpath)))
        self.driver.find_element_by_xpath(self.btnProceed_Xpath).click()

    def clickBuyNow(self):
        time.sleep(3)
        self.driver.find_element_by_xpath(self.btnBuyNow_Xpath).click()

    def setAddOnCover(self, addCoverage):
        time.sleep(3)
        self.driver.find_element_by_xpath(self.iconAdditionalCoverage_Xpath).click()
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.txtAdditionalCoverageValue_Xpath)))
        self.driver.find_element_by_xpath(self.txtAdditionalCoverageValue_Xpath).send_keys(addCoverage)