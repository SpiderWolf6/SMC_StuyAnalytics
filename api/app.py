#Import necessary packages
import os
import pickle
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, session, jsonify, send_file
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
from waitress import serve
from datetime import date, datetime, timedelta
import dateutil.parser as date_parser
import gevent
from gevent.pywsgi import WSGIServer

#Create separate Flask Apps for the home page, metrics, players, dates, and graph pages
app = Flask(__name__)
metrics_app = Flask(__name__)
players_app = Flask(__name__)
dates_app = Flask(__name__)
graph_app = Flask(__name__)
CORS(app)
CORS(metrics_app)
CORS(players_app)
CORS(dates_app)
CORS(graph_app)
api = Api(app)
metrics_api = Api(metrics_app)
players_api = Api(players_app)
dates_api = Api(dates_app)
graph_api = Api(graph_app)

#Initialize RequestParser and add arguments, which will help receive and parse post requests
parser = reqparse.RequestParser()
parser.add_argument("first_name")
parser.add_argument('list_names', '--list', action='append', help='<Required> Set flag', required=True)
parser.add_argument('date_range', '--list', action='append', help='<Required> Set flag', required=True)
parser.add_argument("metric")
parser.add_argument("test")

metrics_parser = reqparse.RequestParser()
metrics_parser.add_argument("metric")

players_parser = reqparse.RequestParser()
players_parser.add_argument("average")
players_parser.add_argument("player_names", '--list', action='append', help='<Required> Set flag', required=True)

dates_parser = reqparse.RequestParser()
dates_parser.add_argument("date_range", '--list', action='append', help='<Required> Set flag', required=True)

#Create dictionary with players roster and associated information to easily graph desired output later
data = {"Name": ["Eben Eichenwald", "Giles El-Assal", "Anselm", "Farzad Hoque ",
                 "Nicholas Jung", "Martin I", "Ryan Petrauskas",
                 "Jack", "Aden", "Mitchell Deutsch",
                 "Patrick Kawulok", "Kaeden Ruparel", "Soham Mukherjee", "Frederik", "Duncan",
                 "Michael",
                 "Ethan", "Rafael Zornoza ", "Noah", "Gabriel", "Stefan Broge", "John Kennedy"],
        "Position": ["LB", "LCB", "RCB", "RB", "LCM", "CM", "RCM", "LW", "ST", "RW", "SUB", "SUB",
                     "SUB",
                     "SUB", "SUB", "SUB", "SUB", "SUB", "SUB", "SUB", "SUB", "SUB"],
        "Number": ["#34", "#15", "#20", "#9", "#16", "#8", "#6", "#30", "#11", "#5",
                   "#47", "#4", "#19", "#23", "#25", "#18", "#21", "#27", "#12", "#33", "#36", "#35"]}
map_key = pd.DataFrame(data=data)
print(map_key)

d = {}
fin = []

#Using read_files and findpath, read Catapult raw data files from computer files
def read_files(file_path, name):
    with open(file_path, 'r') as file:
        d[name] = pd.read_csv(file_path, usecols=[2, 8, 10, 15, 16, 17])
        d[name].loc["Average"] = d[name].mean(numeric_only = True)
        d[name].insert(0, "Date", name, True)
        fin.append(d[name])

def findpath(path):
    for dirpath, dirname, filename in os.walk(path):
        for f in filename:
            path_new = os.path.join(dirpath, f)
            if f.endswith('_22.csv'):
                name = f[16:24]
                read_files(path_new, name)

findpath("C:/goutam/soham/Catapult") #replace with appropriate filepath
fin_new = pd.concat(fin)

#Initialize home page
@app.route("/home", methods=['GET', 'POST'])
def home():
    return ("Python says hello")

#Get selected metric
@metrics_app.route("/metrics_selection", methods=['GET', 'POST'])
def metrics_selection():
    args = metrics_parser.parse_args()
    global mtr
    mtr = args["metric"]
    print(mtr)
    return ("Metric selection has been changed to: " + str(mtr))

#Get player squad numbers
@players_app.route("/players_selection", methods=['GET', 'POST'])
def players_selection():
    args = players_parser.parse_args()
    global players
    players = args["player_names"]
    print(players)
    global average
    average = args["average"]
    print(average)
    return ("Player selection has been changed to " + str(players) + "Average turned on: " + str(average))

#Get dates range and feed dates_command function
@dates_app.route("/dates_selection", methods=['GET', 'POST'])
def dates_selection():
    args = dates_parser.parse_args()
    global dates
    dates = args["date_range"]
    print(dates)
    print(dates_command(dates))
    return ("Session range has been changed to include " + str(dates_command(dates)))

#Use input variables (players, metrics, session) to return desired graph as PNG file
@graph_app.route("/graph", methods=['GET', 'POST'])
def graph():
    print(dates)
    print(players)
    print(mtr)
    print(average)
    dates_command(dates)

    disp = fin_new[["Date", "Player Name", mtr]]
    disp = disp.replace(r"_", "-", regex=True)
    for value in disp["Date"]:
        cool = date_parser.parse(value, dayfirst=True)
        value = cool
    disp["Date"] = pd.to_datetime(disp["Date"])

    selected_players=[]
    for s in players:
        for index,row in map_key.iterrows():
            if row["Number"] == s:
                print(row["Name"])
                selected_players.append(row["Name"])
    print("selected players list:" + str(selected_players))

    sdate = date_parser.parse(dates[0]).date()
    edate = date_parser.parse(dates[1]).date()
    date_range_old = pd.date_range(sdate, edate - timedelta(days=1),freq='d')
    date_range_new = []
    for d in date_range_old:
        date_range_new.append(d.date())
    print("This is date range new:" + str(date_range_new))

    temp = []
    for x in selected_players:
        filter_name = disp["Player Name"].isin([x.title()])
        disp_new = disp[filter_name]
        for y in date_range_new:
            filter_date = disp_new["Date"].isin([y])
            disp_fin = disp_new[filter_date]
            print(disp_fin)
            temp.append(disp_fin)
    test = pd.concat(temp)
    test["Date"] = test["Date"].astype(str)
    print(test)

    plt.clf()
    sns.set(color_codes=True)
    sns.set(rc={'figure.figsize': (11.7, 8.27)})

    if average == True:
        sns.lineplot(x=test["Date"], y=test[mtr]).set(title="Graph1")
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
    else:
        sns.barplot(x=test["Date"], y=test[mtr], hue=test["Player Name"]).set(
            title="Graph1")
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

    plt.show()
    plt.savefig("test100.png", transparent=True, bbox_inches='tight', dpi=150)
    return send_file('test100.png', mimetype='image/png')

#Gather all dates between start and end date, convert to correct datetime format
def dates_command(range):
    sdate = date_parser.parse(range[0])
    edate = date_parser.parse(range[1])
    print("This is sdate:" + str(sdate))
    print("This is edate:" + str(edate))
    date_range = pd.date_range(sdate, edate - timedelta(days=1),freq='d')
    return date_range

#Assign every server a unique localhost port and start servers
home_server = WSGIServer(("0.0.0.0", 5000), app)
home_server.start()

metrics_server = WSGIServer(("0.0.0.0", 5001), metrics_app)
metrics_server.start()

players_server = WSGIServer(("0.0.0.0", 5002), players_app)
players_server.start()

dates_server = WSGIServer(("0.0.0.0", 5003), dates_app)
dates_server.start()

graph_server = WSGIServer(("0.0.0.0", 5004), graph_app)
graph_server.start()

#Host all servers using Gevent loop
while True:
    gevent.sleep(60)