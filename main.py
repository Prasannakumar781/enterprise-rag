import uvicorn
 
if __name__ == "__main__":
    uvicorn.run(
        "app.api.server:app",  # ✅ now resolves correctly (server.py created)
        host="0.0.0.0",
        port=8000,
        reload=False
    )
 