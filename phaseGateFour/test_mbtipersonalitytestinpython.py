import unittest
import mbtipersonalitytestinpython

class TestMbtiPersonalityTest(unittest.TestCase):
		def test_that_get_user_input_function_exist(self):

			survey = [[""]*2 for _ in range(20)]
			mbtipersonalitytestinpython.get_user_input(survey)
		
		def test_that_get_user_input_receives_correct_input(self):
			character = ["A","B"]
			expected = ["A","B"]

			self.assertEqual(mbtipersonalitytestinpython.get_user_input(character), expected)
		
		def test_that_display_introverts_vs_extroverts_results_function_exist(self):
			survey = [[""]*2 for _ in range(20)]

			options= [["A","B"]]*20
		
			answers = ["A","B","A","B","A","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A"]

			name = "interesting"

			personality_type = [""]*4
		

			mbtipersonalitytestinpython.display_introverts_vs_extroverts_results(answers, survey, options, name, personality_type)


		def test_that_display_introverts_vs_extroverts_results_function_returns_result(self):
			survey = [[""]*2 for _ in range(20)]

			options= [["A","B"]]*20
		
			answers = ["A","B","A","B","A","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A"]

			name = "interesting"

			personality_type = [""]*4
		

			expected = "I"
			mbtipersonalitytestinpython.display_introverts_vs_extroverts_results(answers, survey, options, name, personality_type)
			self.assertEqual(personality_type[0], expected)


		def test_that_display_sensing_vs_intuitive_results_function_returns_result(self):
			survey = [[""]*2 for _ in range(20)]

			options= [["A","B"]]*20
		
			answers = ["A","B","A","B","A","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A"]


			personality_type = [""]*4
		

			expected = "N"
			mbtipersonalitytestinpython.display_sensing_vs_intuitive_results(answers, survey, options, personality_type)
			self.assertEqual(personality_type[1], expected)


		def test_that_display_thinking_vs_feeling_results_function_returns_result(self):
			survey = [[""]*2 for _ in range(20)]

			options= [["A","B"]]*20
		
			answers = ["A","B","A","B","A","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A"]


			personality_type = [""]*4
		

			expected = "F"
			mbtipersonalitytestinpython.display_thinking_vs_feeling_results(answers, survey, options, personality_type)
			self.assertEqual(personality_type[2], expected)



		def test_that_display_judging_vs_perceptive_inputs_function_returns_result(self):
			survey = [[""]*2 for _ in range(20)]

			options= [["A","B"]]*20
		
			answers = ["A","B","A","B","A","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A"]

			personality_type = [""]*4
		

			expected = "P"
			mbtipersonalitytestinpython.display_judging_vs_perceptive_inputs(answers, survey, options, personality_type)
			self.assertEqual(personality_type[3], expected)
	
	