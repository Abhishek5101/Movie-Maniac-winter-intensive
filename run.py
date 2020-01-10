from flaskblog import app


if __name__ == "__main__":
	app.run(debug=True)


# cluster = MongoClient("mongodb+srv://abhi:%40AKak5101mongo@cluster0-dd95h.mongodb.net/test?retryWrites=true&w=majority")
# db = cluster["test"]
# collection = db["test"]


