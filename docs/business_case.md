# Business Case: NordBank

## The Company
NordBank is a fictional retail bank in Germany. It manages customers 
(retail, premium, students), their current and savings accounts, 
their transactions, and loans.

## The Problem
Management wants to (1) track business activity, (2) detect fraud, 
and (3) limit non-performing loans. The data is scattered and 
not always reliable.

## The Thread
Each project phase addresses this problem using a more advanced tool 
(see the table in the README).

## Business Questions

| No. | Who | Business Question | Why It's Useful | Data | Tool | Status |
|-----|-----|-------------------|-----------------|------|------|--------|
| Q1  | Management | What is the transaction volume by category evtl..(and month?) | Track business activity | transactions | SQL | done |
| Q2  | Risk Management | What share of transactions are fraudulent, and which categories are most affected? | Target fraud controls | transactions | pandas | To do |
| Q3  | Sales & Marketing | Who are the top 10 customers by spending? | Targeted offers | customers, accounts, transactions | SQL (JOIN) | done |
| Q4  | Credit Risk | What is the default rate by customer segment? | Measure credit risk | loans, customers | SQL | To do |
| Q5  | Sales & Marketing | What is the average transaction amount per customer? | Understand customer spending | transactions, customers | SQL (JOIN) | done |

## Assumptions and Limitations
- Synthetic data: results do not reflect a real bank.
