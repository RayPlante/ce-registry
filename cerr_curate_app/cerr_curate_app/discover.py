import logging
from core_main_app.commons import exceptions

logger = logging.getLogger("core_main_registry_app.discover")


def init_cerr():
    try:
        _create_material_list()
        _create_lifeycle_phase_list()
        _create_synthesis_list()
        _create_product_class_list()
        pass
    except Exception as e:
        logger.error("Impossible to init the registry: {0}".format(str(e)))


def _create_lifeycle_phase_list():
    from cerr_curate_app.components.circular import api as circular_api
    from cerr_curate_app.components.circular.models import Circular

    circular = circular_api.get_all()
    if circular.exists() is False:
        materials_design = Circular.objects.create(name="materials design")
        processing = Circular.objects.create(name="processing")
        product_design = Circular.objects.create(name="product design")
        use_reuse = Circular.objects.create(name="use and reuse")
        repair_refurbishment = Circular.objects.create(name="repair and refurbishment")
        collection_sortation = Circular.objects.create(name="collection and sortation")
        recycling = Circular.objects.create(name="recycling")
        solvent = Circular.objects.create(name="solvents", parent=recycling)
        mechanical = Circular.objects.create(name="mechanical", parent=recycling)
        chemical = Circular.objects.create(name="chemical", parent=recycling)
        carbon_capture = Circular.objects.create(name="carbon capture")
        end_life_management = Circular.objects.create(name="end-of-life management")
        unwanted_outcomes = Circular.objects.create(name="unwanted outcomes")
        material_losses = Circular.objects.create(
            name="material losses", parent=unwanted_outcomes
        )
        carbon_emissions = Circular.objects.create(
            name="carbon emissions", parent=unwanted_outcomes
        )
        public_health_impacts = Circular.objects.create(
            name="public health impacts", parent=unwanted_outcomes
        )
        environmental_impacts = Circular.objects.create(
            name="environmental impacts", parent=unwanted_outcomes
        )


def _create_synthesis_list():
    from cerr_curate_app.components.synthesis import api as synthesis_api
    from cerr_curate_app.components.synthesis.models import Synthesis

    synthesis = synthesis_api.get_all()
    if synthesis.exists() is False:
        synthesis = Synthesis.objects.create(name="Synthesis_and_processing")
        synthesis_annealing_and_homogenization = Synthesis.objects.create(
            name="synthesis_annealing_and_homogenization", parent=synthesis
        )
        synthesis_casting = Synthesis.objects.create(
            name="synthesis_casting", parent=synthesis
        )
        synthesis_forming = Synthesis.objects.create(
            name="synthesis_forming", parent=synthesis
        )
        synthesis_mechanical_and_surface = Synthesis.objects.create(
            name="synthesis_mechanical_and_surface", parent=synthesis
        )
        synthesis_powder_processing = Synthesis.objects.create(
            name="synthesis_powder_processing", parent=synthesis
        )
        synthesis_quenching = Synthesis.objects.create(
            name="synthesis_quenching", parent=synthesis
        )
        synthesis_reactive = Synthesis.objects.create(
            name="synthesis_reactive", parent=synthesis
        )
        synthesis_self_assembly = Synthesis.objects.create(
            name="synthesis_self-assembly", parent=synthesis
        )
        synthesis_solidification = Synthesis.objects.create(
            name="synthesis_solidification", parent=synthesis
        )


