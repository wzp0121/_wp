from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from es_client import es, create_index
import uvicorn

# 創建 FastAPI 應用
app = FastAPI(title="產品搜索 API")

# 初始化 Elasticsearch 索引
create_index()

# 掛載靜態文件夾
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    """重定向到主頁"""
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/static/index.html")

@app.get("/search")
async def search(q: str = Query(..., min_length=1)):
    """
    搜索產品
    
    參數:
    - q: 搜索關鍵詞
    
    返回:
    - 匹配的產品列表
    """
    response = es.search(index="products", body={
        "query": {
            "multi_match": {
                "query": q,
                "fields": ["name", "description"]
            }
        }
    })
    
    # 從 Elasticsearch 響應中提取產品數據
    products = [hit["_source"] for hit in response["hits"]["hits"]]
    return products

# 用於本地開發的入口點
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
