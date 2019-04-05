from flask import Flask, render_template,redirect,request,session


app = Flask(__name__)
class Candidate():
   def __init__(self,name,position,story):
      self.name = name
      self.route =  '/'+name
      self.position = position
      self.story = story
      # Vote
      # session[name] = 0

Thanos = Candidate('Thanos','president','Thanos wiped out half of the universe!!!')
Loki = Candidate('Loki','vice president',"Loki isn't low-key!")
Hela = Candidate('Hela','president',"Hela destroyed Thor's hammer!")
Venom = Candidate('Venom','vice president','Venom eats your head!')


candidatelist = [Thanos,Loki,Hela,Venom]
candidatenamelist = []
plist = []
vplist = []
for villian in candidatelist:
   candidatenamelist.append(villian.name)
   if villian.position == 'president':
      plist.append(villian.name)
   else:
      vplist.append(villian.name)

 
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
      return render_template('candidate.html',candidate = cdd.name, position = cdd.position, story = cdd.story)

@app.route('/vote/president')
def voteforp():
   return render_template('vote.html',position = 'President', id = 'p', candidatenamelist = plist)

@app.route('/vote/vicepresident')
def voteforvp():
   return render_template('vote.html',position = 'Vice president', id = 'p', candidatenamelist = vplist)

@app.route('/votesuccessful',methods = ['POST'])
def check():
   # session[p] += 1
   return render_template('sucess.html')

app.run(debug = True)