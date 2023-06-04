def success_response(message):
    return {"status": "SUCCESS", "message": message}


def error_response(message):
    return {"status": "ERROR", "message": message}
