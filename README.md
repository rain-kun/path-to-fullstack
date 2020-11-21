# path-to-fullstack
Want to be a fullstack webdeveloper? here,have a way to do so!



#     GIT
```sh
git clone
git add <file name>
git commit -a -m "message"
git status
git push
```
##	merge conflicts
```sh
git log
git reset --hard <commit>
git reset --hard origin/master
//branch
git branch <branch name>
git branch
git checkout <branch name> -b(for new)
	merging the subbreanches
	git merge <branch name>
git push --set-upstream origin feature
```
##	remotes
```
git fetch
git merge
```

#     HTML 5
audio
video
dataset
specificity:
	inline>id>class>type

#  		CSS
```css
: //means properties
a, b //multiple elements selector
a b //descendant selector
a > b //child selector
a + b //adjacent sibling selector
[a=b] // attribut selector
a:b //pseudoclass selector
a:: b // pseudoelement selector
a{[href=""]//atribute selector
}
```

##	properties
```css
before
after
display: flex;
flex-wrap : wrap;

@media
```
##	animation
```css
@keyframes <name of the animation>{
	//you can use two ways
	//1
	from{}
	to{}
	//2
	0%{}
	50%{}
	100%{}
}
h1{
animation-name: <name of the animation>;
animation-duration: 2s;
animation-fill-mode: forwards;
animation-itiration-count:infinite;
}
```

# SASS
```
sass <file>.scss: <file>.css
sass --watch <file>.scss: <file>.css
```
# FLASK
```py
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

flights=db.execute(<query>)//INSERT querry
db.commit()
```
##with sqlalchemy
```
db.createa_all()
flight = FLIGHT(variables)//rather than querry
db.session.add(flight)
db.session.commmit()
```
##	python(ORM)object relation mapping
```py
flight = Flight(origin="",destination="". duration=)
db.session.add(flight)

Flight.querry.all()//SELECT * FROM fligh;
Flight.querry.filter_By(origin="paris"")all()
Flight.querry.filter_By(origin="paris"").first()
//update work as a variable
db.session.delete()
.orderby(light.origin()) or .orderby(light.origin.dscn())
.filter("expression")
.like(%a%)
.in_()
.filter(and_()) and .filter(or_())
 or
//
```
#     API's
##	using json javascript object notation
	http method
- GET
- POST
- PUT
- PATCH
- DELETE
##	api's status code
- 200 //ok
- 201//Created
- 301//moved permanently
- 400//bad request
- 403//forbidden -> CSRF: Cross site request forgery
- 404//notfound
- 405//method not allowed
- 422//unprogresable Etenty
- 500//internal server error

# 		JavaScript

##	some events:
```js
onclick
onmouseover
onkeydown
onkeyup
onload
onchange
onblur
for button:
.disable = true

setInterval()

document.createElement('li')

querySelector:
document.querySelector('tag')
document.querySelector('#id')
document.querySelector('.class')

document.querySelectorAll()
document.createElement('put in the tag ex li')
addEventListener:
document.addEventListener('DOMContentLoaded',function(){});

to plugin a variable
${variable}
template string: `string${variable}`

styling with javaScript
arrow function
() =>{
	alert(x);
}

x => x*2

THIS: this - recieve the value from the event
javaScript local storage logic:

.forEach


javascript local storage:
localStorage.getItem('counter')
localStorage.setItem('counter',0)
```
#	window property
window.innerHeight, window.innerLength, window.scrollY, window.
```js
window.onscrool = ()=>{
if( window.innerHeight + window.scrollY >= document.body.offsetHeight){
	load();
}
}
```

# 		React, ReactDOM, Babel,jsx

##src:
```js
<script type="text/babel"></script>
```
##define:
```js
<body>

<script>
another component hello
	<h1> Hello, {this.props.name}</h1>


class <app name> extends React.Component{
	render(){
		return(
		<div>
		<hello name="rain" />
		<hello name="vishu" />
		<hello name="cat" />
		</div>
		);
	}

}

ReactDom.render(<app name/>, document.querySelector('#app'));
</script>
```
##	a more complex example in the projects
#		AJAX
##	for asrinconous request
```js
fetch('url')
.then(response=>{return response.json()})
.then(data=>{
console.log(data);
});
.catch(error=>
{do something};
);
```
#      Socket.IO

#       Django
```py
//to use the name for url
{% url 'add' %}
CSRF token: {% csrf_takon%}
```
##		adding a django form:
```py
form django import forms
>class NewTaskForm(forms.Form):
>>task = forms.CharField(label = "new task")
adding a variable form in function
in html add a variable {{form}}

sessions
checking session request.session ==
making a variable task = request.session["tasks"]
```

#     SQL(post and mysql)

##sql types:
- TEXT
- NUMERIC
- INTEGER
- REAL
- BLOB
##sam:
- .modes, .heades
##fun:
- AVERAGE COUNT MIN MAX SUM
##clause:
- LIMIT
- ORDER BY
- GROUP BY
- HAVING
##mysql Types:
- CHAR(size)
- VARCHAR(size)
- SMALLINT
- INT
- BRGINT
- FLOAT
- DOUBLE

##constraints-
-CHECK
-UNIQUE
-PRIMARY KEY
-NOT NULL


##  django sql
```py
models.objects.all()
models.objects.filters().filters()
```

##  	Testing

##	assert //ignore the correct line and give error if there is any
```py
assert square(10) = 100
```
##	unittest //testing the values
```py
ex: import unittest
class Tests(unittest.TestCase):
	def test_28(self):
		self.assertFalse(is_prime(28))
if __name__ == "__main__":
unittest.main()
```
##unittest methods

- assertTrue()
- assertFalse()
- assertEqual()
- assertNotEqual()
- assertIn()
- assertNotIn()

##  selenium
```py
from tests import *
uri = file_uri("conter.html")
driver.get(uri)
```
##cmd
```
python3 manage.py test
```

##		CI/CD(git hub actions(YAML))//use inside .github

		 **continuous Integration 
			frequent merges to main branch
			automated unit testing
		continous Delivery
			short release schedules**

##	yaml(ylm)//a language to virtualy make a application
```
	ci.yml
	
	name: Testing
	on: push
	
	jobs:
		test_project:
			runs-on: ubuntu-latest
			steps:
			- uses: actons/checkout@v2
			- name: Run Django unit tests
				run:
					pip3 install --user django //or other requirements
					python3 manage.py test
```
#   Docker //a container

##	cmd
```sh
docker ps// show all dockers

docker exec -it <docid> bash -l//getting inside the docker

logout // get to the main machine
```
#	Dockfile //the main file

docker-compose.yml // a yaml file to compose two dockers

##cmd
```sh
	docker-compose up
```
##	implimentation
	version: '3'
```yml	
	services:
		db: 
			image: postgres
			
		web 
			build: .
			volumes:
				-.:usr/src/app
			ports:
				-"8000:8000"
				
```		
##  	some security
```py
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
 SECURE_HSTS_SECONDS = 15768090   set low, but when site is ready for deployment, set to at least 15768000 (6 months)
 SECURE_HSTS_INCLUDE_SUBDOMAINS = True
 SECURE_HSTS_PRELOAD = True


<!-- The core Firebase JS SDK is always required and must be listed first -->
<script src="/__/firebase/8.0.2/firebase-app.js"></script>

<!-- TODO: Add SDKs for Firebase products that you want to use
     https://firebase.google.com/docs/web/setup#available-libraries -->
<script src="/__/firebase/8.0.2/firebase-analytics.js"></script>

<!-- Initialize Firebase -->
<script src="/__/firebase/init.js"></script>
```
