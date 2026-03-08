# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# import boto3
# import uuid

# app = FastAPI()

# # Enable CORS so React can talk to this API
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"], 
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # ⚠️ YAHAN APNI DETAILS DAAL ⚠️
# REGION = 'ap-southeast-2' # Apna region check kar lena
# AGENT_ID = 'DNPCA8NOEM' 
# AGENT_ALIAS_ID = 'DRK7ZNS3KF' # e.g., 'TSTALIASID' ya 'v1'

# # Initialize Bedrock Client
# client = boto3.client('bedrock-agent-runtime', region_name=REGION)

# @app.get("/api/consult")
# async def consult_agent(patient_id: str, drug: str, reason: str):
#     prompt = f"Patient {patient_id} has {reason}. Can I prescribe {drug}?"
#     session_id = str(uuid.uuid4()) # Unique session for every request
    
#     try:
#         response = client.invoke_agent(
#             agentId=AGENT_ID,
#             agentAliasId=AGENT_ALIAS_ID,
#             sessionId=session_id,
#             inputText=prompt,
#         )
        
#         full_response = ""
#         for event in response.get('completion'):
#             if 'chunk' in event:
#                 full_response += event['chunk']['bytes'].decode('utf-8')
                
#         return {"status": "success", "verdict": full_response}
        
#     except Exception as e:
#         print(f"AWS Error: {e}")
#         raise HTTPException(status_code=500, detail=str(e))


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import boto3
import uuid

app = FastAPI()

# Enable CORS so React can talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ⚠️ EXACT DETAILS ⚠️
REGION = 'ap-southeast-2' 
AGENT_ID = '3FPI35FCWF' 
AGENT_ALIAS_ID = 'TSTALIASID' # 👈 Isko strict TSTALIASID rakh!

# Initialize Bedrock Client
client = boto3.client('bedrock-agent-runtime', region_name=REGION)

@app.get("/api/consult")
async def consult_agent(patient_id: str, drug: str, reason: str):
    prompt = f"Patient {patient_id} has {reason}. Can I prescribe {drug}?"
    session_id = str(uuid.uuid4()) # Unique session for every request
    
    try:
        response = client.invoke_agent(
            agentId=AGENT_ID,
            agentAliasId=AGENT_ALIAS_ID,
            sessionId=session_id,
            inputText=prompt,
        )
        
        full_response = ""
        for event in response.get('completion'):
            if 'chunk' in event:
                full_response += event['chunk']['bytes'].decode('utf-8')
                
        return {"status": "success", "verdict": full_response}
        
    except Exception as e:
        # 🛑 MAGIC: Crash hone ke bajaye, hum seedha AWS ka exact error UI pe bhejenge!
        print(f"AWS Error: {str(e)}")
        return {"status": "error", "verdict": f"🛑 AWS ERROR: {str(e)}"}