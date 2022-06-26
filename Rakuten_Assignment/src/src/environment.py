import logging
from src.steps.API.users_endpoint import UsersEndpoint
import src.steps.common.common_ui_utility as ui_utility
from src.steps.common.common_utility import *
import configparser
import os


def initialise_logger(context, feature):
        context.logger_name = 'test_framework'
        context.logger = logging.getLogger(context.logger_name)
        context.logger.setLevel(logging.INFO)
        logfile_name='testfile'
        ##Lets create formatter
        formatter = logging.Formatter('%(levelname)s %(name)s %(asctime)s %(module)s %(funcName)s %(message)s')
        ##Lets create file handler
        file_handler = logging.FileHandler(logfile_name)
        # Add formating to file handlere and not the logger
        file_handler.setFormatter(formatter)
        # Now add this handler to logger
        context.logger.addHandler(file_handler)
        log_console_handler = logging.StreamHandler()
        log_console_handler.setFormatter(formatter)
        context.logger.addHandler(log_console_handler)
        context.logger.info('#############LOGGER CREATED ################## ')



def before_feature(context,feature):
    initialise_logger(context, feature)

##Open the config file to read configurable data

    path_current_directory = os.path.dirname(__file__)
    context.path_config_file = path_current_directory + '/steps/config/commonconfig.ini'

    config = read_config_file(context.path_config_file)

    context.users_obj = UsersEndpoint(context)
    initialise_logger(context, feature)
    if 'ui_youtube_test' in feature.tags:
        ##read the youtube link from config file and also read the chrome exe file location for browser launch
        youtubeurl = config['configuration_setting']['youtubeurl']
        chrome_exe_location = config['configuration_setting']['chrome_exe_location_path']
        context.username = config['configuration_setting']['username']
        context.password = config['configuration_setting']['password']
        context.wrong_username = config['configuration_setting']['wrong_username']
        context.wrong_password = config['configuration_setting']['wrong_password']
        context.wrong_password = config['configuration_setting']['wrong_password']
        browser_to_use = config['configuration_setting']['browser_to_use']

        context.catalogue_driver = ui_utility.initialise_webdriver(context,youtubeurl, chrome_exe_location , browser_to_use)


def after_feature(context,feature):

    #We want to close the driver once ui test are finished
    if 'ui_youtube_test' in feature.tags:
        context.catalogue_driver.close()



