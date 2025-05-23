from elasticsearch import Elasticsearch
import os
from dotenv import load_dotenv

# 加載環境變量（如果有的話）
load_dotenv()

# 獲取 Elasticsearch 連接配置
ES_HOST = os.getenv("ES_HOST", "http://localhost:9200")
ES_USER = os.getenv("ES_USER", "")
ES_PASSWORD = os.getenv("ES_PASSWORD", "")

# 創建 Elasticsearch 客戶端
if ES_USER and ES_PASSWORD:
    es = Elasticsearch(
        ES_HOST,
        basic_auth=(ES_USER, ES_PASSWORD),
        verify_certs=False
    )
else:
    es = Elasticsearch(ES_HOST)

def create_index():
    """
    創建 products 索引（如果不存在）
    定義映射以優化搜索結果
    """
    # 檢查索引是否存在
    if not es.indices.exists(index="products"):
        # 創建索引及其映射
        mapping = {
            "mappings": {
                "properties": {
                    "name": {
                        "type": "text",
                        "analyzer": "standard",
                        "fields": {
                            "keyword": {
                                "type": "keyword"
                            }
                        }
                    },
                    "description": {
                        "type": "text",
                        "analyzer": "standard"
                    },
                    "price": {
                        "type": "float"
                    },
                    "category": {
                        "type": "keyword"
                    },
                    "image_url": {
                        "type": "keyword"
                    }
                }
            }
        }
        es.indices.create(index="products", body=mapping)
        print("索引 'products' 已創建")
        
        # 添加一些測試數據（可選）
        sample_data = [
            {
                "name": "iPhone 13",
                "description": "Apple iPhone 13 智能手機，128GB 存儲容量",
                "price": 25900,
                "category": "電子產品"
            },
            {
                "name": "Samsung Galaxy S21",
                "description": "Samsung Galaxy S21 智能手機，高性能處理器，出色的相機系統",
                "price": 21500,
                "category": "電子產品"
            },
            {
                "name": "MacBook Pro",
                "description": "Apple MacBook Pro 13英寸筆記本電腦，M1晶片，8GB內存",
                "price": 39900,
                "category": "電子產品"
            },
            {
                "name": "無線耳機",
                "description": "藍牙5.0無線耳機，降噪功能，長達8小時的電池續航",
                "price": 1200,
                "category": "配件"
            },
            {
                "name": "智能手錶",
                "description": "防水智能手錶，心率監測，睡眠追蹤，多種運動模式",
                "price": 3500,
                "category": "可穿戴設備"
            }
        ]
        
        # 批量索引數據
        operations = []
        for i, doc in enumerate(sample_data):
            operations.append({"index": {"_index": "products", "_id": str(i+1)}})
            operations.append(doc)
        
        if operations:
            es.bulk(operations)
            print(f"已添加 {len(sample_data)} 個產品到索引")
    else:
        print("索引 'products' 已存在")

