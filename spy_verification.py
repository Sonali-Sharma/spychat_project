import spychat_project1         #importing the file with spy details input
from steganography.steganography import Steganography
friend_list = []
existing_spy=raw_input("Are you an existing user Y/N??")        #check for an existing spy or not
if existing_spy.upper() == 'N':
    spychat_project1.new_user_verification()        #in case of new user call the function of imported file
else:
    print "already verified"                        #in case of old user we will continue

status_list = ['Hello,Member of spy community', 'Available', 'Busy', 'Out of station', 'Do not disturb','In a meeting']
chat = []

def add_status(current_status):                     #defining add status method
    #list for available status
    if current_status==None:
        print "currently no status updated"
        default_choice=int(raw_input("\n 1-Update old status\n 2-New status"))      #asking user for their choice and storing it in default status
        if default_choice == 1:
            print"\nYour old statuses:-"                            # if user is updating old status than first displaying the list of atatus
            position=1
            for status in status_list:
                print str(position) + "-" +status
                position=position+1
            status_no=int(raw_input("Enter the status number you want to choose from old status") )      #user enter the status no which he/she wants to update
            if len(status_list)>=status_no:     #returns no. of elements in list
                current_status=status_list[status_no-1]
                return(current_status)              #it will return the selected status from list
        else:
            your_status=raw_input("Enter a new status")     #new status is added
            if len(your_status)>0:
                current_status = your_status
                status_list.append(current_status)   #adding the new status to the list
                return current_status
            else:                                   #check if user is entering empty field
                print"entry is empty!!  Try again"
                add_status(None)
    else:
        print current_status    #it will run if there is any current status in the list
        spy_menu_options()
def add_new_friend():       #defining add new friend method..it will take all details of friend and add it to the list
    friend={                #creating a dictionery for cleaner code containg all details of friend in one varialble
        'name' :'',
        'salutation':'',
        'age':0,
        'rating':0.0
    }
    friend['salutation'] = raw_input(" Is your friend Mister or Miss?")
    friend['name'] = raw_input("Enter your friends name :")  # taking name from user
    friend['name'] = friend['salutation'] + " " + friend['name']
    friend['age'] =  raw_input("Enter your friend's age:")  # taking age from user and converting string  type to int type:e.g name=int(name)
    friend['age'] = int(friend['age'])
    friend['rating'] =raw_input("Enter your friend's current rating between 1 to 10:")  # taking rating from user and converting string  type to float type:e.g rating=float(rating)
    friend['rating'] = float(friend['rating'])
    if len(friend['name'])>0 and friend['age']>20 and friend['rating']>5:# check for the correct entries of the friend
        friend_list.append(friend)      #adding the new friend to the friend list
        print("\n \"Authentication successful!! Your friend is added")
        spy_menu_options()              #calling this method to go back to the menu options
    else:
        print "Sorry your friend cannot be added,Thank You!!"#code reaches else block if conditions are not satisfied in if block
        spy_menu_options()
    return len(friend_list)         #returns total number of friends


def select_friend(selected_friend):      #definig a send message function here user will select the friend to chat with from his/her friend list
    number = 1
    for frn in friend_list:
        print ' %d    friend name:-%s,\n friend age:- %d  ,\n friend rating:- %.2f, is online' % (number , frn['name'], frn['age'],frn['rating'])
        number = number + 1
    your_friend_choice = int(raw_input("Choose from your friends"))

    if len(friend_list)>=your_friend_choice:
        selected_friend = friend_list[your_friend_choice - 1]    #subtracted 1 because indexing stats from 0 and we have initialized from 1
       # print "\n%d,\n%s %s,\n%d,\n%.2f,\nis online"%(your_friend_choice,frn['salutation'],frn['name'],frn['age'],frn['rating'])#printng details of the friend you have choosen
        print "friend selected"
        return(selected_friend)

def send_message():
        friend_choice=select_friend(None)
        original_image =raw_input("What is the name of the jpgimage /specify complete path?")        #select an image from browser and save it as .jpg extention give the name of your image as input
        output_path = raw_input("enter the path of output file")     #ncustom ++++++++ ame of the image with encrypted message....Generated by steagonography.encode()
        text = raw_input("your message?")           #contains text to be encoded
        Steganography.encode(original_image, output_path, text)  #function of staegonography module 3hide the original message inside image
        print "message sent"
        spy_menu_options()
def read_message():
        sender=select_friend(None)
        output_path = raw_input("enter the path of output file")
        secret_text = Steganography.decode(output_path)
        #chat=[secret_text]
        chat.append(secret_text)
        read_options=int(raw_input("\n 1-read older text \n 2-new message from friend"))
        if read_options==1:
            for message in chat:
                print "\n from " + sender['name'] + " message " +  message
        elif read_options==2:
            print  secret_text
        spy_menu_options()

def spy_menu_options(): #this is the menu functions... it provides list of options from which spy will choose
    choice=int(raw_input("\nEnter your choice(numeric value):-\n 1-Update Status\n 2-Add a new friend\n 3-Send a secret message\n 4-Read a personal message\n 5-close application"))
    if choice == 1:
        status_list = ['Hello,Member of spy community', 'Available', 'Busy', 'Out of station', 'Do not disturb','In a meeting']
        updated_status=add_status(None)
        print "\n Status Updated" + "\n" + updated_status
        status_list.append(updated_status)
        spy_menu_options()
    elif choice == 2:
        add_new_friend()
    elif choice == 3:
        selected_friend=None
        send_message()

    elif choice == 4:
        read_message()
    elif choice == 5:
        "call close application"
#basedon the choice selected respective function is called in if else statement
spy_menu_options()