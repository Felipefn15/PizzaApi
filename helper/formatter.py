import datetime
import re
import unicodedata

class Formatter(object):

    @staticmethod
    def format_cursor(cursor):
        resp_list = []
        names_list = [Formatter.camel_case_name(value.name)
                      for value in cursor.description]

        for row in cursor:
            resp_list.append(dict(zip(names_list, row)))

        return Formatter.clear_nulls(resp_list)

    @staticmethod
    def format_salesforce_response(response):
        parse_list = []

        for obj in response:
            new_dict = {}

            for k, v in obj.items():
                new_key = Formatter.camel_case_name(k.replace("__c", ""))
                new_dict[new_key] = obj[k]

            parse_list.append(new_dict)

        return parse_list

    @staticmethod
    def camel_case_name(name):
        return re.sub('_.', lambda x: x.group()[1].upper(), name)

    @staticmethod
    def old_contract_list(object_list):
        return {obj['name']: obj['id'] for obj in object_list}

    @staticmethod
    def clear_nulls(dict_list):
        for obj in dict_list:
            for k, v in obj.items():
                if isinstance(v, str) and v.lower() == "null":
                    obj[k] = None

        return dict_list

    @staticmethod
    def filter_top(data, top, min_cases):

        sort_list = sorted(data, key=lambda k: k["avgAdherence"], reverse=True)

        resp_list = []
        for obj in sort_list:

            if len(resp_list) >= top:
                break

            if obj["d0"] > min_cases:
                resp_list.append(obj)

        return resp_list

    @staticmethod
    def format_time(values):
        for value in values:
            dt = datetime.datetime.strptime(value["date"], "%Y-%m-%d")
            ndt = dt.replace(hour=int(value["hour"]))
            value["hour"] = ndt.isoformat()

        return values
    @staticmethod
    def remove_special_characters(word):

        # Unicode normalize transforma um caracter em seu equivalente em latin.
        nfkd = unicodedata.normalize('NFKD', word)
        word_without_accent = u"".join([c for c in nfkd if not unicodedata.combining(c)])

        # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
        return re.sub('[^a-zA-Z0-9 \\\]', '', word_without_accent)
