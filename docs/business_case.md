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
| Q1  | Management | What is the transaction volume by category and by month? | Track business activity | transactions | SQL | To do |
| Q2  | Risk Management | What is the share of fraud, and in which categories? | Target fraud controls | transactions | pandas | To do |
| Q3  | Sales & Marketing | Who are the top 10 spending customers? | Targeted offers | customers, accounts, transactions | SQL (JOIN) | To do |
| Q4  | Credit Risk | What is the default rate by customer segment? | Measure credit risk | loans, customers | SQL | To do |

## Assumptions and Limitations
- Synthetic data: results do not reflect a real bank.
