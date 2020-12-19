import os

class Variables:
    def __init__(self):
        self.__sqs_url = os.environ.get('sqs_url', '')
        self.__sqs_url_dest = os.environ.get('sqs_url_dest', '')
        self.__arnvsf = os.environ.get('arnvsf', '')

    def get_sqs_url(self):
        return self.__sqs_url
    def get_sqs_url_dest(self):
        return self.__sqs_url_dest
    def get_arnvsf(self):
        return self.__arnvsf