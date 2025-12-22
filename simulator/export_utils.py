
import json, csv, io

def export_csv(arr):
    buf = io.StringIO()
    writer = csv.writer(buf)
    for row in arr:
        writer.writerow(row)
    return buf.getvalue()

def export_json(arr):
    return json.dumps(arr.tolist(), indent=2)
