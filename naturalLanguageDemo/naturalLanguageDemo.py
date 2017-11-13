import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as Features

natural_language_understanding = NaturalLanguageUnderstandingV1(
    username = "1a6f78be-7029-449f-80bd-2eac012779ff",
    password = "zTbvMxO2ndiX",
    version = "2017-02-27")

with open("archivo.txt", "r") as archivo:
    texto = archivo.read().replace("\n", ' ')

response = natural_language_understanding.analyze(
    text = texto,
    features = [
        Features.Entities(
            emotion = True,
            sentiment = True,
            limit = 2
        ),
        Features.Keywords(
            emotion = True,
            sentiment = True,
            limit = 2
        ),
        Features.Concepts(
            limit = 3
        )
    ]
)

archivo.close()
print(json.dumps(response, indent = 2))

responseURL = natural_language_understanding.analyze(
    url = "www.tecmilenio.mx",
    features = [
        Features.Categories()
    ]
)

# print(json.dumps(responseURL, indent=2))
