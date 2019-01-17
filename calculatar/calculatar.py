from opratarsInCalculatar import *	
	
while True:
	def calculatar(num1,num2,operation):
		if operation =="add" or operation=="ADD":
			add(num1,num2,operation)

		elif operation == "subtract" or operation == "SUBTRACT":
			sub(num1,num2,operation)

		elif operation == "multiply" or operation == "MULTIPLY":
			mul(num1,num2,operation)

		elif operation == "division" or operation == "DIVISION":
			div(num1,num2,operation)

		elif operation == "modulas" or operation == "MODULAS":
			mod(num1,num2,operation)

	calculatar(num1 = int(raw_input("Enter number  ")),num2 = int(raw_input("Enter second number  ")),operation = (raw_input("Enter any operation for example 1.add 2.subtract 3.multiply 4.division 5.modulas   ")))

	Agen = raw_input("Do you want to play Agen Yes/No  ")
	if Agen == "No" or Agen == 'no':
		break