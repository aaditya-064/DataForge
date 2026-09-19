from analysis import analyze_csv

result = analyze_csv("./data/test.csv")

print("\nDATASET")
print("-------")
print("Rows:", result["rows"])
print("Columns:", result["columns"])
print("Missing values:", result["missing_values"])
print("Duplicates:", result["duplicates"])


print("\nCOLUMNS")
print("-------")

for column in result["column_analysis"]:
    print(
        f'{column["name"]}: '
        f'{column["type"]}, '
        f'missing={column["missing"]}, '
        f'unique={column["unique"]}'
    )
