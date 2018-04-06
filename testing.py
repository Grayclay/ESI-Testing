from esipy import App
from esipy import EsiClient
from esipy import EsiSecurity

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

# this print a URL where we can log in
print security.get_auth_uri(scopes=['esi-markets.structure_markets.v1'])

tokens = security.auth('drsYPDYBwgMwNKkLOS2egrb-vlpxzITrrDJFiE-lO_4HKjVbLuXOfoGySZlR3hsw0')

print tokens

{
  "access_token": "frenafeifafrbaefluerbfeainb",
  "token_type": "Bearer",
  "expires_in": 1200,
  "refresh_token": "fera48ftea4at64fr684fae"
}

# use the verify endpoint to know who we are
api_info = security.verify()

# api_info contains data like this
# {
#   "Scopes": "esi-wallet.read_character_wallet.v1",
#   "ExpiresOn": "2017-07-14T21:09:20",
#   "TokenType": "Character",
#   "CharacterName": "SOME Char",
#   "IntellectualProperty": "EVE",
#   "CharacterOwnerHash": "4raef4rea8aferfa+E=",
#   "CharacterID": 123456789
# 

