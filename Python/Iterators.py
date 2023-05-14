# Напишите свой итератор

class MyIterator:
	def __init__(self, limit):
		self.limit = limit
		self.counter = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.counter < self.limit:
			self.counter += 1
			return self.counter
		else:
			raise StopIteration



myIter = MyIterator(5)
for i in myIter:
	print(i)



# Напишите декоратор функции, который будет 
# логировать входные параметры и результат

from functools import wraps
from typing import Callable

def loggin(func):
	@wraps(func)
	def wraper(*args, **kwargs):
		print("~ Debug ~")
		result = func(*args, **kwargs)
		print(result)
		print("~ Debug end ~")
		return result
	return wraper

@loggin
def testing_func():
	print("working process")


# Напишите декортор функции принимающий аргументы настройки

def loggin(custom_args, custom_kwargs):
	def wrapper(func):
		@wraps(func)
		def inner(*args, **kwargs):
			print("~ Debug ~")
			print(custom_args)
			print(custom_kwargs)
			result = func(*args, **kwargs)
			print(result)
			print("~ Debug end ~")
			return result
		return inner
	return wrapper

@loggin("hello", "world")
def testing_func():
	print("working process")

# testing_func()




# Напишите декоратор хеширования для функиции

def hashing(func: Callable):
	hashing_data = {}
	@wraps(func)
	def wraper(*args: tuple, **kwargs: dict):
		if args in hashing_data:
			print("getting from cache")
			return hashing_data[args]
		else:
			print("creating value")
			result = func(*args, **kwargs)
			hashing_data[args] = result
			return result
	return wraper


@hashing
def testing_func():
	print("working process")

testing_func()