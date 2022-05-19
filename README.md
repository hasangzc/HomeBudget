# HomeBudget
HomeBudget project with FastApi

HomeBudgetProject; Daily expenditure information is obtained from the user. The user specifies his salary during registration. Considered as a means of regulating the economy


In this project;
- a user registration and login system has been set up.
- User table was created for the user using Sqlalchemy in PostgreSQL. Budget Table was created for the information from the user.(OBJECT RELATIONAL MAPPER(ORM) concept
- Schemas were created with the Pydantic Module. 
- CRUD ops applied
- Edited Swagger Doc that is automatically created with FastAPI
- API tests done with Postmen
- The password received from the user was added to the db as hashed
- JSON Web Token (JWT)  applied
- Setting Env variables
- Database migration tool was used

Some Screenshots;
Postmen;
<img src="https://user-images.githubusercontent.com/75543671/169335476-b6902b1e-c3a9-44b8-aee7-04418c2b7728.png" width="800" height="400"/>
