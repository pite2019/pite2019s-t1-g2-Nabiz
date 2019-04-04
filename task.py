#!/usr/bin/python3

class Car(object):
	def __init__(self):
		self.speed = 0
		self.wheel_angle = 0
	def act(self,*event):
		eName = event[0]
		eValue = float(event[1])
		eTime = float(event[2])

		print(eName,eValue,eTime)

		if eName == '1':
			self.speed += eValue * eTime 
		elif eName == '2':
			self.wheel_angle += eValue * eTime;
			if(self.wheel_angle > 360+180):
				self.wheel_angle=360+180
			if(self.wheel_angle < -360-180):
				self.wheel_angle=-360-180
'''
	def wheel_angle(self):
		return self.wheel_angle
	def speed(self):
		return self.speed
'''
print("Hello!")
instruction="1. Add acceleration\n2. Change angle\n3. Exit"

car1 = Car()
while True:
	print("Current angle: "+str(car1.wheel_angle)+", Current speed: "+ str(car1.speed))
	print(instruction)
	option = input()
	if option == '3':
		break
	else:
		value = input("Type value:\n")
		time = input("Type duration time:\n")
		car1.act(option,value,time)