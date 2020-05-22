from datetime import datetime
from calendar import monthrange
from ntplib import NTPClient


def get_timestamp(ntp_client):
    ntp_response = ntp_client.request('ntp.shoa.cl')
    return datetime.fromtimestamp(ntp_response.tx_time)


def main():
    ntp_client = NTPClient()
    date_obj = get_timestamp(ntp_client)

    first_day = date_obj.replace(day=1).day
    days_in_month = monthrange(date_obj.year, date_obj.month)[1]

    month = [day for day in range(first_day, days_in_month)]
    print(month)


if __name__ == '__main__':
    main()
