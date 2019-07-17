import logging
import unittest
from api.stu_query import StuQuery
from data import test_data


class TestStuQuery(unittest.TestCase):
    # 初始化 StuAdd 类实例
    def setUp(self):
        self.stu_query = StuQuery()

    def test_query(self):
        response = self.stu_query.query_stu_data()
        logging.info("query_status_code={}".format(response.status_code))
        self.assertEqual(200, response.status_code)

