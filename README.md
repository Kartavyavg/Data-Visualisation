
# 📊 Python CLI Graph Visualizer

This is an interactive **Command-Line Interface (CLI)** tool built in Python that allows users to visualize a given dataset in various formats including **Line Graph**, **Bar Graph**, **Pie Chart**, and **3D Bar Graph**. It’s great for beginners learning data visualization or anyone who needs quick visual insights from small datasets.

---

## 🧠 Overview

The application reads a pre-defined dataset containing labels and numerical values and presents users with a menu to choose a visualization type. Upon selection, the corresponding graph is rendered using **Matplotlib**, a powerful Python plotting library. The 3D plotting is supported by **mpl\_toolkits.mplot3d** and numerical processing via **NumPy**.

---

## 🎯 Features

* **Line Graph**: Ideal for visualizing trends over ordered categories.
* **Bar Graph**: Useful for comparing individual category values.
* **Pie Chart**: Displays proportions and relative sizes of categories.
* **3D Bar Graph**: Offers a visually rich way to present bar data in 3D space.

Each graph includes:

* Title
* Axis labels (where applicable)
* Color styling for better readability

---

## 🧰 Technologies Used

* **Python 3**: Programming language
* **Matplotlib**: For all 2D and 3D visualizations
* **NumPy**: For efficient numeric operations

---

## 🗂 File Structure

```
project-root/
│
├── app.py         # Main application file with all logic
└── README.md      # Project documentation (you're reading it!)
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/graph-visualizer-cli.git
cd graph-visualizer-cli
```

### 2. Install Required Libraries

Use `pip` to install the required Python libraries:

```bash
pip install matplotlib numpy
```

### 3. Run the Application

```bash
python app.py
```

---

## 🧪 Sample Data

The data is hardcoded inside `app.py` and can be modified as needed:

```python
data = {
    "labels": ["A", "B", "C", "D", "E", "F"],
    "values": [65, 20, 70, 40, 10, 65]
}
```

To visualize your own data, just replace the `labels` and `values` lists with your desired values.

---

## 🖼 Example Output

Here’s what each graph represents:

### Line Graph

Shows how values change across different categories.

```
X-axis: Labels → A, B, C, ...
Y-axis: Values → 65, 20, ...
```

### Bar Graph

Vertical bars representing each value.

### Pie Chart

Slices proportional to the values.

### 3D Bar Graph

A 3-dimensional bar chart for more advanced visual appeal.

*You can take screenshots while running to include them here.*

---

## 🧑‍💻 How It Works

1. When you run `app.py`, a CLI menu is displayed:

   ```
   Hello!
   Select the type of graph you want to create:
   1. Line Graph
   2. Bar Graph
   3. Pie Chart
   4. 3D Bar Graph
   ```

2. Based on user input, the respective plotting function is triggered.

3. The selected graph is displayed using `matplotlib.pyplot`.

---

## 👨‍🏫 Ideal Use Cases

* Educational demos for students learning data visualization
* Quick mock-up visualizations for small datasets
* Prototyping UI ideas without full web dashboards

---

## 🔒 License

This project is licensed under the **MIT License**, allowing anyone to use, modify, and distribute the code with proper attribution.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

* Submit bug reports
* Improve UI or plotting functionality
* Add support for dynamic CSV/JSON file input
* Create new graph types (e.g., scatter plots, histograms)

To contribute:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a Pull Request

---

## 📬 Contact

For questions, suggestions, or collaboration opportunities, feel free to open an issue or email at **[kartavyavgupta@gmail.com](mailto:kartavyavgupta@gmail.com)**

---

