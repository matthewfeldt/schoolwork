import csv
from MyClasses import Manufacturer, User, TestLab, TestResults, Product
def getResults():
    results = open('test_results.csv')
    getResults.results = results

def registerModule():
    mds = {}

    model_number = input('Model number: ')
    manufacturer = input('Manufacturer: ')
    manufacturing_date = input('Manufacturing Date: ')
    length= input('Module Length: ')
    width = input('Module Width: ')
    module_weight = input('Module weight: ')
    cell_area = input('Cell area: ')
    cell_technology = input('Cell technology (mono-Si, poly-Si, a-Si, CIS, CdTe, etc.):')
    cell_total = input('Total number of cells: ')
    cell_series = input('Number of cells in series: ')
    string_series = input('Number of strings in series: ')
    bypass_diodes = input('Number of bypass diodes: ')
    series_fuse_rating = input('Series fuse rating (A): ')
    interconnect_material = input('Interconnect material: ')
    interconnect_supplier = input('Interconnect supplier: ')
    superstrate_type = input('Superstrate type (eg.. strengthened glass, etc.): ')
    superstrate_manufacturer = input('Superstrate manufacturer and part number: ')
    substrate_type = input('Substrate type: ')
    substrate_manufacturer = input('Substrate manufacturer and part number: ')
    frame_type = input('Frame type/material: ')
    frame_adhesive = input('Frame adhesive: ')
    encapsulation_type = input('Encapsulation type: ')
    encapsulation_manufacturer = input('Encapsulation manufacturer and part number: ')
    junction_box_type = input('Junction box type: ')
    junction_box_manufacturer = input('Junction box manufactuer and part number: ')
    junction_box_adhesive = input('Junction box adhesive: ')
    cable_type = input('Cable type: ')
    connector_type = input('Connector type: ')
    max_sys_voltage = input('Maximum system voltage: ')
    voc = input('VOC(V): ')
    isc = input('ISC(A): ')
    vmp = input('VMP(V): ')
    imp = input('IMP(A): ')
    pmp = input('PMP(W): ')
    ff = input('FF(%): ')

    mds['Model number'] = model_number
    mds['Manufacturer'] = manufacturer
    mds['Manufacturing date'] = manufacturing_date
    mds['Module length'] = length
    mds['Module width'] = width
    mds['Module weight(kg)'] = module_weight
    mds['Individual cell area'] = cell_area
    mds['Cell technology'] = cell_technology
    mds['Total number of cells'] = cell_total
    mds['Number of cells in series'] = cell_series
    mds['Number of series strings'] = string_series
    mds['Number of bypass diodes'] = bypass_diodes
    mds['Series fuse rating(A)'] = series_fuse_rating
    mds['Interconnect material'] = interconnect_material
    mds['Interconnect supplier'] = interconnect_supplier
    mds['Superstrate type'] = superstrate_type
    mds['Superstrate manufacturer and part #'] = superstrate_manufacturer
    mds['Substrate type'] = substrate_type
    mds['Substrate manufacturer and part #'] = substrate_manufacturer
    mds['Frame type/material'] = frame_type
    mds['Frame adhesive'] = frame_adhesive
    mds['Encapsulant type'] = encapsulation_type
    mds['Encapsulant manufacturer and part #'] = encapsulation_manufacturer
    mds['Junction box type'] = junction_box_type
    mds['Junction box manufacturer and part #'] = junction_box_manufacturer
    mds['Junction box adhesive'] = junction_box_adhesive
    mds['Cable type'] = cable_type
    mds['Connector type'] = connector_type
    mds['Maximum system voltage'] = max_sys_voltage
    mds['VOC (V)'] = voc
    mds['ISC (A)'] = isc
    mds['VMP (V)'] = vmp
    mds['IMP (A)'] = imp
    mds['PMP (W)'] = pmp
    mds['FF (%)'] = ff

    return mds


