from woocommerce import API

wcapi = API(
    url="http://localhost:8888/",
    consumer_key="ck_aed107877c117d4ddc610b0c986af9e703e379a1",
    consumer_secret="cs_0035cd989fd9a84582f37f280528eb77443d0d3c",
    version="wc/v3"
)

import pprint
pprint.pprint(wcapi.get("products").json())