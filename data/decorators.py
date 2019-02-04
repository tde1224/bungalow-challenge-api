from rest_framework.response import Response
from rest_framework.views import status

def validate_request_data(fn):
    def decorated(*args, **kwargs):
        address = args[0].request.data.get("address", "")
        city = args[0].request.data.get("city", "")
        state = args[0].request.data.get("state", "")
        zipcode = args[0].request.data.get("zipcode", "")
        if not address or not city or not state or not zipcode:
            return Response(
                data={
                    "message": "Address, city, state, and zipcode are all required to add a record"
                },
                status = status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated