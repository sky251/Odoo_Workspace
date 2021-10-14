# if use https get error SSLError: [SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:1131)
url = "http://127.0.0.1:9993"
db = "partner_db"
username = "admin"
password = "admin"

import csv  # Imported to read csv files
import os
import xmlrpc.client  # import to user xmlrpc API
from datetime import datetime

common = xmlrpc.client.ServerProxy("%s/xmlrpc/2/common" % url)  # for authentication
version = common.version()  # to check if connection is correct before authentication
uid = common.authenticate(
    db, username, password, {}
)  # Used as parameter while calling methods
models = xmlrpc.client.ServerProxy(
    "{}/xmlrpc/2/object".format(url)
)  # Used as parameter while calling method

start_time = datetime.now()

with open("res.partner.csv", newline="") as csv_file:
    csv_file = csv.DictReader(csv_file)
    excel_row = 2
    partner_count = models.execute_kw(
        db, uid, password, "res.partner", "search_count", [[]]
    )
    print("partner_count:::::::>>", partner_count)

    for row in csv_file:
        rec = dict(row)
        print("Rec -------------------", rec)
        print("\n Excel Row>>>>>>>>", excel_row)

        if excel_row >= 2:
            partner_id = models.execute_kw(
                db,
                uid,
                password,
                "res.partner",
                "search",
                [[["email", "=", rec["email"].strip()]]],
            )

            vals = {
                "name": rec["name"].strip(),
                "phone": rec["phone"].strip(),
                "email": rec["email"].strip(),
                "city": rec["city"].strip(),
            }
            if not partner_id:
                partner_id = models.execute_kw(
                    db, uid, password, "res.partner", "create", [vals]
                )
            else:
                partner_id = models.execute_kw(
                    db, uid, password, "res.partner", "write", [[partner_id[0]], vals]
                )

            print("\n\n\n\npartner_detail-------------")
        excel_row += 1

print(":::::::::::::start::::::::::", start_time)
print("::::::End Time:::::::::", datetime.now())
