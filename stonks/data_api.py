"""
House all data fetching info. Abstracts away from the actual implementations in favour of setting the table clearly
for the APIs usage.
"""

from stonks import config
from stonks._apis import finnhubb


finnhub_api = finnhubb.FinnhubAPI(config.FINNHUB_TOKEN)

