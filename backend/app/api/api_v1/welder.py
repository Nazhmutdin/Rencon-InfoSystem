from fastapi import APIRouter, Request, Response


router = APIRouter()


@router.get("/get_welder")
def get_welder_request(request: Request) -> Response:
    return Response(
        "hello_world!"
    )