import pandas as pd

url = 'https://apidocs.hkma.gov.hk/chi/apidata?api=market-data-and-statistics.monthly-statistical-bulletin.banking.residential-mortgage-survey&page=1'

df = pd.read_html(url)
print()
