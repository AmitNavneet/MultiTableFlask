from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/printMultiTable',methods=["POST"])
def printMultiTable():
    startNum=int(request.form.get('startNum'))
    stopNum=int(request.form.get('stopNum'))

    if startNum>stopNum:
        step=-1
        stopNum=stopNum-1
    else:
        step=1
        stopNum=stopNum+1

    message=''
    for num in range(startNum,stopNum,step):
        for row in range(1,11):
            message+=f"{num}x{row}={num*row}<br>"
        
        message+="<br><br>"
    
    return message

if __name__=='__main__':
    app.run(debug=True)