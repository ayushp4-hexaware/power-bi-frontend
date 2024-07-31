from pydantic import BaseModel

class EmbeddingInfo(BaseModel):
    embedToken: str
    embedUrl: str
    reportID: str

