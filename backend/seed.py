"""
Seed Neo4j with 2 users, 2 restaurants, and reviews
"""
from db import get_driver

def seed_database():
    driver = get_driver()
    session = driver.session()
    try:
        # Create Users
        session.run("CREATE (:User {username: 'johndoe', name: 'John Doe'})")
        session.run("CREATE (:User {username: 'janedoe', name: 'Jane Doe'})")

        # Create Restaurants
        session.run("CREATE (:Restaurant {name: 'KingsBurgers'})")
        session.run("CREATE (:Restaurant {name: 'QueensBurgers'})")

        # Create Reviews with WITH clause for proper query chaining
        session.run("""
            MATCH (u:User {username: 'johndoe'}), (r:Restaurant {name: 'KingsBurgers'})
            WITH u, r
            CREATE (u)-[:REVIEWED {rating: 4, comment: 'Great burgers!'}]->(r)
        """)

        session.run("""
            MATCH (u:User {username: 'janedoe'}), (r:Restaurant {name: 'QueensBurgers'})
            WITH u, r
            CREATE (u)-[:REVIEWED {rating: 5, comment: 'Absolutely loved it!'}]->(r)
        """)

        session.run("""
            MATCH (u:User {username: 'johndoe'}), (r:Restaurant {name: 'QueensBurgers'})
            WITH u, r
            CREATE (u)-[:REVIEWED {rating: 3, comment: 'Decent, but could be better.'}]->(r)
        """)

        session.run("""
            MATCH (u:User {username: 'janedoe'}), (r:Restaurant {name: 'KingsBurgers'})
            WITH u, r
            CREATE (u)-[:REVIEWED {rating: 2, comment: 'Not great, too greasy.'}]->(r)
        """)

        print("Database successfully seeded with users, restaurants, and reviews.")
    
    except Exception as e:
        print(f"Error seeding database: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    seed_database()