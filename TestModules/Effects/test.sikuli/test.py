import unittest
import sys
import StringIO
import HTMLTestRunner
import xlrd
setAutoWaitTimeout(10)

class TestUM(unittest.TestCase):
                    
    def test_step2_handleGoalScreen(self):
        print sys.path
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestUM)

fp = file('my_report.html', 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='My unit test',
                description='Test report for searching all Effects in PRE.'
                )
runner.run(suite)
