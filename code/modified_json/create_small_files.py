import json

train_obj = json.load(open("train-v2.0.json", "r"))
dev_obj = json.load(open("dev-v2.0.json", "r"))

import random
random.seed(421)


'''
# count set questions
obj = dev_obj
counter = 0
for data in obj["data"]: # 16 of these in dev, 16 different articles?
        
    for paragraph in data["paragraphs"]: # paragraphs per article?

        for questions in paragraph["qas"]: # questions per paragraph

            counter += 1

print (counter)
'''


# ~100 training
new_train_obj = {}
new_train_obj["version"] = train_obj["version"]
new_train_obj["data"] = []

# pick 18 articles out of 442
for article in random.sample(range(len(train_obj["data"])), 18):
    data = train_obj["data"][article]

    data_obj = {}
    data_obj["title"] = data["title"]
    data_obj["paragraphs"] = []

    # take 3 random paragraphs
    for paragraph_idx in random.sample(range(len(data["paragraphs"])), 3):
        paragraph = data["paragraphs"][paragraph_idx]
        
        paragraph_obj = {}
        paragraph_obj["context"] = paragraph["context"]
        paragraph_obj["qas"] = []

        # take 2 random questions
        for question_idx in random.sample(range(len(paragraph["qas"])), 2):
            question = paragraph["qas"][question_idx]

            question_obj = question

            paragraph_obj["qas"].append(question_obj)
    
        data_obj["paragraphs"].append(paragraph_obj)

    new_train_obj["data"].append(data_obj)



# ~10 dev
new_dev_obj = {}
new_dev_obj["version"] = dev_obj["version"]
new_dev_obj["data"] = []

# pick 2 articles out of 16
for article in random.sample(range(len(dev_obj["data"])), 2):
    data = dev_obj["data"][article]

    data_obj = {}
    data_obj["title"] = data["title"]
    data_obj["paragraphs"] = []

    # take 3 random paragraphs
    for paragraph_idx in random.sample(range(len(data["paragraphs"])), 3):
        paragraph = data["paragraphs"][paragraph_idx]
        
        paragraph_obj = {}
        paragraph_obj["context"] = paragraph["context"]
        paragraph_obj["qas"] = []

        # take 2 random questions
        for question_idx in random.sample(range(len(paragraph["qas"])), 2):
            question = paragraph["qas"][question_idx]

            question_obj = question

            paragraph_obj["qas"].append(question_obj)
    
        data_obj["paragraphs"].append(paragraph_obj)

    new_dev_obj["data"].append(data_obj)


with open("train-v2.0_small.json", "w") as outfile:
    json.dump(new_train_obj, outfile)

with open("dev-v2.0_small.json", "w") as outfile:
    json.dump(new_dev_obj, outfile)
