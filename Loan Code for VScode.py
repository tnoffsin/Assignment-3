# Step 1: Read the CSV data
data = """
customer_id,customer_age,customer_income,home_ownership,employment_duration,loan_intent,loan_grade,loan_amnt,loan_int_rate,term_years,historical_default,cred_hist_length,Current_loan_status
1,22,59000,RENT,123,PERSONAL,C,"£35,000.00",16.02,10,Y,3,DEFAULT
2,21,9600,OWN,5,EDUCATION,A,"£1,000.00",11.14,1,,2,NO DEFAULT
3,25,9600,MORTGAGE,1,MEDICAL,B,"£5,500.00",12.87,5,N,3,DEFAULT
4,23,65500,RENT,4,MEDICAL,B,"£35,000.00",15.23,10,N,2,DEFAULT
5,24,54400,RENT,8,MEDICAL,B,"£35,000.00",14.27,10,Y,4,DEFAULT
6,21,9900,OWN,2,VENTURE,A,"£2,500.00",7.14,1,N,2,DEFAULT
7,26,77100,RENT,8,EDUCATION,A,"£35,000.00",12.42,10,,3,NO DEFAULT
8,24,78956,RENT,5,MEDICAL,A,"£35,000.00",11.11,10,,4,NO DEFAULT
9,24,83000,RENT,8,PERSONAL,A,"£35,000.00",8.9,10,,2,NO DEFAULT
10,21,10000,OWN,6,VENTURE,C,"£1,600.00",14.74,1,N,3,DEFAULT
11,22,85000,RENT,6,VENTURE,A,"£35,000.00",10.37,10,,4,NO DEFAULT
12,21,10000,OWN,2,HOMEIMPROVEMENT,A,"£4,500.00",8.63,1,N,2,DEFAULT
13,23,95000,RENT,2,VENTURE,A,"£35,000.00",7.9,10,,2,NO DEFAULT
14,26,108160,RENT,4,EDUCATION,D,"£35,000.00",18.39,10,N,4,DEFAULT
15,23,115000,RENT,2,EDUCATION,A,"£35,000.00",7.9,10,,4,NO DEFAULT
16,23,500000,MORTGAGE,7,DEBTCONSOLIDATION,A,"£30,000.00",10.65,10,,3,NO DEFAULT
17,23,120000,RENT,0,EDUCATION,A,"£35,000.00",7.9,10,,4,NO DEFAULT
18,23,92111,RENT,7,MEDICAL,E,"£35,000.00",20.25,10,N,4,DEFAULT
19,23,113000,RENT,8,DEBTCONSOLIDATION,C,"£35,000.00",18.25,10,N,4,DEFAULT
20,24,10800,MORTGAGE,8,EDUCATION,A,"£1,750.00",10.99,4,N,2,DEFAULT
21,25,162500,RENT,2,VENTURE,A,"£35,000.00",7.49,10,,4,NO DEFAULT
22,25,137000,RENT,9,PERSONAL,D,"£34,800.00",16.77,10,Y,2,NO DEFAULT
23,22,65000,RENT,4,EDUCATION,C,"£34,000.00",17.58,10,N,4,DEFAULT
24,24,10980,OWN,0,PERSONAL,A,"£1,500.00",7.29,4,Y,3,NO DEFAULT
25,22,80000,RENT,3,PERSONAL,C,"£33,950.00",14.54,10,Y,4,DEFAULT
26,24,67746,RENT,8,HOMEIMPROVEMENT,B,"£33,000.00",12.68,10,N,3,DEFAULT
27,21,11000,MORTGAGE,3,VENTURE,D,"£4,575.00",17.74,1,Y,3,DEFAULT
28,23,11000,OWN,0,PERSONAL,A,"£1,400.00",9.32,3,,3,NO DEFAULT
29,24,65000,RENT,6,HOMEIMPROVEMENT,A,"£32,500.00",9.99,10,,3,NO DEFAULT
30,21,11389,OTHER,5,EDUCATION,B,"£4,000.00",12.84,1,Y,2,DEFAULT
31,21,11520,OWN,5,MEDICAL,A,"£2,000.00",11.12,1,N,3,DEFAULT
32,25,120000,RENT,2,VENTURE,A,"£32,000.00",6.62,10,,2,NO DEFAULT
33,26,95000,RENT,7,HOMEIMPROVEMENT,B,"£31,050.00",14.17,10,Y,3,DEFAULT
34,25,306000,RENT,2,DEBTCONSOLIDATION,B,"£24,250.00",13.85,10,,3,NO DEFAULT
"""

# Step 2: Extract the loan interest rates
lines = data.strip().split('\n')
header = lines[0].split(',')
loan_int_rate_index = header.index('loan_int_rate')

interest_rates = []
for line in lines[1:]:
    fields = line.split(',')
    interest_rate = fields[loan_int_rate_index]
    if interest_rate:
        interest_rates.append(float(interest_rate))

# Step 3: Count the occurrences of each interest rate
rate_counts = {}
for rate in interest_rates:
    if rate in rate_counts:
        rate_counts[rate] += 1
    else:
        rate_counts[rate] = 1

# Step 4: Sort the interest rates by their frequency
sorted_rates = sorted(rate_counts.items(), key=lambda x: x[1], reverse=True)

# Step 5: Output the top 3 most common interest rates
top_3_rates = sorted_rates[:3]
for rate, count in top_3_rates:
    print(f"Interest Rate: {rate}%, Count: {count}")









import csv
from collections import Counter

# Step 1: Read the CSV data from the file
file_path = 'Loan Data.csv'

interest_rates = []

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        interest_rate = row['loan_int_rate']
        if interest_rate:
            interest_rates.append(float(interest_rate))

# Step 2: Count the occurrences of each interest rate
rate_counts = Counter(interest_rates)

# Step 3: Sort the interest rates by their frequency
sorted_rates = rate_counts.most_common(3)

# Step 4: Output the top 3 most common interest rates
for rate, count in sorted_rates:
    print(f"Interest Rate: {rate}%, Count: {count}")