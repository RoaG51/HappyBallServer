from ServerApp import app,pw
from flask import request
import Functions

@app.route('/')
def index():
    return  "HomePage"

@app.route('/HB_showWorldRank')
def show_world_ranklist():
    return  Functions.showWorldRank()

@app.route('/HB_getSelfData',methods=['POST'])
def get_self_data():
    return  Functions.getSelfData(request.form['wxid'])

@app.route('/HB_buyItems',methods=['POST'])
def buy_items():
    if(request.form['pw'] == pw):
        Functions.buyItems(request.form['wxid'],request.form['itemNum'],request.form['sale'])
        return "updated"
    else:
        return "wrong pw"

@app.route('/HB_submitData',methods=['POST'])
def submit_data():
    if(request.form['pw'] == pw):
        Functions.submitData(request.form['wxid'],request.form['bestScore'],request.form['bestCombo'],request.form['coin'],request.form['name'],request.form['head'])
        return "submitted"
    else:
        return "wrong pw"