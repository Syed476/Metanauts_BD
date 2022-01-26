from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(2)
}

dag_docs = """
## My Awesome DAG Name
#### Purpose
This DAG does awesome stuff!
#### Outputs
This cool data `pipeline` has the following outputs:
- `output_1` 
- `output_2` 
#### Owner/Maintainer
You can reach the maintainer on this email: 
[maintainer@my-startup-example.io](mailto:maintainer@my-startup-example.io).
"""

with DAG('doc_md_style_2', default_args=default_args, description='Dag DocString',
         schedule_interval='@once', catchup=False) as dag:

    dag.doc_md = dag_docs

    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t1.doc_md = """/
    ### Task 1 message.
    """

    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )

    t3 = BashOperator(
        task_id='greeting',
        bash_command='echo Hello World!',
    )

    t1 >> t2 >> t3
