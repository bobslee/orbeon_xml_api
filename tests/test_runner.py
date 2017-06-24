import unittest
import re

from builder import Builder
from runner import Runner
from utils import xml_from_file


class RunnerTestCase(unittest.TestCase):

    def setUp(self):
        super(RunnerTestCase, self).setUp()

        self.runner_xml = xml_from_file('tests/data', 'test_controls_runner.xml')
        self.builder_xml = xml_from_file('tests/data', 'test_controls_builder.xml')

        self.runner = Runner(self.runner_xml, None, self.builder_xml)

    def test_constructor(self):
        self.assertRaisesRegex(
            Runner(self.runner_xml)
        )

        self.assertRaisesRegex(
            Runner(self.runner_xml, self.builder_xml)
        )

        self.assertRaisesRegex(
            Runner(self.runner_xml, self.builder)
        )

        self.assertRaisesRegex(
            Runner(self.runner_xml, self.builder_xml, self.builder)
        )

        # Ok tests
        runner = Runner(self.runner_xml, None, self.builder_xml)
        self.assertIsInstance(runner, Runner)

        runner = Runner(self.runner_xml, self.builder)
        self.assertIsInstance(runner, Runner)
