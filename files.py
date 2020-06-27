import json
import wget

with open('forest_fire.json') as data_file:
    for line in data_file:
        data = json.loads(line)
        if data['annotation']['labels'][0] == "+Fire+Smoke":
            local_image_filename = wget.download(data['content'], 'data/dattusk/+Fire+Smoke')
        elif data['annotation']['labels'][0] == "-Fire-Smoke":
            local_image_filename = wget.download(data['content'], 'data/dattusk/-Fire-Smoke')
        elif data['annotation']['labels'][0] == "+Fire-Smoke":
            local_image_filename = wget.download(data['content'], 'data/dattusk/+Fire-Smoke')
        elif data['annotation']['labels'][0] == "-Fire+Smoke":
            local_image_filename = wget.download(data['content'], 'data/dattusk/-Fire+Smoke')
        elif data['annotation']['labels'][0] == "garbage":
            local_image_filename = wget.download(data['content'], 'data/dattusk/garbage')
        