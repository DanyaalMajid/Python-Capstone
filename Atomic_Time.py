import ntplib
from time import ctime

def get_time(server="europe.pool.ntp.org"):
    c = ntplib.NTPClient()
    response = c.request(server, version=3)
    print(f"The Current Time From NTP Server \"{server}\" is:")
    print(ctime(response.tx_time))

get_time()
get_time("time.windows.com")
get_time("time.nist.gov")
get_time("0.asia.pool.ntp.org")