
import json
import requests
import os
from bottle import request, get, post, run, debug, route, template, error, TEMPLATE_PATH, default_app, static_file

@route('/name/<name>')
def nameindex(name='Stranger'):
    return '<strong>Hello, %s!</strong>' % name

@route('/')
def buscar():
	return template('index')
@route('/bbva')
def bbva():
	return template('bbva')

@route('/bbva/clasificacion')
def clasificacion1():
		doc={'key':'d39d0f99f77d0db10f87e93a7dc1f958','league':'1','req':'tables','format':'json'}
		r = requests.get("http://www.resultados-futbol.com/scripts/api/api.php", params=doc)
		datos = json.loads(r.text)
		return template('clasificacion',datos=datos)
def clasificacion1():
		doc={'key':'d39d0f99f77d0db10f87e93a7dc1f958','league':'2','req':'tables','format':'json'}
		r = requests.get("http://www.resultados-futbol.com/scripts/api/api.php", params=doc)
		datos = json.loads(r.text)
		return template('clasificacion',datos=datos)
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()

