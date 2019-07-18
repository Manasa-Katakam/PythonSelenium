from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


class DetailPage():
    txtStructureValue = "//div[contains(text(),'Structure Value')]//span"
    txtContentValue = "//div[contains(text(),'Content Value')]//span"
    txtAddOnValue = "//div[contains(text(),'Add ons')]//span"
    txtPremiumValue = "//div[contains(text(),'Total Premium')]/..//div[2]"
    spnAddCoOwner_Xpath = "//input[@id='IsCoOwnerAdd']/../../..//span"
    txtCoOwnername_ID = "CoOwnerName"
    txtPropertyPincode_ID = "InsuredPinCode"
    lnkPropertyPincode_Xpath = "//a[@class='dropdown-item']"
    txtPropertyHouseNo_ID = "InsuredAddress_HouseNo"
    txtPropertyArea_ID = "InsureStreetSectorArea"
    txtDOB_ID = "DateOfBirth"
    spnIsSameAddress_Xpath = "//input[@id='IsCpdSameAsInsured']/../../..//span"
    txtCpdPincode_ID = "CPDPinCode"
    txtCpdHouseNo_ID = "CorrespondenceAddress_HouseNo"
    txtCpdArea_ID = "CPDStreetSectorArea"
    spnAddFinancier_Xpath = "//input[@id='IsInsuredPropUnderLoan']/../../..//span"
    txtLoanProvider_ID ="LoanProvider"


    def __init__(self,driver):
        self.driver = driver

    def getStructureValue(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.txtStructureValue)))
        return self.driver.find_element_by_xpath(self.txtStructureValue).text

    def getAddOnValue(self):
        return self.driver.find_element_by_xpath(self.txtAddOnValue).text

    def getPremiunmValue(self):
        return self.driver.find_element_by_xpath(self.txtPremiumValue).text

    def getContentValue(self):
        return self.driver.find_element_by_xpath(self.txtContentValue).text

    def setDateOfBirth(self, DOB):
        self.driver.find_element_by_id(self.txtDOB_ID).send_keys(DOB)

    def setCoOwner(self, coName):
        self.driver.find_element_by_xpath(self.spnAddCoOwner_Xpath).click()
        time.sleep(1)
        self.driver.find_element_by_id(self.txtCoOwnername_ID).send_keys(coName)
        print("Added co-owner successfully as",coName)

    def setPropertyAddress(self, propertyPincode, faltNo, propertyArea):
        self.driver.find_element_by_id(self.txtPropertyPincode_ID).send_keys(propertyPincode)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.lnkPropertyPincode_Xpath).click()
        time.sleep(3)
        self.driver.find_element_by_id(self.txtPropertyHouseNo_ID).send_keys(faltNo)
        self.driver.find_element_by_id(self.txtPropertyArea_ID).send_keys(propertyArea)
        print("Successfully added Insurance Property Address")

    def setCorrespondenceAddress(self, propertyPincode, cpdFlatNo, cpdArea):
        self.driver.find_element_by_xpath(self.spnIsSameAddress_Xpath).click()
        time.sleep(2)
        self.driver.find_element_by_id(self.txtCpdPincode_ID).send_keys(propertyPincode)
        time.sleep(3)
        self.driver.execute_script("document.getElementsByClassName('dropdown-item')[1].click()")
        time.sleep(3)
        self.driver.find_element_by_id(self.txtCpdHouseNo_ID).send_keys(cpdFlatNo)
        self.driver.find_element_by_id(self.txtCpdArea_ID).send_keys(cpdArea)
        print("Successfully added Correspondence Property Address")

    def setLoanFinancier(self, financeCompany):
        self.driver.execute_script("window.scrollTo(0, Y)")
        self.driver.find_element_by_xpath(self.spnAddFinancier_Xpath).click()
        time.sleep(2)
        self.driver.find_element_by_id(self.txtLoanProvider_ID).send_keys(financeCompany)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.lnkPropertyPincode_Xpath).click()
        print("Successfully added Finance Comapy as", financeCompany)