def userRegister():

    userForm = {}

    username = input('Username: ')
    password = input ('Password: ')
    first_name = input('First Name: ')
    middle_name = input('Middle Name (optional):')
    last_name = input('Last Name: ')
    company_name = input('Company Name: ')
    company_type = input('Company Type (test lab or manufacturer): ')
    address = input('Address: ')
    office_phone  = input('Office Phone: ')
    cell_phone = input('Cell Phone: ')
    email = input('Email: ')

    userForm['Username'] = username
    userForm['Password'] = password
    userForm['First name'] = first_name
    userForm['Middle name'] = middle_name
    userForm['Last name'] = last_name
    userForm['Company name'] = company_name
    userForm['Company type'] = company_type
    userForm['Address'] = address
    userForm['Office phone'] = office_phone
    userForm['Cell phone'] = cell_phone
    userForm['Email'] = email

    return userForm

def manufacturerRegister():
    manForm = {}

    name = input('Company Name: ')
    registered_country = input('Registered Country: ')
    contact_person = input('Contact Person: ')

    manForm['Name'] = name
    manForm['Country'] = registered_country
    manForm['Contact'] = contact_person

    return manForm

def main():
    choice = 0
    while choice != '5':
        choice = input('Please select an action below:\n1. View baseline test results.\n2. Register a PV module.\n3. Register a User.\n4. Register a Manufacturer.\n5. Quit.\n Select a Number: ')
        
        if choice  == '1':
            getResults()
            for line in getResults.results:
                if 'Baseline' in line:
                    print(line.rstrip('\n'))
        elif choice == '2':
            mds = registerModule()
            userForm = userRegister()
            manForm = manufacturerRegister()

            manufacturer = mds['Manufacturer']
            first_name = userForm['First name']
            last_name = userForm['Last name']
            email = userForm['Email']
            model_number = mds['Model number']
            cell_technology = mds['Cell technology']
            max_sys_voltage = mds['Maximum system voltage']
            rated_pmp = mds['PMP (W)']

            p = Product(mds)
            u = User(userForm)
            t = TestLab(userForm)
            m = Manufacturer(manForm)
            p.setManufacturer(manufacturer)
            m.setName(manufacturer)
            u.setFirst(first_name)
            u.setLast(last_name)
            t.setContact(first_name, last_name)
            u.setEmail(email)
            p.setModelNumber(model_number)
            p.setCellTech(cell_technology)
            p.setMaxSysVoltage(max_sys_voltage)
            p.setRatedPMP(rated_pmp)

            print('Manufacturer: ', p.getManufacturer(), 'Conact Name: ', t.getContact(), 'Email: ', u.getEmail(),
            'Model Number: ', p.getModelNumber(), 'Cell Technology: ', p.getCellTech(), 'System Voltage: ', p.getMaxSysVoltage(), 
            'Rated Power (PMP)', p.getRatedPMP())

        elif choice =='3':

            userForm = userRegister()

            username = userForm['Username']
            password = userForm['Password']
            first_name = userForm['First name']
            middle_name = userForm['Middle name']
            last_name = userForm['Last name']
            company_name = userForm['Company name']
            company_type = userForm['Company type']
            address = userForm['Address']
            office_phone = userForm['Office phone']
            cell_phone = userForm['Cell phone']
            email = userForm['Email']

            u = User(userForm)
            u.setUsername(username)
            u.setPassword(password)
            u.setFirst(first_name)
            u.setMiddle(middle_name)
            u.setLast(last_name)
            u.setCompanyName(company_name)
            u.setCompanyType(company_type)
            u.setAddress(address)
            u.setOfficePhone(office_phone)
            u.setCell(cell_phone)
            u.setEmail(email)

        elif choice =='4':
            manForm = manufacturerRegister()

            name = manForm['Name']
            country = manForm['Country']
            contact_person = manForm['Contact']

            m = Manufacturer(manForm)
            m.setName(name)
            m.setCountry(country)
            m.setContact(contact_person)

    

if __name__ == '__main__':
    main()
