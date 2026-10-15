-- staging: rename and cast only, no business logic
select
    transaction_id,
    account_id,
    amount,
    category,
    ts as transaction_ts,
    is_fraud
from {{ source('raw', 'transactions') }}
