from csp import CSP, Constraint
from typing import Dict, List


class SendMoreMoneyConstraint(Constraint[str, int]):
    def __init__(self, letters: List[str]) -> None:
        super().__init__(letters)
        self.letters = letters

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        if len(set(assignment.values())) < len(assignment):
            return False

        if len(assignment) == len(self.letters):
            s, e, n, d, m, o, r, y = [assignment[letter] for letter in "SENDMORY"]
            send = 1000 * s + 100 * e + 10 * n + d
            more = 1000 * m + 100 * o + 10 * r + e
            money = 10000 * m + 1000 * o + 100 * n + 10 * e + y
            return send + more == money
        return True


if __name__ == "__main__":
    letters = list("SENDMORY")
    domains = {letter: list(range(10)) for letter in letters}
    domains["S"].remove(0)
    domains["M"].remove(0)

    csp = CSP(letters, domains)
    csp.add_constraint(SendMoreMoneyConstraint(letters))

    solution = csp.backtracking_search()
    if solution:
        print(solution)
    else:
        print("Unsolvable")
