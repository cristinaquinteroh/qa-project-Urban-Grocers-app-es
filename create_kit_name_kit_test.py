import data
import sender_stand_request


def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = kit_name
    return current_kit_body


def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]


def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert kit_body["name"] == response.json()["name"]


def negative_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400


def test_1_kit_name_with_1_character():
    current_kit_body = get_kit_body("a")
    positive_assert(current_kit_body)


def test_2_kit_name_with_511_characters():
    current_kit_body = get_kit_body(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    )
    positive_assert(current_kit_body)


def test_3_kit_without_name():
    current_kit_body = get_kit_body("")
    negative_assert(current_kit_body)


def test_4_kit_name_with_512_characters():
    current_kit_body = get_kit_body(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    )
    negative_assert(current_kit_body)


def test_5_kit_name_with_special_characters():
    current_kit_body = get_kit_body('№%@",')
    positive_assert(current_kit_body)


def test_6_kit_name_with_spaces():
    current_kit_body = get_kit_body(" A Aaa ")
    positive_assert(current_kit_body)


def test_7_kit_name_with_numbers_as_string():
    current_kit_body = get_kit_body("123")
    positive_assert(current_kit_body)


def test_8_kit_body_without_name_parameter():
    current_kit_body = data.kit_body.copy()
    current_kit_body.pop("name")
    negative_assert(current_kit_body)


def test_9_kit_name_with_wrong_data_type():
    current_kit_body = get_kit_body(123)
    negative_assert(current_kit_body)