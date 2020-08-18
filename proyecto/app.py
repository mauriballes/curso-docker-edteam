import psycopg2
import os

from flask import Flask


app = Flask(__name__)


def get_conexion():
	info = ''
	user = os.getenv('DB_USER','gmfqxtjr')
	password = os.getenv('DB_PASS','uhAmgqUuk4hVAgMAeRvHovJIa94DeG1x')
	host = os.getenv('DB_HOST','tuffi.db.elephantsql.com')
	port = os.getenv('DB_PORT','5432')
	database = os.getenv('DB_NAME','gmfqxtjr')
	try:
		connection = psycopg2.connect(
			user=user, password=password, 
			host=host, port=port, database=database)
		info = str(connection.get_dsn_parameters())
		connection.close()
	except:
		info = 'ERROR'
	return info


@app.route('/', methods=['GET'])
def index():
	conexion = get_conexion()
	return {
		'mensaje': 'Hola mundo', 
		'conexion': conexion
	}


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)


