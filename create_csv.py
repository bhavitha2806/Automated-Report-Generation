import pandas as pd

# Extended sample data
data = {
    "Name": [
        "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah",
        "Ian", "Judy", "Kevin", "Laura", "Mike", "Nina", "Oscar", "Paul",
        "Quincy", "Rachel", "Steve", "Tina"
    ],
    "Age": [
        25, 30, 35, 40, 22, 29, 33, 27, 31, 28,
        45, 26, 39, 24, 36, 41, 34, 23, 38, 32
    ],
    "Salary": [
        50000, 60000, 70000, 80000, 45000, 62000, 71000, 55000, 64000, 53000,
        90000, 48000, 83000, 47000, 76000, 87000, 73000, 46000, 85000, 69000
    ],
    "Department": [
        "HR", "IT", "Finance", "IT", "HR", "Marketing", "Finance", "HR",
        "IT", "Marketing", "Finance", "HR", "IT", "Marketing", "Finance",
        "IT", "Finance", "HR", "IT", "Marketing"
    ]
}

# Create DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv("sample_data.csv", index=False)

print("Extended CSV file 'sample_data.csv' created successfully.")
