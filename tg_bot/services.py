import json
from collections import OrderedDict

from django.db import connection


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone()))


def get_kelgan_time(user):
    with connection.cursor() as cursor:
        cursor.execute(f"""
                SELECT kelgan_vaqt FROM tg_bot_kelgantime
                WHERE user = '{user}'
                
                 
                


        """)
        data = dictfetchall(cursor)

    return data


def get_ketgan_time(user):
    with connection.cursor() as cursor:
        cursor.execute(f"""
                SELECT ketgan_vaqt FROM tg_bot_ketgantvaqt
                WHERE user = "{user}"  
                



        """)
        data = dictfetchall(cursor)

    return data