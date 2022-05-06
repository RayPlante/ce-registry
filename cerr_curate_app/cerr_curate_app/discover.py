import logging
from core_main_app.commons import exceptions

logger = logging.getLogger("core_main_registry_app.discover")


def init_cerr():
    try:
        _create_material_list()
        _create_circular_pathway_list()
        _create_synthesis_list()
        pass
    except Exception as e:
        logger.error("Impossible to init the registry: {0}".format(str(e)))


def _create_circular_pathway_list():
    from cerr_curate_app.components.circular import api as circular_api
    from cerr_curate_app.components.circular.models import Circular

    circular = circular_api.get_all()
    if circular.exists() is False :
        circular = Circular.objects.create(name="Circular Pathways")
        solvent = Circular.objects.create(name="solvents",parent=circular)
        mechanical = Circular.objects.create(name="mechanical",parent=circular)
def _create_synthesis_list():
    from cerr_curate_app.components.synthesis import api as synthesis_api
    from cerr_curate_app.components.synthesis.models import Synthesis

    synthesis = synthesis_api.get_all()
    if synthesis.exists() is False :
        synthesis =  Synthesis.objects.create(name="Synthesis_and_processing")
        synthesis_annealing_and_homogenization = Synthesis.objects.create(name="synthesis_annealing_and_homogenization",
                                                                  parent="synthesis")
        synthesis_casting = Synthesis.objects.create(name="synthesis_casting", parent="synthesis")
        synthesis_forming = Synthesis.objects.create(name="synthesis_forming", parent="synthesis")
        synthesis_mechanical_and_surface = Synthesis.objects.create(name="synthesis_mechanical_and_surface", parent="synthesis")
        synthesis_powder_processing = Synthesis.objects.create(name="synthesis_powder_processing", parent="synthesis")
        synthesis_quenching = Synthesis.objects.create(name="synthesis_quenching", parent="synthesis")
        synthesis_reactive = Synthesis.objects.create(name="synthesis_reactive", parent="synthesis")
        synthesis_self_assembly = Synthesis.objects.create(name="synthesis_self-assembly", parent="synthesis")
        synthesis_solidification = Synthesis.objects.create(name="synthesis_solidification", parent="synthesis")


def _create_material_list():
    from cerr_curate_app.components.material import api as material_api
    from cerr_curate_app.components.material.models import Material

    materials = material_api.get_all()
    if materials.exists() is False :
        #create method Add init materials
        biomaterials = Material.objects.create(name="Biomaterials")
        biomaterials_child = Material.objects.create(name="biomaterials",parent=biomaterials)

        ceramics = Material.objects.create(name="Ceramics")
        ceramics_child =  Material.objects.create(name="ceramics",parent=ceramics)
        ceramics_carbide =  Material.objects.create(name="ceramics: carbides",parent=ceramics)
        ceramics_nitrides =  Material.objects.create(name="ceramics: nitrides",parent=ceramics)
        ceramics_cememts =  Material.objects.create(name="ceramics: cements",parent=ceramics)
        ceramics_oxides =  Material.objects.create(name="ceramics: oxides",parent=ceramics)
        ceramics_perovskites =  Material.objects.create(name="ceramics: perovskites",parent=ceramics)
        ceramics_silicates =  Material.objects.create(name="ceramics: silicates",parent=ceramics)

        metals =  Material.objects.create(name="Metals and Alloys")
        metals_child = Material.objects.create(name="metals and alloys", parent = metals)
        metals_al =  Material.objects.create(name="metals and alloys: Al-containing",parent=metals)
        metals_pure = Material.objects.create(name="metals and alloys: commercially pure metals",parent=metals)
        metals_cu = Material.objects.create(name="metals and alloys: Cu-containing",parent=metals)
        metals_fe = Material.objects.create(name="metals and alloys: Fe-containing",parent=metals)
        metals_intermetallics = Material.objects.create(name="metals and alloys: intermetallics",parent=metals)
        metals_mg = Material.objects.create(name="metals and alloys: Mg-containing",parent=metals)

        organics =  Material.objects.create(name="Organic Compounds")
        organics_child = Material.objects.create(name="organic compounds", parent = organics)
        organics_alcohol = Material.objects.create(name="organic compounds: alcohols", parent = organics)
        organics_aldehydes = Material.objects.create(name="organic compounds: aldehydes", parent = organics)
        organics_alkanes = Material.objects.create(name="organic compounds: alkanes", parent = organics)
        organics_alkynes = Material.objects.create(name="organic compounds: alkynes", parent = organics)
        organics_amines = Material.objects.create(name="organic compounds: amines", parent = organics)
        organics_carboxylic_acids = Material.objects.create(name="organic compounds: carboxylic acids", parent = organics)
        organics_cyclic_compounds = Material.objects.create(name="organic compounds: cyclic compounds", parent = organics)




        polymers = Material.objects.create(name="Polymers")
        polymers_child = Material.objects.create(name="polymers",parent = polymers)
        polymers_copolymers = Material.objects.create(name="copolymers",parent = polymers)
        polymers_homopolymers = Material.objects.create(name="homopolymers",parent = polymers)
        polymers_elastomers = Material.objects.create(name="elastomers",parent = polymers)
        polymers_liquid_crystals = Material.objects.create("polymers: liquid crystals",parent = polymers)
        polymers_polymer_blends = Material.objects.create("polymers: polymer blends",parent = polymers)
        polymers_rubbers = Material.objects.create("polymers: rubbers",parent = polymers)
        polymers_thermoplastics = Material.objects.create("polymers: thermoplastics",parent = polymers)
        polymers_thermosets = Material.objects.create("polymers: thermosets",parent = polymers)

