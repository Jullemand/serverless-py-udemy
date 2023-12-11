import time, json

def query_data(bq_client, q):
    print("Query:", q)
    try:
        query_result = bq_client.query(q).result()  # API request
        records = [dict(row) for row in query_result]
        json_obj = json.dumps(str(records))
        print(json_obj)
        return json_obj, 0
    except Exception as e:
        print(e)
        return None, 1

def insert_data(bq_client, q):
    print("Insert Query:", q)
    try:
        bq_client.query(q)
        time.sleep(0.5)
        return 0
    except Exception as e:
        print(e)
        return 1


