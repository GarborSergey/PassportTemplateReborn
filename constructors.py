import datetime


class PassportException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'PassportException, {self.message}'
        else:
            return 'PassportException have been raised'


class PassportData:
    @staticmethod
    def control_input_data(data):
        if data is None or data == '':
            raise PassportException('An empty line has been submitted for input')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.control_input_data(value)
        setattr(instance, self.name, value)


class Passport:
    panelAssignment = PassportData()
    purposeOfTheIntroductoryControlUnit = PassportData()
    additionalEquipment = PassportData()
    protectiveDevices = PassportData()
    ingressProtectionRating = PassportData()
    climaticVersion = PassportData()
    databaseNumber = PassportData()
    nameBox = PassportData()
    nominalCurrent = PassportData()
    nominalShortCircuitCurrent = PassportData()
    systemGrounding = PassportData()
    installationMethod = PassportData()
    inputCrossSection = PassportData()
    height = PassportData()
    width = PassportData()
    depth = PassportData()
    weight = PassportData()
    protectionClass = PassportData()
    montagePlace = PassportData()

    def __init__(self, panelAssignment, purposeOfTheIntroductoryControlUnit, additionalEquipment, protectiveDevices,
                 ingressProtectionRating, climaticVersion, databaseNumber, nameBox, nominalCurrent,
                 nominalShortCircuitCurrent, systemGrounding, installationMethod, inputCrossSection, height, width,
                 depth, weight, protectionClass):
        self.panelAssignment = panelAssignment
        self.purposeOfTheIntroductoryControlUnit = purposeOfTheIntroductoryControlUnit
        self.additionalEquipment = additionalEquipment
        self.protectiveDevices = protectiveDevices
        self.ingressProtectionRating = ingressProtectionRating
        self.climaticVersion = climaticVersion
        self.databaseNumber = databaseNumber
        self.nameBox = nameBox
        self.nominalCurrent = nominalCurrent
        self.nominalShortCircuitCurrent = nominalShortCircuitCurrent
        self.systemGrounding = systemGrounding
        self.installationMethod = installationMethod
        self.inputCrossSection = inputCrossSection
        self.height = height
        self.width = width
        self.depth = depth
        self.weight = weight
        self.protectionClass = protectionClass
        self.montagePlace = 'полу' if self.installationMethod == 'Напольный' else 'стене'
        self._year = datetime.datetime.now().year
        self._basicName = self.construct_base_name()

    def construct_base_name(self):
        if self.protectiveDevices[0] == '1':
            baseName = f'ВРУ-{self.panelAssignment[0]}-{self.purposeOfTheIntroductoryControlUnit[:2].replace(" ", "")}-' \
                       f'{self.additionalEquipment[0]}-А-' \
                       f'{self.ingressProtectionRating}-{self.climaticVersion}'
        else:
            baseName = f'ВРУ-{self.panelAssignment[0]}-{self.purposeOfTheIntroductoryControlUnit[:2].replace(" ", "")}-' \
                       f'{self.additionalEquipment[0]}-' \
                       f'{self.ingressProtectionRating}-{self.climaticVersion}'

        return baseName

    def get_context(self):
        context = {
            'basicName': self._basicName,
            'databaseNumber': self.databaseNumber,
            'nameBox': self.nameBox,
            'year': self._year,
            'nominalCurrent': self.nominalCurrent,
            'nominalShortCircuitCurrent': self.nominalShortCircuitCurrent,
            'ingressProtectionRating': self.ingressProtectionRating,
            'systemGrounding': self.systemGrounding,
            'installationMethod': self.installationMethod,
            'inputCrossSection': self.inputCrossSection,
            'height': self.height,
            'width': self.width,
            'depth': self.depth,
            'weight': self.weight,
            'protectionClass': self.protectionClass,
            'montagePlace': self.montagePlace
        }
        return context


x = Passport('1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
             '1', '1', '1', '1', '1', '1', '1', '1',)
print(x.get_context())