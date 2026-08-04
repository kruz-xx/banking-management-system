# Banking Management System Database Schema

## Customers

| Field | Type |
|------|------|
| customer_id | INT |
| customer_name | VARCHAR(100) |
| email | VARCHAR(100) |
| phone | VARCHAR(15) |
| address | VARCHAR(150) |

---

## Accounts

| Field | Type |
|------|------|
| account_number | VARCHAR(20) |
| customer_id | INT |
| account_type | VARCHAR(20) |
| branch | VARCHAR(50) |
| balance | DECIMAL(12,2) |
| currency | VARCHAR(10) |
| status | VARCHAR(20) |

---

## Transactions

| Field | Type |
|------|------|
| transaction_id | INT |
| account_number | VARCHAR(20) |
| transaction_type | VARCHAR(20) |
| amount | DECIMAL(12,2) |
| transaction_date | DATETIME |