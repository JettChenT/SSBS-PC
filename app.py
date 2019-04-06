from flask import Flask, render_template,redirect,request,session
import json
# ----app init-----
with open('votes.json','r') as f:
   data = json.load(f)
app = Flask(__name__)
class Candidate():
   def __init__(self,name,position,story):
      self.name = name
      self.route =  '/'+name
      self.position = position
      self.story = story
      self.votes = data[self.name]
      # Vote
      # session[name] = 0
   def vote(self):
      data[self.name]+=1
      with open('votes.json','w') as f:
         json.dump(data,f)
Thanos = Candidate('Thanos','president','Thanos wiped out half of the universe!!!')
Loki = Candidate('Loki','vice president',"Loki isn't low-key!")
Hela = Candidate('Hela','president',"Hela destroyed Thor's hammer!")
Venom = Candidate('Venom','vice president','Venom eats your head!')
Magneto = Candidate('Magneto','president','Magneto!!!')
RedSkull = Candidate('Red Skull','vice president','Reeeeeeed Skulllllllllll!!!!!!')
Ultron = Candidate('Ultron','president','Ultron is anywhere!')
Surtur = Candidate('Surtur','vice president','Sutur is going to destroy Asguard!!!')
candidatelist = [Thanos,Loki,Hela,Venom,Magneto,RedSkull,Ultron,Surtur]
candidatenamelist = []
plist = []
vplist = []
for villian in candidatelist:
   candidatenamelist.append(villian.name)
   if villian.position == 'president':
      plist.append(villian.name)
   else:
      vplist.append(villian.name)

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
      lis = cdd.position.split(' ')
      pst = ''.join(lis)
      return render_template('candidate.html',candidate = cdd.name, position = cdd.position, story = cdd.story,pst = pst)

@app.route('/vote/president')
def voteforp():
   return render_template('vote.html',position = 'President', candidatenamelist = plist)
@app.route('/vote/vicepresident')
def voteforvp():
   return render_template('vote.html',position = 'Vice president', candidatenamelist = vplist)
@app.route('/votesuccessful',methods = ['POST'])
def check():
   candidatelist[candidatenamelist.index(request.form['p'])].vote()
   return render_template('sucess.html')
@app.route('/stats')
def show_stats():
   pprint = ''
   for i in data:
      pprint+=i+':'+str(data[i])+'</br>'
   return pprint
if __name__ == '__main__':
   app.run(debug=True)