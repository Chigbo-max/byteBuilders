class CompoundInterestCalculator:


    def calculate_compound_interest(self):
        try:
            principal = self.collect_float_input("Enter initial investment amount: ")
            interest_rate = self.collect_float_input("Enter annual interest rate e.g 5: ")/100
            compound_frequency = self.collect_float_input("Enter compound frequency: ")
            time = self.collect_int_input("Enter number of years: ")
            monthly_contribution = self.collect_float_input("Enter monthly contribution: ")
            interest_factor_result = self.get_interest_factor_result(interest_rate, compound_frequency, time)
            compound_interest = interest_factor_result * principal
            denominator = interest_rate / compound_frequency
            interest_factor_from_contribution = (interest_factor_result - 1) / denominator
            contribution_compound_interest = monthly_contribution * interest_factor_from_contribution
            total_amount = compound_interest + contribution_compound_interest
            print(f'The final amount after {time} years with ${monthly_contribution:,.2f} contributions is ${total_amount:,.2f}')
        except ValueError:
            print("Invalid input. Please try again.")


    def get_interest_factor_result(self,interest_rate, compound_frequency, time):
        interest_factor = 1 + (interest_rate / compound_frequency)
        interest_factor_result = interest_factor ** (compound_frequency * time)
        return interest_factor_result

    def collect_float_input(self, prompt):
        try:
            float_input = float(input(prompt))
            return float_input
        except ValueError:
            print("Invalid input. Please try again.")
            return self.collect_float_input(prompt)

    def collect_int_input(self, prompt):
        try:
            int_input = int(input(prompt))
            return int_input
        except ValueError:
            print("Invalid input. Please try again.")
            return self.collect_int_input(prompt)


CompoundInterestCalculator().calculate_compound_interest()
