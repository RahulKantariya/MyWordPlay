from flask import Flask,render_template,request
import json
from difflib import get_close_matches
app = Flask(__name__)


@app.route('/')
def gettext():
    return render_template('index.html')

@app.route('/translator',methods=['POST','GET'])
def translator():
    if request.method == 'POST':
        word=request.form['text']
        data = json.load(open("data.json"))
        word = word.lower()
        if word in data:
            output=" ".join(data[word])
        else:
            return render_template('error.html',text='sorry!! this word doesn\'t exists, try agian ')
    return render_template('show.html',text=output)    
        
@app.route('/analyzer')
def analyzer():
    return render_template('index1.html',text="hello")

@app.route('/analyze',methods=['POST','GET'])
def analyze():
    global params
    if request.method=='POST':
        txt=request.form['text']
        removepunc=request.form.get('removepunc')
        capslock=request.form.get('capslock')
        
        charcount=request.form.get('charcount')
        

        if removepunc == "on":
            punctuations = ''' !()-{}[]:;'"\,<>./?@#$%^&*_~ '''
            analyzed = ""
            for char in txt:
                if char not in punctuations:
                    analyzed = analyzed + char
            params = {'purpose': 'REMOVE PUNCTUATION', 'analyzed_text': analyzed}
            txt = analyzed

        if capslock == 'on':
            analyzed = ""
            for char in txt:
                analyzed = analyzed + char.upper()
            params = {'purpose': 'CHANGE TO UPPERCASE', 'analyzed_text': analyzed}
            txt = analyzed

        if charcount == 'on':
            analyzed = ""
            count = 0
            for char in txt:
                count = count + 1
            params = {'purpose': 'CHARACTER COUNTING', 'analyzed_text': count}

        if (removepunc != "on"  and capslock != "on" and charcount != "on"):
            return render_template('error1.html')
        return render_template('analyzer.html',purpose=params['purpose'],analyzed_text=params['analyzed_text'])    








@app.route('/about')
def about():
    return render_template('about.html',text="hello")    
