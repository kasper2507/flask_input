from flask import Flask, render_template
from udlaan import UdlaanForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'noget_hemmeligt'

@app.route('/', methods=['GET', 'POST'])
def start():
    uform =  UdlaanForm()

    if uform.validate_on_submit():
        print(uform.customerID.data)
        print("Sucess")


    print(uform.errors) 
    return render_template('start.html', afrm = uform)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000", debug=True)


