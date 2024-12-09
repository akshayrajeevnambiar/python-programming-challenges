# Challenge 11: Merging two csv files
# Define a function to merge 2 csv files
import csv

def merge_csv (input_files, output_file):
    field_names = []
    for file in input_files:
        with open(file, 'r', encoding="utf-8") as input_file:
            fields = csv.DictReader(input_file).fieldnames
            field_names.extend(field for field in fields if field not in field_names)

    with open(output_file, 'w', encoding="utf-8") as output_file:
        writter = csv.DictWriter(output_file, fieldnames=field_names)
        writter.writeheader()
        for file in input_files:
            with open(file) as input_file:
                reader = csv.DictReader(input_file)
                for row in reader:
                    writter.writerow(row)

