import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Data input (you can edit this data directly)
data = {
    "labels": ["A", "B", "C", "D", "E", "F"],
    "values": [65, 20, 70, 40, 10, 65 ]
}

def display_menu():
    print("Hello!")
    print("Select the type of graph you want to create:")
    print("1. Line Graph")
    print("2. Bar Graph")
    print("3. Pie Chart")
    print("4. 3D Bar Graph")
    choice = input("Enter your choice (1/2/3/4): ")
    return choice

def plot_line_graph(labels, values):
    plt.plot(labels, values, marker='o')
    plt.title("Line Graph")
    plt.xlabel("Labels")
    plt.ylabel("Values")
    plt.grid()
    plt.show()

def plot_bar_graph(labels, values):
    plt.bar(labels, values)
    plt.title("Bar Graph")
    plt.xlabel("Labels")
    plt.ylabel("Values")
    plt.show()

def plot_pie_chart(labels, values):
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Pie Chart")
    plt.show()

def plot_3d_bar_graph(labels, values):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x_pos = np.arange(len(labels))  # Position on the x-axis
    y_pos = np.zeros(len(labels))   # Position on the y-axis (set to 0 as 2D data projected in 3D)
    z_pos = np.zeros(len(labels))   # Starting height

    dx = np.ones(len(labels))       # Width of each bar in x direction
    dy = np.ones(len(labels))       # Depth of each bar in y direction
    dz = values                     # Height of each bar

    ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color='b', zsort='average')
    ax.set_title("3D Bar Graph")
    ax.set_xlabel("Labels")
    ax.set_ylabel("Y")
    ax.set_zlabel("Values")

    ax.set_xticks(x_pos)
    ax.set_xticklabels(labels)

    plt.show()

def main():
    choice = display_menu()
    labels = data["labels"]
    values = data["values"]
    
    if choice == "1":
        plot_line_graph(labels, values)
    elif choice == "2":
        plot_bar_graph(labels, values)
    elif choice == "3":
        plot_pie_chart(labels, values)
    elif choice == "4":
        plot_3d_bar_graph(labels, values)
    else:
        print("Invalid choice. Please run the program again.")

if __name__ == "__main__":
    main()
