from flask import Flask, render_template,redirect,flash

app=Flask(__name__)
from form import RegistrationForm,loginForm
app.config["SECRET_KEY"]="willaddlater"
posts=[
    {
    "author":"Sandeep",
    "title":"ME learning Flask",
    "content":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Incidunt consectetur, mollitia repellat corporis eveniet expedita tempore! Laudantium minima voluptatem eaque velit dolore reprehenderit, vero alias eius illum sit, blanditiis excepturi.",
    "date":"27 March 2021"
    },
    {
    "author":"Sandeep",
    "title":"ME learning Flask",
    "content":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Incidunt consectetur, mollitia repellat corporis eveniet expedita tempore! Laudantium minima voluptatem eaque velit dolore reprehenderit, vero alias eius illum sit, blanditiis excepturi.",
    "date":"27 March 2021"
    }
]
@app.route("/")
def home():
    
    return render_template("index.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register",methods=["GET","POST"])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account was successfully created for {form.user_name.data}","success")
        return redirect("/")

    return render_template("register.html",form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    form=loginForm()
    form=RegistrationForm()
    if form.validate_on_submit():
        # flash(f"Account was successfully created for {form.user_name.data}","success")
        return redirect("/")
    return render_template("login.html",form=form)




if __name__=="__main__":
    app.run(debug=True)


