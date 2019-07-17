"""
设计增加接口的的文件
"""
import requests
import utils


class StuAdd:
    def __init__(self):
        self.stu_add_url = utils.BASE_URL

    def add_stu_data(self, jsondata):
        return requests.post(self.stu_add_url, json=jsondata)


if __name__ == '__main__':
    stu = StuAdd()
    # result = stu.add_stu_data()
