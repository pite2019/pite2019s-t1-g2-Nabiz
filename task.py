#!/usr/bin/python3

class Event():

	names = {1:'startEngine',
	2:'stopEngine',
	3:'accelerate',
	4:'slow',
	5:'turnLeft',
	6:'turnRight'}

	def __init__(self,option):
		self.name = Event.names[option]
		self.value = 0
		self.time = 0
		if option > 2: 
			self.value = abs(float(input('Insert value:')))
		if  2 < option < 5:
			self.time = abs(float(input('Insert duration:')))

class Car():

	def __init__(self):
		self.engine_status = False
		self.speed = 0
		self.wheel_angle = 0
			
	def getParams(self):
		return (self.engine_status, self.speed, self.wheel_angle)

	def act(self,event):
		n = event.name
		v= event.value
		t = event.time

		if n == 'startEngine':
			self.startEngine()
		elif n == 'stopEngine':
			self.stopEngine()
		elif n == 'accelerate':
			self.accelerate(v,t)
		elif n == 'slow':
			self.slow(v,t)
		elif n == 'turnLeft':
			self.turnLeft(v)
		elif n == 'turnRight':
			self.turnRight(v)
		else:
			pass

	def startEngine(self):
		self.engine_status = True

	def stopEngine(self):
		self.engine_status = False
		self.speed = 0

	def accelerate(self,value=0,time=0):
		if self.engine_status == True:
			self.speed += value * time
	
	def slow(self,value=0,time=0):
		self.speed -= value * time
		if self.speed < 0:
			self.speed = 0

	def turnLeft(self,value=0):
		self.wheel_angle -= value
		if self.wheel_angle < -720:
			self.wheel_angle = -720
	
	def turnRight(self,value=0):
		self.wheel_angle += value
		if self.wheel_angle > 720:
			self.wheel_angle = 720



def main():

	car = Car()
	while True:
		print('''MENU:
1. Start engine
2. Stop engine
3. Add acceleration
4. Slow
5. Turn Left
6. Turn Right
0. Exit''')
		try:
			option = int(input())
			if option == 0:
				break
			else:
				event = Event(option)
		except Exception as e:
			print("Your input is wrong")
		
		car.act(event)
		print("Engine status: {} Speed: {} Wheel angle: {}".\
				format(*car.getParams()))

if __name__ == "__main__":
	main()