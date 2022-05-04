import os
import json
from googletrans import Translator


def prepare_json():
    filenames = os.listdir("./data")
    alldata = {}
    translator = Translator()

    for filename in filenames:
        loaded_dict = json.load(open(f"data/{filename}", encoding="utf-8"))

        for k, v in loaded_dict.items():
            k = translator.translate(k, dest="tr").text
            v = [
                translator.translate(v_single, dest="tr").text
                for v_single in v
                if v_single != ""
            ]
            alldata[k] = v

            print("All data len:", len(alldata)),

    json_object = json.dumps(alldata, indent=4).encode("utf-8")

    with open("all_data.json", "w") as outfile:
        outfile.write(json_object)
