from cerr_curate_app.components.circular.models import Circular


def get_by_id(circular_id):
    """

    :param circular_id:
    :return: Circular
    """
    return Circular.get_by_id(circular_id)


def get_list_by_id(id_list):
    """

    :param id_list: list of circular ids
    :return: list of circular objects
    """
    circular = []
    for id in id_list:
        circular.append(Circular.get_by_id(id))
    return circular


def get_all():
    """List of all circular

    Returns:

        List of all circular
    """
    return Circular.get_all()
