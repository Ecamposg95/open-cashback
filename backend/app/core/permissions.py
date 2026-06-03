from fastapi import Header


def get_request_organization_id(x_organization_id: str | None = Header(default=None)) -> str | None:
    return x_organization_id
