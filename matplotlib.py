import pandas as pd
from matplotlib import pyplot as plt


# =========================
# 1. Linear and Quadratic Plots
# =========================

x_values = list(range(-10, 11))

# Linear function: y = 2x + 1
linear_values = [2 * x + 1 for x in x_values]

plt.scatter(x_values, linear_values, color="blue", label="Data")
plt.title("Linear Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

# Quadratic function: y = x^2 - 3x + 2
quadratic_values = [x**2 - 3 * x + 2 for x in x_values]

plt.plot(x_values, quadratic_values, color="red", label="Data")
plt.title("Quadratic Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()


# =========================
# 2. Students' Scores (Bar Charts)
# =========================

students = ["Anna", "Bartek", "Cezary", "Daria", "Ela"]
math_scores = [78, 88, 95, 72, 80]
physics_scores = [85, 79, 92, 68, 82]
chemistry_scores = [92, 85, 88, 74, 78]

plt.figure(figsize=(12, 8))

plt.subplot(1, 3, 1)
plt.bar(students, math_scores)
plt.title("Mathematics")
plt.xlabel("Students")
plt.ylabel("Score")

plt.subplot(1, 3, 2)
plt.bar(students, physics_scores)
plt.title("Physics")
plt.xlabel("Students")
plt.ylabel("Score")

plt.subplot(1, 3, 3)
plt.bar(students, chemistry_scores)
plt.title("Chemistry")
plt.xlabel("Students")
plt.ylabel("Score")

plt.tight_layout()
plt.show()


# =========================
# 3. Weekly Step Count Analysis
# =========================

df = pd.read_excel(
    "Data_Pandas.xlsx",
    sheet_name="Sheet1",
)

plt.figure(figsize=(10, 6))

days_of_week = df.columns[1:].tolist()
user_names = df["FirstName"].tolist()

line_styles = ["-", "--", "-."]
colors = ["blue", "green", "red"]
markers = ["o", "s", "^"]

# Plot step counts for each user
for i in range(len(user_names)):
    steps = df.iloc[i, 1:].tolist()
    plt.plot(
        days_of_week,
        steps,
        linestyle=line_styles[i],
        color=colors[i],
        marker=markers[i],
        label=user_names[i],
    )

# Highlight maximum step count for each user
for i in range(len(user_names)):
    steps = df.iloc[i, 1:].tolist()
    max_index = steps.index(max(steps))
    plt.scatter(
        days_of_week[max_index],
        steps[max_index],
        color=colors[i],
        marker="*",
        s=150,
        label=f"Highest step count - {user_names[i]}",
    )

plt.title("Users' Weekly Step Count")
plt.xlabel("Day of the Week")
plt.ylabel("Number of Steps")
plt.legend()
plt.grid(True)

plt.show()