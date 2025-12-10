import pandas as pd

# ---------- FIRST DATAFRAME ----------
employee_details = pd.DataFrame({
    "Name": ["Alex", "John", "Michael", "Emma", "Sophia"],
    "Age": [28, 34, 29, 31, 26],
    "Department": ["IT", "Finance", "IT", "HR", "Marketing"],
    "Salary": [4500, 5200, 4800, 5000, 4700]
})

# ---------- SECOND DATAFRAME ----------
salary_update = pd.DataFrame({
    "Name": ["Alex", "Emma", "Sophia"],
    "New_Salary": [4800, 5500, 5000]
})

# ---------- MERGE (COMPARISON) ----------
merged = employee_details.merge(salary_update, on="Name", how="left")

# ---------- APPLY UPDATED SALARIES ----------
merged["Final_Salary"] = merged["New_Salary"].fillna(merged["Salary"])

# ---------- CLEAN RESULT ----------
final_df = merged[["Name", "Age", "Department", "Final_Salary"]]

print("----- FINAL RESULT -----")
print(final_df)
