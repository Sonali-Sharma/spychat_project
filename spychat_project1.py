def new_user_verification():
    print "\nWelcome to the spy community"          #printing welcome message
    print "\nWe would like to know some basic details before getting started"
    spy_salutation=raw_input("Should i call you Mister or Miss?")
    spy_name=raw_input("Enter your name :")       #taking name from user
    spyname_length=len(spy_name)
    if spyname_length==0:                            #checking spy_name length to prevent empty entry by user
        print ("\n\"sorry\", Invalid entry...please specify a name") #print error message for empty entry                                                           #declaring int variable
    spy_age=raw_input("Enter your age:")#taking age from user and converting string  type to int type:e.g name=int(name)
    if spy_age.isdigit():
        spy_age=int(spy_age)
    else:
        pass
    if spy_age>20 and spy_age<45:
        #you can check the type of data by writing print type(spy_age)
        spy_rating=0.0                                                          #declaring float variable
        spy_rating=float(raw_input("Your current rating between 1 to 10:"))      #taking rating from user and converting string  type to float type:e.g rating=float(rating)
        my_rating=spy_rating
        print("\n \"Authentication successful\"..welcome,%s %s,\n your age is %d,\n your curent rating is % .2f" %(spy_salutation,spy_name,spy_age,spy_rating))#string formatting:- using place holders like %s,%d,%f and than giving their name inside a tuple e.g(name,age) for a clener code
#also used escape sequence to distinguish inner quotes..e.g in welcome using \
        print "\nyour rating summary is"
        if spy_rating<=2.0:         #checking the ratings of spy using if and elif and giving the associated star to that rating
            print "\n       *"
        elif spy_rating > 2.0 and spy_rating < 4.0:     # and opertor is used to satisfy both conditions for < and >
            print"\n       **"
        elif spy_rating > 4.0 and spy_rating < 6.0:
            print"\n      ***"
        elif spy_rating > 6.0 and spy_rating < 8.0:
            print"\n     ****"
        else:
            print"\n    *****"
    else:
        print "Sorry you are not of the correct age  to be a spy,Thank You!!"
    spy_is_online=True                 #declaring boolean datatype
    print "online"
