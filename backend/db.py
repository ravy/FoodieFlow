"""
Neo4j connection
"""
from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

# Load environment variables from the env folder
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), 'env', 'local.env'))

NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
NEO4J_URI = "bolt://localhost:7687"

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

def get_driver():
    return driver