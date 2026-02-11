# ======================
# Project Name: Day 101 - Linear regression enrollment forecast
# Section: Advance Python Projects
# Description: Python results table + plot + CSV export
# ======================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

FORECAST_YEARS = 5


def main():

    # -----------------------------
    # Paths
    # -----------------------------
    data_file = Path("data") / "enrollment.csv"
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    if not data_file.exists():
        print(f"File not found: {data_file}")
        return

    # -----------------------------
    # Load data
    # -----------------------------
    df_input = pd.read_csv(data_file).sort_values("Year")

    years = df_input["Year"].tolist()
    students = df_input["Students"].astype(int).tolist()

    # -----------------------------
    # Regression
    # -----------------------------
    numeric_years = np.array([int(y.split("-")[0]) for y in years])
    y = np.array(students)

    m, b = np.polyfit(numeric_years, y, 1)

    # -----------------------------
    # Predictions
    # -----------------------------
    future_x = np.arange(numeric_years[-1] + 1, numeric_years[-1] + 1 + FORECAST_YEARS)
    predictions = (m * future_x + b).round().astype(int)

    future_years = [f"{yr}-{str(yr+1)[-2:]}" for yr in future_x]

    df_results = pd.DataFrame({
        "Year": future_years,
        "Predicted Students": predictions
    })

    # -----------------------------
    # Print results
    # -----------------------------
    print("\n" + "=" * 55)
    print("ENROLLMENT FORECAST RESULTS")
    print("=" * 55)
    print(df_results.to_string(index=False))
    print(f"\nTrend: {round(m, 1)} students per year")
    print("=" * 55 + "\n")

    # -----------------------------
    # Save CSV
    # -----------------------------
    csv_path = output_dir / "enrollment_forecast.csv"
    df_results.to_csv(csv_path, index=False)
    print(f"CSV saved as: {csv_path}")

    # -----------------------------
    # Plot
    # -----------------------------
    plt.figure(figsize=(10, 6))

    # plot lines
    plt.plot(numeric_years, y, marker="o", linewidth=2, label="Actual")
    plt.plot(future_x, predictions, marker="o", linestyle="--", label="Predicted")

    # ---- ADD VALUE LABELS ----
    # actual values
    for x_val, y_val in zip(numeric_years, y):
        plt.text(x_val, y_val + 55, f"{int(y_val)}", ha="center", fontsize=9)

    # predicted values
    for x_val, y_val in zip(future_x, predictions):
        plt.text(x_val, y_val + 55, f"{int(y_val)}", ha="center", fontsize=9)
    # --------------------------

    all_x = list(numeric_years) + list(future_x)
    all_labels = years + future_years

    plt.xticks(all_x, all_labels, rotation=45, ha="right")
    plt.xlabel("Academic Year")
    plt.ylabel("Number of Students")
    plt.title("Student Enrollment Forecast")
    plt.legend()
    plt.grid(True, color="lightgray", linestyle="--", linewidth=0.7, alpha=0.7)

    plt.tight_layout()

    img_path = output_dir / "enrollment_forecast.png"
    plt.savefig(img_path, dpi=300)
    plt.close()

    print(f"Chart saved as: {img_path}")


if __name__ == "__main__":
    main()