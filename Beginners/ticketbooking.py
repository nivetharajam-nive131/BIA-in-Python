# define a function to book a movie ticket
def book_ticket():
    # ask for user input for movie, date, and number of tickets
    movie = input("Enter the movie name: ")
    date = input("Enter the date of the show (dd/mm/yyyy): ")
    tickets = int(input("Enter the number of tickets: "))
    # ask the user if they want to make an online payment
    payment = input("Do you want to make an online payment? (y/n): ")
    if payment == "y":
        # code to process online payment
        # ...
        print("Payment Successful!")
    else:
        print("You have chosen to pay at the counter.")

    # display the booking details
    print("Booking details:")
    print("Movie:", movie)
    print("Date:", date)
    print("Number of tickets:", tickets)
    print("Thank you for booking with us!")

#define a function to cancel the movie ticket
def cancel_ticket():
    # ask for user input for movie, date, and number of tickets
    movie = input("Enter the movie name: ")
    date = input("Enter the date of the show (dd/mm/yyyy): ")
    tickets = int(input("Enter the number of tickets: "))
    # display the cancelation details
    print("Cancellation details:")
    print("Movie:", movie)
    print("Date:", date)
    print("Number of tickets:", tickets)
    print("Ticket Cancelled Successfully!")

# call the function to book or cancel a ticket
while True:
    action = input("Enter 'b' to book a ticket or 'c' to cancel a ticket: ")
    if action == 'b':
        book_ticket()
    elif action == 'c':
        cancel_ticket()
    else:
        print("Invalid input. Please enter 'b' or 'c'.")
'''
Sample Output:
    Enter 'b' to book a ticket or 'c' to cancel a ticket: b
    Enter the movie name: varisu
    Enter the date of the show (dd/mm/yyyy): 15/01/2023
    Enter the number of tickets: 4
    Do you want to make an online payment? (y/n): y
    Payment Successful!
    Booking details:
    Movie: varisu
    Date: 15/01/2023
    Number of tickets: 4
    Thank you for booking with us!
    Enter 'b' to book a ticket or 'c' to cancel a ticket: c
    Enter the movie name: varisu
    Enter the date of the show (dd/mm/yyyy): 15/01/2023
    Enter the number of tickets: 2
    Cancellation details:
    Movie: varisu
    Date: 15/01/2023
    Number of tickets: 2
    Ticket Cancelled Successfully!
    Enter 'b' to book a ticket or 'c' to cancel a ticket: b
    Enter the movie name: thunivu
    Enter the date of the show (dd/mm/yyyy): 16/01/2023
    Enter the number of tickets: 4
    Do you want to make an online payment? (y/n): n
    You have chosen to pay at the counter.
    Booking details:
    Movie: thunivu
    Date: 16/01/2023
    Number of tickets: 4
    Thank you for booking with us!
'''
'''
Logic of above code: 
    The above Python program is a simple movie ticket booking system that allows users to book and cancel tickets. It includes a function book_ticket() that prompts the user for the movie name, date of the show, and number of tickets. The user also has the option to make an online payment, and the program will display a message if the payment is successful.  The program also includes a function cancel_ticket() which prompts the user for the same information as book_ticket() and display a message for successfully cancelling the ticket. A while loop is used to keep prompting the user to choose whether they want to book or cancel a ticket, and calls the appropriate function based on their choice. The program also has error handling in case the user enters an invalid input.
'''