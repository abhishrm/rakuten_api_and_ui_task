@rakuten_apis_api
Feature: Rakuten API endpoint
description

This feature file contain test the correct behavior of these endpoints related to Rakuten.
• Movies
• Video Qualities
• Audio Qualities
• Genre
Code requisite: This solu


  ##### The test are written in such a way that each test run for four differnt endpoints .For this I have user Scenario Outline feature of behave
@TC-1 @rakuten
Scenario Outline: Create/Get/Update/Delete(POST/PATCH/GET/DELETE) for Movie/Video/Audio/Genres endpoint should be successful with respective status code (Positive case)

When user tries to create entity "E1" using endpoint "<endpoint_to_be_used>"
Then user gets "201" and can verify entity details in response json of user "E1"

When user tries to get entity "E1" by using endpoint "<endpoint_to_be_used>"
Then user gets "200" and can verify entity "E1" in get response

When user tries to update entity "E1" by using endpoint "<endpoint_to_be_used>"
Then user gets "204" and can verify entity details in response json of entity "E1" under patch response

When user tries to delete entity "E1" by using endpoint "<endpoint_to_be_used>"
Then user gets "204" and entity "E1" is deleted

When user tries to get entity "E1" by using endpoint "<endpoint_to_be_used>"
Then user gets "404" in entity "E1" return response

Examples: API
| endpoint_to_be_used |

| Movie |
| Video Qualities  |
| Audio Qualities  |
| Genres  |


@TC-2 @rakuten
Scenario Outline:When user tries to create entity by using POST (/movies, /video_qualities, /audio_qualities. /Genres) with wrong payload or any/all field missing in payload then the user should get 422

When user tries to create entity "E1" using endpoint "<endpoint_to_be_used>" but field "all_the_fields" "missing"
Then user gets "422" and can verify entity details in response json of user "E1"

When user tries to create entity "E1" using endpoint "<endpoint_to_be_used>" but fields "as" "wrong_parameters"
Then user gets "422" and can verify entity details in response json of user "E1"

Examples: API
| endpoint_to_be_used |

| Movie |
| Video Qualities  |
| Audio Qualities  |
| Genres  |


@TC-3 @rakuten
Scenario Outline:When user tries to create entity by using POST (/movies, /video_qualities, /audio_qualities. /Genres) with mandatory parameter missing.

When user tries to create entity "E1" using endpoint "<endpoint_to_be_used>" but field "<field>" "missing"
Then user gets "422" and can verify entity details in response json of user "E1"


Examples: API
| endpoint_to_be_used | field |

| Movie | year                |
| Movie | title                |

| Video Qualities | name                |
| Video Qualities | abbr                |

| Audio Qualities | name                |
| Audio Qualities | abbr                |

|Genres | name                |


@TC-4 @rakuten
Scenario Outline:When user tries to create entity by using POST for (audio/video/genres) with parametric value as "empty string"/"trailing spaces"/"leading spaces"

When user tries to create entity "E1" using endpoint "<endpoint_to_be_used>" but fields "<field>" "empty string"
Then user gets "422" and can verify entity details in response json of user "E1"

When user tries to create entity "E1" using endpoint "<endpoint_to_be_used>" but fields "<field>" "trailing spaces"
Then user gets "422" and can verify entity details in response json of user "E1"

When user tries to create entity "E1" using endpoint "<endpoint_to_be_used>" but fields "<field>" "leading spaces"
Then user gets "422" and can verify entity details in response json of user "E1"

When user tries to create entity "E1" using endpoint "<endpoint_to_be_used>" but fields "<field>" "empty string"
Then user gets "422" and can verify entity details in response json of user "E1"

Examples: API
| endpoint_to_be_used | field |

| Movie | year                |
| Movie | title                |

| Video Qualities | name                |
| Video Qualities | abbr                |

| Audio Qualities | name                |
| Audio Qualities | abbr                |

|Genres | name                |


@TC-5 @rakuten
Scenario Outline:When user tries to GET entity for (movies/audio/video/genres) after entity is deleted from the system or try to GET invalid entity then response should be 404

When user tries to create entity "E1" using endpoint "<endpoint_to_be_used>"
Then user gets "201" and can verify entity details in response json of user "E1"

When user tries to delete entity "E1" by using endpoint "<endpoint_to_be_used>"
Then user gets "204" and entity "E1" is deleted

When user tries to get entity "E1" by using endpoint "<endpoint_to_be_used>"
Then user gets "404" in entity "E1" return response

When user tries to get entity "E1" by using endpoint "<endpoint_to_be_used>"
Then user gets "404" in entity "E1" return response

When user tries to get entity "E1" by using endpoint "<endpoint_to_be_used>" but with "invalid_entity_id"
Then user gets "404" in entity "E1" return response

Examples: API
| endpoint_to_be_used |

| Movie |
| Video Qualities  |
| Audio Qualities  |
| Genres  |


@TC-6 @rakuten
Scenario Outline: When user tries to do PATCH operation for (movies/audio/video/genres) endpoints with invalid parameters.

When user tries to create entity "E1" using endpoint "<endpoint_to_be_used>"
Then user gets "201" and can verify entity details in response json of user "E1"

When user tries to update entity "E1" by using endpoint "<endpoint_to_be_used>" but with "invalid" parameters
Then user gets "422" in update response of entity "E1"

Examples: API
| endpoint_to_be_used |

| Movie |
| Video Qualities  |
| Audio Qualities  |
| Genres  |

@TC-7 @rakuten
Scenario Outline: When user tries to do PATCH operation for (movies/audio/video/genres) endpoint with empty payload parameters

When user tries to create entity "E1" using endpoint "<endpoint_to_be_used>"
Then user gets "201" and can verify entity details in response json of user "E1"

When user tries to update entity "E1" by using endpoint "<endpoint_to_be_used>" but with "no_payload" parameters
Then user gets "422" in update response of entity "E1"

Examples: API
| endpoint_to_be_used |

| Movie |
| Video Qualities  |
| Audio Qualities  |
| Genres  |

@TC-8 @rakuten
Scenario Outline: When user tries to delete entity i.e. (movies/audio/video/genres) by using invalid entity id/non existent id in the system, then user should get 404.

  When user tries to delete entity "invalid_entity" by using endpoint "<endpoint_to_be_used>"
Then user gets "404" for entity "invalid_entity"

Examples: API
| endpoint_to_be_used |

| Movie |
| Video Qualities  |
| Audio Qualities  |
| Genres  |

  ###########################Other test which can be add to the test automation are below but not added due to incomplete information #####################

#We can also validate the length of the accepted characters in each parameter which need to be feeded during POST/PATCH of (movies/audio/video/genres) endpoint
#We can also validate whether the parameter value can accept value with some special characters or not.
#We can also validate that the POST/PUT request shoudl not accept payload containing non-string data.
# GET the endpoint (movies/audio/video/genres) with filter query,pagination,sorting
