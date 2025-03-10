document.addEventListener("DOMContentLoaded", function () {
    var choices = document.querySelectorAll(".choice");

    choices.forEach(function (choice) {
        choice.addEventListener("click", function () {
            var category = choice.innerText.trim();

            choices.forEach(function (item) {
                item.classList.remove("selected");
            });


            choice.classList.add("selected");


            if (category === "Depth") {
                chart("Depth (ft)");
            } else if (category === "ROP") {
                chart("ROP (ft/hr)");
            } else if (category === "Torque") {
                chart("Torque (ft-lbs)");
            } else if (category === "RPM") {
                chart("RPM");
            } else if (category === "Standpipe Pressure") {
                chart("Standpipe Pressure (psi)");
            } else if (category === "WOB") {
                chart("WOB (klbf)");
            } else if (category === "Hook Load") {
                chart("Hook Load (klbf)");
            } else if (category === "Mud Density") {
                chart("Mud Density (ppg)");
            } else if (category === "Mud Flow Rate") {
                chart("Mud Flow Rate (gpm)");
            } else if (category === "Gas Detection") {
                chart("Gas Detection (ppm)");
            }
        });
    });
});


function chart(category) {
    fetch(`/chart?category=${encodeURIComponent(category)}`)
        .then(response => response.json())
        .then(data => {
            var graph = JSON.parse(data);
            Plotly.newPlot('chart', graph.data, graph.layout);
        })

}


chart("Depth (ft)");