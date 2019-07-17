import requests
import utils


class StuQuery:
    def __init__(self):
        self.stu_query_url = utils.BASE_URL + "T012"

    def query_stu_data(self):
        return requests.get(self.stu_query_url)
