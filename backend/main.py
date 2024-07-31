from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schema_classes import *
from service.embed_token_generator import get_embed_token

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/embed-info', response_model= EmbeddingInfo)
def get_embed_info():
    try:
        embed_token, embed_url, report_id = get_embed_token()
        return EmbeddingInfo(embedToken= embed_token, embedUrl= embed_url, reportID= report_id)
    except Exception as e:
        raise HTTPException(status_code= 500, detail= str(e))
    
if __name__ =='__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port= 3005)

