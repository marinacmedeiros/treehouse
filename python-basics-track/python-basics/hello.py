first_name = input("What is your first name? ")
print("Hello, {}!!".format(first_name))
if first_name =="Amora":
	print(first_name, "is learning Python.")
elif first_name == "Adail":
	print("You still have a lot to learn, Padawan {}!!".format(first_name))
else:
	#just a ranodm  comment
	age = int(input("How old are you? "))
	if age <= 5:
		print("Wow, you're {}! If you're confident with your reading already...".format(age))
	print("You should totally learn Python, {}!!".format(first_name))
print("Have a great day, {}!".format(first_name))



