class Car(object):
	def __init__(self):
		self.speed = 0
		self.wheel_angle = 0
	def act(*event):
		eName = event[1]
		eValue = event[2]
		eTime = event[3]

		print(eName,eValue,eTime)

		if eName == '1':
			self.speed += eValue * eTime 
		elif eName == '2':
			self.wheel_angle += eValue * eTime;
			if(self.wheel_angle > 360+180):
				self.wheel_angle=360+180
			if(self.wheel_angle < -360-180):
				self.wheel_angle=-360-180
	def wheel_angle():
		return self.wheel_angle
	def speed():
		return self.speed

print("Hello!")
instruction="1. Add acceleration\n2. Change angle\n3. Exit"

car1 = Car()
while True:
	print("Current angle: %f, Current speed %f") % (car1.wheel_angle, car1.speed)
	print(instruction)
	option = raw_input()
	if option == '3':
		break
	else:
		value = raw_input("Type value:\n")
		time = raw_input("Type duration time:\n")
		car1.act(option,value,time)