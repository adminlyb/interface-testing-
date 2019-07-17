import json
import logging
import unittest

import config
from api.stu_add import StuAdd
from data import test_data


# 加载测试数据
def load_data():
    with open(config.BASE_DIR + "/data/data.json", encoding="utf-8") as f:
        json_data = json.load(f)
    logging.info("json_data={}".format(json_data))
    return json_data


class TestStuAdd(unittest.TestCase):
    # 初始化StuAdd类实例

    def setUp(self):
        self.stu_add = StuAdd()

    def test_add1(self):
        # response = self.stu_add.add_stu_data(load_data())
        response = self.stu_add.add_stu_data(test_data.jsondata)
        logging.info("Add_status_code={}".format(response.status_code))
        self.assertEqual(201, response.status_code)

    # def test_add2(self):
    #     response = self.stu_add.add_stu_data(test_data.jsondata1)
    #     self.assertEqual(201, response.status_code)
    #
    # def test_add3(self):
    #     response = self.stu_add.add_stu_data("")
    #     self.assertEqual(201, response.status_code)
