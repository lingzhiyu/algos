import unittest
import order_alternated_list as solution


class TestSum(unittest.TestCase):
    def test_construct_ll_from_list(self):
        data = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
        head = solution.construct_ll_from_list(data)
        result = solution.get_ll_as_list(head)
        self.assertEqual(data, result)

    def test_solution_1(self):
        data = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
        head = solution.construct_ll_from_list(data)
        target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = solution.solve(head)
        self.assertEqual(target, solution.get_ll_as_list(result))

    def test_solution_2(self):
        data = [1, 41, 5, 32, 8, 8, 10, 7, 1000, 0, 1111]
        head = solution.construct_ll_from_list(data)
        target = [0, 1, 5, 7, 8, 8, 10, 32, 41, 1000, 1111]
        result = solution.solve(head)
        self.assertEqual(target, solution.get_ll_as_list(result))


if __name__ == "__main__":
    unittest.main()
