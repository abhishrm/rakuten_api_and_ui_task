import string
import random
import secrets
import configparser

def random_string_generator():
    random_string_formed= ''.join(random.choices(string.ascii_uppercase +
                           string.digits, k=10))
    return random_string_formed


def read_config_file(path_config_file):
    try:

        config = configparser.ConfigParser()
        config.read(path_config_file)
        return config

    except Exception as e:
        assert False, "Failed to read config file :{}".format(e)

def random_string_only_char():
    return ''.join(secrets.choice(string.ascii_uppercase)
            for i in range(10)).lower()

class RakutenMgmtClassFunctions(object):

    def __init__(self, context):
        self.context = context

    def populate_movie_json(self):
        """
        method to populate movue json
        :return: returns a dictionary containing user input json
        """

        try:


            movie_info = {
                          "data": {
                            "attributes": {


                                "title": "title"+random_string_only_char().lower(),
                                "year": str(random.randint(1111,9999)),
                                "plot": "plot"+random_string_only_char().lower(),
                                "duration": random.randint(1111,9999),
                                "audio_qualities": [
                                ],
                                "video_qualities": [
                                ],
                                "genres": [
                                ]

}
                          }}
            return movie_info
        except:
            raise

    def populate_genres_json(self, ):
        """
        method to populate genres json
        :return: returns a dictionary containing genres input json
        """

        try:

            genres_info = {
                "data": {
                    "attributes": {

                        "name": "name" + random_string_only_char().lower(),

                    }
                }}
            return genres_info
        except:
            raise

    def populate_video_qualities_json(self, ):
        """
        method to populate video json
        :return: returns a dictionary containing user input json
        """

        try:

            video_info = {
                "data": {
                    "attributes": {

                        "name": "name" + random_string_only_char().lower(),
                        "abbr": "VTQ" + random_string_only_char().lower(),
                        "position": None,
                        "default": False
                    }
                }}
            return video_info
        except:
            raise

    def populate_audio_qualities_json(self, ):
        """
        method to populate audio json
        :return: returns a dictionary containing user input json
        """

        try:

            audio_info = {
                "data": {
                    "attributes": {

                        "name": "name" + random_string_only_char().lower(),
                        "abbr": "VTQ" + random_string_only_char().lower(),
                        "position": None,
                        "default": False
                    }
                }}
            return audio_info
        except:
            raise

    def compare_users_json(self, input_users_info, output_users_info):
        """
        This methos is used to compare the input set during POST/PATCH input json against the GET endpoint json.
        :param input_users_info:
        :param output_users_info:
        :return:
        """
        try:

            keys = input_users_info.keys()

            for key in keys:

                if type(input_users_info[key]) == list and type(output_users_info[key]) == list:
                    input_users_info[key].sort()
                    output_users_info[key].sort()
                if input_users_info.get(key) != output_users_info.get(key):
                    raise Exception('Users info :{} does not match, expected:{} , got:{}'.format(
                        key, input_users_info.get(key), output_users_info.get(key)
                    ))
        except:
            raise