from flask import Flask, render_template

app = Flask(__name__,template_folder="template",static_folder="static")

@app.route('/')
def resume():
    return render_template('res.html')

if __name__ == '__main__':
    app.run(debug=True,port=3300,host="0.0.0.0")
