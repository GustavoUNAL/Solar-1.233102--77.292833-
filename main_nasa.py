import os, json, requests

locations = [(1.233102, -77.292833)]
# locations = [(32.929, -95.770), (5, 10)]

output = r""



#DNI % GHI
base_url = r"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=ALLSKY_SFC_SW_DNI,ALLSKY_SFC_SW_DWN,ALLSKY_SFC_SW_DIFF,CLRSKY_KT&community=RE&longitude={longitude}&latitude={latitude}&start=20230101&end=20240101&format=JSON"
# base_url = r"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=ALLSKY_SFC_SW_DNI,ALLSKY_SFC_SW_DWN,ALLSKY_SFC_SW_DIFF,CLRSKY_KT&community=RE&longitude={longitude}&latitude={latitude}&start=20230101&end=20240101&format=JSON"


# base_url = r"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M,T2MDEW,T2MWET,TS,T2M_RANGE,T2M_MAX,T2M_MIN&community=RE&longitude={longitude}&latitude={latitude}&start=20210101&end=20210305&format=JSON"
# base_url = r"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M,T2MDEW,T2MWET,TS,T2M_RANGE,T2M_MAX,T2M_MIN&community=RE&longitude={longitude}&latitude={latitude}&start=20150101&end=20150305&format=JSON"

for latitude, longitude in locations:
    api_request_url = base_url.format(longitude=longitude, latitude=latitude)

    response = requests.get(url=api_request_url, verify=True, timeout=30.00)

    content = json.loads(response.content.decode('utf-8'))
    filename = response.headers['content-disposition'].split('filename=')[1]

    filepath = os.path.join(output, filename)
    with open(filepath, 'w') as file_object:
        json.dump(content, file_object)