import requests
import json


def cleanSchemas():
    # curl  -X GET localhost:8081/subjects/ | jq .
    r = requests.get("http://localhost:8081/subjects")
    j = r.json()
    # data = json.loads(j)
    print(type(j))
    ind = 0
    for sch in j:
        # if ind > 0:
        #     return
        # print(f"{ind} -> {sch}")
        ind = ind + 1
        # url  -X DELETE localhost:8081/subjects/chicaga.transit.authority.*/versions/latest | jq .
        resp = requests.delete(f"http://localhost:8081/subjects/{sch}")
        try:
            resp.raise_for_status()
            print(f"Deleted topic: {ind} -> {sch}")
        except:
            print("Failed to delete topics {json.dumps(resp.json(), indent=2)})")


if __name__ == "__main__":
    cleanSchemas()
