# Geo Django Example

#### Examples of GeoDjango and RestFrameworkGIS.

## Quickstart

##### Create venv

```shell
python -m venv venv
```

- Use `python3` if on macOS

##### Activate venv and install requirements.txt

```shell
source venv/bin/activate
pip install -r requirements.txt
```

##### Install Dependencies

- Only shown using homebrew with macOS, feel free to add other examples

```shell

```

##### How I Generated Data

```shell
python manage.py ogrinspect world/data/business_licenses/business_licenses.shp PhiladelphiaBusinessLicenses --mapping --null=true --blank=true --multi-geom
python manage.py ogrinspect world/data/beverage_tax_registration_data5/beverage_tax_registration_data5.shp PhiladelphiaBeverageTax --mapping --null=true --blank=true --multi-geom
python manage.py ogrinspect world/data/Street_Poles/Street_Poles.shp PhiladelphiaStreetPoles --mapping --null=true --blank=true --multi-geom
python manage.py ogrinspect world/data/BUILDING_CERTS/BUILDING_CERTS.shp PhiladelphiaBuildingCerts --mapping --null=true --blank=true --multi-geom
```