from app.schemas.base import ApiModel, TimestampedRead


class BlockchainAnchorRequest(ApiModel):
    organization_id: str
    batch_id: str
    payload_hash: str
    metadata_uri: str | None = None


class BlockchainTransactionRead(TimestampedRead):
    organization_id: str
    batch_id: str
    network: str
    contract_address: str | None
    transaction_hash: str | None
    block_number: int | None
    payload_hash: str
    status: str
