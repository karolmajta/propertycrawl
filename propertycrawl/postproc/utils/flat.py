"""
Utility functions for extracting district data from datasets.
"""


def get_districts(data):
    """
    Returns a histogram of district names in data.
    :param data:
    :return:
    """
    valid_addresses = [
        datum['address_details'] for datum in data
        if len(datum['address_details']) == 3
    ]
    district_hist = {}
    for address in valid_addresses:
        district = address[1]
        if district in district_hist:
            district_hist[district] += 1
        else:
            district_hist[district] = 1

    edge_score = sorted(
        district_hist.values(), reverse=True)[int(len(district_hist) / 3)]
    return [d for d, s in district_hist.items() if s >= edge_score]


def add_districts(data, districts):
    """
    Normalizes district names in data.
    :param data:
    :param districts:
    :return:
    """
    district_set = set(districts)
    for datum in data:
        datum['district'] = None
        for address_chunk in datum['address_details']:
            if address_chunk in district_set:
                datum['district'] = address_chunk
                break