def _create_material_list():
    from cerr_curate_app.components.material import api as material_api
    from cerr_curate_app.components.material.models import Material

    materials = material_api.get_all()
    if materials.exists() is False:
        # create method Add init materials
        biomass = Material.objects.create(name="Biomass")
        biomass_child = Material.objects.create(name="biomass", parent=biomass)
        cellulosic = Material.objects.create(name="cellulosic", parent=biomass)
        food = Material.objects.create(name="food", parent=biomass)
        compost = Material.objects.create(name="compost", parent=biomass)
        composites = Material.objects.create(name="Composites")
        glass = Material.objects.create(name="Glass")
        glass_child = Material.objects.create(name="glass", parent=glass)
        concrete = Material.objects.create(name="Concrete")
        gases = Material.objects.create(name="Gases")
        chemicals = Material.objects.create(name="Chemicals")
        chemicals_child = Material.objects.create(name="chemicals", parent=chemicals)
        metals = Material.objects.create(name="Metals and Alloys")
        metals_child = Material.objects.create(name="metals and alloys", parent=metals)
        metals_rare = Material.objects.create(
            name="metals and alloys: rare earth elements", parent=metals
        )
        metals_ferrous = Material.objects.create(
            name="metals and alloys: ferrous", parent=metals
        )
        metals_non_ferrous = Material.objects.create(
            name="metals and alloys: non-ferrous", parent=metals
        )
        polymers = Material.objects.create(name="Polymers: property-based")
        polymers_property_based = Material.objects.create(
            name="polymers: property-based", parent=polymers
        )
        polymers_elastomers = Material.objects.create(
            name="polymers: property-based: elastomers", parent=polymers
        )
        polymers_liquid_crystals = Material.objects.create(
            name="polymers: property-based: liquid crystals", parent=polymers
        )
        polymers_marine_debris = Material.objects.create(
            name="polymers: property-based: marine_debris", parent=polymers
        )
        polymers_micro_nano_plastics = Material.objects.create(
            name="polymers: property-based: micro- and nano-plastics", parent=polymers
        )
        polymers_thermosets = Material.objects.create(
            name="polymers: property-based: thermosets", parent=polymers
        )
        polymers_thermoplastics = Material.objects.create(
            name="polymers: property-based: thermoplastics", parent=polymers
        )

        polymers_chemistry = Material.objects.create(name="Polymers: chemistry-based")
        polymers_chemistry_polyolefins = Material.objects.create(
            name="polymers: chemistry-based: polyolefins", parent=polymers_chemistry
        )
        polymers_chemistry_polyesters = Material.objects.create(
            name="polymers: chemistry-based: polyesters", parent=polymers_chemistry
        )
        polymers_chemistry_polyamides = Material.objects.create(
            name="polymers: chemistry-based: polyamides", parent=polymers_chemistry
        )
        polymers_chemistry_polystyrenes = Material.objects.create(
            name="polymers: chemistry-based: polystyernes", parent=polymers_chemistry
        )
        polymers_chemistry_polycarbonates = Material.objects.create(
            name="polymers: chemistry-based: polycarbonates", parent=polymers_chemistry
        )
        polymers_chemistry_specialty = Material.objects.create(
            name="polymers: chemistry-based: specialty carbonates",
            parent=polymers_chemistry,
        )

        small_organic_compounds = Material.objects.create(
            name="Small organic Compounds"
        )
        small_organic_compounds_child = Material.objects.create(
            name="small organic Compounds", parent=small_organic_compounds
        )


def _create_product_class_list():
    from cerr_curate_app.components.productclass import api as productclass_api
    from cerr_curate_app.components.productclass.models import ProductClass

    productclass = productclass_api.get_all()
    if productclass.exists() is False:
        batteries = ProductClass.objects.create(name="Batteries")
        batteries_child = ProductClass.objects.create(
            name="batteries", parent=batteries
        )
        electronics = ProductClass.objects.create(name="Electronics")
        electronics_child = ProductClass.objects.create(
            name="electronics", parent=electronics
        )
        durableplastics = ProductClass.objects.create(name="Durable Plastics")
        durableplastics_child = ProductClass.objects.create(
            name="durable plastics", parent=durableplastics
        )
        packaging = ProductClass.objects.create(name="Packaging")
        packaging_child = ProductClass.objects.create(
            name="packaging", parent=packaging
        )
        solarpanels = ProductClass.objects.create(name="Solar Panels")
        solarpanels_child = ProductClass.objects.create(
            name="solar panels", parent=solarpanels
        )
        packaging_glass = ProductClass.objects.create(
            name="packaging: glass", parent=packaging
        )
        packaging_plastic = ProductClass.objects.create(
            name="packaging: plastic", parent=packaging
        )
        packaging_metals = ProductClass.objects.create(
            name="packaging: metals", parent=packaging
        )
        packaging_fiber = ProductClass.objects.create(
            name="packaging: fiber", parent=packaging
        )
        building_materials = ProductClass.objects.create(name="Building Materials")
        building_materials_child = ProductClass.objects.create(
            name="building materials", parent=building_materials
        )
        building_materials_wood = ProductClass.objects.create(
            name="building materials: wood", parent=building_materials
        )
        building_materials_glass = ProductClass.objects.create(
            name="building materials: glass", parent=building_materials
        )
        building_materials_concrete = ProductClass.objects.create(
            name="building materials: concrete", parent=building_materials
        )
        building_materials_steel = ProductClass.objects.create(
            name="building materials: steel", parent=building_materials
        )
        textiles = ProductClass.objects.create(name="Textiles")
        textiles_child = ProductClass.objects.create(name="textiles", parent=textiles)
