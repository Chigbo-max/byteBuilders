class Calculation:

    def get_interest_factor_result(self, interest_rate, compound_frequency, time)->float:
        if interest_rate < 1 or time < 1 or compound_frequency < 1:
            raise Exception("Input cannot be less than 1")

        else:
            interest_factor = 1 + (interest_rate / compound_frequency)
            interest_factor_result = interest_factor ** (compound_frequency * time)
            return interest_factor_result


    def get_compound_interest(self, interest_factor_result, principal):
        compound_interest = interest_factor_result * principal
        return compound_interest

    def get_interest_factor_from_contribution(self, interest_rate, compound_frequency, time):
        interest_factor_from_contribution = (self.get_interest_factor_result(interest_rate, compound_frequency, time) - 1) / get_denominator(interest_rate, compound_frequency)
        return interest_factor_from_contribution


    def get_denominator(self, interest_rate, compound_frequency):
        denominator = interest_rate / compound_frequency
        return denominator
