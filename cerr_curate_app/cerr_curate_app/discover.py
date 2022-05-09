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
        biomass = Material.objects.create(name="Biomass")
        biomass_child = Material.objects.create(name="biomass",parent=biomass)

        glass = Material.objects.create(name="Glass")
        glass_child = Material.objects.create(name="glass",parent = glass)


        metals =  Material.objects.create(name="Metals and Alloys")
        metals_child = Material.objects.create(name="metals and alloys", parent = metals)
        metals_rare =  Material.objects.create(name="metals and alloys: rare earth elements",parent=metals)
        metals_ferrous = Material.objects.create(name="metals and alloys: ferrous",parent=metals)
        metals_non_ferrous = Material.objects.create(name="metals and alloys: non-ferrous",parent=metals)



        polymers = Material.objects.create(name="Polymers: property-based")
        polymers_property_based = Material.objects.create(name="polymers: property-based",parent = polymers)
        polymers_elastomers = Material.objects.create(name="polymers: property-based: elastomers",parent = polymers)
        polymers_liquid_crystals = Material.objects.create(name="polymers: property-based: liquid crystals",parent = polymers)
        polymers_thermosets = Material.objects.create(name="polymers: property-based thermosets",parent = polymers)
        polymers_thermoplastics = Material.objects.create(name="polymers: property-based: thermoplastics",parent = polymers)

        polymers_chemistry = Material.objects.create(name="Polymers: chemistry-based")
        polymers_chemistry_polyolefins =  Material.objects.create(name="polymers: chemistry-based: polyolefins",parent = polymers_chemistry)
        polymers_chemistry_polyesters =  Material.objects.create(name="polymers: chemistry-based: polyesters",parent = polymers_chemistry)
        polymers_chemistry_polyamides =  Material.objects.create(name="polymers: chemistry-based: polyamides",parent = polymers_chemistry)
        polymers_chemistry_polystyrenes =  Material.objects.create(name="polymers: chemistry-based: polystyernes",parent = polymers_chemistry)
        polymers_chemistry_polycarbonates =  Material.objects.create(name="polymers: chemistry-based: polycarbonates",parent = polymers_chemistry)
        polymers_chemistry_specialty =  Material.objects.create(name="polymers: chemistry-based: specialty carbonates",parent = polymers_chemistry)

        small_organic_compounds = Material.objects.create(name="Small organic Compounds")
        small_organic_compounds_child = Material.objects.create(name="small organic Compounds", parent= small_organic_compounds)