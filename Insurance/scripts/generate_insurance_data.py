import pandas as pd
import numpy as np
from faker import Faker
import random


fake = Faker()
random.seed(42)
np.random.seed(42) 


num_records = 1000
policy_types = ['New', 'Renewal']
products = ['Life', 'Health', 'Term', 'ULIP', 'Motor']
channels = ['Agency', 'Direct', 'Bancassurance', 'Online']
regions = ['North', 'South', 'East', 'West']

# Generate data
Data = {
    'policy_id': [fake.unique.random_int(min=1000, max=9999) for _ in range(num_records)],
    'policy_type': [random.choice(policy_types) for _ in range(num_records)],
    'product': [random.choice(products) for _ in range(num_records)],
    'premium': np.round(np.random.uniform(5000, 50000, size=num_records), 2),
    'issue_date': [fake.date_between(start_date='-6M', end_date='today') for _ in range(num_records)],
    'agent_name': [fake.name() for _ in range(num_records)],
    'channel': [random.choice(channels) for _ in range(num_records)],
    'region': [random.choice(regions) for _ in range(num_records)],
}

df = pd.DataFrame(Data)

# Save to Excel
df.to_excel("D:\Insurance\Data\insurance_data.xlsx", index=False)

print("insurance_data.xlsx created with 1000 synthetic records.")
