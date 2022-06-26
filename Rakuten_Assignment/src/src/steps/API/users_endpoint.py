import logging
import requests


class UsersEndpoint(object):
    """
    This class contain all CRUD related function for various endpoints related to Rakuten audio/video/genres
    """

    def __init__(self, context):
        self.context = context
        self.main_url = 'https://prod-titanic.rakuten.tv/'

        self.create_movie_endpoint = self.main_url + 'movies'
        self.create_genres_endpoint = self.main_url + 'genres'
        self.create_video_qualities_endpoint = self.main_url + 'video_qualities'
        self.create_audio_qualities_endpoint = self.main_url + 'audio_qualities'

        self.movie_get_edit_delete_endpoint = self.create_movie_endpoint + '<name_or_id>'
        self.genres_get_edit_delete_endpoint = self.create_genres_endpoint + '<name_or_id>'
        self.video_quality_get_edit_delete_endpoint = self.create_video_qualities_endpoint + '<name_or_id>'
        self.audio_quality_get_edit_delete_endpoint = self.create_audio_qualities_endpoint + '<name_or_id>'


        self.headers = {'Content-Type': 'application/json; charset=utf-8'}

    def get_logger(self):
        return logging.getLogger(self.context.logger_name + '.' + self._type())

    def fetch_url(self,endpoint_to_be_used, request_type):

        if endpoint_to_be_used == 'Movie':
            if request_type == 'POST':
                url = self.create_movie_endpoint
            elif request_type in ['GET', 'PATCH', 'DELETE']:
                url = self.movie_get_edit_delete_endpoint

        elif endpoint_to_be_used == 'Video Qualities':
            if request_type == 'POST':
                url = self.create_video_qualities_endpoint
            elif request_type in ['GET', 'PATCH', 'DELETE']:
                url = self.video_quality_get_edit_delete_endpoint

        elif endpoint_to_be_used == 'Audio Qualities':
            if request_type == 'POST':
                url = self.create_audio_qualities_endpoint
            elif request_type in ['GET', 'PATCH', 'DELETE']:
                url = self.audio_quality_get_edit_delete_endpoint

        elif endpoint_to_be_used == 'Genres':
            if request_type == 'POST':
                url = self.create_genres_endpoint
            elif request_type in ['GET', 'PATCH', 'DELETE']:
                url = self.genres_get_edit_delete_endpoint
        return url

    def create_entity(self, json, endpoint_to_be_used):
        """
        This method is user to call user POST endpoint.
        :param json:
        :param which_type_of_endpoint:createWithArray/createWithList/user
        :return: tuple of respone status code and response text
        """

        create_user_url  = self.fetch_url(endpoint_to_be_used, 'POST')
        response = requests.post(create_user_url, headers=self.headers, json=json)
        self.context.logger.info('created entity status code : %s' % response.status_code)
        self.context.logger.info('create entity : %s' % response.text)
        return response.status_code, response.json()

    def get_entity(self, entity_id_or_name, entity):
        """
        This method is to call GET endpoint.
        :param user_name: user_name
        :return: tuple of returned user metadata and status code
        """

        get_entity_url = self.fetch_url(entity, 'GET')
        get_url = get_entity_url.replace('<name_or_id>', "/" + str(entity_id_or_name))
        response = requests.get(get_url,  headers=self.headers)
        self.context.logger.info('get status code: %s' % response.status_code)
        self.context.logger.info('get text : %s' % response.text)
        return response.status_code, response.json()

    def update_entity(self, entity,entity_id_or_name, json):
        """
        This method is to call user PATCH endpoint.
        :param user_name: user_name to be updated
        :param json: input json for user
        :return: tuple of returned user metadata and status code
        """
        get_entity_url = self.fetch_url(entity, 'PATCH')
        get_url = get_entity_url.replace('<name_or_id>', "/" + str(entity_id_or_name))
        response = requests.put(get_url, headers=self.headers, json=json)
        self.context.logger.info('updated status code : %s' % response.status_code)
        self.context.logger.info('updated text : %s' % response.text)
        return response.status_code,True

    def delete_user(self, entity, entity_id_or_name):
        """
        This method is user to call user DELETE endpoint.
        :param user_name: user to be deleted
        :return: tuple of returned user status code and string
        """
        get_entity_url = self.fetch_url(entity, 'DELETE')
        get_url = get_entity_url.replace('<name_or_id>', "/" + str(entity_id_or_name))
        response = requests.delete(get_url, headers=self.headers)
        self.context.logger.info('delete status code : %s' % response.status_code)
        self.context.logger.info('delete  text : %s' % response.text)
        return response.status_code,'deleted'


