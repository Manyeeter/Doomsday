#Doomsday Algorithm
#4/4 - 6/6 - 8/8 - 10/10 - 12/12
#9/5 - 5/9 - 7/11 - 11/7
#3/1 or 4/1 leap year
#28/2 or 29/2 leap year
#14/3 / Pi Day

#All on the same day

#Past Doomdsday - 1800 Pi day was a Friday
#Past Doomsday - 1900 Pi day was a  Wednesday
#Future Doomsday - 2000 Pi day was a Tuesday
#Future Doomsday - 2001 Pi day was a Wednesday
#Future Doomsday - 2002 Pi day was a Thursday
#Future Doomsday - 2003 Pi day was a Friday
#Future Doomsday - 2004 Pi day was a Saturday

#Sunday = 0
#Monday = 1
#Tuesday = 2
#Wednesday = 3
#Thursday = 4
#Friday = 5
#Saturday = 6



#_______________________Functions_______________________
    #Num_to_day
def num_to_day(num):
    if num == 0:
        day = "Sunday"
    elif num == 1:
        day = "Monday"
    elif num == 2:
        day = "Tuesday"
    elif num == 3:
        day = "Wednesday"
    elif num == 4:
        day = "Thursday"
    elif num == 5:
        day = "Friday"
    else:
        day = "Saturday"
        
    return(day)
    ##########
    

#_______________________________________________________




#_______________________Variables_______________________
doomsday = 0
leap = False
#_______________________________________________________


year = input("Please enter a year (0000-9999): ")
dd = int(input("\nPlease enter a day (dd): "))
mm = int(input("Please enter a month (mm): "))


year_str = str(year)
year_len = len(year_str)
last_two = int(year_str[year_len - 2: year_len])

first_two = int(year_str[:2])

x = first_two % 4


if x == 0:
    Anchor_day = 2
elif x == 1:
    Anchor_day = 0
elif x == 2:
    Anchor_day = 5
else:
    Anchor_day = 3

twelves_in_year = last_two // 12
diff = int(last_two - (12*twelves_in_year))
fours_in_diff = diff // 4
result = twelves_in_year + diff + fours_in_diff + Anchor_day
sevens_in_result = result % 7
doomsday = sevens_in_result

day = num_to_day(doomsday)

print("\n\nThe doomsday of that year was",day)

def is_leap_year(year):
    year = int(year)
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(year,"is a leap year")
                return True
            else:
                print(year,"is not a leap year")
        else:
            print(year,"is a leap year")
            return True
    else:
        print(year,"is not a leap year")

leap = is_leap_year(year)

# The algorithm below will find the day on the first of jan in that year
if leap == True:
    if doomsday > 3:
        Day_of_jan1 = doomsday - 3
    else:
        Day_of_jan1 = ((doomsday+7)-3)
else:
    if doomsday > 1:
        Day_of_jan1 = doomsday - 2
    else:
        Day_of_jan1 = ((doomsday+7)-2)


Day_of_jan1_str = num_to_day(Day_of_jan1)

print("The day on the first of jan that year was",Day_of_jan1_str)

final_date = 0


if leap == True:
    if mm == 12:
        final_date = (Day_of_jan1 + 334 + dd) % 7
    elif mm == 11:
        final_date = (Day_of_jan1 + 304 + dd) % 7
    elif mm == 10:
        final_date = (Day_of_jan1 + 273 + dd) % 7
    elif mm == 9:
        final_date = (Day_of_jan1 + 243 + dd) % 7
    elif mm == 8:
        final_date = (Day_of_jan1 + 212 + dd) % 7
    elif mm == 7:
        final_date = (Day_of_jan1 + 181 + dd) % 7
    elif mm == 6:
        final_date = (Day_of_jan1 + 151 + dd) % 7
    elif mm == 5:
        final_date = (Day_of_jan1 + 120 + dd) % 7
    elif mm == 4:
        final_date = (Day_of_jan1 + 91 + dd) % 7
    elif mm == 3:
        final_date = (Day_of_jan1 + 61 + dd) % 7
    elif mm == 2:
        final_date = (Day_of_jan1 + 30 + dd) % 7
    else:
        final_date = (Day_of_jan1 + dd - 1) % 7
else:
    if mm == 12:
        final_date = (Day_of_jan1 + 333 + dd) % 7
    elif mm == 11:
        final_date = (Day_of_jan1 + 303 + dd) % 7
    elif mm == 10:
        final_date = (Day_of_jan1 + 272 + dd) % 7
    elif mm == 9:
        final_date = (Day_of_jan1 + 242 + dd) % 7
    elif mm == 8:
        final_date = (Day_of_jan1 + 211 + dd) % 7
    elif mm == 7:
        final_date = (Day_of_jan1 + 181 + dd) % 7
    elif mm == 6:
        final_date = (Day_of_jan1 + 150 + dd) % 7
    elif mm == 5:
        final_date = (Day_of_jan1 + 119 + dd) % 7
    elif mm == 4:
        final_date = (Day_of_jan1 + 90 + dd) % 7
    elif mm == 3:
        final_date = (Day_of_jan1 + 60 + dd) % 7
    elif mm == 2:
        final_date = (Day_of_jan1 + 30 + dd) % 7
    else:
        final_date = (Day_of_jan1 + dd - 1) % 7


final_date_str = num_to_day(final_date)


print(final_date_str)