# This program simulates booking tickets . It has four classes : Train , Passenger , Ticket and Account .


# The train class represents a train with its train number , source , destination , coaches , departure time and the number of seats available . It has methods to display the train information and book tickets .


# The passenger class represents a passenger with their Name , Age , Gender and Mobile number . It has a method to display passenger information .


# The ticket class represents a ticket with the train , source , destination , passengers and PNR (passenger name record) number , time  . It has a method to display ticket information.


# Class called account is defined with a constructor that takes two arguments : username and password . The class also defines a method called check_password which takes a single argument password and returns a boolean indicating whether the input password matches the stored password .


# --------------------------- PROJECT : RAILWAY TICKET BOOKING ---------------------------

import random
from datetime import datetime
# We start by importing the random modules , which we'll use to generate random PNR's from the tickets later on .
# We import datetime from datetime , which will use to generate booking time .

class Train():
    def __init__(self, train_num, source, destination, coaches, departure_time):
        self.train_num = train_num
        self.source = source
        self.destination = destination
        self.coaches = coaches  # This must be a DICTIONARY
        self.departure_time = departure_time
# We define the train class , which takes in four parameters a train number , source , destination , destination time and seats available in the coaches . The __init__() method is called when a new train object is created and initializes these attributes .

    def display_info(self):
        print(f"Train number : {self.train_num}")
        print(f"Source : {self.source}")
        print(f"Destination : {self.destination}")
        print(f"Departure_time : {self.departure_time}")
        print("Available Coaches:")
        for coach, info in self.coaches.items():
            print(f"  {coach}: {info['seats']} seats, ₹{info['price']} per ticket")
        print("_" * 40)
# We define a dispLay_info() method for the train class , which displays the train number , source , destination , destination time and number of seats available in the coach for a given train object .

    def book_tickets(self , num_tickets , coach_type):
        
        if coach_type not in self.coaches:
            return None
        if self.coaches[coach_type]["seats"] < num_tickets:
            return None
        self.coaches[coach_type]["seats"] -= num_tickets
        return [random.randint(1000000000, 9999999999) for _ in range(num_tickets)]

# We define a book_tickets() method for the train class , which takes a number of tickets as input and attempts to book that many tickets on the train . If there are enough available seats , the method generates a list of random PNRs equal to the number of tickets being booked , updates the number of seats and returns the list of PNRs . otherwise , the method returns none to indicate that the booking failed.
# The book_tickets method takes in the number of tickets to be booked and returns a list of PNR numbers for the tickets if they are available , or none if there are not enough seats .


class Passenger:
    def __init__(self , name , age , gender , mobile):
        self.name = name 
        self.age = age
        self.gender =gender
        self.mobile = mobile
# The passanger class is defined , which takes in four parameters : name , age , gender , mobile_number . Thes parametes are used to initialize the attributes of the passengers object.

    def display_info(self):
        print(f"Name :{self.name}")
        print(f"Age :{self.age}")
        print(f"Gender :{self.gender}")
        print(f"Mobile number :{self.mobile}")
# The passenger class has a method called display_info which prints out the name , age , gender and mobile number of the passenger .

GST_PERCENT = 5    
PLATFORM_FEE = 10  

class Ticket:
    def __init__(self , train , source , destination , passenger , pnr , departure_time ,booking_time,coach_type,price):
        self.train = train
        self.coach_type = coach_type
        self.source = source
        self.destination = destination
        self.passenger = passenger
        self.pnr = pnr
        self.departure_time = departure_time
        
        self.booking_time = booking_time
        base_price = price
        gst = base_price * GST_PERCENT / 100
        total_price = base_price + gst + PLATFORM_FEE

        self.base_price = base_price
        self.gst = gst
        self.platform_fee = PLATFORM_FEE
        self.total_price = total_price
