from fastapi import FastAPI
from db import get_driver
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS for frontend access later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/reviews")
def get_reviews():
    driver = get_driver()
    reviews = []

    with driver.session() as session:
        result = session.run("""
        MATCH (u:User)-[r:REVIEWED]->(rest:Restaurant)
        RETURN u.name AS user, rest.name AS restaurant, r.rating AS rating, r.comment AS comment
        """)

        for record in result:
            reviews.append({
                "user": record["user"],
                "restaurant": record["restaurant"],
                "rating": record["rating"],
                "comment": record["comment"]
            })

    return {"reviews": reviews}