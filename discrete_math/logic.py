class Proposition:
     
     def evaluate(self, model)->bool:
          '''Evaluates the logical proposition against a model containing values for each data item'''
          
          raise Exception("Nothing to evaluate ('evaluate' function not implemented)")
     
     def formula(self):
          '''Returns the string representation of the logic'''
          
          return ""
     
     def symbols(self):
          '''Returns the various symbols in the currect expression'''
          
          return set()
     
     def objects(self):
          '''Returns the set of all basic symbol objects in the current expression'''
          
          return set()
     
     @staticmethod
     def validate(proposition):
          '''Validates if an object is a proposition'''
          
          if not isinstance(proposition, Proposition):
               raise TypeError("Must be a logical proposition")
          
          
class Symbol(Proposition):
     def __init__(self, name):
          self.name = name
     
     def __str__(self):
          return self.__repr__()
     
     def __eq__(self, value):
          return isinstance(value, Symbol) and self.name == value.name
     
     def __repr__(self):
          return self.name
     
     def __hash__(self):
          return hash(("symbol", self.name))
          
     def evaluate(self, model:dict):
          try:
               # Checks for the symbol instance as a key in the model dictionary
               return bool(model[self])
          except KeyError:
               raise Exception("No symbol proposition in the provided model")
          
     def formula(self):
          return str(self.name)
     
     def symbols(self)->set:
          return {self.name}
     
     def objects(self):
          return {self}
     
     
class Not(Proposition):
     def __init__(self, operand:Proposition):
          Proposition.validate(operand)
          self.operand = operand
     
     def __eq__(self, value):
          return isinstance(value, Not) and self.operand == value.operand
     
     def __hash__(self):
        return hash(("not", hash(self.operand)))
   
     def __repr__(self):
          return f"NOT({self.operand})"
     
     def evaluate(self, model):
          return not self.operand.evaluate(model=model)
     
     def formula(self):
          return f"¬({self.operand.formula()})"
     
     def symbols(self):
          return self.operand.symbols()
     
     def objects(self):
          return self.operand.objects()
     
class And(Proposition):
     def __init__(self, *conj):
          if len(conj) < 2:
               raise Exception("And requires at least two operands.")
          for conjunction in conj:
               Proposition.validate(conjunction)
          self.conjuncts = list(conj)
          
     def __eq__(self, value):
          return isinstance(value, And) and self.conjuncts == value.conjuncts
     
     def __hash__(self):
          return hash(
                    ("and", tuple(hash(conjunct) for conjunct in self.conjuncts))
          )
          
     def __repr__(self):
          string = ", ".join([str(conjunct) for conjunct in self.conjuncts])
          return f"And({string})"
     
     def add(self, conj):
          Proposition.validate(conj)
          self.conjuncts.append(conj)
          
     def evaluate(self, model:dict):
          for conj in self.conjuncts:
               conj:Proposition = conj
               if not conj.evaluate(model=model):
                    return False
          return True
     def formula(self):
          string =  " ∧ ".join([conj.formula() for conj in self.conjuncts])
          return f"({string})"
     
     def symbols(self):
          return set.union(*[conj.symbols() for conj in self.conjuncts])
     
     def objects(self):
          return set.union(*[conj.objects() for conj in self.conjuncts])
     
class Or(Proposition):
     def __init__(self, *operands):
          if len(operands)<2:
               raise Exception("Or requires atleast two operands")
          for operand in operands:
               Proposition.validate(operand)
          self.operands = list(operands)
          
     def __eq__(self, value):
          return isinstance(value, Or) and self.operands == value.operands
     
     def __hash__(self):
          return hash(
                    ("or", tuple(hash(disjunct) for disjunct in self.operands))
          )
     def __repr__(self):
          string = ", ".join([str(oper) for oper in self.operands])
          return f"Or({string})"
     
     def add(self, disj):
          Proposition.validate(disj)
          self.operands.append(disj)
          
     def evaluate(self, model):
          for oper in self.operands:
               oper:Proposition = oper
               if oper.evaluate(model=model):return True
          return False
     
     def formula(self):
          string = " ∨ ".join([oper.formula() for oper in self.operands])
          return f"({string})"
     
     def symbols(self):
          return set.union(*[oper.symbols() for oper in self.operands])
     
     def objects(self):
          return set.union(*[oper.objects() for oper in self.operands])
     
class Implication(Proposition):
     def __init__(self, antecedent:Proposition, consequent:Proposition):
          Proposition.validate(antecedent)
          Proposition.validate(consequent)
          
          self.antecedent = antecedent
          self.consequent = consequent
          
          
     def __eq__(self, value):
          return (isinstance(value, Implication) 
               and self.antecedent == value.antecedent
               and self.consequent == value.consequent
          )

     def __hash__(self):
          return hash(('implies', hash(self.antecedent), hash(self.consequent)))
     
     def __repr__(self):
          return f"Implication({str(self.antecedent)}, {str(self.consequent)})"
     
     def evaluate(self, model):
          # The only scenario when the this proposition returns False is when the antecedent is True and consequent is False
          if self.antecedent.evaluate(model=model) and not self.consequent.evaluate(model=model):
               return False
          return True
     
     def formula(self):
          return f"({self.antecedent.formula()} => {self.consequent.formula()})"
     
     def symbols(self):
          return set.union(self.antecedent.symbols(), self.consequent.symbols())
     def objects(self):
          return set.union(self.antecedent.objects(), self.consequent.objects())
     
class Biconditional(Proposition):
     def __init__(self, left:Proposition, right:Proposition):
          Proposition.validate(left)
          Proposition.validate(right)
          self.left = left
          self.right = right
          
     def __eq__(self, value):
          return (isinstance(value, Biconditional) 
                  and self.right == value.right
                  and self.left == value.left 
               )
     def __hash__(self):
          return hash(('biconditional', hash(self.left), hash(self.right)))
     
     def __repr__(self):
          return f"Bicondition({str(self.left)}, {str(self.right)})"
     
     def evaluate(self, model):
          # checks for two truths or two false
          true_doublet = self.right.evaluate(model=model) and self.left.evaluate(model=model)
          false_doublet = (not self.right.evaluate(model=model)) and (not self.left.evaluate(model=model))
          
          if true_doublet or false_doublet:
               return True
          return False
     
     def formula(self):
          return f"({self.left.formula()} <=> {self.right.formula()})"
     
     def symbols(self):
          return self.right.symbols().union(self.left.symbols())
     
     def objects(self):
          return set.union(self.left.objects(), self.right.objects())