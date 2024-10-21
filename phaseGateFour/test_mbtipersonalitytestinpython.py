import unittest
import mbtipersonalitytestinpython

class TestMbtiPersonalityTest(unittest.TestCase):
		def test_that_get_user_input_function_exist(self):

			survey = [[0]*2 for _ in range(20)]
			mbtipersonalitytestinpython.get_user_input(survey)
		
		def test_that_get_user_input_receives_correct_input(self):
			character = ["A","B"]
			expected = ["A","B"]

			self.assertEqual(mbtipersonalitytestinpython.get_user_input(character), expected)
		
		def test_that_display_introverts_vs_extroverts_results_function_exist(self):
			survey = [""*2 for _ in range(20)]

			options= [["A","B"]]*20
		
			answers = ["A","B","A","B","A","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A"]

			name = "interesting"

			personality_type = [0]*4
		

			mbtipersonalitytestinpython.display_introverts_vs_extroverts_results(answers, survey, options, name, personality_type)


		def test_that_display_introverts_vs_extroverts_results_function_returns_result(self):
			survey = [[0]*2 for _ in range(20)]

			options= [["A","B"]]*20
		
			answers = ["A","B","A","B","A","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A"]

			name = "interesting"

			personality_type = [0]*4
		

			expected = "I"
		
			self.assertEqual(mbtipersonalitytestinpython.display_introverts_vs_extroverts_results(answers, survey, options, name, personality_type), expected)

	
	