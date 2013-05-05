def _convert_list_of_dict(the_list_of_dicts):
	r_list = []
	for an_item in the_list_of_dicts:
		r_list.append(BaseImmutable(an_item))
	return r_list

class BaseImmutable():
	def __init__(self, a_dict):
		for key, value in a_dict.items():
			if isinstance(value, dict):
				self.__dict__[key] = BaseImmutable(value)
			elif isinstance(value, list):
				self.__dict__[key] = _convert_list_of_dict(value)
			else:
				self.__dict__[key] = value
	
	def __eq__(self, other):

		if not other.__dict__ == self.__dict__:
			print "this: " + str(self.__dict__)
			print "is not equal to this: " + str(other.__dict__)

		return other.__dict__ == self.__dict__

	def __ne__(self, other):
		return not self.__eq__(other.__dict__)

	def __setattr__(self, name, value):
		raise Exception("Immutable Object can not be changed")





