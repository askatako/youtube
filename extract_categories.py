import json
import pickle

def load_json(path):
  """
  Loads the json file in the given path.  

  Precondition:
  path: is a string of a valid json path.
  """
  with open (path) as file:
    return json.load(file)


def save_pickle(path,data):
  """
  Dumps the json file in the given path.  

  Precondition:
  path: is a string of a valid json path.
  """
  # with open (path) as file:
  #   return json.load(file)

  with open(path, 'wb') as outfile:  
    pickle.dump(data, outfile)

def extract_categories(path):

  cats = load_json(path)
  categories = {}

  for item in cats["items"]:
  	
  	video_id = int(item["id"])
  	title = item["snippet"]["title"]
  	categories[video_id] = title

  return categories


def main():
	path = "US_category_id.json"
	data = extract_categories(path)
	outfile = 'US_categories.pickle'
	save_pickle(outfile, data)

if __name__ == '__main__':
	main()