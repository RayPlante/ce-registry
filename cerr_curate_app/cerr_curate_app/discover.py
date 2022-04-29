import logging
from core_main_app.commons import exceptions

logger = logging.getLogger("core_main_registry_app.discover")


def init_cerr():
    try:
        _create_material_list()
    except Exception as e:
        logger.error("Impossible to init the registry: {0}".format(str(e)))


def _create_material_list():
    from cerr_curate_app.components.material import api as material_api
    from cerr_curate_app.components.material.models import Material

    materials = material_api.get_all()
    if materials.exists() is False :
        #create method Add init materials
        a = Material.objects.create(name="A")
        b = Material.objects.create(name="B")
        c = Material.objects.create(name="C", parent=b)
        d = Material.objects.create(name="D", parent=c)
        e = Material.objects.create(name="E", parent=c)
