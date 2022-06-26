import logging
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException, \
    ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


_module = os.path.basename(__file__)


def initialise_webdriver(context, get_url, chrome_exe_location, browser_to_use):
    """
    This function initialise the webdriver
    :param context: behave context var
    :param get_url: url of the browser
    :param chrome_exe_location:location of chrome exe
    :return:
    """
    driver = None
    try:
        if browser_to_use == 'Chrome':
            driver = webdriver.Chrome(executable_path = chrome_exe_location)
        elif browser_to_use == 'Edge':
            driver = webdriver.Edge(executable_path = chrome_exe_location)
        elif browser_to_use == 'Firefox':
            driver = webdriver.Firefox(executable_path=chrome_exe_location)
        else:
            assert False ," Unsupported browser :{} fed from the commonconfig.ini, Provide supported list from fiven set of browser i.e Edge ,Chrome,Firefox".format(browser_to_use)
        driver.maximize_window()
        driver.get(get_url)
        return driver
    except Exception as e:

        context.logger.error('Error in initialising the webdriver : {}'.format(str(e)))
        assert False, "Initialization failed"


class GetElement:

    def __init__(self, context):
        self.context = context

    def get_element_once_visible(self, locator, locator_val, timeout=15,
                                 pollFrequency=0.5):
        try:
            wait = WebDriverWait(self.context.catalogue_driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])

            if locator.upper() == 'ID':
                return wait.until(EC.visibility_of_element_located((By.ID, locator_val)))
            elif locator.upper() == 'NAME':
                return wait.until(EC.visibility_of_element_located((By.NAME, locator_val)))
            elif locator.upper() == 'TAG_NAME':
                return wait.until(EC.visibility_of_element_located((By.TAG_NAME, locator_val)))
            elif locator.upper() == 'CSS_SELECTOR':
                return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator_val)))
            elif locator.upper() == 'XPATH':
                return wait.until(EC.visibility_of_element_located((By.XPATH, locator_val)))
            elif locator.upper() == 'CLASS_NAME':
                return wait.until(EC.visibility_of_element_located((By.CLASS_NAME, locator_val)))
            elif locator.upper() == 'LINK_TEXT':
                return wait.until(EC.visibility_of_element_located((By.LINK_TEXT, locator_val)))
            elif locator.upper() == 'PARTIAL_LINK_TEXT':
                return wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, locator_val)))
            else:
                raise Exception('Locator {} provided is not supported'.format(locator.upper()))
        except Exception as e:
            self.context.logger.info.error('Element not appeared on web page')

    def get_all_elements_once_present(self, locator, locator_val, timeout=15,
                                      pollFrequency=0.5):
        try:
            wait = WebDriverWait(self.context.catalogue_driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])

            if locator.upper() == 'ID':
                return wait.until(EC.presence_of_all_elements_located((By.ID, locator_val)))
            elif locator.upper() == 'NAME':
                return wait.until(EC.presence_of_all_elements_located((By.NAME, locator_val)))
            elif locator.upper() == 'TAG_NAME':
                return wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, locator_val)))
            elif locator.upper() == 'CSS_SELECTOR':
                return wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator_val)))
            elif locator.upper() == 'XPATH':
                return wait.until(EC.presence_of_all_elements_located((By.XPATH, locator_val)))
            elif locator.upper() == 'CLASS_NAME':
                return wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, locator_val)))
            elif locator.upper() == 'LINK_TEXT':
                return wait.until(EC.presence_of_all_elements_located((By.LINK_TEXT, locator_val)))
            elif locator.upper() == 'PARTIAL_LINK_TEXT':
                return wait.until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, locator_val)))
            else:
                raise Exception(f'Locator {locator.upper()} provided is not supported')
        except Exception as e:
            self.context.logger.info.error('Element not appeared on web page')
