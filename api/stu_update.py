import requests
import utils


class StuUpdate:
    def __init__(self):
        self.stu_update_url = utils.BASE_URL + "T012/"

    def update_stu_data(self, jsondata):
        return requests.put(self.stu_update_url, json=jsondata)
