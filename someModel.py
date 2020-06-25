import os
from mlflow import log_metric, log_param, log_artifact

if __name__ == '__main__':
    log_param("param1", 5)
    log_param("foo", 1)
    log_param("foo1", 2)
    log_param("foo2", 3)

    with open("output.txt", "w") as f:
        f.write("hello, output")
    log_artifact("output.txt")
