# SkillNexis Python Programming
# Week 4 - Capstone Project
# Employee Data Analysis

import pandas as pd

INPUT_FILE = "employee_data.csv"
OUTPUT_FILE = "filtered_employees.csv"

try:
    # Load employee data
    df = pd.read_csv(INPUT_FILE)

    print("========================================")
    print("       EMPLOYEE DATA ANALYSIS")
    print("========================================")

    # Display employee data
    print("\nEmployee Data:")
    print(df)

    # Calculate average salary
    average_salary = df["Salary"].mean()

    # Count employees in each department
    department_count = df["Department"].value_counts()

    print("\n========== ANALYSIS RESULTS ==========")
    print(f"Average Salary: ₹{average_salary:.2f}")

    print("\nEmployees by Department:")
    print(department_count)

    # Filter employees above salary threshold
    threshold = float(
        input("\nEnter salary threshold: ₹")
    )

    filtered_employees = df[df["Salary"] > threshold]

    print("\nEmployees Above Salary Threshold:")
    print(filtered_employees)

    # Export filtered results
    filtered_employees.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"\nFiltered employee data exported to "
        f"'{OUTPUT_FILE}' successfully."
    )

    print("========================================")

except FileNotFoundError:
    print(f"Error: '{INPUT_FILE}' not found.")

except ValueError:
    print("Error: Please enter a valid salary value.")

except KeyError as e:
    print(f"Error: Missing column {e}.")

except Exception as e:
    print("Unexpected error:", e)