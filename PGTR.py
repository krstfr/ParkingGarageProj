import os
class ticket():
    AvailableParking = 100

    def __init__(self, name, price):
        self.name = name
        self.price = price

class ParkingCart():
    def __init__(self):
         self.cart ={} ##Item keys : "qty"values
         self.total= 0

    def add_ticket(self,ticket, qty=1):
        if ticket.name in self.cart.keys():
            self.cart[ticket.name]+=qty
        else:
            self.cart[ticket.name]=qty
        self.total += ticket.price*qty

    def remove_ticket(self,ticket,qty=1):
        if ticket.name in self.cart.keys():
            if self.cart[ticket.name]<=qty:
                del self.cart[ticket.name]
            else:
                self.cart[ticket.name]-= qty
        self.total -= ticket.price*qty

    def show_cart(self):
        for ticket, qty in self.cart.ticket():
            print(ticket.title(), qty)
        if len(self.cart.keys())<1:
            print("There are no tickets in your cart")
        else:
            print("Total: $", round(self.total,2))

    def clear_cart(self):
        self.cart.clear()

class UI():
    def __init__(self, parking_cart, ticket_list):
        self.cart = parking_cart
        self.ticket = ticket_list

    def run_UI(self):
        while True:
            response = input("What would you like to do: Add, Remove, Show, Clear Ticket(s)? or Quit? ").lower()
            if response == "quit": 
                self.cart.show_cart()
                break
            elif response== 'add':
                os.system('clear'if os.name == 'nt' else 'clear')
                print("Available Tickets: ")
                for ticket in self.ticket:
                    print(ticket.name.title(), "$"+str(ticket.price))
                add_ticket = input("Which ticket would you like to purchase? ").lower()
                for index, ticket in enumerate(self.ticket): 
                    if ticket.name.lower()== add_ticket:
                        qty = int(input("How many tickets would you like? "))
                        self.cart.add_ticket(ticket,qty)
                        print(f'{qty} {ticket.name}{"s" if qty>1 else " "} was added to your cart')
                        break
                    if index+1 == len(self.ticket):
                        print("Please choose one of the options listed. ")
                        break
            elif response == 'remove':
                os.system('clear'if os.name == 'nt' else 'clear')
                if len(self.cart.get_cart().keys()) <= 0:
                    print("Your cart is empty. Please select a ticket to purchase ")
                    continue
                print("Your cart: ")
                print("Ticket Name", "Quantity")
                for item, qty in self.cart.get_cart().ticket():
                    print(ticket.title(), qty)
                remove_ticket= input("Which ticket would you like to remove? ").lower()
                if remove_ticket not in self.cart.get_cart().keys():
                    print("Ticket not in your cart")
                    continue
                for ticket in self.ticket:
                    if ticket.name == remove_ticket:
                        qty = int(input("How many would you like to remove? "))
                        if qty > self.cart.get_cart()[ticket.name]:
                            print("You don't have that many ticket(s) to remove? ")
                            continue
                        self.cart.remove_ticket(ticket,qty) 

            elif response == 'clear': 
                os.system('clear'if os.name == 'nt' else 'clear')
                self.cart.clear_cart()
                print("You cart was cleared. ")

            elif response == 'show': 
                os.system('clear'if os.name == 'nt' else 'clear')
                self.cart.show_cart()
#Driver Code
general_parking = ticket("General", 2.99)
handicap_parking = ticket ("Handicap", .99)
cart = ParkingCart()

ui = UI(cart, [general_parking, handicap_parking])

ui.run_UI()

##IF I add the 'available' as an attribute to the first 'ticket' class, would that be\
## the correct step in establishing and eventually executing a command that will increase/decrease
##available parking? Essentially treating the 'available' attribute like the 'Qty' attribute