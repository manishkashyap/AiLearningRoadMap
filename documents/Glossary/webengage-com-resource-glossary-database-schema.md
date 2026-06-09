# Database Schema - WebEngage

- URL: https://webengage.com/resource/glossary/database-schema/
- Publication Date: Not found
- Scraped At: 2026-06-04T09:25:10.941411+00:00

Database Schema
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
Home
-
Glossary
-
Database Schema
A database is an organized way of storing, managing, and retrieving data across systems. Ease of access, structuring, and targeting make up for some uses of a good database.
A schema is a blueprint or structure of something.
What is a database schema?
A database schema is nothing but a structure or blueprint of a database, along with a set of rules to govern that database.
It’s like drawing a map. A map is your database; continents, countries, and cities are on that map. A schema’s job is to explain which city is within which country and which country is within which continent. It could do this using borders, labels, latitudes, and longitudes.
Context
A database schema is used in the digital world for managing databases.
Every piece of information that we send or receive in the digital world is stored in a database, either physically or remotely.
The size of a database is directly proportional to the size of the data it houses.
Data is managed differently by different databases using different types of schemas.
Without a schema, data will simply exist meaninglessly without relationships or rules.
Why is a Database Schema important?
A database is made up of tables. Each table contains a specific type of information called fields. Each field has a data type. In database terminology, all these terms are also referred to as entities.
For example, let’s take a database called Map.
Such a database might have a table to store continent information with fields like
continent ID
continent name
Continent location
Then there might be a table for countries with fields like
country ID
country name
country location
And another table for cities with fields like
City ID
City name
City location
Now, these three tables need to be able to communicate with each other, which can’t happen if their relationship with each other isn’t defined.
Without a schema, you won’t know that India and China are in Asia and Mumbai isn’t a continent.
A database schema’s role is to define these relationships and make them structured.
So a schema for this database would basically say, “There is a continent called Asia where India is a country with a city called Mumbai.”
How can I use the Database Schema?
A database schema can either be a visual representation or a bunch of formulas called integrity constraints.
These formulas are written in a data definition language called SQL.
Types of Database Schema
There are essentially three types of database schemas, namely:
Logical Schema
: This type defines all types of logical constraints, like entities, attributes, and views.
Physical Schema
: This type defines how the data is stored physically in a database, like files or indices.
Conceptual Schema
: Indicates a surface-level view of the database that includes details like how the information will be managed, what it will look like, and the business logic that ties everything together.
Illustration
Here’s what a schema looks like​ for an e-commerce database.
Source
Conclusion
Simply put, database schemas are used to define every database we directly or indirectly interact with. Moreover, these blueprints largely help construct scalable databases quickly and seamlessly.
