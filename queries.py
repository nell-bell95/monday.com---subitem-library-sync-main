create_subitems = '''
    mutation (
        $myItemName: String!, 
        $columnVals: JSON!
        $itemId: ID!) { 
            create_subitem (
                parent_item_id:$itemId,
                item_name:$myItemName, 
                column_values:$columnVals,
                create_labels_if_missing: true) { 
                    id 
                    } 
                }
'''

fetch_subitems = '''query ($itemName: CompareValue!, $boardId: [ID!]) {
  boards(ids: $boardId) {
    items_page(query_params: {rules: {column_id: "name", compare_value: $itemName}}) {
      items {
        id
        name
        subitems {
            id
            name
            column_values {
                id
                text
                value
                type
        }
      }
    }
  }
}
}
'''