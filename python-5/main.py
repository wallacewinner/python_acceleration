from datetime import datetime

records = [{
    'source': '48-996355555',
    'destination': '48-666666666',
    'end': 1564610974,
    'start': 1564610674}, {
    'source': '41-885633788',
    'destination': '41-886383097',
    'end': 1564506121,
    'start': 1564504821}, {
    'source': '48-996383697',
    'destination': '41-886383097',
    'end': 1564630198,
    'start': 1564629838}, {
    'source': '48-999999999',
    'destination': '41-885633788',
    'end': 1564697158,
    'start': 1564696258}, {
    'source': '41-833333333',
    'destination': '41-885633788',
    'end': 1564707276,
    'start': 1564704317}, {
    'source': '41-886383097',
    'destination': '48-996384099',
    'end': 1564505621,
    'start': 1564504821}, {
    'source': '48-999999999',
    'destination': '48-996383697',
    'end': 1564505721,
    'start': 1564504821}, {
    'source': '41-885633788',
    'destination': '48-996384099',
    'end': 1564505721,
    'start': 1564504821}, {
    'source': '48-996355555',
    'destination': '48-996383697',
    'end': 1564505821,
    'start': 1564504821}, {
    'source': '48-999999999',
    'destination': '41-886383097',
    'end': 1564610750,
    'start': 1564610150}, {
    'source': '48-996383697',
    'destination': '41-885633788',
    'end': 1564505021,
    'start': 1564504821}, {
    'source': '48-996383697',
    'destination': '41-885633788',
    'end': 1564627800,
    'start': 1564626000}]


call_tax = 0.36  # fixed tax all calls
tax_minute = 0.09  # tax to calls during 6 and 22
call_response = []  # array to save the result
i = 0


def classify_by_phone_number(records):
    
    for record in records:

        # cost of the it call
        total_call = calculate_duration(record['start'], record['end'])
        # save the result on array
        if organiza(record['source'], i, total_call) != True:
            call_response.append({'source': record['source'], 'total': total_call})
    print(call_response)
    return call_response
    


def calculate_duration(start, end):
    # convert the time
    start_convert = datetime.fromtimestamp(start)
    end_convert = datetime.fromtimestamp(end)
    # calculate the duration of call
    duration = end_convert - start_convert
    # define the time that call starts
    if start_convert.hour > 6 and start_convert.hour < 22:
        result = ((int(duration.total_seconds() / 60)) * tax_minute + call_tax)
    else:
        result = ((int(duration.total_seconds() / 60)) * 0 + call_tax)
    # round the result for two decimal points
    return round(result, 2)

def organiza(ligacao, i, total_call):
    while ( i < len(call_response)):
        if ligacao == call_response[i]['source']:
            call_response[i]['total'] = round(call_response[i]['total'] + total_call, 2)
            return True
        else:
            i = i + 1

(classify_by_phone_number(records))