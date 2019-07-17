import requests
import utils


class StuDelete:
    def __init__(self):
        self.stu_delete_url = utils.BASE_URL + "T012/"

    def delete_stu_data(self):
        return requests.delete(self.stu_delete_url)
