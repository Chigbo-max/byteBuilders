import unittest
from fireDrill.stack import Stack, Queue


class MyStackTest(unittest.TestCase):

    def setUp(self):
        self.stack = Stack(3)
    def test_that_stack_pushes_an_element_into_stack(self):
        self.assertTrue(self.stack.empty())
        self.stack.push(5)
        self.stack.push(3)
        self.stack.push(11)
        expect = 3
        self.assertEqual(len(self.stack.getItems()), expect)

    def test_that_stack_pops_an_element_into_stack(self):
        self.assertTrue(self.stack.empty())
        self.stack.push(5)
        self.stack.push(3)
        self.stack.push(11)
        expect = 3
        self.assertEqual(len(self.stack.getItems()), expect)
        self.stack.pop()
        expect2 = 2
        self.assertEqual(len(self.stack.getItems()), expect2)

    def test_that_stack_returns_current_element_pushed_into_stack(self):
        self.assertTrue(self.stack.empty())
        self.stack.push(5)
        self.stack.push(3)
        self.stack.push(11)
        expect = 3
        self.assertEqual(len(self.stack.getItems()), expect)
        expect2 = 11
        self.assertEqual((self.stack.peek()), expect2)

    def test_that_stack_throws_error_if_stack_is_full(self):
        self.stack = Stack(3)
        self.stack.push(5)
        self.stack.push(3)
        self.stack.push(11)
        self.assertRaises(ValueError, self.stack.push, 13)


class MyqueueTest(unittest.TestCase):
    
    def setUp(self):
        self.queue = Queue(3)
        
    def test_that_queue_enqueues_an_element_into_queue(self):
        self.assertTrue(self.queue.empty())
        self.queue.enqueue(22)
        self.queue.enqueue(10)
        self.queue.enqueue(12)
        expect = 3
        self.assertEqual(len(self.queue.getItems()), expect)

    def test_that_queue_dequeues_an_element_from_queue(self):
        self.assertTrue(self.queue.empty())
        self.queue.enqueue(22)
        self.queue.enqueue(10)
        self.queue.enqueue(12)
        expect = 3
        self.assertEqual(len(self.queue.getItems()), expect)
        self.queue.dequeue()
        expect2 = 2
        self.assertEqual(len(self.queue.getItems()), expect2)

    def test_that_queue_displays_most_current_element(self):
        self.queue.enqueue(22)
        self.queue.enqueue(10)
        self.queue.enqueue(12)
        self.queue.dequeue()
        expect = 10
        self.assertEqual(self.queue.front(), expect)

    def test_that_queue_throws_error_if_queue_is_full(self):
        self.queue.enqueue(22)
        self.queue.enqueue(10)
        self.queue.enqueue(12)
        self.assertRaises(ValueError, self.queue.enqueue, 23)