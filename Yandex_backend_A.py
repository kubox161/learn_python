import json
#import_json = json.load(input())
import_json = str([
	{
		"event_id": 1,
		"order_id": 1,
		"item_id": 1,
		"count": 1,
		"return_count": 0,
		"status": "OK"
	},
	{
		"event_id": 2,
		"order_id": 1,
		"item_id": 1,
		"count": 1,
		"return_count": 0,
		"status": "CANCEL"
	}
]
)
import_python = json.load(import_json)
print (import_python)