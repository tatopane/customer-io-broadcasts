import requests as r
import csv
import json
from decouple import config

#### Parameters
broadcast_id = 1000795
file_name = 'cl_leads_cashback.csv'

################################# Don't modify below this line

per_user_data = []
with open(file_name, newline='', encoding='latin-1') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	next(reader, None) #skip headers
	for row in reader:
		## client_email	client_first_name	project_title	project_url_inbox	project_budget	project_category_id	category_name
		user = {'email': row[0], 'data': {'first_name':row[1], 'project_title': row[2], 'project_url_inbox': row[3]}}
		per_user_data.append(user)
		
base_url = 'https://api.customer.io/'
endpoint = '/v1/campaigns/{broadcast_id}/triggers'

headers = {
    'content-type': "application/json",
    'Authorization': "Bearer {}".format(config('CUSTOMERIO_API_KEY'))
    }

payload = {"per_user_data": per_user_data, "email_ignore_missing": True, "email_add_duplicates": True}
#print(json.dumps(payload))

res = r.post(base_url + endpoint.format(broadcast_id = broadcast_id), json = payload, headers = headers)
print(res.status_code)
print(res.json())





