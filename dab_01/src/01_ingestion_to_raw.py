# Databricks notebook source
dbutils.widgets.text("print_job_var", "running the job - default value in notebook")
print(dbutils.widgets.get("print_job_var"))
