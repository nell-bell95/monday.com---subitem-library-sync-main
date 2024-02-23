import requests
import json
from . import config
from . import queries
from . import columnhandler

class DataReplicationService:
    @staticmethod
    def replicate_data():
        fetch_vars = {
            "itemName": "Design",
            "boardId": ["1394650157"]
        }

        fetch_subitem_data = {'query': queries.fetch_subitems, 'variables': fetch_vars}
        r = requests.post(url=config.apiUrl, json=fetch_subitem_data, headers=config.headers)  # make request
        stored_response = r.json()

        for data in stored_response['data']['boards']:
            for item in data['items_page']['items']:
                for subitem in item['subitems']:
                    subitem_name = subitem['name']
                    column_values = {}

                    # Iterate over column_values to get people_ids, subitem_status, and subitem_date
                    for column in subitem['column_values']:
                        column_values.update(
                            columnhandler.column_handler_map[column.get('type', '')](column))
                    # Create mutation variables
                    create_subitem_vars = {
                        'myItemName': subitem_name,
                        'itemId': '1394652952',
                        'columnVals': json.dumps(column_values)
                    }

                    # Create mutation query
                    subitem_data = {'query': queries.create_subitems, 'variables': create_subitem_vars}

                    # Make the request to create the subitem
                    create_subitem_request = requests.post(url=config.apiUrl, json=subitem_data, headers=config.headers)

                    # Print the response
                    print(create_subitem_request.json())