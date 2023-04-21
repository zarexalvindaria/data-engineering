from airflow.models import DagBag
import re

VALID_DAG_OWNERS = frozenset(("squad-a", "squad-b"))
VALID_DAG_EMAILS = frozenset(("foo@foo.com", "foo@bar.com"))

dagbag = DagBag()


def test_dagbag_import():
    """Verify that Airflow will be able to import all DAGs in the repository."""
    number_of_failures = len(dagbag.import_errors)
    assert number_of_failures == 0, \
        f"There should be no DAG failures. Got: {dagbag.import_errors}"


def test_every_task_should_have_an_owner():
    """Check that every task has known owner."""
    for dag_id, dag in dagbag.dags.items():
        for task in dag.tasks:
            check_owner.description = (
                f"Every task should have a valid owner [{task.task_id}]"
            )
            check_owner(task.owner, dag_id, task.task_id)


def test_if_owner_is_in_default_args_it_should_be_a_valid_owner():
    """When the owner is configured in the 'default_args' it should be a valid owner"""
    for dag_id, dag in dagbag.dags.items():
        if "owner" in dag.default_args:
            check_owner(dag.default_args["owner"], dag_id)


def check_owner(owner, dag_id, task_id=False):
    # Check owner against valid owner list.
    error_msg = (
        "Each task must have defined a valid owner (“{}”). Failing task at "
        "(dag_id={}, task_id={})"
        .format("” or “".join(VALID_DAG_OWNERS), dag_id, task_id)
         )
    assert owner in VALID_DAG_OWNERS, error_msg
