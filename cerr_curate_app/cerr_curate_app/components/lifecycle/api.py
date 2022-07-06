from cerr_curate_app.components.lifecycle.models import Lifecycle


def get_by_id(lifecycle_id):
    """

    :param circular_id:
    :return: Circular
    """
    return Lifecycle.get_by_id(circular_id)


def get_list_by_id(id_list):
    """

    :param id_list: list of circular ids
    :return: list of circular objects
    """
    lifecycle = []
    for id in id_list:
        lifecycle.append(Lifecycle.get_by_id(id))
    return circular


def get_all():
    """List of all circular

    Returns:

        List of all circular
    """
    return Lifecycle.get_all()
