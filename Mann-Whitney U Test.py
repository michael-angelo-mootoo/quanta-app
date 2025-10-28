import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu as mwu_test
from scipy.stats import tvar, sem, variation

def mean(n):
    mean_v = sum(n) / len(n)
    return mean_v
def range_v(n):
    rnge = max(n) - min(n)
    return rnge
def StDev(n):
    limits = None
    inclusive = (True, True)
    axis = 0
    ddof = 1
    return np.sqrt(tvar(n, limits, inclusive, axis, ddof))
def Q1(n):
    q1_val = np.percentile(n, 25)
    return q1_val
def Q3(n):
    q3_val = np.percentile(n, 75)
    return q3_val
def IQR(n):
    iqr_val = Q3(n) - Q1(n)
    return iqr_val
def quart_dev(n):
    q_deviation = (Q3(n) - Q1(n)) / 2
    return q_deviation
def input_processing(n):
    n = n.split(",")
    nes_n = []
    for j in n:
        nes_n.append(float(j))
    n = nes_n
    return n
def output_data(n1, n2, nm1, nm2):
    d_val = 0.3
    time.sleep(d_val - (d_val/30))
    print("---------------------------------------------------------------------------------------------------------------")
    print(f"Range for {nm1}: {str(range_v(n1))}")
    print(f"Range for {nm2}: {str(range_v(n2))}")
    time.sleep(d_val - (d_val/28))
    print("---------------------------------------------------------------------------------------------------------------")
    print(f"Mean for {nm1}: {str(mean(n1))}")
    print(f"Mean for {nm2}: {str(mean(n2))}")
    time.sleep(d_val - (d_val/26))
    print("---------------------------------------------------------------------------------------------------------------")
    print(f"First / Lower Quartile for {nm1}: {str(Q1(n1))}")
    print(f"First / Lower Quartile for {nm2}: {str(Q1(n2))}")
    time.sleep(d_val - (d_val/24))
    print("---------------------------------------------------------------------------------------------------------------")
    print(f"Third / Upper Quartile for {nm1}: {str(Q3(n1))}")
    print(f"Third / Upper Quartile {nm2}: {str(Q3(n2))}")
    time.sleep(d_val - (d_val/22))
    print("---------------------------------------------------------------------------------------------------------------")
    print(f"Interquartile Range for {nm1}: {str(IQR(n1))}")
    print(f"Interquartile Range for {nm2}: {str(IQR(n2))}")
    time.sleep(d_val - (d_val/20))
    print("---------------------------------------------------------------------------------------------------------------")
    print(f"Quartile Deviation for {nm1}: {str(quart_dev(n1))}")
    print(f"Quartile Deviation for {nm2}: {str(quart_dev(n2))}")
    time.sleep(d_val - (d_val/18))
    print("---------------------------------------------------------------------------------------------------------------")
    print(f"Value Variation for {nm1}: {str(variation(n1))}")
    print(f"Value Variation for {nm2}: {str(variation(n2))}")
    time.sleep(d_val - (d_val/16))
    print("---------------------------------------------------------------------------------------------------------------")
    print(f"Standard Deviation for {nm1}: {str(StDev(n1))}")
    print(f"Standard Deviation for {nm2}: {str(StDev(n2))}")
    time.sleep(d_val - (d_val/14))
    print("---------------------------------------------------------------------------------------------------------------")
    print(f"Standard Error for {nm1}: {str(sem(n1))}")
    print(f"Standard Error for {nm2}: {str(sem(n2))}")
    time.sleep(d_val - (d_val/12))
    print("---------------------------------------------------------------------------------------------------------------")
    Mann_Whitney = mwu_test(n1, n2, alternative='two-sided')
    print(f"Mann-Whitney U Test - Two Tailed (U-Value): {Mann_Whitney[0]}")
    time.sleep(d_val - (d_val/10))
    print(f"Mann-Whitney U Test - Two Tailed (p-Value): {Mann_Whitney[1]}")
    time.sleep(d_val - (d_val/8))
    print("---------------------------------------------------------------------------------------------------------------")
    message = "Given a significance threshold of 0.05, this result is "
    if Mann_Whitney[1] >= 0.05:
        print(f"{message}not significant, thus the null hypothesis cannot be rejected!")
    else:
        print(f"{message}significant, thus the null hypothesis can be rejected!")
def test_cond():
    cond1 = [8, 5, 10, 8, 6, 2, 5, 8, 4, 6] #Black Condition
    cond2 = [5, 4, 5, 6, 4, 3, 5, 5, 3, 4] #Red Condition
    nam1 = "Black (Reference) Condition"
    nam2 = "Red (Experimental) Condition"
    return [cond1, cond2, nam1, nam2]
def reg_cond():
    nam1 = input("Name your First condition (e.g. Black (Reference) Condition): ")
    nam2 = input("Name your Second condition (e.g. Red (Experimental) Condition): ")
    cond1 = input_processing(input(f"Enter the dataset for {nam1}: "))
    cond2 = input_processing(input(f"Enter the dataset for {nam2}: "))
    return [cond1, cond2, nam1, nam2]

print("------------------------------------------------------------------------------------------------------")
print("      MANN-WHITNEY U-TEST CALCULATOR -- TWO TAILED HYPOTHESIS (NON-PARAMETRIC STATISTICAL TEST)")
print("                  (Make sure to input your data using commas as separators)")
print("------------------------------------------------------------------------------------------------------")
op_vals = test_cond()
condition1 = op_vals[0]
condition2 =  op_vals[1]
name1 = op_vals[2]
name2 = op_vals[3]
output_data(condition1, condition2, name1, name2)

x = np.array([name1, name2])
y = np.array([float(mean(condition1)), float(mean(condition2))])

conditions = ['Black (Reference) Condition', 'Red (Experimental) Condition']
mean_anagrams_solved = [float(mean(condition1)), float(mean(condition2))]
std_dev = [StDev(condition1), StDev(condition2)]

plt.figure(figsize=(8, 6))  # Set the figure size
bars = plt.bar(conditions, mean_anagrams_solved, yerr=std_dev, capsize=7, color=['blue', 'red'], width=0.6, zorder=0)
plt.title("Mean number of anagrams solved in Black and Red condition")
plt.ylabel("Mean Number of Anagrams Solved")
plt.ylim(0, 10)
plt.minorticks_on()
plt.grid(True, which='both', linestyle='--', linewidth=0.5, zorder=1)  # Enable major and minor grid lines with dashed lines
plt.errorbar(conditions, mean_anagrams_solved, yerr=std_dev, fmt='o', ecolor='gray', capsize=7)
plt.show()