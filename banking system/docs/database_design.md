# Banking Management System Database Design

## Customers

- customer_id
- customer_name
- email
- phone
- address

---

## Accounts

- account_number
- customer_id
- account_type
- branch
- balance
- currency
- status

---

## Transactions

- transaction_id
- account_number
- transaction_type
- amount
- transaction_date