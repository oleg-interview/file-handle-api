""" Module provide class FileHandleApi as interface for testing file handle API
"""

import inspect
import requests


class Result(object):
    """ Result handler class
    """

    def __init__(self, status_code=None, text=None, action=None):
        self.status_code = status_code
        self.text = text
        self.action = action

    def __str__(self):
        # return "Action: {:>11};   Code: {:>4};   Message: {:<10}".format(self.action, self.status_code, self.text)
        return "{}\nAction:\n  {}\nCode:\n  {}\nMessage: \n{}".format("="*20, self.action, self.status_code, self.text)


def url_request(url):
    """ Function return result of request by url
    :return:
    """
    result = Result()
    req = requests.get(url)
    result.status_code = req.status_code
    result.text = req.text
    result.action = inspect.getouterframes(inspect.currentframe())[1].function
    return result


class FileHandleApi(object):
    """ File Handle API interface
    """

    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.create_pattern = "http://%s/file/create?name={}&username={}" % self.endpoint
        self.list_pattern = "http://%s/file/list?username={}" % self.endpoint
        self.delete_pattern = "http://%s/file/delete?name={}&username={}" % self.endpoint

    def create_file(self, filename=None, username=None):
        """ api method for creation file
        :param filename:
        :param username:
        :return:
        """
        url = self.create_pattern.format(filename, username)
        return url_request(url)

    def show_list(self, username):
        """ api method for browsing existed files
        :param username:
        :return:
        """
        url = self.list_pattern.format(username)
        return url_request(url)

    def delete_file(self, filename, username):
        """ api method for deleting file
        :param filename:
        :param username:
        :return:
        """
        url = self.delete_pattern.format(filename, username)
        return url_request(url)


if __name__ == "__main__":
    pass
    endpoint = "77.222.149.50:1310"
    fh_api = FileHandleApi(endpoint)

    # data
    VALID_USERNAME = "Abcde"
    VALID_USERNAME = "test"
    INVALID_USERNAME = "/"

    VALID_FILENAME = "File01.txt"
    VALID_FILENAME_NOT_EXIST = "not_exist.file"
    INVALID_FILENAME = "/"

    # examples of usage

    print(fh_api.show_list(username=VALID_USERNAME))
    print(fh_api.show_list(username=INVALID_USERNAME))

    print(fh_api.create_file(filename=VALID_FILENAME, username=VALID_USERNAME))
    print(fh_api.create_file(filename=VALID_FILENAME, username=INVALID_USERNAME))

    print(fh_api.show_list(username=VALID_USERNAME))

    print(fh_api.delete_file(filename=VALID_FILENAME, username=INVALID_USERNAME))
    print(fh_api.delete_file(filename=VALID_FILENAME, username=VALID_USERNAME))
    print(fh_api.delete_file(filename=VALID_FILENAME_NOT_EXIST, username=VALID_USERNAME))

    print(fh_api.show_list(username=VALID_USERNAME))


    # Clean:
    for user in ("Abcde", "test", "testuser"):
        files = fh_api.show_list(username=user).text.split()
        print(user)
        print(files)
        for file in files:
            fh_api.delete_file(filename=file, username=user)
