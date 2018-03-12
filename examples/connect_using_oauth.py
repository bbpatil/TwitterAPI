from TwitterAPI import TwitterAPI

# If you are behind a firewall you may need to provide proxy server
# authentication.
proxy_url = None  # Example: 'https://USERNAME:PASSWORD@PROXYSERVER:PORT'

# Using OAuth 1.0 to authenticate you have access all Twitter endpoints.
api = TwitterAPI(<consumer key>, 
                 <consumer secret>,
                 <access token key>,
                 <access token secret>,
                 auth_type='oAuth1',
                 proxy_url=proxy_url)
# Using OAuth 2.0 to authenticate you lose access to user specific endpoints 
# (ex. statuses/update and statuses/filter), but you increase your rate limits.
# api = TwitterAPI(<consumer key>, 
#                  <consumer secret>,
#                  auth_type='oAuth2', 
#                  proxy_url=proxy_url)

r = api.request('application/rate_limit_status')

# Print HTTP status code (=200 when no errors).
print(r.status_code)

# Print the raw response.
print(r.text)

# Parse the JSON response.
j = r.response.json()
print(j['resources']['search'])