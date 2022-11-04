from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder, MontgomeryCountyParcel, MontgomeryCountyGeology, MontgomeryCountyWatershed, \
    InvasivePlant
from django.db import transaction

world_mapping = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'mpoly': 'MULTIPOLYGON',
}

world_shp = Path(__file__).resolve().parent / 'data' / 'TM_WORLD_BORDERS-0.3.shp'

montgomerycountyparcel_mapping = {
    'objectid': 'OBJECTID',
    'taxpin': 'TAXPIN',
    'alternatei': 'ALTERNATEI',
    'parceltype': 'PARCELTYPE',
    'calcacreag': 'CALCACREAG',
    'truecalcul': 'TrueCalcul',
    'created_us': 'created_us',
    'created_da': 'created_da',
    'last_edite': 'last_edite',
    'last_edi_1': 'last_edi_1',
    'objectid_1': 'OBJECTID_1',
    'parcel_num': 'PARCEL_NUM',
    'location_c': 'LOCATION_C',
    'class_fix': 'CLASS',
    'nbhd': 'NBHD',
    'zoning': 'ZONING',
    'liv_units': 'LIV_UNITS',
    'util1': 'UTIL1',
    'util2': 'UTIL2',
    'util3': 'UTIL3',
    'traffic': 'TRAFFIC',
    'roads1': 'ROADS1',
    'roads2': 'ROADS2',
    'block': 'BLOCK',
    'unit': 'UNIT',
    'alt_id': 'ALT_ID',
    'prop_info_field': 'PROP_INFO_',
    'total_appr': 'TOTAL_APPR',
    'total_asse': 'TOTAL_ASSE',
    'restrictio': 'RESTRICTIO',
    'farmland': 'FARMLAND',
    'obyval': 'OBYVAL',
    'land_use': 'LAND_USE',
    'asmt_chgda': 'ASMT_CHGDA',
    'own1': 'OWN1',
    'own2': 'OWN2',
    'careof': 'CAREOF',
    'addr1': 'ADDR1',
    'addr2': 'ADDR2',
    'addr3': 'ADDR3',
    'zip1_zip2': 'ZIP1_ZIP2',
    'own_info_c': 'OWN_INFO_C',
    'muni_code': 'MUNI_CODE',
    'sch_dist': 'SCH_DIST',
    'subdivisio': 'SUBDIVISIO',
    'lot_no': 'LOT_NO',
    'frontft': 'FRONTFT',
    'legal1': 'LEGAL1',
    'legal2': 'LEGAL2',
    'legal3': 'LEGAL3',
    'loc_no': 'LOC_NO',
    'loc_add': 'LOC_ADD',
    'loc_dir': 'LOC_DIR',
    'loc_str': 'LOC_STR',
    'loc_suf': 'LOC_SUF',
    'loc_suf2': 'LOC_SUF2',
    'loc_unitde': 'LOC_UNITDE',
    'loc_unitno': 'LOC_UNITNO',
    'location1': 'LOCATION1',
    'location2': 'LOCATION2',
    'loc_zip1_z': 'LOC_ZIP1_Z',
    'legal_chgd': 'LEGAL_CHGD',
    'est_co_tax': 'EST_CO_TAX',
    'est_muni_t': 'EST_MUNI_T',
    'est_sch_ta': 'EST_SCH_TA',
    'deed_book': 'DEED_BOOK',
    'deed_page': 'DEED_PAGE',
    'sale_date': 'SALE_DATE',
    'considerat': 'CONSIDERAT',
    'state_tax_field': 'STATE_TAX_',
    'steb': 'STEB',
    'land_sf': 'LAND_SF',
    'land_acres': 'LAND_ACRES',
    'land_chgda': 'LAND_CHGDA',
    'pool': 'POOL',
    'oby_chgdat': 'OBY_CHGDAT',
    'condition': 'CONDITION',
    'degree_rem': 'DEGREE_REM',
    'yr_rem': 'YR_REM',
    'sfla': 'SFLA',
    'finbsmt_sf': 'FINBSMT_SF',
    'stories': 'STORIES',
    'extwall': 'EXTWALL',
    'basement': 'BASEMENT',
    'fuel': 'FUEL',
    'heat': 'HEAT',
    'year_built': 'YEAR_BUILT',
    'style': 'STYLE',
    'bedrooms': 'BEDROOMS',
    'baths': 'BATHS',
    'half_baths': 'HALF_BATHS',
    'rm_tot': 'RM_TOT',
    'prefab_frp': 'PREFAB_FRP',
    'frpl_open': 'FRPL_OPEN',
    'frpl_stack': 'FRPL_STACK',
    'bsmt_car': 'BSMT_CAR',
    'dwel_chgda': 'DWEL_CHGDA',
    'comm_area': 'COMM_AREA',
    'comm_nla': 'COMM_NLA',
    'structure': 'STRUCTURE',
    'use_type': 'USE_TYPE',
    'comm_bsmt': 'COMM_BSMT',
    'comm_heat': 'COMM_HEAT',
    'comm_air': 'COMM_AIR',
    'comm_yr_bl': 'COMM_YR_BL',
    'comm_units': 'COMM_UNITS',
    'comm_ident': 'COMM_IDENT',
    'park_cov': 'PARK_COV',
    'park_uncov': 'PARK_UNCOV',
    'partition': 'PARTITION',
    'residual': 'RESIDUAL',
    'elev': 'ELEV',
    'comm_chgda': 'COMM_CHGDA',
    'assessment': 'ASSESSMENT',
    'prop_info1': 'PROP_INFO1',
    'assmt_chgd': 'ASSMT_CHGD',
    'own_info_1': 'OWN_INFO_1',
    'legal_ch_1': 'LEGAL_CH_1',
    'sale_date_field': 'SALE_DATE_',
    'land_chdat': 'LAND_CHDAT',
    'oby_chgd_1': 'OBY_CHGD_1',
    'dwel_chg_1': 'DWEL_CHG_1',
    'comm_chg_1': 'COMM_CHG_1',
    'parcel': 'PARCEL',
    'landsf': 'LANDSF',
    'est_mccc_t': 'EST_MCCC_T',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

montgomerycountyparcel_shp = Path(
    __file__).resolve().parent / 'data' / 'Montgomery_County_Parcels' / 'Montgomery_County_Parcels.shp'

# Auto-generated `LayerMapping` dictionary for MontgomeryCountyGeology model
montgomerycountygeology_mapping = {
    'objectid': 'OBJECTID',
    'original_l': 'Original_L',
    'sgmc_label': 'SGMC_Label',
    'unit_name': 'Unit_Name',
    'minimum_ag': 'Minimum_Ag',
    'maximum_ag': 'Maximum_Ag',
    'major_1': 'Major_1',
    'major_2': 'Major_2',
    'minor_1': 'Minor_1',
    'minor_2': 'Minor_2',
    'reference_field': 'Reference_',
    'reference': 'Reference',
    'generalize': 'Generalize',
    'digital_ur': 'Digital_UR',
    'ngmdb1': 'NGMDB1',
    'shape_are': 'Shape__Are',
    'shape_len': 'Shape__Len',
    'geom': 'MULTIPOLYGON',
}

montgomerycountygeology_shp = Path(
    __file__).resolve().parent / 'data' / 'Montgomery_County_Geology' / 'Montgomery_County_Geology.shp'

montgomerycountywatershed_mapping = {
    'objectid': 'OBJECTID',
    'huc12': 'HUC12',
    'name': 'NAME',
    'shape_are': 'Shape__Are',
    'shape_len': 'Shape__Len',
    'geom': 'MULTIPOLYGON',
}

montgomerycountywatershed_shp = Path(
    __file__).resolve().parent / 'data' / 'Montgomery_County_Watersheds_-_Minor' / 'Montgomery_County_Watersheds_-_Minor.shp'

invasiveplant_mapping = {
    'objectid': 'OBJECTID',
    'site_id_fs': 'SITE_ID_FS',
    'accepted_p': 'ACCEPTED_P',
    'accepted_s': 'ACCEPTED_S',
    'accepted_c': 'ACCEPTED_C',
    'date_colle': 'DATE_COLLE',
    'total_area': 'TOTAL_AREA',
    'infested_a': 'INFESTED_A',
    'infested_p': 'INFESTED_P',
    'fs_unit_na': 'FS_UNIT_NA',
    'crc_value': 'CRC_VALUE',
    'geom': 'MULTIPOLYGON',
}

invasiveplant_shp = Path(
    __file__).resolve().parent / 'data' / 'Current_Invasive_Plants_(Feature_Layer)' / 'Current_Invasive_Plants_(Feature_Layer).shp'

mapping_mapping = {
    'WorldBorder': {
        'mapping': world_mapping,
        'file': world_shp,
        'model': WorldBorder
    },
    'MontgomeryCountyParcel': {
        'mapping': montgomerycountyparcel_mapping,
        'file': montgomerycountyparcel_shp,
        'model': MontgomeryCountyParcel
    },
    'MontgomeryCountyGeology': {
        'mapping': montgomerycountygeology_mapping,
        'file': montgomerycountygeology_shp,
        'model': MontgomeryCountyGeology
    },
    'MontgomeryCountyWatershed': {
        'mapping': montgomerycountywatershed_mapping,
        'file': montgomerycountywatershed_shp,
        'model': MontgomeryCountyWatershed
    },
    'InvasivePlant': {
        'mapping': invasiveplant_mapping,
        'file': invasiveplant_shp,
        'model': InvasivePlant
    }
}


def run(model_name, verbose=False):
    import_map = mapping_mapping.get(model_name, None)
    if not import_map:
        print(f'No mapping for {model_name}, Exiting')
        return
    mapping = import_map.get('mapping')
    file = import_map.get('file')
    model = import_map.get('model')
    lm = LayerMapping(model, file, mapping, transform=False, transaction_mode='autocommit')
    lm.save(strict=False, verbose=verbose)
