import logging
import unittest
from api.stu_update import StuUpdate
from data import test_data


class TestStuUpdate(unittest.TestCase):
    # 初始化 StuAdd 类实例
    def setUp(self):
        self.stu_update = StuUpdate()

    def test_update(self):
        response = self.stu_update.update_stu_data(test_data.jsondata_update)
        logging.info("update_status_code={}".format(response.status_code))
        self.assertEqual(200, response.status_code)
