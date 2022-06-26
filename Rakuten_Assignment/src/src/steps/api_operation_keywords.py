import logging
from behave import *

from src.steps.API.users_endpoint import UsersEndpoint
import random
import os


from src.steps.common.common_utility import *

_module = os.path.basename(__file__)


@When('user tries to create entity "{entity_name}" using endpoint "{endpoint_to_be_used}"')
@When('user tries to create entity "{entity_name}" using endpoint "{endpoint_to_be_used}" but field "{field}" "{missing}"')
@When('user tries to create entity "{entity_name}" using endpoint "{endpoint_to_be_used}" but fields "{field}" "{missing}"')
def step_impl(context, entity_name,endpoint_to_be_used, field=None, missing=None):
    """
    Keyword implemantion to create entity like Movie/genres/Audio/Video using POST endpoint.
    :param context: tries to create entit
    :param entity_name:name of the entity
    :param endpoint_to_be_used: Movie/audio/video/generes
    :return:
    """
    try:

        if not hasattr(context, 'entity_creation_input_list'):
            context.entity_creation_input_list = {}


        if not hasattr(context, 'entity_output_list'):
            context.entity_output_list = {}
        RakutenMgmtFunctions = RakutenMgmtClassFunctions(context)

        if endpoint_to_be_used == 'Movie':
            entity_info_data = RakutenMgmtFunctions.populate_movie_json()
        elif endpoint_to_be_used == 'Video Qualities':
            entity_info_data = RakutenMgmtFunctions.populate_video_qualities_json()
        elif endpoint_to_be_used == 'Audio Qualities':
            entity_info_data = RakutenMgmtFunctions.populate_audio_qualities_json()
        elif endpoint_to_be_used == 'Genres':
            entity_info_data = RakutenMgmtFunctions.populate_genres_json()

        if field is not None and missing is not None:

            if field == 'all_the_fields' and missing == 'missing':
                entity_info_data['data']['attributes'] = {}

            elif field == 'as' and missing == 'wrong_parameters':
                entity_info_data['data']['attributes'] = {random_string_generator(): random_string_generator(),
                                                    random_string_generator(): random_string_generator(),
                                                    random_string_generator(): random_string_generator()}
            elif field and missing == 'empty string':

                entity_info_data['data']['attributes'][field] = ''

            elif field and missing == 'trailing spaces':

                entity_info_data['data']['attributes'][field] = entity_info_data['data']['attributes'][field] + '        '

            elif field and missing == 'leading spaces':

                entity_info_data['data']['attributes'][field] = '     ' + entity_info_data['data']['attributes'][field]


            else:

                del entity_info_data['data']['attributes'][field]

        context.entity_creation_input_list[entity_name] = entity_info_data

        entity_response = context.users_obj.create_entity(entity_info_data['data']['attributes'], endpoint_to_be_used)
        context.entity_output_list[entity_name] = entity_response

    except Exception as e:
        context.logger.error('entity creation failed using endpoint:{0}'.format(str(e)))
        raise


@Then('user gets "{status_code}" and can verify entity details in response json of user "{name}"')
def step_impl(context, status_code,name):
    """
    Keyword implemenation to verify POST call status codes
    :param context:
    :param status_code:return code from the endpoint call
    :param name:name of the entity created
    :return:
    """

    try:

        if int(status_code) != context.entity_output_list[name][0]:
            raise Exception("Status code is not as per expectation, expected: {0}, got: {1}".format
                                (status_code, context.entity_output_list[name][0]))

        context.logger.info('#############Successfully Verified status code ################## ')

    except Exception as e:
        context.logger.error("user status code/details match failed using endpoint:{0}".format(str(e)))
        raise



@When('user tries to get entity "{entity_name}" by using endpoint "{endpoint_to_be_used}"')
@When('user tries to get entity "{entity_name}" by using endpoint "{endpoint_to_be_used}" but with "{invalid_entity_id}"')
def step_impl(context, entity_name, endpoint_to_be_used, invalid_entity_id=None):
    """
    Keyword implementation to get entity like like Movie/genres/Audio/Video using endpoint
    :param context:
    :param entity_name:Name of the entity to be retrived
    :return:
    """
    try:
        if not hasattr(context, 'entity_get_operation_output_list'):
            context.entity_get_operation_output_list = {}

        # if endpoint_to_be_used == 'Movie':
        #     entity_to_be_get = context.entity_output_list[entity_name][1]['id']
        # elif endpoint_to_be_used == 'Genres':
        #     entity_to_be_get = context.entity_output_list[entity_name][1]['name']
        # elif endpoint_to_be_used == 'Video Qualities':
        #     entity_to_be_get = context.entity_output_list[entity_name][1]['name']
        # elif endpoint_to_be_used == 'Audio Qualities':
        if invalid_entity_id is not None:
            entity_to_be_get = random_string_generator()
        else:
            entity_to_be_get = context.entity_output_list[entity_name][1]['id']


        entity_response = context.users_obj.get_entity(entity_to_be_get,endpoint_to_be_used)
        context.entity_get_operation_output_list[entity_name] = entity_response


    except Exception as e:
        context.logger.error('user entity get failed using endpoint:{0}'.format(str(e)))
        raise

