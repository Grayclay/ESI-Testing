from esipy import App
from esipy import EsiClient
from esipy import EsiSecurity
import json
import csv

app = App.create(url="https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility")

# replace the redirect_uri, client_id and secret_key values
# with the values you get from the STEP 1 !
security = EsiSecurity(
    app=app,
    redirect_uri='http://localhost:65432/callback/',
    client_id='3965a624529e416897cc396b6ddea872',
    secret_key='rD7LT8BEHUWlmumN8ylhVvdYgHEI7HOWeHMEFGWc',
)

# and the client object, replace the header user agent value with something reliable !
client = EsiClient(
    retry_requests=True,
    header={'User-Agent': 'grayclay@gmail.com'},
    security=security
)


# to update the security object, 
security.update_token({
    'access_token': '',  # leave this empty
    'expires_in': -1,  # seconds until expiry, so we force refresh anyway
    'refresh_token': 'yUI96Q6kOxvQ6ulwDnQ7VLD1I-4LH-Jz8DOY9Di4NhA1'
})


tokens = security.refresh()

operations = []
for page in range(1,20):
    operations.append(
        app.op['get_markets_structures_structure_id'](
            structure_id=1022734985679,
            page=page
        )
    )

results = client.multi_request(operations)


for (req, res) in results: 
    for order in res.data:
    	print str(order.type_id) + ', ' + str(order.price) + ', ' + str(order.is_buy_order)

with open('test.csv', 'wb') as csvfile:
    datawriter = csv.writer(csvfile, delimiter=',')
    datawriter.writerow(['type_id','price','is_buy_order'])
    for (req, res) in results:
        for order in res.data:
            datawriter.writerow([order.type_id,order.price,order.is_buy_order])