import pandas as pd
import yaml

df = pd.read_csv(
    r"https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv",
    na_values="na"
)

# Define a mapping from pandas dtypes to the types you want in the YAML file
dtype_to_yaml_type = {
    'object': 'category',
    'int64': 'int',
    'float64': 'float',
    'bool': 'bool',
    # Add more mappings if necessary
}

# Calculate missing percentages and identify columns with more than 70% missing
missing = df.isna().sum().div(df.shape[0]).mul(100)
dropcols = missing[missing > 70].index.tolist()


# Generate the columns schema
columns_schema = []
numerical_columns = []
for column in df.columns:
    if column not in dropcols:
        columns_schema.append({column: dtype_to_yaml_type[str(df[column].dtype)]})

        if df[column].dtype in ['int64', 'float64']:
            numerical_columns.append(column)


# Writing to a YAML file in the specified path
schema_path = 'E:\\livesensor\\config\\schema.yaml'  # Ensure to use double backslashes in Windows path
with open(schema_path, 'w') as file:
    yaml.dump({'columns': columns_schema}, file)
    file.write('\n') #added newline for readability
    yaml.dump({'numerical_columns': numerical_columns}, file)
    file.write('\n')
    yaml.dump({'drop_columns': dropcols}, file)

print(f"schema.yaml has been created at {schema_path} with the column data types.")
