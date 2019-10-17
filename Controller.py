from Linda import LindaTuplaSpace

class Controller():
	__instance = None

	@staticmethod
	def get_instance():
		if not Controller.__instance:
			Controller.__instance = Controller()
		return Controller.__instance

	def __init__(self):
		self.linda = LindaTuplaSpace.get_instance()

	def add(self,str_tuple):
		(publisher, topic, message) = self.linda._out(tuple(i for i in str_tuple.split(",")))
		return {'publisher':publisher,'topic':topic,'message':message}
	
	def read(self,tuple):
		return self.linda._rd(tuple)

	def remove(self,tuple):
		return self.linda._in(tuple)