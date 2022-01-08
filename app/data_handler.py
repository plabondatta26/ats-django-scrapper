import html_to_json
import json


def data_formatter(html_data, sender):
    if html_data:
        output_json = html_to_json.convert(html_data)
    result = {"result": "No data found"}
    if sender == "ciranet":
        try:
            result = {
                "Property Address":
                    output_json["div"][0]["div"][0]["div"][0]["div"][0]["table"][0]["tbody"][0]["tr"][0]["td"][1][
                        "_value"],
                "Community":
                    output_json["div"][0]["div"][0]["div"][0]["div"][0]["table"][0]["tbody"][0]["tr"][0]["td"][2][
                        "_value"],
                "Property CSZ":
                    output_json["div"][0]["div"][0]["div"][0]["div"][0]["table"][0]["tbody"][0]["tr"][0]["td"][3][
                        "_value"],
                "Owner": output_json["div"][0]["div"][0]["div"][0]["div"][0]["table"][0]["tbody"][0]["tr"][0]["td"][4][
                    "_value"],
            }
        except:
            pass
        return result

    elif sender == "condocerts":
        try:
            result = {
                "Association": output_json["address"][0]["_value"]
            }
        except:
            pass
        return result

    elif sender == "estoppels":
        try:
            if output_json["div"][0]["div"][0]["table"][0]["tbody"][0]["tr"][0]["td"][1]["h1"][0][
                "_value"] == "We found it!":
                result = {
                    "data": "Property avialibe on estoppels.com please check with property manager before placing the order"
                }
        except:
            pass
        return result

    elif sender == "ff":
        try:
            result = {
                "Community": output_json["div"][1]["div"][0]["div"][1]["div"][0]["div"][0]["address"][0]["_value"],
                "CurrentOwner": output_json["div"][1]["div"][0]["input"][1]["_attributes"]["value"]
            }
        except:
            pass
        return result

    elif sender == 'homewise':
        try:
            result = {
                "searched_address": output_json["div"][0]["span"][0]["_value"],
                "result": {
                    "address_title": output_json["div"][1]["div"][1]["div"][0]["h3"][0]["_value"],
                    "state": output_json["div"][1]["div"][1]["div"][0]["span"][0]["_value"],
                    output_json["div"][1]["div"][1]["h3"][0]["_value"]: output_json["div"][1]["div"][1]["div"][1][
                        "_value"]
                }

            }
        except:
            pass
        return result

    elif sender == "sentry":
        try:
            result = {
                "Community": output_json["div"][1]["div"][0]["div"][1]["div"][0]["div"][0]["address"][0]["_value"],
                "CurrentOwner": output_json["div"][1]["div"][0]["input"][1]["_attributes"]["value"]
            }
        except:
            pass
        return result

    elif sender == "market":
        try:
            result = {
                "Community":
                    output_json["shop-community-shop"][0]["commarchives-page"][0]["nz-layout"][0]["div"][0]["div"][0][
                        "section"][0]["nz-card"][0]["div"][0]["div"][1]["div"][0]["h2"][0]["_value"],
                "area":
                    output_json["shop-community-shop"][0]["commarchives-page"][0]["nz-layout"][0]["div"][0]["div"][0][
                        "section"][0]["nz-card"][0]["div"][0]["div"][1]["div"][0]["p"][0]["_value"]
            }
        except:
            pass
        return result


def location_engineering(location):
    try:
        data = location.split(',')
        street = data[0]
        city = data[1]
        zip_state = data[2].split(' ')
        zip_code = zip_state[2]
        state = zip_state[1]
        location_list = [street, city, zip_code, state]
        return location_list
    except:
        return 'N/A'
