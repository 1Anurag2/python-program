import pandas as pd

# Person DataFrame
person_data = {
    'personId': [1, 2],
    'lastName': ['Wang', 'Alice'],
    'firstName': ['Allen', 'Bob']
}
person_df = pd.DataFrame(person_data)

# Address DataFrame
address_data = {
    'addressId': [1, 2],
    'personId': [2, 3],  # Note that personId 1 is missing in Address
    'city': ['New York City', 'Leetcode'],
    'state': ['New York', 'California']
}
address_df = pd.DataFrame(address_data)

# Perform a left join on 'personId'
result = pd.merge(person_df[['personId','firstName','lastName']], address_df, 
                  on='personId', how='left')

# Display the result
print(result[['firstName', 'lastName', 'city', 'state']])
