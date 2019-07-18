from selenium.webdriver.support.select import Select
from selenium.common.exceptions import ElementNotInteractableException
import time
class StructureDetailsPage():
    # Locators from the current page
    selectPropertyValuation_Xpath = "//select[@name='HomeShield.SelectedValueType']"
    txtStructureValue_ID = "StructureValue"
    txtBuildUpArea_ID = "HomeShield_Area"
    selectBuildingAge_Name = "HomeShield.StructureAge"
    selectPropertyType_ID = "dropSelectPropertyType"
    spnSecurityGuard_Xpath = "//input[@id='HomeShield_Is24x7Security']/../../..//span"
    spnInterCom_Xpath = "// input[ @ id = 'HomeShield_IsIntercomBurglary'] /../../..// span"
    spnIsSalariedIndividual_Xpath = "// input[ @ id = 'HomeShield_IsSalariedIndvidual'] /../../..// span"
    btnNext_Xpath = "//a[@class='customize-btn sec-btn btn_StructCont_HS']"
    txtFullNama_ID = "FullName"
    txtEmail_ID = "Email"
    txtMobileNo_ID = "MobileNo"
    chkTermsAndCond_Xpath = "//input[@id='ViewQuoteCondition']/..//span[@class='t-and-c']"
    btnViewQuote_Xpath = "//button[text()='View Quote ']"
    txtContentValue_ID = "ContentValue"


    def __init__(self, driver):
        self.driver = driver

    def setStructureValue(self, propertyValuation, structureValue, area, age, propertyType):
        time.sleep(3)
        selectPropertyValue = Select(self.driver.find_element_by_xpath(self.selectPropertyValuation_Xpath))
        selectPropertyValue.select_by_visible_text(propertyValuation)
        self.driver.find_element_by_id(self.txtStructureValue_ID).send_keys(structureValue)
        self.driver.find_element_by_id(self.txtBuildUpArea_ID).send_keys(area)
        selectPropertyAge = Select(self.driver.find_element_by_name(self.selectBuildingAge_Name))
        selectPropertyAge.select_by_visible_text(age)
        selectPropertyType = Select(self.driver.find_element_by_id(self.selectPropertyType_ID))
        selectPropertyType.select_by_visible_text(propertyType)


    def setSecurityMeasures(self):
        time.sleep(3)
        self.driver.find_element_by_xpath(self.spnSecurityGuard_Xpath).click()
        self.driver.find_element_by_xpath(self.spnInterCom_Xpath).click()
        self.driver.find_element_by_xpath(self.spnIsSalariedIndividual_Xpath).click()

    def clickNext(self):
        self.driver.find_element_by_xpath(self.btnNext_Xpath).click()

    def setPersonalDetails(self, name, email, phone):
        self.driver.find_element_by_id(self.txtFullNama_ID).send_keys(name)
        self.driver.find_element_by_id(self.txtEmail_ID).send_keys(email)
        self.driver.find_element_by_id(self.txtMobileNo_ID).send_keys(phone)
        try:
            self.driver.execute_script("document.getElementById('ViewQuoteCondition').click()")
        except ElementNotInteractableException:
            print("Element not interatectable to handle!")

    def clickGetQuote(self):
        self.driver.find_element_by_xpath(self.btnViewQuote_Xpath).click()

    def setContentValue(self,insureAmount):
         self.driver.find_element_by_id(self.txtContentValue_ID).send_keys(insureAmount)

