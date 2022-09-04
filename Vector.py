# Q(9): Create a random vector of size 30 and find the mean value.
import numpy as np

ran_vec = np.random.random(30)
ran_len = len(ran_vec)
ran_sum = np.sum(ran_vec)
mean_value = ran_sum / ran_len
print("Mean Value of Random Vector Size of 30 : %d " % mean_value)
