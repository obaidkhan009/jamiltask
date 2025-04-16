from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class ResearchPaper(BaseModel):
    id: int
    title: str
    author: str
    abstract: str


# In-memory store
papers: List[ResearchPaper] = []


# POST - Add a new research paper
@app.post("/papers/")
def add_paper(paper: ResearchPaper):
    for p in papers:
        if p.id == paper.id:
            raise HTTPException(status_code=400, detail="Paper ID already exists")
    papers.append(paper)
    return {"message": "Paper added successfully"}


# GET - Get all research papers
@app.get(
    "/papers/",
    response_model=List[ResearchPaper]
)


def get_papers():
    return papers


# DELETE - Remove a paper by ID
@app.delete("/papers/{paper_id}")
def delete_paper(paper_id: int):
    for i, paper in enumerate(papers):
        if paper.id == paper_id:
            del papers[i]
            return {"message": "Paper deleted successfully"}
        raise HTTPException(status_code=404, detail="Paper not found")

