from base import BaseImmutable
from model import ImmutableModel

'''return dictonary object of object given keys minus ignore keys'''
def _sub_dict(object, keys, ignore=[]):
	return_dict = {}

	for key, value in object.__dict__.items():
		if key in keys and key not in ignore:
			return_dict[key] = value

'''return recursive (dictonaries within dictonaries) union of dictonary object.  object and sec_object must be dicts '''
def _r_sub_dict(object, second_obj):
	#todo: add checking for lists and convert immutable models contained within them.
	return_dict = {}
	for key,value in object.items():
		if key in second_obj.keys():
			if isinstance(value, dict) and isinstance(second_obj[key],dict):
				return_dict[key] = _r_sub_dict(value, second_obj[key])
			else:
				return_dict[key] = value
	return return_dict


'''convert all nested immutables into dict.  use im comparison, or kept public for you in cases of pretty printing'''
def convert_immutables(obj):
	new_dict = {}
	for key, value in obj.__dict__.items():
		if isinstance(value, BaseImmutable):
			new_dict[key] = convert_immutables(value)
		elif isinstance(value, list):
			new_dict[key] = _convert_list_of_immutables(value)
		else:
			new_dict[key] = value

	return new_dict

def _convert_list_of_immutables(a_list):
	r_immutable_list = []
	for immutable_obj in a_list:
		r_immutable_list.append(convert_immutables(immutable_obj))
	return r_immutable_list


'''create standalone immutable for comparison testing'''
def create(a_dict):
	return BaseImmutable(a_dict)

''' turn query set into list of immutable models'''
def immutable_model_list(list_o_models):
	a_list = []
	for a_model in list_o_models:
		a_list.append(ImmutableModel(a_model))
	return a_list

'''merges object's dict with one given.   cheaters way out of funcational style'''
def change(obj, new_dict):
	temp_dict = obj.__dict__
	for key,value in new_dict.items():
		temp_dict[key] = value

	return create(temp_dict)

'''returns true if the union of dicts are the same minus the key in the ignore list'''
def fuzzyEquals(obj, other_obj, ignore=[]):
	obj = convert_immutables(obj)
	other_obj =convert_immutables(other_obj)

	refined_obj = _r_sub_dict(other_obj, obj)
	refined_other = _r_sub_dict(obj, other_obj )

	if refined_obj != refined_other:
		pass
		#print 'not equal!'
		#print refined_other
		#print refined_obj

	return refined_obj == refined_other 
