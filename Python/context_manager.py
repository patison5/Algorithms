class Resource:
	def __init__(self, name):
		print('Resource: create {}'.format(name))
		self.__name = name
		
	def get_name(self):
		return self.__name

	def start_work(self):
		print('Resource: close')


class ResouceContextWith:
	def __init__(self, name):
		self.__resource = Resource(name)

	def __enter__(self):
		return self.__resource

	def __exit__(self, type, value, traceback):
		self.__resource.start_work()


with ResouceContextWith('Worker') as r:
	print(r.get_name())


print("\n")

from contextlib import contextmanager

@contextmanager
def processor():
	print("start process")
	yield
	print('stop process')

with processor():
	print("processing")


@contextmanager
def open_file(path, mode):
	f = open(path, mode)
	yield f
	f.close()

with open_file("test.txt", 'w') as fw:
	fw.write("hello")