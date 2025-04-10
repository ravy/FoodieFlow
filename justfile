runb:
  cd backend && uvicorn main:app --reload

seedb:
  cd backend && python seed.py