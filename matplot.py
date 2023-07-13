import matplotlib.pyplot as plt


exp_values = [20,40,60,80]
exp_names= [25,45,65,25]
plt.xlabel("number")
plt.ylabel("frequency")
plt.title("bar graph")
plt.hist([exp_values,exp_names],label=[exp_values,exp_names],histtype="barstacked")
plt.legend()
plt.show()
