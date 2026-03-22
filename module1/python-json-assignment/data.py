import json


def main():
    # Step 1: JSON string (API response)
    json_string = '''
    {
        "id": "req_123",
        "status": "success",
        "result": {
            "text": "Hello world",
            "confidence": 0.98
        }
    }
    '''

    # Step 2: Parse JSON string into Python dictionary
    data = json.loads(json_string)

    # Step 3: Extract required fields
    request_id = data["id"]
    status = data["status"]
    text_result = data["result"]["text"]
    confidence = data["result"]["confidence"]

    # Step 4: Print extracted values
    print("Request ID:", request_id)
    print("Status:", status)
    print("Text:", text_result)
    print("Confidence:", confidence)

    # Step 5: Check confidence threshold
    if confidence < 0.9:
        print("Warning: Low confidence score!")

    # Step 6: Create a new Python dictionary (follow-up result)
    follow_up = {
        "request_id": request_id,
        "processed": True,
        "message": "Response processed successfully",
        "confidence": confidence
    }

    # Step 7: Convert dictionary to JSON string
    json_output = json.dumps(follow_up, indent=4)

    # Step 8: Write JSON to file
    with open("response.json", "w") as file:
        file.write(json_output)

    print("\nJSON output written to response.json")


if __name__ == "__main__":
    main()