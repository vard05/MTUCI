import uvicorn
from fastapi import FastAPI, Request, status
from pydantic import BaseModel
from typing import Optional
import wikipedia

app = FastAPI()

class Article(BaseModel):
    title: str

# PATH запрос

@app.get("/article/{title}")
def search_by_path(request: Request, title: str):
    
    for title in title.split():
        if title != "":
            try:
                data = wikipedia.summary(title, sentences=4)
            except wikipedia.exceptions.DisambiguationError as e:
                data = e.options
            return data, status.HTTP_200_OK

    return status.HTTP_500_INTERNAL_SERVER_ERROR

# QUERY запрос

@app.post("/query_search/")
def search_by_query(query: Optional[str] = None):

    articles = [wikipedia.search(title) for title in query.split() if title != ""]
    data = {
        "articles": [
            {"titles": article}
            for article in articles
        ]
    }
    return data, status.HTTP_200_OK

# BODY запрос

@app.post("/post_search/")
def search_by_body(article: Article):

    try:
        data = wikipedia.summary(article, sentences=4)
    except wikipedia.exceptions.DisambiguationError as e:
        return status.HTTP_500_INTERNAL_SERVER_ERROR

    return data, status.HTTP_200_OK

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
