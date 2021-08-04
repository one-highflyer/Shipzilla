import csv
import pickle

# export_zones_dict = {}
# path = "./UPS_Export_Zones.csv"
# with open(path, "r") as f:
#     export_zones = csv.reader(f, delimiter=',')
#     for row in export_zones:
#         if row[0] != "" and row[1] != "":
#             export_zones_dict[row[0]] = row[1]
    
# with open("./pickle_files/export_zones_dict.pickle", "wb") as f:
#     pickle.dump(export_zones_dict, f, protocol=pickle.HIGHEST_PROTOCOL)


# ups_documents_fee_dict = {}
# path = "./UPS_Documents.csv"
# with open(path, "r") as f:
#     ups_documents_fees = csv.reader(f, delimiter=',')
#     for row in ups_documents_fees:
#         ups_documents_fee_dict[row[0]] = []
#         for fee in row[1:]:
#             ups_documents_fee_dict[row[0]].append(fee)

# with open("./pickle_files/ups_documents_fee_dict.pickle", "wb") as f:
#     pickle.dump(ups_documents_fee_dict, f, protocol=pickle.HIGHEST_PROTOCOL)


# ups_packages_fee_dict = {}
# path = "./UPS_Package.csv"
# with open(path, "r") as f:
#     ups_packages_fees = csv.reader(f, delimiter=',')
#     for row in ups_packages_fees:
#         ups_packages_fee_dict[row[0]] = []
#         for fee in row[1:]:
#             ups_packages_fee_dict[row[0]].append(fee)

# with open("./pickle_files/ups_packages_fee_dict.pickle", "wb") as f:
#     pickle.dump(ups_packages_fee_dict, f, protocol=pickle.HIGHEST_PROTOCOL)
