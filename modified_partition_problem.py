"""
This is a solution to Mathologer's "What comes next?" puzzle at the end of his video:
The hardest "What comes next?" (Euler's pentagonal formula)
https://youtu.be/iJ8pnCO0nTY?t=2960

The approach in answering this problem is presented in the same video at 4:00 minutes into the video:
https://youtu.be/iJ8pnCO0nTY?t=241

For example, for integer 4, 4 blocks represents the number 4 that is gonna be chopped, between the blocks are 3 gaps.
The different ways of splitting up the integer 4 corresponds to the different ways of opening and closing those 3 gaps.
"""

import itertools
import numpy as np


class PartitionProblem:
    """
        Takes in an integer and returns the sum of the products of each representation of the integer as the sum of positive
        integers.

        Example:
            The integer 4 can be written in 8 different ways as a sum of positive integers
            4
            3+1
            1+3
            2+2
            2+1+1
            1+2+1
            1+1+2
            1+1+1+1

        The script then takes the product of the positive integers in each representations
            4 = 4
            3*1 = 3
            1*3 = 3
            2*2 = 4
            2*1*1 = 2
            1*2*1 = 2
            1*1*2 = 2
            1*1*1*1 = 1

        Then returns the sum of all the products
            4+3+3+4+2+2+2+1 = 21

        So integer 4 returns 21

            * * *
            Parameters:
                integer (int): An integer

            Returns:
                sum_all (int): An integer
        """
    def __init__(self, integer):
        self.integer = int(integer)
        self.bin_list = ["".join(seq) for seq in itertools.product("01", repeat=integer-1)]
        self.num_partitions = [[] for _ in range(len(self.bin_list))]

    def get_int_partition(self):
        # this is where all the magic happens lol,
        for i, bin_partition in enumerate(self.bin_list):
            # all integers representations starts at at least 1
            factor = 1
            for j, binary in enumerate(bin_partition):
                # if the gap is "closed" add 1 to the factor
                if binary == '0':
                    factor += 1
                else:
                    # if the gap is "open" append the factor as an integer representation and reset factor to 1
                    self.num_partitions[i].append(factor)
                    factor = 1
                if j == len(bin_partition) - 1:
                    # if at the last gap, append the factor
                    self.num_partitions[i].append(factor)
        return self.num_partitions

    def get_sum(self):
        self.get_int_partition()
        sum_all = 0
        for num_partition in self.num_partitions:
            sum_all += np.prod(num_partition)
        return sum_all
