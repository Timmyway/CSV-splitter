import json

def read_json(path):
	try:
		with open(path + '.json', encoding='utf-8') as json_data:
			json_to_dic = json.load(json_data)
			#print('Donnée: %s\nType: %s' % (self.dict_data, type(self.dict_data)))
			return json_to_dic
	except FileNotFoundError:
		print('No such file or directory: "%s"' % path)
		return 'file_not_found'

		
def main():	
	tool = ToolBox()
	urls = ['https://tracker.affility.net/complaints/image/zc7cdzxokb481jujgwz0wpw', 'http://impfr.tradedoubler.com',
	'http://collecte.alailomredirection.com/tracking/?type=redirectemail&i=bah0bah0djfi0hbgi0bdihdd0fh']
	# tool.encode_base64('Hello')
	print(tool.is_alive('http://www.google.com'))
	

if __name__ == '__main__':
	main()