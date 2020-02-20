from flask import Flask, render_template,request,redirect,url_for


app = Flask(__name__)

# # Use the application default credentials
# app.config['SECRET_KEY'] = 'supersecretkeygoeshere'

# UPLOAD_FOLDER = 'static/images/children'
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Use a service account
# cred = credentials.Certificate('static/fields-of-hope-3b250-firebase-adminsdk-worse-24b070b472.json')
# firebase_admin.initialize_app(cred)

# db = firestore.client()


@app.route("/")
def index():

	# children = []

	# docs = db.collection(u'children').stream()

	# for doc in docs:
	# 	children.append(doc.to_dict())


	return render_template("index.html", title="Homepage")
	

@app.route("/education")
def education():
	return render_template("what we do/education.html", title="Education")

# @app.route("/children")
# def children():
# 	children = []

# 	docs = db.collection(u'children').stream()

# 	for doc in docs:
# 		children.append(doc.to_dict())

# 	return render_template("children.html", title="Children", children=children)


# @app.route("/index_admin")
# def index_admin():
# 	return render_template("index_admin.html", title="Admin")

# @app.route("/children_admin")
# def children_admin():

# 	children = []

# 	docs = db.collection(u'children').stream()

# 	for doc in docs:
# 		children.append(doc.to_dict())
# 		# children.append(temp_storage)
# 	    # print(u'{} => {}'.format(doc.id, doc.to_dict()))


# 	return render_template("children_admin.html", title="Children",children=children)




# @app.route("/upload_child", methods=["POST"])
# def upload_child():
# 	ChildID = request.form["ChildID"]
# 	Name = request.form["name"]	
# 	Grade = request.form["grade"]	
# 	Start_date = request.form["admission_date"]
# 	Gender = request.form["gender"]
# 	DOB = request.form["D.O.B"]
# 	Country = request.form["Country"]
# 	Hobbies = request.form["hobbies"]
# 	file = request.files["image"]
# 	def allowed_file(filename):
# 		return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

# 	if file and allowed_file(file.filename):
# 		filename = secure_filename(file.filename)
# 		file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

# 	Child = db.collection(u'children').document()

	
# 	Child.set({
# 		u'ChildID' : u'{}'.format(ChildID),
# 		u'Country' : u'{}'.format(Country),
# 		u'DateOfBirth' : u'{}'.format(DOB),
# 		u'Gender' : u'{}'.format(Gender),
# 		u'Grade': u'{}'.format(Grade),
# 		u'Hobbies': u'{}'.format(Hobbies),
# 		u'Image' : u'{}'.format(filename),
# 		u'Name' : u'{}'.format(Name),
# 		u'StartDate' : u'{}'.format(Start_date)	    
# 	})

# 	return redirect(url_for("children_admin"))

