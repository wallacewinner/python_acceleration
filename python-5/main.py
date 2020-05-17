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


def calculate_duration(start, end):
    call_tax = 0.36  # fixed tax all calls
    tax_minute = 0.09  # tax to calls during 6 and 22
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


def search_array(call, value, result):
    index = 0
    while (index < len(result)):
        if call == result[index]['source']:
            result[index]['total'] = round(
                result[index]['total'] + value, 2)
            return True
        else:
            index = index + 1


def classify_by_phone_number(records):
    result = []  # array to save the result
    for record in records:
        # cost of the it call
        value = calculate_duration(record['start'], record['end'])
        # search on array for equals values
        if search_array(record['source'], value, result) is not True:
            result.append({'source': record['source'], 'total': value})

    return sorted(result, key=lambda k: k['total'], reverse=True)


print(classify_by_phone_number(records))
