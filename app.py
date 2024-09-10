from flask import Flask


app = Flask(__name__)

## create the idea repository , this ideas will be stored
ideas = {
    1:{
        "id":1,
        "idea_name":"Adeeb",
        "idea_decription" : "details about ondc",
        "idea_author":"Adeeb"
    },
    2:{
       "id":1,
        "idea_name":"Save soil",
        "idea_decription" : "details about soil",
        "idea_author":"Save"
     
    }
}

## create an restful endpoint for fetching all the ides

@app.get("/ideaapp/app/v1/ideas")
def get_all_ideas():
    return ideas

if __name__ =="__main__":
    app.run(debug=True,port=5080) 
