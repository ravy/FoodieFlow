## FoodieFlow 
Restaurant review application

#### Start application
- Install python dependencies
  - Manually
  ```bash
  pip install -r requirements.txt
  ```
  OR
  - VSCode
      - Python: create environment
      - Select runtime
      - Select requirements.txt
- Install neo4j server
  ```bash
  docker run \
    --name foodie-neo4j \
    -p 7474:7474 -p 7687:7687 \
    -d \
    -e NEO4J_AUTH=none \
    neo4j:5
  ```
  neo4j runs at `http://localhost:7474`
- setup data in db
  `just seedb`
- run application
  `just runb`

Then open: `http://localhost:8000/reviews`
