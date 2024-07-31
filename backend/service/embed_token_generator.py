import msal
import requests
from fastapi import HTTPException
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
TENANT_ID = os.getenv('TENANT_ID')
WORKSPACE_ID = os.getenv('WORKSPACE_ID')
REPORT_ID = os.getenv('REPORT_ID')
DATASET_ID = os.getenv('DATASET_ID')

def get_embed_token():
    authority = f"https://login.microsoftonline.com/{TENANT_ID}"
    app = msal.ConfidentialClientApplication(
        CLIENT_ID, authority=authority, client_credential=CLIENT_SECRET
    )
    token_response = app.acquire_token_for_client(scopes=["https://analysis.windows.net/powerbi/api/.default"])
    access_token = token_response.get('access_token')

    if not access_token:
        raise HTTPException(status_code=500, detail="Failed to acquire access token")

    embed_token_url = f"https://api.powerbi.com/v1.0/myorg/groups/{WORKSPACE_ID}/reports/{REPORT_ID}/GenerateToken"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        "datasets": [{"id": DATASET_ID}],
        "reports": [{"id": REPORT_ID}],
        "targetWorkspaces": [{"id": WORKSPACE_ID}]
    }
    response = requests.post(embed_token_url, headers=headers, json=data)
    response_data = response.json()

    embed_token = response_data.get('token')
    if not embed_token:
        raise HTTPException(status_code=500, detail="Failed to generate embed token")

    embed_url = f"https://app.powerbi.com/reportEmbed?reportId={REPORT_ID}"
    return embed_token, embed_url, REPORT_ID
