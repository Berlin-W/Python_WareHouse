
import os

# 锁定远端操作环境, 避免存在多个版本环境的问题
os.environ['JAVA_HOME'] = '/export/server/jdk'
os.environ['HADOOP_HOME'] = '/export/server/hadoop'
os.environ['SPARK_HOME'] = '/export/server/spark-local'
os.environ["PYSPARK_PYTHON"] = "/export/server/anaconda3/bin/python3"
os.environ["PYSPARK_DRIVER_PYTHON"] = "/export/server/anaconda3/bin/python3"

# 快捷键:  main 回车
if __name__ == '__main__':
    print("pyspark模板")
