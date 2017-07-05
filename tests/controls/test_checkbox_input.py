from . import CommonTestCase

from orbeon_xml_api.controls import BooleanControl


class CheckboxInputTestCase(CommonTestCase):

    def setUp(self):
        super(CheckboxInputTestCase, self).setUp()
        self.control = self.builder.controls['checkbox-input']

    def test_control(self):
        self.assertIsInstance(self.control, BooleanControl)

    def test_builder_bind(self):
        self.assertEqual(self.control.bind.id, 'checkbox-input-bind')
        self.assertEqual(self.control.bind.name, 'checkbox-input')

    def test_builder_parent(self):
        self.assertEqual(self.control.parent.bind.id, 'selection-controls-bind')
        self.assertEqual(self.control.parent.bind.name, 'selection-controls')
        self.assertEqual(self.control.parent.element.label, 'Selection Controls')

    def test_builder_form(self):
        self.assertEqual(self.control.element.label, 'Single Checkbox')
        self.assertEqual(self.control.element.hint, 'An input which captures "true" or "false"')

        self.assertEqual(self.control.label, 'Single Checkbox')
        self.assertEqual(self.control.hint, 'An input which captures "true" or "false"')

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, 'false')
        self.assertEqual(self.control.default_value, False)

    def test_runner_form(self):
        self.assertEqual(self.runner.get_raw_value('checkbox-input'), 'true')
        self.assertEqual(self.runner.get_value('checkbox-input'), True)
        self.assertEqual(self.runner.form.yesnoinput, True)
