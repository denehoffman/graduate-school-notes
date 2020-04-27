import numpy as np
N = 1000000
p = 0.01
alpha = 0.98
beta = 0.001
has_disease = np.random.choice([True, False], size=N, p=[p, 1 - p])
tests_positive = np.empty(N, dtype=bool)
tests_positive_twice = np.empty(N, dtype=bool)
tests_positive_thrice = np.empty(N, dtype=bool)


def test(has_disease):
    if has_disease:
        return np.random.rand() < alpha
    else:
        return np.random.rand() < beta


for patient in range(N):
    tests_positive[patient] = test(has_disease[patient])
    if tests_positive[patient]:
        tests_positive_twice[patient] = test(has_disease[patient])
    if tests_positive_twice[patient]:
        tests_positive_thrice[patient] = test(has_disease[patient])


tests_correct = np.logical_xor(has_disease, tests_positive)
tests_correct_twice = np.logical_xor(has_disease, tests_positive_twice)
tests_correct_thrice = np.logical_xor(has_disease, tests_positive_thrice)
print("Percent misdiagnosed after a single test: {0:.5f}%".format(np.sum(tests_correct) / N * 100))
print("Percent misdiagnosed after two tests:     {0:.5f}%".format(np.sum(tests_correct_twice) / N * 100))
print("Percent misdiagnosed after three tests:   {0:.5f}%".format(np.sum(tests_correct_thrice) / N * 100))
