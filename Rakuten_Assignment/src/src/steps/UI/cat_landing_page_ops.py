from .cat_landing_page_locators import *
from src.steps.common import common_ui_utility
import logging
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
from src.steps.common.common_utility import read_config_file
import time


class CatLandingPageOps(object):
    """
    This Class conatin all the methods to locate all the elements from the youtube landing page and search related methos
    """
    def __init__(self, context):
        self.context = context
        self.get_elem_obj = common_ui_utility.GetElement(self.context)

    def _type(self):
        return self.__class__.__name__


    def _locate_and_click_sign_in_button(self,click):
        """
        Function to locate SIGN in button

        :return:
        """

        return_value= self.get_elem_obj.get_element_once_visible(*elements_on_youtube_page['YOUTUBE_SIGN_IN_BUTTON'])
        if click is not None:
            return_value.click()
        return True

    def _locate_verify_username_login_window(self,username,next_button):
        """
        Function to send the username text
        :param username:username to be send
        :param next_button: Next button seen on login page
        :return:
        """

        return_value= self.get_elem_obj.get_element_once_visible(*elements_on_youtube_page['YOUTUBE_USERNAME_IN_BUTTON'])
        if username is not None and next_button is not None:
            return_value.send_keys(username)
            all_matched_objects = self.get_elem_obj.get_all_elements_once_present(
                *elements_on_youtube_page['NEXT_BUTTON'])
            object = [ object for object in all_matched_objects if object.text =='Next']
            object[0].click()

        return True


    def _get_search_box_and_then_click_it(self,search_text):
        """
        Function to search text on youtube
        :param search_text:
        :return:
        """
        res = self.get_elem_obj.get_element_once_visible(*elements_on_youtube_page['YOUTUBE_PASSWORD_IN_BUTTON'])
        res.send_keys(search_text)
        res.send_keys("\n")
        return True

    def _verify_search_result(self, search_text):
        """
        Function to verify the ens search result pop up on youtube after search.
        :param search_text:resultant value of search
        :return:
        """
        xpath = "//*[@aria-label="  + search_text  + "]"
        res = self.get_elem_obj.get_element_once_visible(*elements_on_youtube_page[xpath])
        return True

    def _locate_verify_password_login_window(self, password,next_button):
        """
        Function to pass input text to password field and click next button
        :param password: User pssword required to youtube login
        :param next_button:nect button to be clicked
        :return:
        """

        return_value = self.get_elem_obj.get_element_once_visible(
            *elements_on_youtube_page['YOUTUBE_PASSWORD_IN_BUTTON'])

        if password is not None and next_button is not None:
            return_value.send_keys(password)
            all_matched_objects = self.get_elem_obj.get_all_elements_once_present(
                *elements_on_youtube_page['NEXT_BUTTON'])
            object = [ object for object in all_matched_objects if object.text =='Next']
            object[0].click()

        return True

    def _verify_username_failure_text(self,text_to_look_for):
        """
        Function to verify the the wrong username text.
        :param search_text:resultant value of search
        :return:
        """
        if text_to_look_for == 'Couldn’t find your Google Account':
            res = self.get_elem_obj.get_element_once_visible(*elements_on_youtube_page['USERNAME_WRONG_TEXT'])

        elif text_to_look_for == 'Enter an email or phone number.':
            res = self.get_elem_obj.get_element_once_visible(*elements_on_youtube_page['USERNAME_MISSING_TEXT'])

        return True

    def _verify_password_failure_text(self,text_to_look_for ):
        """
        Function to verify the the wrong password text.
        :param search_text:resultant value of search
        :return:
        """

        if text_to_look_for == 'Wrong password':
            res = self.get_elem_obj.get_element_once_visible(*elements_on_youtube_page['WRONG_PASSWORD_TEXT'])

        elif text_to_look_for == 'Enter a password':
            res = self.get_elem_obj.get_element_once_visible(*elements_on_youtube_page['MISSING_PASSWORD_TEXT'])

        return True
