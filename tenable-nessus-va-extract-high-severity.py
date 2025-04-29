import csv

# Import Tenable Vulnerability Scan result in csv and extract the high-severity 
with open('VA_Scan_ddyy.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['Severity'] == 'High' or row['Severity'] == 'Critical':
            print(f"{row['Host']} - {row['Plugin ID']} - {row['Name']}")
