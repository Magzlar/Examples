from math import log, e

class RadioactiveDecayCalculator:
    __auth__ = "Ryan Maguire"
    __vers__ = 1.6

    def __init__(self, initial_amount: float = 0, remaining_amount: float = 0, time_passed: float = 0, half_life: float = 0):
        """Accepts minimum of 3 arugments and returns the 4th missing parameter"""
        if sum(arg != 0 for arg in (initial_amount, remaining_amount, time_passed, half_life)) < 3:
            raise ValueError("At least three parameters must be provided to make an instance of the class")
        
        self.initial_amount = initial_amount
        self.remaining_amount = remaining_amount
        self.time_passed = time_passed
        self.half_life = half_life
        self.__mean_lifetime = -self.half_life / log(2)

        if self.initial_amount == 0:
            self.initial_amount = self.calculate_original_amount()
        elif self.remaining_amount == 0:
            self.remaining_amount = self.calculate_remaining_amount()
        elif self.time_passed == 0:
            self.time_passed = self.calculate_time_passed()
        elif self.half_life == 0:
            self.half_life = self.calculate_half_life()

    @staticmethod
    def convert_half_life_to_mean_lifetime(half_life: float) -> float:
        """Returns mean lifetime from half-life"""
        return half_life / log(2)

    @staticmethod
    def convert_half_life_to_decay_constant(half_life: float) -> float:
        """Returns decay constant from half-life"""
        return log(2) / half_life

    def calculate_original_amount(self) -> float:
        """Returns the original amount of radioactivity (CPM) from time passed (days),
        remaining amount (CPM), and half-life (days)"""
        try:
            return self.remaining_amount * e ** (self.time_passed / abs(self.__mean_lifetime))
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero. Check arguments in the instance.")

    def calculate_remaining_amount(self) -> float:
        """Returns the remaining amount of radioactivity (CPM) after time (days) from the current amount (CPM),
        time passed (days), and half-life (days)"""
        try:
            return self.initial_amount * e ** (-self.time_passed / abs(self.__mean_lifetime))
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero. Check arguments in the instance.")

    def calculate_time_passed(self) -> float:
        """Calculates the amount of time passed (days) from the half-life (days),
        initial amount (CPM), and remaining amount (CPM)"""
        try:
            return abs(self.__mean_lifetime * log(self.initial_amount / self.remaining_amount))
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero. Check arguments in the instance.")

    def calculate_half_life(self) -> float:
        """Calculates the half-life (days) from the time passed (days), initial amount (CPM), and remaining amount (CPM)"""
        try:
            mean_lifetime = self.time_passed / log(self.initial_amount / self.remaining_amount)
            return mean_lifetime*log(2) # convert mean_lifetime to half-life
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero. Check arguments in the instance.")

    def __str__(self):
        values = [
            f"The original amount of radioactivity in the sample is {self.initial_amount:.4F} CPM",
            f"The remaining amount of radioactivity in the sample is {self.remaining_amount:.4F} CPM",
            f"The amount of time passed between readings is {self.time_passed:.4F} days",
            f"The half-life of the radioactive sample is {self.half_life:.4f} days"]

        return "\n".join(values)
    
if __name__ == '__main__':
    """# Example usage
    # Half-life of various radioisotopes in days
    half_life_tritium = 4499.88
    half_life_iodine_125 = 59.49
    half_life_carbon_14 = 2091450

    tritium = RadioactiveDecayCalculator(initial_amount=15000,time_passed=365,half_life=half_life_tritium)
    print(tritium) # printing the class provides a summary of all parameters
    print(tritium.calculate_remaining_amount()) #attaching the method allows for the use of the calculated value elsewhere

    iodine_125 = RadioactiveDecayCalculator(remaining_amount=750,time_passed=59,half_life=59)
    print(iodine_125.calculate_original_amount())

    carbon_14 = RadioactiveDecayCalculator(initial_amount=20000,remaining_amount=10000,half_life=204540)
    print(carbon_14.calculate_time_passed())

    unknown = RadioactiveDecayCalculator(initial_amount=1500,remaining_amount=750,time_passed=59.49)
    print(unknown.calculate_half_life())"""