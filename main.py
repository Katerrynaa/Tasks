from src.config import read_config
import uvicorn
from src.views import app

if __name__ == '__main__':
    config = read_config()
    uvicorn.run("main:app", port=5000, log_level="info")
