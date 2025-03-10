setInterval(update, 60000);

function update(){

    fetch('/update')
        .then(response => response.json())
                .then(data => {
                    document.getElementById("depth").innerText = data.depth + " ft";
                    document.getElementById("ROP").innerText = data.ROP + " ft/hr";
                    document.getElementById("torque").innerText = data.torque + " ft-lbs";
                    document.getElementById("RPM").innerText = data.RPM;
                    document.getElementById("pipe").innerText = data.pipe + " psi";
                    document.getElementById("WOB").innerText = data.WOB + " klbf";
                    document.getElementById("hook").innerText = data.hook + " klbf";
                    document.getElementById("mud_den").innerText = data.mud_den + " ppg";
                    document.getElementById("mud_flow").innerText = data.mud_flow + " gpm";
                    document.getElementById("gas").innerText = data.gas + " ppm";
                })


}