# The ticket class is defined , which takes in five parameters - train ,coaches, source , destination ,departure time , prices, passengers and PNR . These parameters are used to initialize the attributes of the ticket object.

    def display_info(self):
        print(f"Train number :{self.train.train_num}")
        print(f"Source :{self.source}")
        print(f"Destination :{self.destination}")
        print(f"Coach Type: {self.coach_type}")
        print(f"PNR :{self.pnr}")
        print(f"Departure time : {self.departure_time}")
        print(f"Booking time : {self.booking_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
        for passenger in self.passenger:
            passenger.display_info()
    
        print(f"Fare breakdown:")
        print(f"  Base Price     : ₹{self.base_price:.2f}")
        print(f"  GST (@{GST_PERCENT}%) : ₹{self.gst:.2f}")
        print(f"  Platform Fee   : ₹{self.platform_fee:.2f}")
        print(f"  Total Price    : ₹{self.total_price:.2f}")
        print("_" * 40)
        
        print("_"* 40)
# The ticket class has a method called display_info which prints out the train number ,coaches , departure time , booking time , prices, source , destination , pnr number , and the information of each passenger.

class Account():
     
    def __init__(self , username , password):
        self.username = username
        self.password = password
        
    def check_password(self,password):
        return self.password == password
    
# Class called account is defined with a constructor that takes two arguments : username and password . these arguments are used to initialize instance variables with the same names . the class also defines a method called check_password which takes a single argument password and return a boolean indicting whether the input password matches the stored password.

Accounts = [
    Account("user1" , "password1"),
    Account("user2" , "password2")
]

# A list called accounts is initialized with two account objects already in it , with the usernames "user1" and "user2" and passwords "password1" and "password2" respectively .

logged_in_account = None
# A variable called logged_in_account is initialized to none . this variable will be used later to keep track of the currently with the available train details.

while True: 
# A while loop is started that will run idefinitely until the user logs in successfully and is presented with the available train details.
    print("\n1.Create an account\n2.login\n")
    choice = input ("Enter choice :- ")
    if choice == "1":
        user = input("Enter username :- ")
        password = input("Enter password :- ")
        Accounts.append(Account(user , password))
# If the user chooses to create an account (choice =="1") , they are prompted to enter a user and password . the inputted username and password are then used to create a new account object , which is appended to the accounts list.
        print("Account created successfully...!")
# Inside the loop , the user is presented with two options : either to create an account or to login . the user's choice is stored in a variable called choice.
    elif choice =="2":
        username = input("Enter username :- ")
        password = input("Enter password :- ")
        for account in Accounts:
            if account.username == username and account.check_password(password):
                logged_in_account = account
                break
        if logged_in_account is None:
            print("Invalid user or password...!")
# If the user chooses to login (choice == "2") , they are prompted to enter a username and password . the program then iterates through the accounts list and check if any of the stored accounts match the inputted username and password . if a match is found , the corresponding account objects is assigned to the loggged_in_account variable and the loop is broken . otherwise , an error message is printed.
        else:
            print(
                f"\nlogged in as {logged_in_account.username}\n\n-----Available train details-----\n")
            
            break
    else:
        print("Invalid choice")
        
if logged_in_account is not None:
    trains = [
    Train(
        "12737",
        "tadepalligudem",
        "secunderabad",
        {
            "1AC": {"seats": 5, "price": 1500},
            "2AC": {"seats": 10, "price": 1200},
            "3AC": {"seats": 20, "price": 900},
            "Sleeper": {"seats": 30, "price": 500},
            "General": {"seats": 50, "price": 200},
            "Tatkal": {"seats": 10, "price": 800},
            "Ladies": {"seats": 5, "price": 450},
            "Senior Citizen": {"seats": 5, "price": 300},
            "Physically Handicapped": {"seats": 5, "price": 300}
        },
        "09:20 AM"
    ),
    Train(
        "09256",
        "Delhi",
        "Araku",
        {
            "1AC": {"seats": 45, "price": 1256},
            "2AC": {"seats": 52, "price": 985},
            "3AC": {"seats": 12, "price": 758},
            "Sleeper": {"seats": 125, "price": 658},
            "General": {"seats": 189, "price": 150},
            "Tatkal": {"seats": 15, "price": 480},
            "Ladies": {"seats": 6, "price": 450},
            "Senior Citizen": {"seats": 8, "price": 420},
            "Physically Handicapped": {"seats": 5, "price": 650}
        },
        "12:45 AM"
    ),
    Train(
        "15625",
        "Thirupathi",
        "Guntur",
        {
            "1AC": {"seats": 2, "price": 2500},
            "2AC": {"seats": 82, "price": 1200},
            "3AC": {"seats": 26, "price": 900},
            "Sleeper": {"seats": 56, "price": 800},
            "General": {"seats": 96, "price": 200},
            "Tatkal": {"seats": 12, "price": 800},
            "Ladies": {"seats": 5, "price": 450},
            "Senior Citizen": {"seats": 42, "price": 300},
            "Physically Handicapped": {"seats": 12, "price": 300}
        },
        "04:35 AM"
    ),
    Train(
        "98655",
        "Kakinada",
        "Arunachal pradesh",
        {
            "1AC": {"seats": 8, "price": 1450},
            "2AC": {"seats": 15, "price": 1100},
            "3AC": {"seats": 2, "price": 920},
            "Sleeper": {"seats": 45, "price": 820},
            "General": {"seats": 96, "price": 280},
            "Tatkal": {"seats": 52, "price": 600},
            "Ladies": {"seats": 5, "price": 460},
            "Senior Citizen": {"seats": 15, "price": 300},
            "Physically Handicapped": {"seats": 45, "price": 380}
        },
        "06:15 PM"
    ),

]
# The program creates a list of trains objects , with each train havinng a unique number , source , detination and the number of seats available.

#display available trains
    for train in trains:
        train.display_info()
# If the logged_in_account variables is not none, it means that the user has successfully logged in . a message is printed confirming the login, and then a list of available train details is printed.

    
    while True:
        train_num = input("Enter train number: ")
        coach_type = input("Enter coach type (1AC, 2AC, Sleeper, etc.): ").strip()
        try:
            num_tickets = int(input("Enter number of tickets: "))
            if num_tickets <= 0:
                raise ValueError("Ticket count must be more than 0.")
            train = next((t for t in trains if t.train_num == train_num), None)
            if not train:
                raise ValueError("Train not found.")
            if coach_type not in train.coaches:
                raise ValueError("Invalid coach type.")
            if train.coaches[coach_type]["seats"] < num_tickets:
                raise ValueError("Not enough seats in this coach.")
            break
        except ValueError as e:
            print(f"Invalid input : {e}")
# The program asks the user to enter train number and the number of tickets they want to book.

train = None
for t in trains:
    if t.train_num == train_num:
        train = t
        break
# The program then searches for the train object with the corresponding train number entered by the user.

if train is None:
    print ("Invalid train number.")
# If the train is invalid , the program prints "Invalid train number." and exits.

else:
    passengers=[]
    for i in range(num_tickets):
        print(f"\nEnter details for passenger {i + 1}:")
        while True:
            try:
                name = input("Name :- ")
                if not name:
                    raise ValueError("Name cannot be empty")
                age = int(input("Age :- "))
                if age <=0 or age >120:
                    raise ValueError ("Invalid age")
                gender = input("Gender (M/F/O): ").strip().upper()
                if gender not in ["M", "F", "O"]:
                    raise ValueError("Invalid gender")
                mobile = input("Mobile number :- ")
                if not mobile or len(mobile) != 10 or not mobile.isdigit():
                    raise ValueError ("Invalid mobile number")
                passenger_obj = Passenger(name, age, gender, mobile)
                passengers.append(passenger_obj)
                break
            except ValueError as e:
                print(f"Invalid input: {e}")
# If the train number is invalid , the program prompts the user to enter the details of each passenger.
# For each passenger , the program creates a passanger object with the name , age , gender , and mobile number entered  by the user and appends it to a list of passengers.

    pnr_list = train.book_tickets(num_tickets,coach_type)
    if pnr_list is None:
        print("Tickets not available.")
# The program then calls the book_tickets method of the train object to book the tickets . if there are enough seats available , the book_tickets method returns a list of pnr numbers for tickets , which the programm saves in the list called pnr_list.
# If there are not enough seats available , the book_tickets nethod returns none , and the program prints "tickets not avalible ." and exits.
    else:
        print("\n-------------------- Booking successful! --------------------\n\nyour ticket details : \n")
        
    booking_time = datetime.now()
    
    for i in range(num_tickets):
        ticket_obj = Ticket(
            train,
            train.source,
            train.destination,
            [passengers[i]],
            pnr_list[i],
            train.departure_time,
            booking_time,
            coach_type,
            train.coaches[coach_type]["price"]
        )
        ticket_obj.display_info()
    
    print("\n----------Thank you---------- \n----------Safe journey----------")

# If the tickets are successfully booked , the program prints "booking successfully!" and creates a ticket object for each passwnger with the train , source , destination , passenger information and pnr number . the program then calls the display_info method of each ticket object to display the information to the user.