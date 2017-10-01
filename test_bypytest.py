import pytest
from filehandleapi import FileHandleApi
from username_fixtures import VALID_USERNAMES, INVALID_USERNAMES
from filename_fixtures import VALID_FILENAMES, INVALID_FILENAMES

endpoint = "77.222.149.50:1310"
api = FileHandleApi(endpoint)
VALID_USERNAME = "Abcde"
VALID_FILENAME = "File01.txt"


#
# test username pattern processing by api method LIST
#

@pytest.mark.parametrize("username", VALID_USERNAMES)
def test_valid_usernames(username):
    result = api.show_list(username=username)
    assert result.status_code == 200, "List: Incorrect status code for valid user name"


@pytest.mark.parametrize("username", INVALID_USERNAMES)
def test_invalid_usernames(username):
    result = api.show_list(username=username)
    assert result.status_code == 400 and len(result.text), "List: Incorrect status code or text for invalid user name"


#
# test filename pattern processing by api method CREATE
#

@pytest.mark.parametrize("filename", VALID_FILENAMES)
def test_creation_valid_filenames(filename):
    result = api.create_file(username=VALID_USERNAME, filename=filename)
    api.delete_file(username=VALID_USERNAME, filename=filename)
    assert result.status_code == 200 and result.text == "OK", "Create: Incorrect status code or text for valid file name"


@pytest.mark.parametrize("filename", INVALID_FILENAMES)
def test_creation_invalid_filenames(filename):
    result = api.create_file(username=VALID_USERNAME, filename=filename)
    api.delete_file(username=VALID_USERNAME, filename=filename)
    assert result.status_code == 400 and len(result.text) > 0, "Create: Incorrect status code or text for invalid file name"


def test_creation_file_duplicate():
    api.create_file(username=VALID_USERNAME, filename=VALID_FILENAME)
    api.create_file(username=VALID_USERNAME, filename=VALID_FILENAME)

    result = api.show_list(username=VALID_USERNAME)

    api.delete_file(username=VALID_USERNAME, filename=VALID_FILENAME)
    api.delete_file(username=VALID_USERNAME, filename=VALID_FILENAME)

    number_instance = result.text.splitlines().count(VALID_FILENAME)

    assert number_instance == 1, "Create: There are file with same name"


#
# test filenames by api method DELETE
#

def test_delete_existed_file():
    api.create_file(username=VALID_USERNAME, filename=VALID_FILENAME)
    result = api.delete_file(username=VALID_USERNAME, filename=VALID_FILENAME)
    assert result.status_code == 200 and result.text == "OK", "Delete: Incorrect status code or text"


def test_delete_not_existed_file():
    # Delete existed files
    result = api.show_list(username=VALID_USERNAME)
    number_instance = result.text.splitlines().count(VALID_FILENAME)
    for _ in range(number_instance):
        api.delete_file(username=VALID_USERNAME, filename=VALID_FILENAME)

    # Delete not existed files
    result = api.delete_file(username=VALID_USERNAME, filename=VALID_FILENAME)
    assert result.status_code == 400 and len(result.text) > 0, "Delete: Incorrect status code or no text"
