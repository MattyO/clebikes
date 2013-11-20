from django.test import TestCase
from django.test.simple import DjangoTestSuiteRunner,reorder_suite
from django.conf import settings
from django.utils.unittest.loader import defaultTestLoader

class AppTestSuiteRunner(DjangoTestSuiteRunner):
	def build_suite(self, test_labels, extra_tests=None, **kwargs):
		suite=None

		if test_labels:
			suite = defaultTestLoader.loadTestsFromNames(test_labels)
		else:
			
			test_labels = [app for app in settings.INSTALLED_APPS if not app.startswith(settings.TEST_IGNORE_APPS) ]
			suite = super(AppTestSuiteRunner,self).build_suite(test_labels)
			suite.addTests(defaultTestLoader.discover('libs'))
			#for test in  defaultTestLoader.discover('libs'):
			#	suite.addTest(test)

		return reorder_suite(suite, (TestCase,))



	def run_tests(self, test_labels, extra_tests=None, **kwargs):

	#	if not test_labels:
	#		test_labels = [app for app in settings.INSTALLED_APPS if not app.startswith(settings.TEST_IGNORE_APPS) ]
		return super(AppTestSuiteRunner, self).run_tests(test_labels, extra_tests, **kwargs)
