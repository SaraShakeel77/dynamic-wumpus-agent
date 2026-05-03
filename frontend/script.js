async function loadState() {
    const res = await fetch("http://127.0.0.1:5000/state");
    const data = await res.json();

    const grid = document.getElementById("grid");
    grid.innerHTML = "";

    for(let r=0;r<4;r++){
        for(let c=0;c<4;c++){
            const cell = document.createElement("div");
            cell.className = "cell unknown";

            if(data.visited.some(v => v[0]===r && v[1]===c))
                cell.className = "cell safe";

            if(data.agent[0]===r && data.agent[1]===c){
                cell.className = "cell agent";
                cell.innerText = "A";
            }

            grid.appendChild(cell);
        }
    }

    document.getElementById("metrics").innerHTML =
        `Percepts: ${data.percepts.join(", ")} |
         Inference Steps: ${data.inference_steps}`;
}

async function move(dir){
    await fetch(`http://127.0.0.1:5000/move/${dir}`);
    loadState();
}

loadState();