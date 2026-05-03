Here is a **ready-to-paste `README.md`** for your GitHub repo. Just copy everything below and paste it into `README.md` on GitHub.

---

```markdown
# Dynamic Wumpus Logic Agent

## Overview
This project is a Web-based Dynamic Wumpus World Agent that uses Artificial Intelligence concepts to navigate a grid environment safely. The agent applies propositional logic, a knowledge base, and resolution refutation to infer safe and unsafe cells in real time.

---

## Features
- Dynamic grid size (Rows × Columns)
- Random placement of Wumpus and Pits
- Percept generation (Breeze and Stench)
- Knowledge Base for logical reasoning
- Resolution Refutation for safety checking
- Real-time agent movement
- Web-based visualization dashboard
- Inference step counter

---

## Technologies Used
- Python
- Flask
- HTML
- CSS
- JavaScript

---

## Project Structure
```

backend/
app.py
world.py
logic.py
requirements.txt

frontend/
index.html
style.css
script.js

report/
(PDF Report)

````

---

## How to Run the Project

### 1. Install Dependencies
```bash
pip install -r backend/requirements.txt
````

### 2. Run Backend Server

```bash
cd backend
python app.py
```

Server runs at:

```
http://127.0.0.1:5000
```

---

### 3. Run Frontend

Open:

```
frontend/index.html
```

in your browser.

---

## AI Logic Explanation

### Knowledge Base

The agent stores logical rules based on percepts received from the environment.

### Percepts

* Breeze → Nearby Pit
* Stench → Nearby Wumpus

### Resolution Refutation

The system checks if a cell is safe by assuming danger and trying to derive a contradiction using stored logical clauses.

If contradiction is found → cell is SAFE.

---

## Objective

To demonstrate a Knowledge-Based Agent that uses logical reasoning and inference to make decisions in an uncertain environment.

---

