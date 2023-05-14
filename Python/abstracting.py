from abc import ABC, abstractmethod

class CallDeviceInterface(ABC):
	@abstractmethod
	def call():
		pass

class SmsDeviceInterface(ABC):
	@abstractmethod
	def sms():
		pass

class seatchDeviceInterface(ABC):
	@abstractmethod
	def call():
		pass

class MobilePhone(CallDeviceInterface, SmsDeviceInterface):
	def call(self):
		print("call")

	def sms():
		print("call")

mobile = MobilePhone()
mobile.call()