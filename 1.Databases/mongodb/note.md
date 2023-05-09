## Create operations
- Read the guideline [here](https://www.mongodb.com/docs/manual/tutorial/insert-documents/) and do the following tasks:
  - Task 1: Use `db.restaurants.insertOne()` to insert one document in this file [restaurants_insert_one.json](restaurants_insert_one.json) to restaurants collection.

    db.restaurants.insertOne({
        "address": "So 1 Dai Co Viet",
        "borough": "Hai Ba Trung",
        "cuisine": "Lau nuong",
        "grades": "One Star",
        "name": "Lau nuong Bach Khoa",
        "restaurant_id": "00000001"
    })

  - Task 2: Use `db.restaurants.insertMany()` to insert many documents in this file [restaurants_insert_many.json](restaurants_insert_many.json) to restaurants collection.

    db.restaurants.insertMany({
        [
            {"address": "So 2 Dai Co Viet", "borough": "Hai Ba Trung", "restaurant_id": "00000002"},
            {"address": "So 3 Dai Co Viet", "borough": "Hai Ba Trung", "restaurant_id": "00000003"},
            {"address": "So 4 Dai Co Viet", "borough": "Hai Ba Trung", "restaurant_id": "00000004"}
        ]
    })

## Read operations
- Read the guideline [here](https://www.mongodb.com/docs/manual/tutorial/query-documents/) (note: change code from Compass to MongoDB Shell) and do the following tasks:
  - Task 3: Write a MongoDB query to display all the documents in the collection restaurants.

  db.restaurants.find({});


  - Task 4: Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine for all the documents in the collection restaurant.

  db.restaurants.find(
    {}, 
    {restaurant_id: 1, name: 1, borough: 1, cuisine: 1 }
    )

  - Task 5: Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine, but exclude the field _id for all the documents in the collection restaurant.

  db.restaurants.find(
    {},
    {_id: 0, restaurant_id: 1, name: 1, borough:1 , cuisine: 1}
  )
  - Task 6: Write a MongoDB query to display all the restaurant which is in the borough Bronx.

  db.restaurants.find({
    borough: "Bronx"
  })

  - Task 7: Write a MongoDB query to display the first 5 restaurant which is in the borough Bronx.

  db.restaurants.find({
    borough: "Bronx"
  }).limit(5)


  - Task 8: Write a MongoDB query to display the next 5 restaurants after skipping first 5 which are in the borough Bronx.

  db.restaurants.find({
    borough: "Bronx"
  }).skip(5).limit(5)


  - Task 9: Write a MongoDB query to find the restaurants who achieved a score more than 90.

  db.restaurant.find({ "grades.score": { $gt: 90 } })

  - Task 10: Write a MongoDB query to find the restaurants that achieved a score, more than 80 but less than 100.

  db.restaurant.find({ "grades.score": { $gt: 80, $lt: 100 } })

  - Task 11: Write a MongoDB query to find the restaurants that do not prepare any cuisine of 'American' and their grade score more than 70 and latitude less than -65.754168. Note : Do this query without using $and operator.
  - Task 12: Write a MongoDB query to find the restaurants which belong to the borough Bronx and prepared either American or Chinese dish.
  - Task 13: Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which belong to the borough Staten Island or Queens or Bronxor Brooklyn.
  - Task 14: Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which are not belonging to the borough Staten Island or Queens or Bronxor Brooklyn.
  - Task 15: Write a MongoDB query to find the restaurant Id, name, address and geographical location for those restaurants where 2nd element of coord array contains a value which is more than 42 and upto 52.
  - Task 16: Write a MongoDB query to know whether all the addresses contains the street or not. 
## Update operations
- MongoDB has many update operations. But in this level we just focus on two update methods: updateOne, updateMany. Read [this](https://www.mongodb.com/docs/manual/reference/update-methods/) article to learn about the methods and do the following tasks:
  - Task 17: Update document has restaurant_id is "00000001": Change field grades from "One Star" to "Five Star".
  - Task 18: Update documents have "borough" is "Hai Ba Trung": Change field "borough" from "Hai Ba Trung" to "Hanoi".
## Delete operations
- We often use two delete methods: deleteOne, deleteMany. Read [this](https://www.mongodb.com/docs/manual/reference/delete-methods/) article to learn more about the methods and do the followings tasks:
  - Task 19: Delete the document which has restaurant_id is "00000001". 
  - Task 20: Delete all documents which have field "borough" is "Hanoi".