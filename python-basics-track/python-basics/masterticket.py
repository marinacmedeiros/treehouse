TICKET_PRICE = 10

tickets_remaining = 100

while tickets_remaining >=1:
	print("There are {} tickets remaining.".format(tickets_remaining))
	name = input("What is your name? ")
	num_tickets = input("How many tickets would youy like, {}? ".format(name))
	# Expect a ValueError to happen and handle it appropriately...remember to test it out!
	try:
		num_tickets = int(num_tickets)
		# Raise ValueError if the request is for more tickets than are available
		if num_tickets > tickets_remaining:
			raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
	except ValueError as err:
		# Include the error text in the output
		print("Oh no, we ran into an issue. {} Please try again!".format(err))
	else:
		amount_due = num_tickets * TICKET_PRICE
		print("The total due is ${}.".format(amount_due))
		should_proceed = input("Do you want to proceed? Y/N ")
		if should_proceed.lower() == "y":
			print("SOLD!")
			tickets_remaining -= num_tickets 
		else:
			print("Thank you anyways, {}!".format(name))
print("Sorry, the ticktes are all sold out! :(")


# #code with comments
# TICKET_PRICE = 10

# tickets_remaining = 100

# # Run this code continously until we run out of tickets
# while tickets_remaining >=1:

# 	# Output how many tickets are remaining using the tickets_remaining variable

# 	print("There are {} tickets remaining.".format(tickets_remaining))

# 	# Gather the user's name and assign it to a new variable
# 	name = input("What is your name? ")

# 	# Prompt the user by name and ask how many tickets they would like
# 	num_tickets = input("How many tickets would youy like, {}? ".format(name))
# 	num_tickets = int(num_tickets)

# 	# Calculete the price (number of tickets multiplied by the price) and assign it to a variable
# 	amount_due = (num_tickets * TICKET_PRICE)

# 	# Output the price to the screen 
# 	print("The total due is ${}.".format(amount_due))

# 	# Prompt user if they want to proceed. Y/N?
# 	should_proceed = input("Do you want to proceed? Y/N ")

# 	# If they want to proceed
# 	if should_proceed.lower() == "y":
# 		# print out to the screen "SOLD!" to confirm purchase
# 		# TO DO: Gather credit card information
# 		print("SOLD!")
# 		# And then decrement the tickets remaining by the number of tickets purchased
# 		tickets_remaining -= num_tickets 
# 	# Otherwise...
# 	else:
# 		#thank them by name
# 		print("Thank you anyways, {}!".format(name))

# # Notify user that the tickets are sold out
# print("Sorry, the ticktes are all sold out! :(")