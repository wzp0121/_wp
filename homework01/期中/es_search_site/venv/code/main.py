from fastapi import FastAPI, Query
from es_client import es, create_index

app = FastAPI()

create_index()

@app.get("/search")
def search(q: str = Query(..., min_length=1)):
    response = es.search(index="products", query={
        "multi_match": {
            "query": q,
            "fields": ["name", "description"]
        }
    })
    return [hit["_source"] for hit in response["hits"]["hits"]]