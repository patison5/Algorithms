# Написать декоратор, который будет выводить на экран имя декорируемой функции,
# а также все ее агрументы. Также он должен вывести результат выполнения функции

from functools import wraps
from typing import Callable, Optional

def debug(func: Callable):
	@wraps(func)
	def wraper(*args, **kwargs):
		print("Debug function name:", func.__name__)
		print("Debug function args", args)
		print("Debug function kwargs:", kwargs)
		result = func(*args, **kwargs)	
		print("result: ", result)
		print("")
		return result
	return wraper

def configurable_debug(exclude_args: list = [], exclude_kwargs: list = []):
	def wraper(func: Callable):
		@wraps(func)
		def inner(*args: tuple, **kwargs: dict):
			print("\n<------------ Debuging ------------>")
			result = func(*args, **kwargs)	
			printed_args = [arg for arg in args if arg not in exclude_args]
			printed_kwargs = {key: value for key, value in kwargs.items() if key not in exclude_kwargs}

			for key, kwarg in kwargs.items():
				print(key, kwarg)

			print("Debuging. Args to exclude: ", exclude_args, "kwargs to exclude", exclude_kwargs)
			print("Debug function name:", func.__name__)
			print("Debug function args", printed_args)
			print("Debug function kwargs:", printed_kwargs)
			print("result: ", result)
			print("<------------ Debuging ------------>\n")
			return result
		return inner
	return wraper

@configurable_debug(["Oh", "fucking", "word", "i", "fuck", "you"], ["keyword1"])
def get_message_length(message: Optional[str] = None, desctiption: Optional[str] = None, **kwargs) -> int:
	if message:
		return len(message)
	return 0

keywords = {'keyword1': 'foo', 'keyword2': 'bar'}

print(get_message_length("hello", "Oh", keyword1='oh', keyword2='God'))
get_message_length()