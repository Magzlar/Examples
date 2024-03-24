from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from math import log, e


class RadioactiveDecayCalculator:
    '''Contains the logic for GUI, enter 3 parameters the class returns the 4th'''
    def __init__(self, initial_amount: float = 0, remaining_amount: float = 0, time_passed: float = 0, half_life: float = 0):
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

    def calculate_original_amount(self) -> float:
        return self.remaining_amount * e ** (self.time_passed / abs(self.__mean_lifetime))

    def calculate_remaining_amount(self) -> float:
        return self.initial_amount * e ** (-self.time_passed / abs(self.__mean_lifetime))

    def calculate_time_passed(self) -> float:
        return abs(self.__mean_lifetime * log(self.initial_amount / self.remaining_amount))

    def calculate_half_life(self) -> float:
        mean_lifetime = self.time_passed / log(self.initial_amount / self.remaining_amount)
        return mean_lifetime * log(2)

    def __str__(self):
        values = [
            f"The original amount of radioactivity in the sample is {self.initial_amount:.4F} CPM",
            f"The remaining amount of radioactivity in the sample is {self.remaining_amount:.4F} CPM",
            f"The amount of time passed between readings is {self.time_passed:.4F} days",
            f"The half-life of the radioactive sample is {self.half_life:.4f} days"]
        return "\n".join(values)


def calculate():
    try:
        inputs = [initial_var.get(), remaining_var.get(), time_var.get(), half_life_var.get()]
        inputs = [float(i) if i else 0 for i in inputs]
        calculator = RadioactiveDecayCalculator(*inputs)
        result_message = str(calculator)
        messagebox.showinfo("Calculation Result", result_message)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

#intialise the winodow
root = Tk()
root.title("Radioactive Decay Calculator")
# Explanation of the calculator 
explanation_text = ("Enter at least three of the following parameters"
                    " and the calculator will compute the missing one")
Label(root, text=explanation_text, wraplength=400).grid(row=0, column=0, columnspan=2, sticky="w")

# declar variables
initial_var = StringVar()
remaining_var = StringVar()
time_var = StringVar()
half_life_var = StringVar()

# initial amount fields
Label(root, text="Initial Amount (CPM):").grid(row=1, column=0, sticky="w")
Entry(root, textvariable=initial_var).grid(row=1, column=1)

# remaining amount fields
Label(root, text="Remaining Amount (CPM):").grid(row=2, column=0, sticky="w")
Entry(root, textvariable=remaining_var).grid(row=2, column=1)

# time passed fields
Label(root, text="Time Passed (days):").grid(row=3, column=0, sticky="w")
Entry(root, textvariable=time_var).grid(row=3, column=1)

# half-life field, in days
Label(root, text="Half-Life (days):").grid(row=4, column=0, sticky="w")
Entry(root, textvariable=half_life_var).grid(row=4, column=1)

# calc button
Button(root, text="Calculate", command=calculate).grid(row=4, column=0, columnspan=2)

# run the main program
root.mainloop()


