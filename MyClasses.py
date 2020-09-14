class Manufacturer:
    def __init__(self, name='', registered_country='', contact_person=''):
        self.name = name
        self.registered_country = registered_country
        self.contact_person = contact_person
    def setName (self, name):
        self.name = name
    def setCountry (self, registered_country):
        self.registered_country = registered_country
    def setContact (self, contact_person):
        self.contact_person = contact_person
    def getName (self):
        return self.name
    def getCountry (self):
        return self.registered_country
    def getContact (self):
        return self.contact_person

class User:
    def __init__(self, username='', password='', first_name='', middle_name='', last_name='', company_name='', company_type='',
    address='', officePhone='', cellphone='', email=''):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.company_name = company_name
        self.company_type = company_type
        self.address = address
        self.officePhone = officePhone
        self.cellphone = cellphone
        self.email = email
    def setUsername (self, username):
        self.username = username
    def setPassword (self, password):
        self.password = password
    def setFirst (self, first_name):
        self.first_name = first_name
    def setMiddle (self, middle_name):
        self.middle_name = middle_name
    def setLast (self, last_name):
        self.last_name = last_name
    def setCompanyName (self, company_name):
        self.company_name = company_name
    def setCompanyType (self, company_type):
        self.company_type = company_type
    def setAddress (self, address):
        self.address = address
    def setOfficePhone (self, officePhone):
        self.officePhone = officePhone
    def setCell (self, cellphone):
        self.cellphone = cellphone
    def setEmail (self, email):
        self.email = email
    def getUsername (self):
        return self.username
    def getPassword (self):
        return self.password
    def getFirst (self):
        return self.first_name
    def getMiddle (self):
        return self.middle_name
    def getLast (self):
        return self.last_name
    def getCompanyName (self):
        return self.company_name
    def getCompanyType (self):
        return self.company_type
    def getAddress (self):
        return self.address
    def getOfficePhone (self):
        return self.officePhone
    def getCell (self):
        return self.cellphone
    def getEmail (self):
        return self.email

