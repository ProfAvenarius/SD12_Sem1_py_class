#Description: From Exercises 31/32 A program for Local Hotel to manage bookings and reservations for their Convention Ctr.
#Author: DCE
#Date: Jul 10

#Program libraries:

import datetime
import time


try:
    with open('Defaults.dat') as file:
        print("Existing Default file exists.")
except:
    print("Creating a new Default file.")
    f = open('Defaults.dat', 'w')
    f.write(f"{1000}\n")
    f.write(f"{0.15}\n")
    f.write(f"{180.00}\n")
    f.write(f"{340.00}\n")
    f.write(f"{530.00}\n")
    f.write(f"{12.95}\n")
    f.write(f"{21.95}\n")
    f.write(f"{34.95}\n")
    f.write(f"{7.95}\n")
    f.close()



#Program Constants 

CURR_DATE = datetime.datetime.now()

f = open('Defaults.dat', 'r')
CONF_NUM = int(f.readline())
HST_RATE = float(f.readline())
SMALL_ROOM = float(f.readline()) # <= 30 people
MED_ROOM = float(f.readline()) # <= 100 people
LARGE_ROOM = float(f.readline()) # <= 250 people
COST_BRK = float(f.readline()) 
COST_LUN = float(f.readline()) 
COST_SUP = float(f.readline())
COST_COF = float(f.readline())
f.close()



#Program Functions


def RoomSize(attend):
    price = 0.00
    Room_Cost = []
    l_count = 0
    m_count = 0
    s_count = 0
    while True:
        if attend <= 30:
            price += SMALL_ROOM
            s_count += 1
            break
        elif attend <= 100:
            price += MED_ROOM
            m_count += 1
            break
        elif attend <= 250:
            price += LARGE_ROOM
            l_count += 1
            break
        else:
            attend = attend - 250
            price += LARGE_ROOM
            l_count += 1
    Room_Cost= [s_count, m_count, l_count, price]
    return (Room_Cost)
    
    

def FoodCost(brk,lun, sup, cof,attend):
    Food_Cost = []
    tot_break = brk*COST_BRK*attend
    tot_lunch = lun*COST_LUN*attend
    tot_supper = sup*COST_SUP*attend
    tot_coffee = cof*COST_COF*attend
    tot_food =tot_break + tot_lunch + tot_supper + tot_coffee
    Food_Cost =[tot_break, tot_lunch, tot_supper, tot_coffee, tot_food]
    return (Food_Cost)


def Money(enter_num):
    #Formats a float into a cash value.
    price_dsp = "${:,.2f}".format(enter_num)
    return price_dsp


def FDate(userdate):
    #Function to turn string object to date object
    day = int(userdate[0:2])
    month = int(userdate[3:5])
    year =int(userdate[6:10])
    date_dsp = datetime.datetime(year, month, day)
    return date_dsp

def FDateL(DateValue):
    # Function will accept a value and format it to Day, Month dd, yyyy.
    DateValueStr = DateValue.strftime("%A, %B %d, %Y")
    return DateValueStr

def Progress():
    for i in range (51):
        print('\r[' + '*' * i + ' ' * (50 - i) + ']', end='')
        time.sleep(0.02)
    print()



print()
print()
print()
print ("*********************************************************************************")
print ("Welcome to the Local Hotel Convention Centre Booking and Reservation System")
print ("Complete all fields, enter 'end' in customer's name to exit.")
print()
print()
print ("Here are the current program constants in use, if any are incorrect end program")
print ("immediately and make required updates:")
print()
# print (f"The Confrence # is: {CONF_NUM}")
print (f"The HST Rate is: {HST_RATE}")
print (f"The small room rate is: {SMALL_ROOM}")
print (f"The medium room rate is: {MED_ROOM}")
print (f"The large room rate is: {LARGE_ROOM}")
print (f"The cost of breakfast per person is: {COST_BRK}")
print (f"The cost of lunch per person is: {COST_LUN}")
print (f"The cost of supper per person is: {COST_SUP}")
print (f"The cost of a coffee break per person is: {COST_COF}")
print()
print()



