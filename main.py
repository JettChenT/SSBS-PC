from flask import Flask, render_template,redirect

app = Flask(__name__)
class Candidate():
   def __init__(self,name,position,story):
      self.name = name
      self.route =  '/'+name
      self.position = position
      self.story = story
Thanos = Candidate('Thanos','president','Thanos wiped out half of the universe!!!')
Loki = Candidate('Loki','vice president',"Loki isn't low-key!")

candidatelist = [Thanos,Loki]
candidatenamelist = []
for villian in candidatelist:
   candidatenamelist.append(villian.name)

 
@app.route('/')
def homepage():
   return render_template('index.html')


@app.route('/<candidate>')
def generate(candidate):
   if candidate not in candidatenamelist:
      return redirect('/404')
   else:
      i = candidatenamelist.index(candidate)
      cdd = candidatelist[i]
      return render_template('candidate.html',candidate = cdd.name, position = cdd.position, story = cdd.story)


app.run(debug = True)