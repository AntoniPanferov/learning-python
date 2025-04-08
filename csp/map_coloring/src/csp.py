# From Classic Computer Science Problems in Python Chapter 3
# Copyright 2018 David Kopec
#

from typing import Generic, TypeVar, Dict, List, Optional
from constraint import Constraint

V = TypeVar('V') # variable type
D = TypeVar('D') # domain type
# Ein Bedingungserfüllungsproblem besteht aus Variablen vom Typ V,
# die Wertebereiche namens Domänen vom Typ D und Bedingungen haben,
# die bestimmen, ob die Domänenauswahl einer bestimmten Variablen gültig ist
class CSP(Generic[V, D]):
    '''
    variables: Erwartet eine Liste von Variablen
    domains: Erwartet ein Dictionary. Die Variablen sind der key. Die values zu den keys sind
        Listen mit den jeweils definierten/erlaubten Werten
    constraints: Erwartet ein Dictionary das jeder Variable eine Liste mit der für sie geltenden
        Bedingungen zuordnet. Initial enthält das Dictionary nur keys, die values sind leer.
        Values werden über add_constraint befüllt.
    '''
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables # Variablen, für die Bedingungen gelten
        self.domains: Dict[V, List[D]] = domains # Die Wertebereiche der Variablen
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        #Prüfen, ob jede Variable einen Wertebereich hat
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it.")

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

    # Check if the value assignment is consistent by checking all constraints
    # for the given variable against it
    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[List[Dict[V, D]]]:
        results: Optional[List[Dict[V, D]]]

        # assignment is complete if every variable is assigned (our base case)
        # Abbruchbedingung: Wenn alle Bedingungen der Variablen erfolgreich berücksichtigt wurden,
        # wird diese Lösung zurückgegeben und die weitere Suche eingestellt.
        ooo: List[Dict[V, D]]
        if len(assignment) == len(self.variables):
            ooo.append(assignment)
            return ooo

        # get all variables in the CSP but not in the assignment
        # unassigned enthält in einer Liste alle Variablen, die noch nicht erfolgreich überprüft wurden
        unassigned: List[V] = [v for v in self.variables if v not in assignment]
        '''print("unassigned List:",unassigned)'''
        # get the every possible domain value of the first unassigned variable
        # first: Nimmt den ersten Wert aus der unassigned-Liste
        first: V = unassigned[0]
        '''
        Wir versuchen, der Variablen nacheinander alle möglichen Domänenwerte zuzuweisen.
        Die neue Zuordnung für jeden Wert wird in einem lokalen Dictionary namens local_
        assignment gespeichert.
        '''
        for value in self.domains[first]:
            #print(value) #Aktuellen Farbwert ausgeben
            local_assignment = assignment.copy()
            #print(local_assignment) #Aktuelles local_assignment-Dictionary ausgeben
            local_assignment[first] = value
            #print("zweiter aufruf",local_assignment) #Neues aktuelles local_assignment-Dictionary ausgeben
            '''
            Wenn die neue Zuordnung in local_assignment mit allen Bedingungen konsistent ist
            (der Fall, auf den consistent() prüft), fahren wir unter Beibehaltung der neuen Zuord-
            nung mit der rekursiven Suche fort. 
            '''
            if self.consistent(first, local_assignment):
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
                '''
                Wenn die neue Zuordnung als vollständig herausstellt (die Abbruchbedingung), geben wir die neue
                Zuordnung entlang der Rekursionsaufrufe zurück.
                '''
                if result is not None:
                    results.append(result)
        '''
        Wenn wir schließlich jeden möglichen Domänenwert für eine bestimmte Variable
        durchgegangen sind und es keine Lösung unter Verwendung des bestehenden Satzes
        von Zuordnungen gibt, geben wir None zurück, was bedeutet, dass es keine Lösung gibt.
        Dies führt zum Backtracking die Rekursionskette hinauf bis zu dem Punkt, wo eine an-
        dere Zuordnung hätte gemacht werden können.
        '''
        if len(results) > 0:
            return results

        return None
