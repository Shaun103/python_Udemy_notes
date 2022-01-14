# https://docs.python.org/3/library/datetime.html#module-datetime
# https://www.youtube.com/watch?v=-5wpm-gesOY



import time
import datetime
import pytz



def main():
    print()

    # print("The epoch on this system starts at: " + time.strftime('%c', time.gmtime(0)))
    # print(f"The current timezone is {time.tzname[0]} with an offset of {time.timezone}")


    # if time.daylight != 0:
    #     print("\tDaylight saving time is in effect for this location")
    #     print("\tThe DST timezone is " + time.tzname[1])

    # print("Local time is " + time.strftime('%Y-%m-%d %H:%M%S', time.localtime()))

    # print("UTC time is " + time.strftime('%Y-%m-%d %H:%M%S', time.gmtime()))


    
#_____________________________________________________________________________________


    # print(datetime.datetime.today())
    # print(datetime.datetime.now())
    # print(datetime.datetime.utcnow())

    # print()

    
#_____________________________________________________________________________________

    # # Desired timezone to be looked up
    # country = "US/Central"

    # # Grabbing that timezone 
    # tz_to_display = pytz.timezone(country)

    # # Grabbing the current time from the timezone
    # local_time = datetime.datetime.now(tz=tz_to_display)
    
    # # Displaying information 
    # print(f"The time in {country} is {local_time}")
    # print(f"UTC is {datetime.datetime.utcnow()}")

#_____________________________________________________________________________________

    # displays all of the timezones
    # for x in pytz.all_timezones:
    #     print(x)

    # Displays country names in the timezones
    # for x in sorted(pytz.country_names):
    #     print(f"{x}: {pytz.country_names[x]} ")

    # for x in sorted(pytz.country_names):
    #     print(f"{x}: {pytz.country_names[x]}: {pytz.country_timezones.get(x)}")



    # prints all the timzones with their current times 
    # for x in sorted(pytz.country_names):
    #     print(f"{x}: {pytz.country_names[x]}")
    #     if x in pytz.country_timezones:
    #         for zone in sorted(pytz.country_timezones[x]):
    #             tz_to_display = pytz.timezone(zone)
    #             local_time = datetime.datetime.now(tz=tz_to_display)
    #             print(f"\t\t{zone}: {local_time}")
    #     else:
    #         print("\t\tNo time zone defined ")

#_____________________________________________________________________________________

    # local_time = datetime.datetime.now()
    # utc_time = datetime.datetime.utcnow()

    # # use this when you are working with datetime
    # # aware_local_time = pytz.utc.localize(local_time)

    # # use this when you are displaying to the user
    # aware_local_time = pytz.utc.localize(utc_time).astimezone()


    # aware_utc_time = pytz.utc.localize(utc_time)

    # print(f"Naive local time {local_time}")
    # print(f"UTC time {utc_time}")

    # print(f"Aware local time {aware_local_time}, time zone {aware_local_time.tzinfo}")
    # print(f"Aware UTC time {aware_utc_time}, time zone {aware_utc_time.tzinfo}")

#_____________________________________________________________________________________

    # October, 25, 2015 1:30:0:0
    gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
    print(gap_time)
    print(gap_time.timestamp())

    # number of seconds since epoch
    s = 1445733000 

    # convert seconds 
    t = s + (60 * 60)

    # grabing great britain timezone
    gb = pytz.timezone('GB')
    
    # before the clocks went back
    dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb) 
    
    # clocks went back to 00
    dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb) 

    # displaying information
    print(f"{s} seconds since he epoch is {dt1}")
    print(f"{t} seconds since he epoch is {dt2}")





if __name__ == "__main__":
    main() 