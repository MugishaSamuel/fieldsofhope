<<<<<<< HEAD
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_render_template]

from flask import Flask, render_template
=======
from flask import Flask, render_template,request,redirect,url_for

>>>>>>> 693dafcbaba0df91e839b3fd15e6ab92ed5d942f

app = Flask(__name__)


@app.route('/')
def index():
<<<<<<< HEAD
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.

    return render_template('index.html', title="Homepage")


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [START gae_python37_render_template]
=======

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

>>>>>>> 693dafcbaba0df91e839b3fd15e6ab92ed5d942f
