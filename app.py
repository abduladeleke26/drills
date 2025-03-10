from flask import Flask, render_template, jsonify, request
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
import os
app = Flask(__name__)


current_time = datetime.now().time().replace(microsecond=0)


os.environ['TZ'] = 'America/Chicago'


file_path = ""

df = None



def getInfo():
    global df
    df = pd.read_csv(file_path)


    df["Timestamp"] = pd.to_datetime(df["Timestamp"]).dt.strftime("%H:%M:%S")


    current_time = datetime.now().strftime("%H:%M:%S")
    five_min_ago = (datetime.now() - timedelta(minutes=5)).strftime("%H:%M:%S")


    recent_data = df[(df["Timestamp"] >= five_min_ago) & (df["Timestamp"] <= current_time)]

    return recent_data.values.tolist()

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/black_thunder_rig')
def black_thunder_rig():
    global file_path

    file_path = "data/Black Thunder Drill.csv"

    data = getInfo()



    depth = data[0][1]
    ROP = data[0][2]
    WOB = data[0][3]
    torque = data[0][4]
    RPM = data[0][5]
    pipe = data[0][6]
    mud_flow = data[0][7]
    hook = data[0][8]
    mud_den = data[0][9]
    gas = data[0][10]



    return render_template("rig.html", name ="Black Thunder Rig ⚡", depth=round(depth,2),ROP=round(ROP,2),WOB=round(WOB,2),torque=round(torque,2),RPM=round(RPM,2),pipe=round(pipe,2),mud_flow=round(mud_flow,2),mud_den=round(mud_den,2),gas=round(gas,2), hook=round(hook,2), tag="b", data="Black Thunder Drill.csv" )

@app.route('/blackrock_7_well')
def blackrock_7_well():
    global file_path

    file_path = "data/Blackrock-7 Well.csv"

    data = getInfo()



    depth = data[0][1]
    ROP = data[0][2]
    WOB = data[0][3]
    torque = data[0][4]
    RPM = data[0][5]
    pipe = data[0][6]
    mud_flow = data[0][7]
    hook = data[0][8]
    mud_den = data[0][9]
    gas = data[0][10]



    return render_template("rig.html", name ="Blackrock-7 Well", depth=round(depth,2),ROP=round(ROP,2),WOB=round(WOB,2),torque=round(torque,2),RPM=round(RPM,2),pipe=round(pipe,2),mud_flow=round(mud_flow,2),mud_den=round(mud_den,2),gas=round(gas,2), hook=round(hook,2), tag="z", data="Blackrock-7 Well.csv" )

@app.route('/super_drill')
def super_drill():
    global file_path

    file_path = "data/Super drill.csv"

    data = getInfo()



    depth = data[0][1]
    ROP = data[0][2]
    WOB = data[0][3]
    torque = data[0][4]
    RPM = data[0][5]
    pipe = data[0][6]
    mud_flow = data[0][7]
    hook = data[0][8]
    mud_den = data[0][9]
    gas = data[0][10]



    return render_template("rig.html", name ="Super Drill", depth=round(depth,2),ROP=round(ROP,2),WOB=round(WOB,2),torque=round(torque,2),RPM=round(RPM,2),pipe=round(pipe,2),mud_flow=round(mud_flow,2),mud_den=round(mud_den,2),gas=round(gas,2), hook=round(hook,2), tag="s", data="Super drill.csv" )

@app.route('/arctic_drill')
def arctic_drill():
    global file_path

    file_path = "data/Arctic Drill.csv"

    data = getInfo()



    depth = data[0][1]
    ROP = data[0][2]
    WOB = data[0][3]
    torque = data[0][4]
    RPM = data[0][5]
    pipe = data[0][6]
    mud_flow = data[0][7]
    hook = data[0][8]
    mud_den = data[0][9]
    gas = data[0][10]



    return render_template("rig.html", name ="Arctic Drill ❄️", depth=round(depth,2),ROP=round(ROP,2),WOB=round(WOB,2),torque=round(torque,2),RPM=round(RPM,2),pipe=round(pipe,2),mud_flow=round(mud_flow,2),mud_den=round(mud_den,2),gas=round(gas,2), hook=round(hook,2), tag="c", data="Arctic Drill.csv" )

@app.route('/update')
def update():
    data = getInfo()


    depth = round(data[0][1],2)
    ROP = round(data[0][2],2)
    WOB = round(data[0][3],2)
    torque = round(data[0][4],2)
    RPM = round(data[0][5],2)
    pipe = round(data[0][6],2)
    mud_flow = round(data[0][7],2)
    hook = round(data[0][8],2)
    mud_den = round(data[0][9],2)
    gas = round(data[0][10],2)

    return jsonify({
        "depth":depth, "ROP":ROP, "WOB":WOB, "torque":torque, "RPM":RPM, "pipe":pipe, "mud_flow":mud_flow, "hook":hook,
        "mud_den":mud_den, "gas":gas

    })


@app.route('/chart')
def chart():
    category = request.args.get("category")


    df["Timestamp"] = pd.to_datetime(df["Timestamp"], format="%H:%M:%S").apply(
        lambda t: datetime.combine(datetime.today().date(), t.time())
    )

    start = datetime.combine(datetime.today().date(), datetime.strptime("00:00:58", "%H:%M:%S").time())
    right_now = datetime.now()
    times = df[(df["Timestamp"] >= start) & (df["Timestamp"] <= right_now)]

    if category == "Depth (ft)":
        title = "Depth"
    elif category == "ROP (ft/hr)":
        title = "Rate of Penetration"
    elif category == "WOB (klbf)":
        title = "Weight on Bit"
    elif category == "Torque (ft-lbs)":
        title = "Torque"
    elif category == "RPM":
        title = "Rotations Per Minute"
    elif category == "Standpipe Pressure (psi)":
        title = "Standpipe Pressure"
    elif category == "Mud Flow Rate (gpm)":
        title = "Mud Flow Rate"
    elif category == "Hook Load (klbf)":
        title = "Hook Load"
    elif category == "Mud Density (ppg)":
        title = "Mud Density"
    elif category == "Gas Detection (ppm)":
        title = "Gas Detection"
    else:
        title = "Unknown Category"


    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=times["Timestamp"],
        y=times[category],
        mode="lines",
        name=title
    ))

    fig.update_layout(
        title=title,
        xaxis_title="Time (HH:MM:SS)",
        yaxis_title=category,
        xaxis=dict(tickformat="%H:%M:%S"),
        template="plotly_dark",
    )

    return jsonify(fig.to_json())


if __name__ == "__main__":
    app.run(debug=True)