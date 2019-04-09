from flask import Flask, render_template,redirect,request,make_response
import json
# ----app init-----
with open('votes.json','r') as f:
   data = json.load(f)
app = Flask(__name__)
class Candidate():
   def __init__(self,name,story):
      self.name = name
      self.route =  '/'+name
      self.story = story
      self.votes = data[self.name]
   def vote(self):
      data[self.name]+=1
      with open('votes.json','w') as f:
         json.dump(data,f)
TL = Candidate('Thanos and Loki','Thanos and Loki, the most powerful couple!')
HV = Candidate('Hela and Venom',"Hela destroyed Thor's hammer, and Venom got Eminem's help!")
MR = Candidate('Magneto and Red Skull','A cute cuple from WWII!')
US = Candidate('Ultron and Surtur','AI and a giant!')

candidatelist = [TL,HV,MR,US]
candidatenamelist = []
for i in candidatelist:
   candidatenamelist.append(i.name) 
# Routes
@app.route('/')
def homepage():
   return render_template('index.html')


@app.route('/<candidate>')
def generate(candidate):
   if candidate not in candidatenamelist:
      return
   else:
      i = candidatenamelist.index(candidate)
      cdd = candidatelist[i]
      return render_template('candidate.html',candidate = cdd.name, story = cdd.story)
@app.route('/vote')
def voting():
   return render_template('vote.html',candidatenamelist = candidatenamelist)
@app.route('/votesuccessful',methods = ['POST'])
def check():
   candidatelist[candidatenamelist.index(request.form['p'])].vote()
   return render_template('sucess.html')
@app.route('/stats')
def show_stats():
   return str(data)
if __name__ == '__main__':
   app.run(debug=True)