"""Helper script"""
import json
import requests

if __name__ == "__main__":
    lines = []
    with open("example_data.jsonl", "r") as fh:
        for line in fh.readlines():
            p_line = json.loads(line)
            lines.append(p_line)
    response = requests.post(
        "https://fastapi-app-0101-yq35nm2v3q-lm.a.run.app/cluster",
        json={"data": lines, "model_conf": {"n_clusters": 4}},
    )
    print(response.json())
