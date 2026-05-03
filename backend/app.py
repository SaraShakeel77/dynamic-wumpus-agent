from flask import Flask, jsonify
from flask_cors import CORS
from world import WumpusWorld
from logic import KnowledgeBase

app = Flask(__name__)
CORS(app)

world = WumpusWorld()
kb = KnowledgeBase()

visited = set()

@app.route('/state')
def state():
    pos = world.agent
    percepts = world.percepts(pos)

    if "Breeze" not in percepts:
        for n in world.neighbors(*pos):
            kb.tell({f"Safe_{n}"})

    visited.add(pos)

    return jsonify({
        "agent": pos,
        "percepts": percepts,
        "visited": list(visited),
        "inference_steps": kb.inference_steps,
        "wumpus": world.wumpus,
        "pits": world.pits
    })

@app.route('/move/<direction>')
def move(direction):
    r, c = world.agent

    moves = {
        "up": (r-1,c),
        "down": (r+1,c),
        "left": (r,c-1),
        "right": (r,c+1)
    }

    if direction in moves:
        nr, nc = moves[direction]
        if 0 <= nr < world.rows and 0 <= nc < world.cols:
            world.agent = (nr,nc)

    return state()

if __name__ == '__main__':
    app.run(debug=True)