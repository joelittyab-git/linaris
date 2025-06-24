from logic import (
     Symbol,
     Not, 
     Or, 
     And, 
     Implication, 
     Biconditional,
     Proposition
)
from itertools import product

class LogicalInferenceEngine():
     def  __init__(self, knowledge:And):
          Proposition.validate(knowledge)
          self.knowledge_base = knowledge
          
     def evaluate_for(self, query:Proposition):
          '''Evaluaties a logical proposition based on the current knowledge_base'''
          
          def evaluate_query(query:Proposition, model):
               return query.evaluate(model)
               
          # creating all possible models of symbols and storing them in model space
          Proposition.validate(query)
          symbols = query.objects().union(self.knowledge_base.objects())
          n_s = len(symbols)
          
          # generates cartesian product of three sets of (True, False) values to attain all possible combination of models
          values = product([True, False], repeat=n_s)
          model_space = []
          for value in values:
               model_space.append(dict(zip(symbols, value)))
               
          # checks all model in model_space against the knowldge_base
          for model in model_space:
               if self.knowledge_base.evaluate(model=model):
                    if not evaluate_query(query, model):
                         return False
                    
          return True
     
     def add_knowledge(self, propostion:Proposition):
          '''Adds knowledge proposition to the knowledge base'''

          Proposition.validate(proposition=Proposition)
          self.knowledge_base.add(propostion)
                    