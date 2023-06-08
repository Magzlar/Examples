import math
import Levenshtein

class Radioactive:
    e = math.log(2)  # Euler's number remains constant

    def __init__(self, nt: float, t: float):
        """Class receives three parameters:
        nt = The amount of radioactivity in the sample when received,
        t = The time passed since the sample was received,
        T = The type of isotope - Tritium or Iodine"""
        self.nt = nt
        self.t = t
        choice = input("Are you using 1) Tritium? or 2) Iodine 125? :")
        if self.is_approximate_match(choice, ["1", "tritium"]):
            self.T = 365 * 12.5
        elif self.is_approximate_match(choice, ["2", "iodine"]):
            self.T = 59.86
        else:
            raise ValueError("Invalid choice.")

    @staticmethod
    def is_approximate_match(word, expected_words, threshold=2):
        for expected_word in expected_words:
            distance = Levenshtein.distance(word.lower(), expected_word.lower())
            if distance <= threshold:
                return True
        return False

    def decay(self):
        return self.nt * Radioactive.e ** (self.t / self.T)

    def __str__(self):
        return f"The CPM of your sample is now {self.decay()}"

if __name__ == '__main__':
    answer1 = Radioactive(1500, 15)
    print(answer1.decay())
