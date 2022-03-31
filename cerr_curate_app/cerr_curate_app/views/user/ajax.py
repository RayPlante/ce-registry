def data_structure_element_value(request):
    """Endpoint for data structure element value

    Args:
        request:

    Returns:

    """
    if request.method == "POST":
        return save_data_structure_element_value(request)


def save_data_structure_element_value(request):
    print("test")
