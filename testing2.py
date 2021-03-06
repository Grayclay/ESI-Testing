from esipy import App
from esipy import EsiClient
from esipy import EsiSecurity
import json

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

# print tokens

op = app.op['get_markets_structures_structure_id'](
    structure_id=1022734985679,
    page='-1'
)

structure = client.request(op)

y=0

for x in structure.data:
	print str(structure.data[y].type_id) + ', ' + str(structure.data[y].price) + ', ' + str(structure.data[y].is_buy_order)
	y+=1