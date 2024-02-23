import json

column_id_to_type_map = {
    'status': 'status',
    'date': 'date0',
    "people": 'person',
    'dropdown': 'dropdown',
    'numbers': 'numbers',
    'timeline': 'timeline',
    'checkbox': 'checkbox',
    'link': 'link',
    'text': 'text',
    'long_text': 'long_text',
    'email': 'email'
}

def parse_email(column):
    email_value = ''
    display_text = ''
    if column['value'] is not None:
        email_data = json.loads(column['value'])
        email_value = email_data.get('email') or ''
        display_text = email_data.get('text') or ''
    return {column_id_to_type_map[column['type']]: {'email': email_value, 'text': display_text}}   

def people_id_handler(column):
    people_ids = {}
    if column['value'] is not None:
        people_data = json.loads(column['value'])
        people_ids = ','.join(str(person['id']) for person in people_data.get('personsAndTeams', []))
    return {column_id_to_type_map[column['type']]: people_ids}
 

def parse_timeline(column):
    from_value = {}
    to_value = {}
    if column['value'] is not None:
        timeline_data = json.loads(column['value'])
        from_value = timeline_data.get('from') or ''
        to_value = timeline_data.get('to') or ''
    return {column_id_to_type_map[column['type']]: {'from': from_value, 'to': to_value}}

def parse_link(column):
    url_value = ''
    link_text = ''
    if column['value'] is not None:
        link_data = json.loads(column['value'])
        url_value = link_data.get('url') or ''
        link_text = link_data.get('text') or ''
    return {column_id_to_type_map[column['type']]: {'url': url_value, 'text': link_text}}

def parse_text(column):
    return {column_id_to_type_map[column['type']]: column.get('text') or ''}

def parse_checkbox(column):
     checked = None
     if column['value'] is not None:
         checkbox_data = json.loads(column['value'])
         if checkbox_data.get('checked') == True:
             checked = 'true'
             return {column_id_to_type_map[column['type']]: {'checked': checked}}
         else:
             checked = None
             return {column_id_to_type_map[column['type']]: checked}

column_handler_map = {
    'people': people_id_handler,
    'status': parse_text,
    'date': parse_text,
    'dropdown': parse_text,
    'numbers': parse_text,
    'timeline': parse_timeline,
    'dropdown': parse_text,
    'text': parse_text,
    'long_text': parse_text,
    'checkbox': parse_checkbox,
    'link': parse_link,
    'email': parse_email
}