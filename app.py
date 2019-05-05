from flask import Flask, render_template, redirect, request, make_response, abort
import json
from pymongo import MongoClient
# ----app init-----
client = MongoClient(
    "mongodb+srv://admin:JettChen@cluster0-869xj.mongodb.net/test?retryWrites=true")
db = client.votes

app = Flask(__name__)

db = client.votes


def addvote(name):
    cd = db.votes.find_one({'name': name})
    cd['votes'] += 1
    db.votes.update_one({'_id': cd['_id']}, {'$set': {'votes': cd['votes']}})


class Candidate():
    def __init__(self, name, story, Type):
        self.name = name
        self.type = Type
        self.route = '/'+name
        self.story = story

    def vote(self):
        addvote(self.name)


TL = Candidate('Thanos and Loki',
               'Thanos and Loki, the most powerful couple!', 'villain')
HV = Candidate('Hela and Venom',
               "Hela destroyed Thor's hammer, and Venom got Eminem's help!", 'villain')
MR = Candidate('Magneto and Red Skull', 'A cute cuple from WWII!', 'villain')
US = Candidate('Ultron and Surtur', 'AI and a giant!', 'villain')
DI = Candidate('Dr Strange and Iron Man', 'Magic and technology!', 'hero')
SC = Candidate('Spiderman and Scarlet Witch', 'Spider and a witch!', 'hero')
DS = Candidate('Deadpool and Starlord',
               'Two of the most talkative heros in the Marvel universe!', 'hero')
GH = Candidate('Groot and Hulk', 'Two giants!!!', 'hero')
villainlist = [TL, HV, MR, US]
herolist = [DI, SC, DS, GH]
candidatelist = villainlist+herolist
villain_name_list = []
hero_name_list = []
for i in villainlist:
    villain_name_list.append(i.name)
for i in herolist:
    hero_name_list.append(i.name)
candidatenamelist = villain_name_list + hero_name_list
# Routes
@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/<candidate>')
def generate(candidate):
    if candidate not in candidatenamelist:
        abort(404)
    else:
        i = candidatenamelist.index(candidate)
        cdd = candidatelist[i]
        return render_template('candidate.html', candidate=cdd.name, story=cdd.story, Type=cdd.type)


@app.route('/vote/hero')
def votehero():
    return render_template('vote.html', candidatenamelist=hero_name_list, Type='hero')


@app.route('/vote/villain')
def votevillain():
    return render_template('vote.html', candidatenamelist=villain_name_list, Type='villain')


@app.route('/votesuccessful', methods=['POST'])
def check():
    candidatelist[candidatenamelist.index(request.form['p'])].vote()
    return render_template('sucess.html')


@app.route('/stats')
def show_stats():
    return render_template('stats.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
