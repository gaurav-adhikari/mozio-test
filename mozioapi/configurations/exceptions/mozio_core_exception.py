
from rest_framework.exceptions import APIException
from mozioapi.configurations.utilities.http_codes import BAD_REQUEST
from ..utilities.api_response import MozioResponse


class MozioError(APIException):
    """Define the Api response error constants here.
    We should never alter the value of these constants
    from outside the scope of this class.
    """

    status_code = BAD_REQUEST
    message = "A server error has occurred."
    data = []
    success = False
    code = "00"

    def __init__(
        self,
        http_status=None,
        message=None,
        data=None,
        code=None,
    ):
        http_status = (
            MozioError.status_code if (http_status is None) else http_status
        )

        code = MozioError.code if code is None else code

        success = False
        message = MozioError.message if message is None else message
        data = MozioError.data if data is None else data

        super(MozioError, self).__init__(
            detail=MozioResponse(
                http_status=http_status,
                message=message,
                data=data,
                success=success,
                code=code,
            ).format_response(),
            code=http_status,
        )