while True:


    #Program Inputs

    cust_name = input ("Enter the customer's name:  ").upper()
    if cust_name == '':
        print ("This field cannot be left blank.")
    elif cust_name == "END":
        break
    else:

        conf_title = input ("Enter the conference title:  ").upper()

        start_date = input ("Enter the conference start date (DD-MM-YYYY):  ")

        conf_len = int(input("Enter the length of the conference in days:  "))

        max_attend = int(input ("Enter the number of attendeees:  "))

        num_meal_brk = int(input("Enter the number of breakfast meals per person requested:  "))

        num_meal_lun = int(input("Enter the number of lunch meals per person requested:  "))

        num_meal_sup = int(input("Enter the number of supper meals per person requested:  "))

        num_meal_cof = int(input("Enter the number of coffee breaks per person requested:  "))




        #Program Calculations


        Room_Cost = RoomSize(max_attend)

        tot_room_cost = Room_Cost[3]*conf_len

     
        Food_Cost = FoodCost(num_meal_brk, num_meal_lun, num_meal_sup, num_meal_cof, max_attend)

        tot_food_cost = Food_Cost[4]

        subtotal = tot_room_cost + tot_food_cost

        tot_tax = subtotal * HST_RATE

        conf_cost = subtotal + tot_tax

        cost_person = conf_cost/max_attend

        today_dsp = FDateL(CURR_DATE)

        start_date_work = FDate(start_date)

        start_dsp = FDateL(start_date_work)

        end_date = start_date_work +datetime.timedelta(days=(conf_len))

        end_dsp = FDateL(end_date)


        #Program Outputs
        
        print()
        print()
        print ("*******************************************************************************************")
        print (f"THE LOCAL HOTEL AND CONFERENCE CENTRE              DATE PROCESSED: {today_dsp} ")
        print()
        print()
        print (f"CONFERENCE #:      {CONF_NUM}                               ")
        print (f"CONFERENCE TITLE:  {conf_title:<16}                CONFERENCE ORGANIZER: {cust_name}")
        print (f"START DATE:        {start_dsp:<28}    CONFERENCE LENGTH:    {conf_len} days     ")
        print (f"END DATE:          {end_dsp:<28}    NUMBER OF ATTENDEES:  {max_attend}")
        print()
        print (f"             CONFERENCE ROOMS BOOKED:          SMALL ROOM:   {Room_Cost[0]}")
        print (f"                                               MEDIUM ROOM:  {Room_Cost[1]}")
        print (f"                                               LARGE ROOM:   {Room_Cost[2]}")
        print()
        print (f"             MEALS SELECTION (PER GUEST):      BREAKFAST:    {num_meal_brk}")
        print (f"                                               LUNCH:        {num_meal_lun}")
        print (f"                                               SUPPER:       {num_meal_sup}")
        print (f"                                               COFFEE BREAK: {num_meal_cof}")
        print()
        print (f"TOTAL COST OF ROOMS:                                                   {Money(tot_room_cost)} ")
        print (f"COST OF BREAKFAST:                             {Money(Food_Cost[0])}")
        print (f"COST OF LUNCH:                                 {Money(Food_Cost[1])}")
        print (f"COST OF SUPPER:                                {Money(Food_Cost[2])}")
        print (f"COST OF COFFEE BREAK:                          {Money(Food_Cost[3])}")
        print (f"TOTAL COST OF FOOD:                                                    {Money(tot_food_cost)} ")
        print()
        print (f"SUBTOTAL:                                      {Money(subtotal)}")
        print (f"TOTAL TAX:                                     {Money(tot_tax)}")
        print()
        print (f"TOTAL CONFERENCE COSTS:                                                {Money(conf_cost)}  ")
        print (f"COST PER ATTENDEE                                                      {Money(cost_person)} ")
        print()
        print ("*******************************************************************************************")
        print()
        print()
        f2 = open("Conference.dat", "a")

        f2.write(f"{CONF_NUM}, {cust_name}, {conf_title}, {start_date_work}, {conf_len}, {max_attend}, {num_meal_brk}, {num_meal_lun}, {num_meal_sup}, {num_meal_cof}, {conf_cost} \n")

        f2.close()
        print()
        print ("Saving conference data...")
        print()
        Progress()
        print()
        print("All data saved!")
        CONF_NUM += 1

        f = open('Defaults.dat', 'w')
        f.write(f"{CONF_NUM}\n")
        f.write(f"{HST_RATE}\n")
        f.write(f"{SMALL_ROOM}\n")
        f.write(f"{MED_ROOM}\n")
        f.write(f"{LARGE_ROOM}\n")
        f.write(f"{COST_BRK}\n")
        f.write(f"{COST_LUN}\n")
        f.write(f"{COST_SUP}\n")
        f.write(f"{COST_COF}\n")
        f.close()
        print()
        print()
        print()






print()
print()
print()
print("Thank for using this program, have a nice day!")
print()
print()
print()
