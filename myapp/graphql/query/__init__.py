from graphene import ObjectType 
from core.schema.utils import CustomNode 
from graphene_django.filter import DjangoFilterConnectionField 

from .Question import QuestionType 
from .Choice import ChoiceType 


class Query(ObjectType):
	question = CustomNode.Field(QuestionType) 
	all_question = DjangoFilterConnectionField(QuestionType) 

	choice = CustomNode.Field(ChoiceType) 
	all_choice = DjangoFilterConnectionField(ChoiceType) 


