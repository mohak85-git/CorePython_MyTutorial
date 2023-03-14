import json
import urllib.request

json_data_source = "https://www.ncei.noaa.gov/access/monitoring/" \
                   "climate-at-a-glance/global/time-series/globe/land_ocean" \
                   "/1/1/1850-2023.json"

with urllib.request.urlopen(json_data_source) as json_stream:
    data = json_stream.read().decode('utf-8')  # decoding data
    anomalies = json.loads(data)  # notice, method name is loads() not load()

print(anomalies['description'])

for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(f"{year} ...{value:6.2f}")
print('*' * 80)
