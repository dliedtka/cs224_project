import json

obj = json.load(open("../../../starter_code/squad/data/train-v2.0.json", "r"))

new_obj = {}
new_obj["version"] = obj["version"]
new_obj["data"] = []

data_obj = {}
data_obj["title"] = obj["data"][199]["title"]
data_obj["paragraphs"] = []

paragraph_obj = {}
paragraph_obj["context"] = obj["data"][199]["paragraphs"][11]["context"]
paragraph_obj["qas"] = []

paragraph_obj["qas"].append(obj["data"][199]["paragraphs"][11]["qas"][0])
paragraph_obj["qas"].append(obj["data"][199]["paragraphs"][11]["qas"][-1])

data_obj["paragraphs"].append(paragraph_obj)

new_obj["data"].append(data_obj)




data_obj = {}
data_obj["title"] = obj["data"][24]["title"]
data_obj["paragraphs"] = []

paragraph_obj = {}
paragraph_obj["context"] = obj["data"][24]["paragraphs"][11]["context"]
paragraph_obj["qas"] = []

paragraph_obj["qas"].append(obj["data"][24]["paragraphs"][11]["qas"][0])

data_obj["paragraphs"].append(paragraph_obj)

new_obj["data"].append(data_obj)



with open("overfit_v2.0.json", "w") as outfile:
    json.dump(new_obj, outfile)
