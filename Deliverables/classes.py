# This file turns the datapoint textfile into a class.

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats



class DataPoint:

    modulation_type: str = None
    mod_order = None
    snr = None
    rotation = None
    constellation= None
    magnitude = None

    def __init__(self, file_name: str) -> None:
        # Open the file
        with open(file_name, 'r') as f:
            # Read the first line
            line = f.readline()

            # Split the line into a list
            line = line.split(',')

            # Set the modulation type
            self.modulation_type = str(line[0])

            # Set the modulation order
            self.mod_order = int(line[1])

            # Set the SNR
            self.snr = float(line[2])

            # Set the rotation
            self.rotation = float(line[3])

            # For each line in the file, add the point to the constellation
            # and magnitude lists
            self.constellation = []
            self.magnitude = []

            for line in f:
                line = line.split(',')
                x = float(line[0])
                y = float(line[1])
                sample = complex(x, y)
                self.constellation.append(sample)


    def plot_constellation(self) -> None:
        # scatter plot the constellation

        x = [i.real for i in self.constellation]
        y = [i.imag for i in self.constellation]

        ax = plt.axes()
        ax.set_facecolor('black')

        plt.scatter(x,y, s=0.5, color='y')
        plt.show()

    def plot_magnitude(self) -> None:
        # plot the magnitude
        plt.plot(self.magnitude)
        plt.show()

    def first_order_cumulant(self):
        # Calculate the first order cumulant
        # This is the mean of the constellation
        return np.mean(np.absolute(self.constellation))

    def second_order_cumulant(self):
        # Calculate the second order cumulant
        # This is the variance
        return np.var(np.absolute(self.constellation))

    def third_order_cumulant(self):
        # Calculate the third order cumulant
        # This is the skewness
        return stats.skew(np.absolute(self.constellation))

    def fourth_order_cumulant(self):
        # Calculate the fourth order cumulant
        # This is the kurtosis
        return stats.kurtosis(np.absolute(self.constellation))


if __name__ == "__main__":
    file = "G:/UNI/23 Spring/Adv Comm 2/Project/archive/Dataset/Dataset/QAM16_4.txt"
    dp = DataPoint(file)

    print(dp.modulation_type)

    print(dp.first_order_cumulant())
    print(dp.second_order_cumulant())
    print(dp.third_order_cumulant())
    print(dp.fourth_order_cumulant())