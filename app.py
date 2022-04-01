from flask import Flask, render_template
from udlaan import UdlaanForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'noget_hemmeligt'



@app.route('/', methods=['GET', 'POST'])
def start():
    print("1.   ")
    uform =  UdlaanForm()
    print(uform.errors)

    if uform.is_submitted():
        print("submitted")

    if uform.validate():
        print ("valid")

    print(uform.errors)
    print("2.   ")

    if uform.validate_on_submit():
        print(f"{uform.customerID.data}")
        print(f"{uform.inventoryID.data}")
        print(f"{uform.staffID.data}")
        print(f"{uform.amount.data}")
        print("4.   ")
    print("3.   ")
    return render_template('start.html', afrm = uform)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000", debug=True)


