

class CalculateInterest:

    def __init__(self, initial_balance, interest_rate, num_interest_applied, num_periods):
        #self._final_amount = final_amount
        self._initial_balance = inital_balance
        self._interest_rate = interest_rate
        self._num_interest_applied = num_interest_applied
        self._num_periods = num_periods

    def calc_interest(self):

        final_amount = self._initial_balance * (1 + (self._interest_rate / self._num_interest_applied)) ** (self._num_interest_applied * self._num_periods)
        return final_amount
