from flask import Flask, render_template
app = Flask(__name__)





@app.route('/')
def index():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


    return render_template("index.html", users = users)




if __name__=="__main__":
    app.run(debug=True)



# users = [
#     {'first_name' : 'Michael', 'last_name' : 'Choi'},
#     {'first_name' : 'John', 'last_name' : 'Supsupin'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]


# for list in users:
#     for key in list:
#         first_table = f"<td>{list[key]}</td>"
#         print(first_table)
#             # first_table = "<tr></tr>"

