from graphene import ObjectType

from .Question import QuestionMutation, RemoveQuestion 
from .Choice import ChoiceMutation, RemoveChoice 


class Mutation(ObjectType):
	question = QuestionMutation.Field() 
	remove_question = RemoveQuestion.Field() 

	choice = ChoiceMutation.Field() 
	remove_choice = RemoveChoice.Field() 

