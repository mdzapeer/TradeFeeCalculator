from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate",methods=['POST'])
def calculate():
    if request.method=='POST':
        balance = request.form['balance']
        investiable = request.form['investiable']
        unitSharePrice = request.form['unitSharePrice']
        shareNumber = request.form['shareNumber']
        shareCommission = request.form['shareCommission']
        fixedCommission = request.form['fixedCommission']
        # totalCommission = request.form['totalCommission']
        # totalInvestedCost = request.form['totalInvestedCost']
        # balanceAfter = request.form['balanceAfter']
        shareNumber=float(investiable)/float(unitSharePrice)
        totalCommission=shareNumber*float(shareCommission)+float(fixedCommission)
        totalInvestedCost=totalCommission+float(investiable)
        balanceAfter = float(balance) - totalInvestedCost
        print(totalInvestedCost)

        return render_template(
            "calculate.html",
            balance=balance,
            investiable=investiable,
            unitSharePrice=unitSharePrice,
            shareNumber=shareNumber,
            shareCommission=shareCommission,
            fixedCommission=fixedCommission,
            totalCommission=totalCommission,
            totalInvestedCost=totalInvestedCost,
            balanceAfter=balanceAfter
        )