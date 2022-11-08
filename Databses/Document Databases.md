---
date created: Monday, November 7th 2022, 3:14:19 pm
date modified: Tuesday, November 8th 2022, 5:27:06 pm
date_created: Monday, November 7th 2022, 3:14:19 pm
date_modified: Tuesday, November 8th 2022, 5:30:19 pm
---

# Databases

	These are the databses I've used to build something.

##### Mongo 
#nodejs document databse that uses a JSON syntax for queries inserts etc.


# ORM

	An "Object Relational Mapper" acts as a bridge between the various slightly different sql syntaxes and the object model in programming languages  


##### Mongoose
#nodejs ORM and databse schema system (for mongodb), used with express for [[Cancard]].



## snippets
##### create admin user

```shell
mongosh
use admin
db.createUser(
 {
     user: "phlawless",
     pwd: "1ntheattic",
     roles: [
           { role: "userAdminAnyDatabase", db: "admin" },
           { role: "readWriteAnyDatabase", db: "admin" },
           { role: "dbAdminAnyDatabase", db: "admin" }
        ]
 })
```
