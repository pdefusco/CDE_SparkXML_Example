# Parsing XML's in Cloudera Data Engineering with the Spark XML Package

### Objective

This git repository supports the [Cloudera Community article on using Spark XML in Cloudera Data Engineering (CDE)](). You can run the following commands to parse XML files with Spark in Cloudera Data Engineering (CDE).

CDE is the only cloud-native service purpose-built for enterprise data engineering teams. Building on Apache Spark, Data Engineering is an all-inclusive data engineering toolset that enables orchestration automation with Apache Airflow, advanced pipeline monitoring, visual troubleshooting, and comprehensive management tools to streamline ETL processes across enterprise analytics teams.

CDE is fully integrated with Cloudera Data Platform (CDP), enabling end-to-end visibility and security with SDX as well as seamless integrations with CDP services such as Data Warehouse and Machine Learning. Data Engineering on CDP powers consistent, repeatable, and automated data engineering workflows on a hybrid cloud platform anywhere.

Spark-XML is a library for parsing and querying XML data with Apache Spark, for Spark SQL and DataFrames. Spark Data Engineers use the package in CDE to parse XML files at scale. In the rest of this tutorial we will run a few commands to demonstrate basic functionality of this package in CDE.

### Requirements

The following are required to reproduce the Demo in your CDE Virtual Cluster:

* CDE Service version 1.19 and above with Spark version 3.x (Spark 2 is not compatible with SparkXML).
* A Working installation of the CDE CLI. Instructions to install the CLI are provided [here](https://docs.cloudera.com/data-engineering/cloud/cli-access/topics/cde-cli.html).
* A working installation of git in your local machine. Please clone this git repository and keep in mind all commands assume they are run in the project's main directory.
* No code edits required but familiarity with Python, Spark and XML is recommended.

### CDE CLI Steps

##### Create a CDE Files Resource

```
cde resource create --name files --type files
```

##### Upload Files to the Resource

```
cde resource upload --name files --local-path read_xml.py --local-path books.xml
```

##### Create a CDE Spark Job

```
cde job create --name sparkxml --application-file read_xml.py --mount-1-resource files --type spark --packages com.databricks:spark-xml_2.12:0.16.0
```

##### Run the CDE Spark Job

```
cde job run --name sparkxml
```
````
+-----+--------------------+--------------------+---------------+-----+------------+--------------------+
|  _id|              author|         description|          genre|price|publish_date|               title|
+-----+--------------------+--------------------+---------------+-----+------------+--------------------+
|bk101|Gambardella, Matthew|\n\n\n         An...|       Computer|44.95|  2000-10-01|XML Developer's G...|
|bk102|          Ralls, Kim|A former architec...|        Fantasy| 5.95|  2000-12-16|       Midnight Rain|
|bk103|         Corets, Eva|After the collaps...|        Fantasy| 5.95|  2000-11-17|     Maeve Ascendant|
|bk104|         Corets, Eva|In post-apocalyps...|        Fantasy| 5.95|  2001-03-10|     Oberon's Legacy|
|bk105|         Corets, Eva|The two daughters...|        Fantasy| 5.95|  2001-09-10|  The Sundered Grail|
|bk106|    Randall, Cynthia|When Carla meets ...|        Romance| 4.95|  2000-09-02|         Lover Birds|
|bk107|      Thurman, Paula|A deep sea diver ...|        Romance| 4.95|  2000-11-02|       Splish Splash|
|bk108|       Knorr, Stefan|An anthology of h...|         Horror| 4.95|  2000-12-06|     Creepy Crawlies|
|bk109|        Kress, Peter|After an inadvert...|Science Fiction| 6.95|  2000-11-02|        Paradox Lost|
|bk110|        O'Brien, Tim|Microsoft's .NET ...|       Computer|36.95|  2000-12-09|Microsoft .NET: T...|
|bk111|        O'Brien, Tim|The Microsoft MSX...|       Computer|36.95|  2000-12-01|MSXML3: A Compreh...|
|bk112|         Galos, Mike|Microsoft Visual ...|       Computer|49.95|  2001-04-16|Visual Studio 7: ...|
+-----+--------------------+--------------------+---------------+-----+------------+--------------------+

root
 |-- _id: string (nullable = true)
 |-- author: string (nullable = true)
 |-- description: string (nullable = true)
 |-- genre: string (nullable = true)
 |-- price: double (nullable = true)
 |-- publish_date: string (nullable = true)
 |-- title: string (nullable = true)
````

## References

[Spark XML Package](https://github.com/databricks/spark-xml)

[Cloudera Data Engineering Documentation](https://docs.cloudera.com/data-engineering/cloud/index.html)