@Then('user gets "{status_code}" in entity "{entity_name}" return response')
@Then('user gets "{status_code}" and can verify entity "{entity_name}" in get response')
def step_impl(context, status_code,entity_name):
    """
    Keyword implemenation to verify GET call status codes
    :param context:
    :param status_code:return code from the endpoint call
    :param name:name of the user created
    :return:
    """
    users_mgmt = RakutenMgmtClassFunctions(context)
    try:

        if int(status_code) != context.entity_get_operation_output_list[entity_name][0]:
            raise Exception("Status code is not as per expectation, expected: {0}, got: {1}".format
                                (status_code, context.entity_get_operation_output_list[entity_name][0]))

        if status_code ==200:
            users_mgmt.compare_users_json(context.entity_creation_input_list[name]['data']['attributes'],
                                      context.entity_get_operation_output_list[entity_name][1])



        context.logger.info('#############Successfully Verified status code ################## ')

    except Exception as e:
        context.logger.error("user status code/details match failed using endpoint:{0}".format(str(e)))
        raise

@When('user tries to update entity "{entity_name}" by using endpoint "{endpoint_to_be_used}"')
@When('user tries to update entity "{entity_name}" by using endpoint "{endpoint_to_be_used}" but with "{parameter_type}" parameters')
def step_impl(context,entity_name,endpoint_to_be_used,parameter_type= None):
    """
    Keyword implemenation to update entity like Movie/genres/Audio/Video PATCH endpoint of the user.
    :param context:
    :param name:
    :param parameter_type:
    :return:
    """
    try:
        rakuten_mgmt = RakutenMgmtClassFunctions(context)

        if not hasattr(context, 'update_entity_output_list'):
            context.update_entity_output_list = {}

        if not hasattr(context, 'entity_creation_input_list'):
            context.entity_creation_input_list = {}

        if not hasattr(context, 'entity_output_list'):
            context.entity_output_list = {}

        #entity_info_data = rakuten_mgmt.populate_movie_json()
        RakutenMgmtFunctions = RakutenMgmtClassFunctions(context)

        if endpoint_to_be_used == 'Movie':
            entity_info_data = RakutenMgmtFunctions.populate_movie_json()
        elif endpoint_to_be_used == 'Video Qualities':
            entity_info_data = RakutenMgmtFunctions.populate_video_qualities_json()
        elif endpoint_to_be_used == 'Audio Qualities':
            entity_info_data = RakutenMgmtFunctions.populate_audio_qualities_json()
        elif endpoint_to_be_used == 'Genres':
            entity_info_data = RakutenMgmtFunctions.populate_genres_json()


        context.entity_creation_input_list[entity_name] = entity_info_data


        if parameter_type is not None:
            if parameter_type == 'no_payload':
                entity_info_data['data']['attributes'] = {}
            else:
                entity_info_data['data']['attributes'] = {random_string_generator(): random_string_generator()}

        entity_to_be_updated = context.entity_output_list[entity_name][1]['id']

        users_response = context.users_obj.update_entity(endpoint_to_be_used, entity_to_be_updated, entity_info_data)
        context.update_entity_output_list[entity_name] = users_response

    except Exception as e:
        context.logger.error('Entity update failed using endpoint:{0}'.format(str(e)))
        raise

@Then('user gets "{status_code}" in update response of entity "{name}"')
@Then('user gets "{status_code}" and can verify entity details in response json of entity "{name}" under patch response')
def step_impl(context, status_code,name):
    """
    Keyword implemenation to verify PUT call status codes
    :param context:
    :param status_code:return code from the endpoint call
    :param name:name of the user created
    :return:
    """

    try:

        if int(status_code) != context.update_entity_output_list[name][0]:
            raise Exception("Status code is not as per expectation, expected: {0}, got: {1}".format
                                (status_code, context.update_entity_output_list[name][0]))

        context.logger.info('#############Successfully Verified status code ################## ')

    except Exception as e:
        context.logger.error("user status code/details match failed using endpoint:{0}".format(str(e)))
        raise


@When('user tries to delete entity "{entity_name}" by using endpoint "{endpoint_to_be_used}"')
def step_impl(context,entity_name, endpoint_to_be_used):
    """
    Keyword implemenation to delete entity like Movie/genres/Audio/Video info using DELETE endpoint.
    :param context:
    :param name:
    :return:
    """
    try:

        if not hasattr(context, 'delete_users_output_list'):
            context.delete_users_output_list = {}

        if entity_name == 'invalid_entity':
            entity_to_be_deleted = random_string_generator()
        else:
            entity_to_be_deleted = context.entity_output_list[entity_name][1]['id']


        users_response = context.users_obj.delete_user(endpoint_to_be_used, entity_to_be_deleted)

        context.delete_users_output_list[entity_name] = users_response

    except Exception as e:
        context.logger.error('user creation failed using endpoint:{0}'.format(str(e)))
        raise

@Then('user gets "{status_code}" for entity "{entity_name}"')
@Then('user gets "{status_code}" and entity "{entity_name}" is deleted')
def step_impl(context, status_code,entity_name):
    """
    Keyword implemenation to verify DELETE call status codes
    :param context:
    :param status_code:return code from the endpoint call
    :param name:name of the user created
    :return:
    """

    try:

        if int(status_code) != context.delete_users_output_list[entity_name][0]:
            raise Exception("Status code is not as per expectation, expected: {0}, got: {1}".format
                                (status_code, context.delete_users_output_list[entity_name][0]))

        context.logger.info('#############Successfully Verified status code ################## ')

    except Exception as e:
        context.logger.error("Entity status code/details match failed using endpoint:{0}".format(str(e)))
        raise