class TestLab:
    def __init__(self, name='', address='', contact_person=''):
        self.name = name
        self.address = address
        self.contact_person = contact_person
    def setName (self, name):
        self.name = name
    def setAddress (self, address):
        self.address = address
    def setContact (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def getName (self):
        return self.name
    def getAddress (self):
        return self.address
    def getContact (self):
        return self.contact_person

class TestResults:
    def __init__(self, dataSource='', product='', reporting_condition='', test_sequence='', test_date='',
    isc='', voc='', imp='', vmp='', pmp='', ff='', noct=''):
        self.dataSource = dataSource
        self.product = product
        self.reporting_condition = reporting_condition
        self.test_sequence = test_sequence
        self.test_date = test_date
        self.isc = isc
        self.voc = voc
        self.imp = imp
        self.vmp = vmp
        self.pmp = pmp
        self.ff = ff
        self.noct = noct
    def setDataSource (self, dataSource):
        self.dataSource = dataSource
    def setProduct (self, product):
        self.product = product
    def setReportCondition (self, reporting_condition):
        self.reporting_condition = reporting_condition
    def setTestSequence (self, test_sequence):
        self.test_sequence = test_sequence
    def setTestDate (self, test_date):
        self.test_date = test_date
    def setISC (self, isc):
        self.isc = isc
    def setVOC (self, voc):
        self.voc = voc
    def setIMP (self, imp):
        self.imp = imp
    def setVMP (self, vmp):
        self.vmp = vmp
    def setPMP (self, pmp):
        self.pmp = pmp
    def setFF (self, ff):
        self.ff = ff
    def setNOCT (self, noct):
        self.noct = noct
    def getDataSource (self):
        return self.dataSource
    def getProduct (self):
        return self. product
    def getReportCondition (self):
        return self.reporting_condition
    def getTestSequence (self):
        return self.test_sequence
    def getTestDate (self):
        return self.test_date
    def getISC (self):
        return self.isc
    def getVOC (self):
        return self.voc
    def getIMP (self):
        return self.imp
    def getVMP (self):
        return self.vmp
    def getPMP (self):
        return self.pmp
    def getFF (self):
        return self.ff
    def getNOCT (self):
        return self.noct

class Product:
    def __init__(self, model_number='', manufacturer='', manufacturing_date='', length='', width='', weight='',
    cell_area='', cell_technology='', total_cells='', cells_series='', strings_series='', bypass_diodes='', fuse_rating='',
    interconnect_material='', interconnect_supplier='', superstrate_type='', superstrate_manufacturer='', substrate_type='',
    substrate_manufacturer='', frame_material='', frame_adhesive='', encapsulant_type='', encapsulant_manufacturer='', 
    junction_box_type='', junction_box_manufacturer='', junction_box_adhesive='', cable_type='', connector_type='',
    max_sys_volt='', rated_voc='', rated_isc='', rated_vmp='', rated_imp='', rated_pmp='', rated_ff=''):
        self.model_number = model_number
        self.manufacturer = manufacturer
        self.manufacturing_date = manufacturing_date
        self.length = length
        self.width = width
        self.weight = weight
        self.cell_area = cell_area
        self.cell_technology = cell_technology
        self.total_cells = total_cells
        self.cells_series = cells_series
        self.strings_series = strings_series
        self.bypass_diodes = bypass_diodes
        self.fuse_rating = fuse_rating
        self.interconnect_material = interconnect_material
        self.interconnect_supplier = interconnect_supplier
        self.superstrate_type = superstrate_type
        self.superstrate_manufacturer = superstrate_manufacturer
        self.substrate_type = substrate_type
        self.substrate_manufacturer = substrate_manufacturer
        self.frame_material = frame_material
        self.frame_adhesive = frame_adhesive
        self.encapsulant_type = encapsulant_type
        self.encapsulant_manufacturer = encapsulant_manufacturer
        self.junction_box_type = junction_box_type
        self.junction_box_manufacturer = junction_box_manufacturer
        self.junction_box_adhesive = junction_box_adhesive
        self.cable_type = cable_type
        self.connector_type = connector_type
        self.max_sys_volt = max_sys_volt
        self.rated_voc = rated_voc
        self.rated_isc = rated_isc
        self.rated_vmp = rated_vmp
        self.rated_imp = rated_imp
        self.rated_pmp = rated_pmp
        self.rated_ff = rated_ff
    def setModelNumber (self, model_number):
        self.model_number = model_number
    def setManufacturer (self, manufacturer):
        self.manufacturer = manufacturer
    def setLength (self, length):
        self.length = length
    def setWidth (self, width):
        self.width = width
    def setWeight (self, weight):
        self.weight = weight
    def setCellArea (self, cell_area):
        self.cell_area = cell_area
    def setCellTech (self, cell_technology):
        self.cell_technology = cell_technology
    def setTotalCells (self, total_cells):
        self.total_cells = total_cells
    def setCellsSeries (self, cells_series):
        self.cells_series = cells_series
    def setStringsSeries (self, strings_series):
        self.strings_series = strings_series
    def setBypassDiodes (self, bypass_diodes):
        self.bypass_diodes = bypass_diodes
    def setFuseRating (self, fuse_rating):
        self.fuse_rating = fuse_rating
    def setInterconnectMaterial (self, interconnect_material):
        self.interconnect_material = interconnect_material
    def setInterconnectSupplier (self, interconnect_supplier):
        self.interconnect_supplier = interconnect_supplier
    def setSuperstrateType (self, superstrate_type):
        self.superstrate_type = superstrate_type
    def setSuperstrateManufacturer (self, superstrate_manufacturer):
        self.superstrate_manufacturer = superstrate_manufacturer
    def setSubstrateType (self, substrate_type):
        self.substrate_type = substrate_type
    def setSubstrateManufacturer (self, substrate_manufacturer):
        self.substrate_manufacturer = substrate_manufacturer
    def setFrameMaterial (self, frame_material):
        self.frame_material = frame_material
    def setFrameAdhesive (self, frame_adhesive):
        self.frame_adhesive = frame_adhesive
    def setEncapsulantType (self, encapsulant_type):
        self.encapsulant_type = encapsulant_type
    def setEncapsulantManufacturer (self, encapsulant_manufacturer):
        self.encapsulant_manufacturer = encapsulant_manufacturer
    def setJunctionBoxType (self, junction_box_type):
        self.junction_box_type = junction_box_type
    def setJunctionBoxManufacturer (self, junction_box_manufacturer):
        self.junction_box_manufacturer = junction_box_manufacturer
    def setJunctionBoxAdhesive (self, junction_box_adhesive):
        self.junction_box_adhesive = junction_box_adhesive
    def setCableType (self, cable_type):
        self.cable_type = cable_type
    def setConnectorType (self, connector_type):
        self.connector_type = connector_type
    def setMaxSysVoltage (self, max_sys_volt):
        self.max_sys_volt = max_sys_volt
    def setRatedVOC (self, rated_voc):
        self.rated_voc = rated_voc
    def setRatedISC (self, rated_isc):
        self.rated_isc = rated_isc
    def setRatedVMP (self, rated_vmp):
        self.rated_vmp = rated_vmp
    def setRatedIMP (self, rated_imp):
        self.rated_imp = rated_imp
    def setRatedPMP (self, rated_pmp):
        self.rated_pmp = rated_pmp
    def setRatedFF (self, rated_ff):
        self.rated_ff = rated_ff
    def getModelNumber (self, model_number):
        return model_number
    def getManufacturer (self, manufacturer):
        return manufacturer
    def getLength (self, length):
        return length
    def getWidth (self, width):
        return width
    def getWeight (self, weight):
        return weight
    def getCellArea (self, cell_area):
        return cell_area
    def getCellTech (self, cell_technology):
        return cell_technology
    def getTotalCells (self, total_cells):
        return total_cells
    def getCellsSeries (self, cells_series):
        return cells_series
    def getStringsSeries (self, strings_series):
        return strings_series
    def getBypassDiodes (self, bypass_diodes):
        return bypass_diodes
    def getFuseRating (self, fuse_rating):
        return fuse_rating
    def getInterconnectMaterial (self, interconnect_material):
        return interconnect_material
    def getInterconnectSupplier (self, interconnect_supplier):
        return interconnect_supplier
    def getSuperstrateType (self, superstrate_type):
        return superstrate_type
    def getSuperstrateManufacturer (self, superstrate_manufacturer):
        return superstrate_manufacturer
    def getSubstrateType (self, substrate_type):
        return substrate_type
    def getSubstrateManufacturer (self, substrate_manufacturer):
        return substrate_manufacturer
    def getFrameMaterial (self, frame_material):
        return frame_material
    def getFrameAdhesive (self, frame_adhesive):
        return frame_adhesive
    def getEncapsulantType (self, encapsulant_type):
        return encapsulant_type
    def getEncapsulantManufacturer (self, encapsulant_manufacturer):
        return encapsulant_manufacturer
    def getJunctionBoxType (self, junction_box_type):
        return junction_box_type
    def getJunctionBoxManufacturer (self, junction_box_manufacturer):
        return junction_box_manufacturer
    def getJunctionBoxAdhesive (self, junction_box_adhesive):
        return junction_box_adhesive
    def getCableType (self, cable_type):
        return cable_type
    def getConnectorType (self, connector_type):
        return connector_type
    def getMaxSysVoltage (self, max_sys_volt):
        return max_sys_volt
    def getRatedVOC (self, rated_voc):
        return rated_voc
    def getRatedISC (self, rated_isc):
        return rated_isc
    def getRatedVMP (self, rated_vmp):
        return rated_vmp
    def getRatedIMP (self, rated_imp):
        return rated_imp
    def getRatedPMP (self, rated_pmp):
        return rated_pmp
    def getRatedFF (self, rated_ff):
        return rated_ff
