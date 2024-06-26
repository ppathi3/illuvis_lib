import matplotlib.pyplot as plt

def create_custom_bar_chart(data, title="Bar Chart", xlabel="X-axis", ylabel="Y-axis", color="blue"):
    plt.figure(figsize=(10, 6))
    plt.bar(data.keys(), data.values(), color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
