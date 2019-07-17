import logging
import unittest

from api.stu_delete import StuDelete
from data import test_data


class TestStuDelete(unittest.TestCase):
    # 初始化 StuAdd 类实例
    def setUp(self):
        self.stu_delete = StuDelete()

    def test_delete(self):
        # 调用添加方法
        response = self.stu_delete.delete_stu_data()
        logging.info("delete_status_code={}".format(response.status_code))
        self.assertEqual(204, response.status_code)
