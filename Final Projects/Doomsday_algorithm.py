#_______________________Functions_______________________

#####Num_to_day##############
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
############################


#####Leap year##############
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
############################


#####Jan first calculation##############
def jan_1st_date(leap,doomsday):
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
    return(Day_of_jan1)
############################

#_______________________________________________________




#_______________________Variables_______________________
doomsday = 0
leap = False
final_date = 0
#_______________________________________________________


year = input("Please enter a year (0000-9999): ")
dd = int(input("\nPlease enter a day (dd): "))
mm = int(input("Please enter a month (mm): "))



year_len = len(year)
last_two = int(year[year_len - 2: year_len])
first_two = int(year[:2])



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
print("")
leap = is_leap_year(year)
Day_of_jan1 = jan_1st_date(leap,doomsday)
Day_of_jan1_str = num_to_day(Day_of_jan1)



if mm == 12:
    final_date = (Day_of_jan1 + 333 + dd)
elif mm == 11:
    final_date = (Day_of_jan1 + 303 + dd)
elif mm == 10:
    final_date = (Day_of_jan1 + 272 + dd)
elif mm == 9:
    final_date = (Day_of_jan1 + 242 + dd)
elif mm == 8:
    final_date = (Day_of_jan1 + 211 + dd)
elif mm == 7:
    final_date = (Day_of_jan1 + 181 + dd)
elif mm == 6:
    final_date = (Day_of_jan1 + 150 + dd)
elif mm == 5:
    final_date = (Day_of_jan1 + 119 + dd)
elif mm == 4:
    final_date = (Day_of_jan1 + 90 + dd)
elif mm == 3:
    final_date = (Day_of_jan1 + 60 + dd)
elif mm == 2:
    final_date = (Day_of_jan1 + 30 + dd)
else:
    final_date = (Day_of_jan1 + dd - 1)

if leap == True and mm > 2:
    final_date += 1
    final_day = final_date % 7
else:
    final_day = final_date % 7

final_day_str = num_to_day(final_day)

print("\nThe day on that date is:",final_day_str)