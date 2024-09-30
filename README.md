# Assignment-3
The question I had to answer was: What are the 3 most common loan interest rates seen in this dataset?
There are currently 32,587 datasets I'm using for my topic Loans.

A.) The purpose of the program was to Write code that would show What are the 3 most common loan interest rates seen in this dataset?
The datasets that were the most common for loan interest rates were 7.51% produced 756 times, 10.99% which was produced 749 times, then 7.49% which was produced 645 times. 

B.) The input would the interest rates. All the inputs for the codes were the columns of the data which are, 
customer_id: Unique identifier for each customer
customer_age: Age of the customer
customer_income: Annual income of the customer
home_ownership: Home ownership status (e.g., RENT, OWN, MORTGAGE)
employment_duration: Duration of employment in months
loan_intent: Purpose of the loan (e.g., PERSONAL, EDUCATION, MEDICAL, VENTURE)
loan_grade: Grade assigned to the loan
loan_amnt: Loan amount requested
loan_int_rate: Interest rate of the loan
term_years: Loan term in years
historical_default: Indicates if the customer has a history of default (Y/N)
cred_hist_length: Length of the customer's credit history in years
Current_loan_status: Current status of the loan (DEFAULT, NO DEFAULT)![image](https://github.com/user-attachments/assets/e5d1cbb9-4d39-49aa-8c51-4ae7bcc1e193)
The input that were are focused on would be the loan interest rates. This is the most and main important input for this program of code. 

The outputs being the three most common loan interest rates. Which are listed above in line six.

Understanding Trends: Identifying the most common interest creates helps financial institutions understand current market trends and customer preferences. 
Helps the loan companies understand what customers like and are most likely looking for when it comes to loans. If they prefer a longer loan payment with a smaller interest rate or vice versa. 
Assessing Risk: Knowing common interest rates, can help assess the risk associated with different loan products. 
Knowing whether or not similar interest rate loans are even paid back in time or if they’re always defaulting on payments. 
Targeted Marketing strategies, identifying common interest rates can help in designing targeted marketing campaigns for different customer segments. 
How you try and appeal to different clients by campaigning to their interest in loans. Knowing what your clients are looking for in loans helps you talk them into getting new ones or to get a loan they need specifically through your company. 


This is how the code works. It imports the csv file, which provides how to read and write the csv file. It imports the "counter" from the collections module, which is used to count the amount of times a elements appears in a list. Then it sets a par=th to the csv file containing the loan data. 
It then makes an empty list to store interest rates. Then seperates all the columns with their names and categorizes them into different keys. It then starts to grab the interest rates from the current row. It then converst the interest rate into a float and puts it into the new list for interest rates. 
Then it creates a line that creates a counter for the interest rates list counting the amount of times each unique interest rate appears and how many times. Then it retreieves the three most common interest rates and how many times they appear by frequency. Then outputs the top three most common interest rates and their counts in a string type format. 

The data range consists of 32,587 clientell. 
The Assignment .py file and the code .py file are the uploaded and updated codes and everything from vscod,
