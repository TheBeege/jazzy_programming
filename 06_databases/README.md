# Databases

Databases are just a way of storing data. You could say that OS X is technically a database, as it provides a way for you to write and read data in the form of files. There are many types of databases to choose from, even the simple concept of a "flat file", such as a CSV or JSON. Here, we'll go over the types of database systems out there, and we'll teach you SQL, the most common database language.

## Types of Databases

### Flat File
Flat file databases are essentially just data written to a text file in some sort of format. 

#### CSV Files
CSV is short for comma separated values. Often, if data needs to be passed around over a network in bulk, a CSV file may be the method of choice. In a CSV, each row is called a record, and each column is called a field. Rows are split by newlines, and columns are split by commas. If there is a comma inside some data, that data will usually be surrounded with double quotes `""` to eliminate ambiguity. Here's an example of a CSV file:
```
id,name,title
1,Bob,Average Joe
2,Jane,Fem Fatale
3,Joe,Plot Device
4,Jazzy,"Snack Queen, Dino Queen, Farm Queen"
```

As above, sometimes the first row of a CSV file contains the name of each field. You'll want to check data for whether or not this is the case before working with it.

#### TSV Files
They're just like CSV files, but they use tabs to separate instead of commas.

#### JSON Files
JSON is short for JavaScript Object Notation. JSON is a common way to represent data structures in text. Fortunately, the syntax is somewhat similar to what you've learned already in Python. Here's an example:
```
{
    "record_count": 4,
    "records": [
        {
            "id": 1,
            "name": "Bob",
            "title": "Average Joe"
        },
        {
            "id": 2,
            "name": "Jane",
            "title": "Fem Fatale"
        },
        {
            "id": 3,
            "name": "Joe",
            "title": "Plot Device"
        },
        {
            "id": 4,
            "name": "Jazzy",
            "title": "Snack Queen, Dino Queen, Farm Queen"
        }
    ]
}
```

This should look a little familiar. You can treat text between curly brackets `{}` as if it were a Python dictionary. Data between square brackets `[]` is like a Python list. I believe this is more common in application development rather than data science, but it's considered common knowledge within the software industry.

### Document Store
A document store is like a flat-file JSON storage on steroids. Specifically, document stores are often JSON document stores. They store data in JSON text format and provide ways to write and retrieve data very quickly using their data storage engine. They're intended to make it easier for application developers to use, but the application developer needs to be careful working with the data. JSON stores often optionally provide structure in their data, meaning application developers can omit or add extra fields as desired, similar to a JSON document.

#### Popular Document Stores
* [DynamoDB](https://aws.amazon.com/dynamodb/) - A document store meant for high-scale applications provided by Amazon's AWS service
* [MongoDB](https://www.mongodb.com/) - A common document store for web applications
* [CouchDB](http://couchdb.apache.org/) - I mean, the Apache Foundation is cool, but I don't know anything about CouchDB other than it exists
* [ElasticSearch](https://www.elastic.co/) - Popular for text searcch

### Relational Database
This is arguably the most popular and long-standing type of database. Relational databases use SQL, or structured query language, for extracting individual bits of data or to aggregate data from huge numbers of rows. This is mostly likely the type of database you'll be working with if you're not using flat files. You'll need to learn SQL to be able to get data out of the database in a format you can use at the level of aggregation required for what you're researching. It's too much to cover in this introduction, but we'll dive into it just afterwards.

Many relational databases perform better at either transactional data, often software applications, or aggregate data, often data warehouses. You'll most likely be working with data warehouses, but some application databases can also scale into data warehouse territory. Additionally, you may need to pull data out of application databases into data warehouses, so it's helpful to be knowledgeable in both.

#### Popular Relational Databases
##### Application
* MySQL
* PostgreSQL
* Oracle
* SQL Server

##### Data Warehouse
* Hadoop Hive
* HP Vertica
* Oracle
* SQL Server Analysis Services

### Key-Value Stores
These are pretty much useless to you, but it's worth recognizing. These are very simple databases, but they're incredibly fast. Many web applications will use them to keep track of logged-in users and cached data for super fast read speeds. They just have one section of data. You request a key, you get a value. That's it. Now scale that to handle thousands of requests per second. Magical, but again, likely not common in data science.

### Things I Don't Know How to Categorize
* Hadoop - Hadoop is just a file system that can scale to store huge amounts of data. Often, Hadoop Hive will be setup for you to access this data in a SQL format
* Spark - I know nothing about format at the time of writing this, but it is the choice system for data warehouses 
* Cassandra - It's like a key-value store, relational database, and document store all had a baby. Also, Netflix uses it for highly redundant, high performance systems. They even have a tool called Chaos Monkey that random kills a Cassandra server to ensure the whole cluster is sufficiently redundant.

## Data Lakes
Recently, the concept of a "data lake" has been popping up, but only the most mature and technically savvy organizations have the manpower and know-how to set them up. The core idea is that data will be stored in any number of different systems, a combination of key-value stores, relational databases, document stores, and who knows what else, but any data should be accessible via one interface. Theoretically, you should be able to get something from both MongoDB and Hadoop Hive using one query language, even though they're completely different systems. If you work at a company that has a data lake, please introduce me to their data team. I want to learn their crazy black magic.