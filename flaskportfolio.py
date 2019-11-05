from flask import Flask, render_template, url_for
app = Flask(__name__)#creating app vairable. special variable, name of module.where flask can look for templates and static files

@app.route("/")#route decorators, functions returns info on website, returning text. may want to return some html.
def home():
    return render_template('home.html')

#@app.route("/about")#route decorators, functions returns info on website, returning text. may want to return some html.
#def about():
    #return render_template('about.html', title = 'About')


if __name__ == '__main__':
    app.run(debug=True)
