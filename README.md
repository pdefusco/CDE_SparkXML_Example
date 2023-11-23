# Parsing XML's in Cloudera Data Engineering with the Spark XML Package

### Objective

This git repository supports the [Cloudera Community article on using Spark XML in Cloudera Data Engineering (CDE)](). You can run the following commands to parse XML files with Spark in Cloudera Data Engineering (CDE).

CDE is the only cloud-native service purpose-built for enterprise data engineering teams. Building on Apache Spark, Data Engineering is an all-inclusive data engineering toolset that enables orchestration automation with Apache Airflow, advanced pipeline monitoring, visual troubleshooting, and comprehensive management tools to streamline ETL processes across enterprise analytics teams.

CDE is fully integrated with Cloudera Data Platform (CDP), enabling end-to-end visibility and security with SDX as well as seamless integrations with CDP services such as Data Warehouse and Machine Learning. Data Engineering on CDP powers consistent, repeatable, and automated data engineering workflows on a hybrid cloud platform anywhere.

Spark-XML is a library for parsing and querying XML data with Apache Spark, for Spark SQL and DataFrames. Spark Data Engineers use the package in CDE to parse XML files at scale. In the rest of this tutorial we will run a few commands to demonstrate basic functionality of this package in CDE.

### Requirements

The following are required to reproduce the Demo in your CDE Virtual Cluster:

* CDE Service version 1.19 and above
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
cde resource upload --name files --local-path read_xml.py --local-path sample_iot.xml --local-path utils.py
```

##### Create a CDE Spark Job

```
cde job create --name sparkxml --application-file read_xml.py --mount-1-resource files --type spark --packages --packages com.databricks:spark-xml_2.12:0.16.0
```

##### Run the CDE Spark Job

```
cde job run --name sparkxml
```

## References

[Spark XML Package](https://github.com/databricks/spark-xml)

[Cloudera Data Engineering Documentation](https://docs.cloudera.com/data-engineering/cloud/index.html)
