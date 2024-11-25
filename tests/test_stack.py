import unittest
from fireDrill.stack import Stack


class MyTestCase(unittest.TestCase):
    def test_that_stack_pushes_an_element_into_stack(self):
        stack = Stack(3)
        self.assertTrue(stack.empty())
        stack.push(5)
        stack.push(3)
        stack.push(11)
        expect = 3
        self.assertEqual(len(stack.getItems()), expect)

    def test_that_stack_pops_an_element_into_stack(self):
        stack = Stack(3)
        self.assertTrue(stack.empty())
        stack.push(5)
        stack.push(3)
        stack.push(11)
        expect = 3
        self.assertEqual(len(stack.getItems()), expect)
        stack.pop()
        expect2 = 2
        self.assertEqual(len(stack.getItems()), expect2)

    def test_that_stack_returns_current_element_pushed_into_stack(self):
        stack = Stack(3)
        self.assertTrue(stack.empty())
        stack.push(5)
        stack.push(3)
        stack.push(11)
        expect = 3
        self.assertEqual(len(stack.getItems()), expect)
        expect2 = 11
        self.assertEqual((stack.peek()), expect2)

    def test_that_stack_throws_error_if_stack_is_full(self):
        stack = Stack(3)
        stack.push(5)
        stack.push(3)
        stack.push(11)
        self.assertRaises(ValueError, stack.push, 13)
