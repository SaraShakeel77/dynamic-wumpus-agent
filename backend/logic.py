class KnowledgeBase:
    def __init__(self):
        self.clauses = []
        self.inference_steps = 0

    def tell(self, clause):
        self.clauses.append(clause)

    def resolve(self, c1, c2):
        resolvents = []
        for literal in c1:
            if f"~{literal}" in c2:
                new_clause = (c1 - {literal}) | (c2 - {f'~{literal}'})
                resolvents.append(new_clause)
            elif literal.startswith("~") and literal[1:] in c2:
                new_clause = (c1 - {literal}) | (c2 - {literal[1:]})
                resolvents.append(new_clause)
        return resolvents

    def ask(self, query):
        clauses = self.clauses[:]
        clauses.append({f"~{query}"})

        new = []

        while True:
            n = len(clauses)
            for i in range(n):
                for j in range(i+1, n):
                    self.inference_steps += 1
                    resolvents = self.resolve(clauses[i], clauses[j])

                    if set() in resolvents:
                        return True

                    new.extend(resolvents)

            if all(c in clauses for c in new):
                return False

            clauses.extend(new)