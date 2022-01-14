import urllib.request
import json


def main():
    print()


    # reading data from weather file, deserialized the data 
    # json_data_source = '/Users/User/Desktop/Python_Udemy/python_JSON.py/temperature_anomaly.json'
    

    # with open(json_data_source, 'r', encoding='utf=8') as data:
    #     anomalies = json.load(data)
    
    # print()
    # print(anomalies['description'])
    # print(anomalies['citation'])
    
    # for year, value in anomalies['data'].items():
    #     year, value = int(year), float(value)

    #     print(f"{year} ...{value:6.2f}") # # formatting code: 6.2f width

    # print('*'*80)
    
    # print(anomalies['citation'])

#____________________________________________________________________________

    # reading from weather website

    json_data_source = 'https://www.ncdc.noaa.gov/cag/global/time-series/globe/land_ocean/1/7/1880-2021/data.json'

    # with open(json_data_source, encoding='utf-8') as data:
    with urllib.request.urlopen(json_data_source) as json_stream:
        data = json_stream.read().decode('utf-8')
        anomalies = json.loads(data)

    print(anomalies['description'])

    for year, value in anomalies['data'].items():
        year, value = int(year), float(value)
        print(f'{year} ...{value:6.2f}')  # # formatting code: 6.2f width
        
    print('*' * 80)

    # print(anomalies['citation'])




if __name__ == "__main__":
    main()