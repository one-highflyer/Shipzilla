from flask import request, url_for, session, jsonify, make_response, current_app
from flask_api import FlaskAPI, status, exceptions
from flask_cors import CORS
from time import time
import pickle
import os

app = FlaskAPI(__name__)
app.config["SECRET_KEY"] = os.urandom(16)
CORS(app)

dollar_rate_path = "./pickle_files/dollar_rate.pickle"
fuel_surcharge_rate_path = "./pickle_files/fuel_surcharge_rate.pickle"

####################################
####### Preload Pickle Files #######
####################################
with open("./pickle_files/export_zones_dict.pickle", "rb") as f:
    export_zones_dict = pickle.load(f)

with open("./pickle_files/ups_documents_fee_dict.pickle", "rb") as f:
    ups_documents_fee_dict = pickle.load(f)

with open("./pickle_files/ups_packages_fee_dict.pickle", "rb") as f:
    ups_packages_fee_dict = pickle.load(f)


####################################
######### Helper Functions #########
####################################
def calculateWeightRange(rawWeight):
    if rawWeight % 1 == 0:
        return int(rawWeight)

    if rawWeight > 20:
        return int(rawWeight) + 1

    if rawWeight % 1 <= 0.5:
        weight = int(rawWeight) + 0.5
    else:
        weight = int(rawWeight) + 1

    return weight

####################################
############## Routes ##############
####################################


@app.route("/calculateFee", methods=["POST"])
def calculateFee():
    weight = float(request.get_json().get('weight', 0))
    zone = int(request.get_json().get('zone', 0))
    price_by_using_package = 0
    price_by_using_document = 0

    if weight == 0 or zone == 0:
        return {"error_msg": "BAD REQUEST"}, status.HTTP_400_BAD_REQUEST

    weight_range = calculateWeightRange(weight)
    print(f"Weight - {weight}, weight range - {weight_range}")
    if weight <= 5:
        # calculate using document price
        price_by_using_document = ups_documents_fee_dict[str(weight_range)][zone - 1]

    if weight > 70:
        zone_price_per_kg = [11.19, 12.73, 12.99, 15.63, 15.4, 18.43, 21.93]
        price_by_using_package = weight_range * zone_price_per_kg[zone - 1]
    else:
        price_by_using_package = ups_packages_fee_dict[str(weight_range)][zone - 1]

    response = jsonify({
        "price_by_using_document": price_by_using_document,
        "price_by_using_package": price_by_using_package
    })
    print(
        f"price_by_using_document - {price_by_using_document}, price_by_using_package - {price_by_using_package}")
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/", methods=["GET"])
def main():
    return "Hi!"

@app.route("/auth")
def auth():
    if request.authorization and request.authorization.username == "pasan@admin.com" and request.authorization.password == "pasan@admin.com":
        return current_app.send_static_file("admin.html")
        # return "Hi!"
    return make_response("Failed to verify", 401, {"WWW-Authenticate": "Basic realm='Login Required'"})

@app.route("/update_data", methods=["POST"])
def update_data():
    if request.method == "GET":
        return {"error_msg": "BAD REQUEST"}, status.HTTP_400_BAD_REQUEST
    if request.method == "POST":
        dollar_rate = float(request.get_json().get('dollar_rate', 0))
        fuel_surcharge_rate = float(
            request.get_json().get('fuel_surcharge_rate', 0))

        with open(dollar_rate_path, "wb") as f:
            pickle.dump(dollar_rate, f)
        with open(fuel_surcharge_rate_path, "wb") as f:
            pickle.dump(fuel_surcharge_rate, f)

        response = jsonify({
            "msg": "Data Update Succeeded!"
        })
        return response

@app.route("/get_data", methods=["GET"])
def get_export_zones():
    if request.method == "GET":
        # export_zones = list(export_zones_dict.keys())[1:] # remove the first "country"
        export_zones = [(key, value)
                        for key, value in export_zones_dict.items()][1:]

        with open(dollar_rate_path, "rb") as f:
            dollar_rate = pickle.load(f)
        with open(fuel_surcharge_rate_path, "rb") as f:
            fuel_surcharge_rate = pickle.load(f)

        response = jsonify({
            "export_zones": export_zones,
            "dollar_rate": dollar_rate,
            "fuel_surcharge_rate": fuel_surcharge_rate
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    # elif request.method == "POST":
    #     if request.form.get("export_zone_name") != None:
    #         export_zone_name = request.form.get("export_zone_name")
    #         export_zone_number = export_zones_dict[export_zone_name]
    #         response = jsonify({
    #             "export_zone_number": export_zone_number
    #         })
    #         response.headers.add('Access-Control-Allow-Origin', '*')
    #         return response
    return {"error_msg": "BAD REQUEST"}, status.HTTP_400_BAD_REQUEST


if __name__ == "__main__":        # on running python app.py
    # run the flask app
    app.run(debug=True, host="0.0.0.0", port="10000")
