from . import CommonTestCase


class InputTestCase(CommonTestCase):

    def test_input(self):
        _input = self.builder.controls['input']

        self.assertEqual(_input.label, 'Input Field')
        self.assertEqual(_input.hint, 'Standard input field')
        self.assertEqual(_input.alert, None)
        self.assertEqual(_input.default_value, 'Michelle')

        self.assertEqual(_input.element.label, 'Input Field')
        self.assertEqual(_input.element.hint, 'Standard input field')

        # Doesn't exist, but shouldn't raise Exception
        self.assertEqual(_input.element.alert, None)

    def test_input_bind(self):
        _input = self.builder.controls['input']

        self.assertEqual(_input.bind.id, 'input-bind')
        self.assertEqual(_input.bind.name, 'input')

    def test_input_parent(self):
        _input = self.builder.controls['input']

        self.assertEqual(_input.parent.bind.id, 'text-controls-bind')
        self.assertEqual(_input.parent.bind.name, 'text-controls')
        self.assertEqual(_input.parent.element.label, 'Text Controls')
