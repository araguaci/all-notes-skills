#! /usr/bin/env python3

import sys

import lm_auth
from ldap3 import SUBTREE


def main():
    for ou, origin in lm_auth.ad_ou_tree.items():
        user_list = get_information(origin[0], origin[1])
        path_to_file = ou + '.html'
        create_html_file(user_list, path_to_file)


def get_information(origin, group_name):

    if group_name == "***REMOVED***":
        conn = lm_auth.active_derectory_connector_***REMOVED***()
        conn.search('dc=***REMOVED***,dc=***REMOVED***,dc=ru',
                    '(&(objectCategory=person)(displayName=*)(givenName=*)(sn=*)(|(ipPhone= *)(mobile=*)(mail=*)('
                    'title=*)(department=*)(physicalDeliveryOfficeName=*)(company=*))(!('
                    'userAccountControl:1.2.840.113556.1.4.803:=2)))',
                    SUBTREE,
                    attributes=['company', 'department', 'ipPhone', 'mobile', 'mail', 'mobile', 'title',
                            'physicalDeliveryOfficeName',
                            'displayName'])

    else:
        conn = lm_auth.active_derectory_connector()
        conn.search(origin,
                    '(&(objectCategory=person)(displayName=*)(givenName=*)(sn=*)(|(ipPhone= *)(mobile=*)(mail=*)('
                    'title=*)(department=*)(physicalDeliveryOfficeName=*)(company=*))(!('
                    'userAccountControl:1.2.840.113556.1.4.803:=2)))',
                    SUBTREE,
                    attributes=['company', 'department', 'ipPhone', 'mobile', 'mail', 'mobile', 'title',
                            'physicalDeliveryOfficeName',
                            'displayName'])

    user_list = {}

    for entry in conn.entries:
        user_list[str(entry.displayName)] = [str(entry.ipPhone).replace('-', ''), entry.mobile, entry.mail, entry.title, entry.department,
                                             entry.physicalDeliveryOfficeName, entry.company]

    conn.unbind()

    return user_list


def create_html_file(user_info, file_name):
    line = ''
    line += html_structure_file('head', file_name)

    for name, user_items in sorted(user_info.items()):
        line += '''                <tr>
                    <th>{}</th>\n'''.format(name)
        for field in user_items:
            if not field or field == '[]':
                line += '                    <th></th>\n'
                continue
            line += '                    <th>{}</th>\n'.format(field)
        line += '                </tr>\n'

    line += html_structure_file('bottom', file_name)

    with open(file_name, 'w') as index_file:
        index_file.write(line)


def html_structure_file(position, file_name):
    _web_header = '''<!DOCTYPE html>
    <html lang="ru">
    <head>
        <title>Справочник</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
        <link rel="stylesheet" href="Bootstrap-4-4.1.1/css/bootstrap.css">
        <link rel="stylesheet" href="DataTables-1.10.18/css/dataTables.bootstrap4.min.css">
        <script type="text/javascript" src="jQuery-3.3.1/jquery-3.3.1.min.js"></script>
        <script type="text/javascript" src="DataTables-1.10.18/js/jquery.dataTables.min.js"></script>
        <script type="text/javascript" src="DataTables-1.10.18/js/dataTables.bootstrap4.min.js"></script>
    </head>
    <body>
        <table id="table_cu" class="table table-striped table-bordered" style="width:100%">
            <thead>
                <tr>
                    <th>ФИО</th>
                    <th>Внутренний номер</th>
                    <th>Рабочий номер</th>
                    <th>E-mail</th>
                    <th>Должность</th>
                    <th>Отдел</th>
                    <th>Кабинет</th>
                    <th>Расположение</th>
                </tr>
            </thead>
            <tbody>\n'''
    _web_bottom = '''       </tbody>
        </table>
    <script>
        $(document).ready(function() {
            $('#table_cu').DataTable( {
            scrollY:        '70vh',
            scrollCollapse: true,
            paging:         false
            } );
        } );
    </script>
    <p><a href="mailto:itinfo@***REMOVED***?subject=Вопрос по web-адресной книге">Нашли ошибку?</a></p>
    </body>
    </html>'''

    if position == 'head':
        return _web_header
    elif position == 'bottom':
        return _web_bottom


if __name__ == "__main__":
    sys.exit(main())
