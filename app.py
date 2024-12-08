# 127.0.0.1:5000/get_form?f_name1=value1&f_name2=value2
from tinydb import TinyDB, Query
from flask import Flask, render_template, request
import datetime
import re


def validate_date(date):
    format_1 = "%d.%m.%Y"
    format_2 = "%Y-%m-%d"
    res = False

    try:
        res = bool(datetime.datetime.strptime(date, format_1))
        return res
    except Exception:
        pass
    try:
        res = bool(datetime.datetime.strptime(date, format_2))
        return res
    except Exception:
        pass


def validate_phone(phone):
    format = r"\+7 \d{3} \d{3} \d{2} \d{2}"

    if len(phone) == 16 and re.match(format, phone):
        return True
    else:
        return False


def validate_email(email):
    format = r"^\S+@\S+\.\S+$"

    if re.match(format, email):
        return True
    else:
        return False


db = TinyDB('db.json')
app = Flask(__name__)


@app.route("/post", methods=["POST"])
def handle_post():
    if request.method == 'POST':
        # check if any values were passed
        if len(request.form) > 0:
            # validation for request values
            request_fields = dict()

            for key, value in request.form.items():
                if validate_date(value):
                    request_fields[key] = "date"
                elif validate_phone(value):
                    request_fields[key] = "phone"
                elif validate_email(value):
                    request_fields[key] = "email"
                else:
                    request_fields[key] = "text"

            templates = []

            # loop through all field names from get request
            for key, value in request_fields.items():
                # find all templates that match at least one pair
                results = db.search(Query()[key] == value)
                # save templates without duplicates
                templates += [res for res in results if res not in templates]
                # sort templates so the first matching template would have
                # more fields -> suits formm fields better
                templates.sort(key=len, reverse=True)

            # if any templates found
            if len(templates) > 0:
                # loop through all of them
                for i in range(len(templates)):
                    t = templates[i]
                    # check every field from current template
                    for key in t.keys():
                        # exclude template's name
                        if key != "name":
                            # if current field wasn't received in GET request
                            if key not in request_fields.keys():
                                # skip current template
                                break
                            else:
                                # if pair (field -> value) from template doesn't
                                # match the pair from request
                                if t[key] != request_fields[key]:
                                    # skip current template
                                    break
                    # if loop ended without breaks it means that current
                    # template matches the request
                    else:
                        # return render_template(t["name"])
                        return t["name"]
                # if no template that matches the request was found
                else:
                    return request_fields
            # if no template that matches the request was found
            else:
                return request_fields


if __name__ == "__main__":
    app.run()
