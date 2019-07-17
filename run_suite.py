import logging
import time
import unittest

from case.test_AddCase import TestStuAdd
from case.test_DeleteCase import TestStuDelete
from case.test_QueryCase import TestStuQuery
from case.test_UpdateCase import TestStuUpdate
from tools.HTMLTestRunner import HTMLTestRunner

try:
    # 构建测试套件
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestStuAdd))
    suite.addTest(unittest.makeSuite(TestStuQuery))
    suite.addTest(unittest.makeSuite(TestStuUpdate))
    suite.addTest(unittest.makeSuite(TestStuDelete))

    report_file = "./report/report{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
    with open(report_file, "wb") as f:
        runner = HTMLTestRunner(f, title="学生管理系统", description="Win10.V1.0")
        runner.run(suite)
except Exception as e:
    logging.exception(e)
finally:
	pass
    
