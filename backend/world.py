import random

class WumpusWorld:
    def __init__(self, rows=4, cols=4):
        self.rows = rows
        self.cols = cols
        self.grid = [['' for _ in range(cols)] for _ in range(rows)]
        self.agent = (0, 0)
        self.place_hazards()

    def place_hazards(self):
        cells = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        cells.remove((0, 0))

        self.wumpus = random.choice(cells)
        cells.remove(self.wumpus)

        self.pits = random.sample(cells, min(3, len(cells)))

    def neighbors(self, r, c):
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        result = []
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                result.append((nr,nc))
        return result

    def percepts(self, pos):
        r, c = pos
        percepts = []

        for n in self.neighbors(r,c):
            if n in self.pits:
                percepts.append("Breeze")
            if n == self.wumpus:
                percepts.append("Stench")

        return percepts