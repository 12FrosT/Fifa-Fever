#from src import app
import csv
from flask import Flask, render_template, request, jsonify, json, Response
#import watson_developer_cloud


app = Flask(__name__)

#conversation = watson_developer_cloud.ConversationV1(
#    username='<YOUR-USERNAME>',
#    password='<YOUR-PASSWORD>',
#    version='2017-05-26'
#)

#workspace_id = '<YOUR-WORKSPACE-ID>'
#context = {}

def data_year(year):
    sends=""
    with open('./data/WorldCupMatches.csv') as wcm:
        readCSV = csv.reader(wcm,delimiter=',')
        match=[]
        stage=[]
        for row in readCSV:
            if row[0]==year:
                match.append(row)
                if row[2] not in stage:
                    stage.append(row[2])

        group=[[] for i in range(0,len(stage))]
        for i in range(0,len(match)):
            group[stage.index(match[i][2])].append(match[i])
        si=0
        for i in group:
            sends+=(stage[si]+'<br>')
            si+=1
            for j in i:
                result=""
                if int(j[6])==int(j[7]):result="Draw"
                elif int(j[6])>int(j[7]):result=j[5]+" won"
                elif int(j[6])<int(j[7]):result=j[8]+" won"
                sends+=(j[5]+" vs "+j[8]+": "+result+'<br>')
    return sends

def data_team(team):
    sends=""
    with open('./data/WorldCupMatches.csv') as wcm:
        readCSV = csv.reader(wcm,delimiter=',')
        matchs=[]
        for i in readCSV:
            if i[5]==team or i[8]==team:
                matchs.append(i)
        won=0
        draw=0
        loss=0
        for j in matchs:
            if int(j[6])==int(j[7]):result="Draw"
            elif int(j[6])>int(j[7]):result=j[5]
            elif int(j[6])<int(j[7]):result=j[8]
            if result==team:won+=1
            elif result=="Draw":draw+=1
            else :loss+=1.
            sends+=("Fifa "+j[0]+": "+"Date:"+j[1]+" "+j[5]+" VS "+j[8]+" "+j[2]+" Stadium: "+j[3]+","+j[4]+" result: "+result+" "+j[6]+"-"+j[7]+'<br>')
        sends+=("Toal matches played:"+str(won+draw+loss)+", won:"+str(won)+", draw:"+str(draw)+", loss:"+str(loss)+'<br>')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET','POST'])
def send():
    json = request.get_json()
    return data_year(json['text'])





# @app.route('/bot')
# def bot():
#     return render_template('form.html')

# @app.route('/chat',methods=['POST'])
# def outputFile():
#     global context
#     msg = request.form['msg']
#     response = conversation.message(
#         workspace_id = workspace_id,
#         input={
#             'text': msg
#         },
#         context = context
#     )
#     context = response['context']
#     output = json.dumps(response, indent=2)
#     content = json.loads(output)
#     return render_template('form.html',output=content['output']['text'][0])

#@app.route('/send', methods=['POST'])
#def output():
#   global context
#    content = request.get_json()
#    msg = content['text']
#    print(msg)
#    response = conversation.message(
#        workspace_id = workspace_id,
#        input={
#            'text':msg
#        },
#        context = context
#    )
#    context = response['context']
#    return json.dumps(response, indent=2)
#
if __name__ == "__main__":
    app.run(debug=True)