from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://Destiqzu:KBSD1HXmW3pEO4rf@destiqzu.3ox00xu.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
db = client['smkn3kuningan'] # ganti sesuai dengan nama database kalian
my_collections = db['user'] # ganti sesuai dengan nama collections kalian

def cek_id(id_data):
	try:
		rfid_id=my_collections.find({"id_read":id_data})
		for data_id in rfid_id:
			print(data_id)
		return data_id,True
	except:
		print(id_data)
		return id_data,False
