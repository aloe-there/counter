from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def counter():
    if "visits" in session:
        session["visits"] += 1
    else:
        session["visits"] = 1
    return render_template("index.html")

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)