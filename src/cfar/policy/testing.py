from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

from zope.configuration import xmlconfig

from avrc.cfar.coreservice.testing import CFAR_CORE_SERVICE_FIXTURE
from avrc.cfar.masterbook.testing import CFAR_MASTER_BOOK_FIXTURE


class CfarPolicy(PloneSandboxLayer):

    # Use dependency fixtures since they specify database installations
    defaultBases = (CFAR_CORE_SERVICE_FIXTURE, CFAR_MASTER_BOOK_FIXTURE)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import cfar.policy as package
        xmlconfig.file('configure.zcml', package, context=configurationContext)

        # Install products that use an old-style initialize() function
        z2.installProduct(app, 'Products.PloneFormGen')

    def tearDownZope(self, app):
        # Uninstall products installed above
        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cfar.policy:default')


CFAR_POLICY_FIXTURE = CfarPolicy()

CFAR_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CFAR_POLICY_FIXTURE,),
    name='Cfar:Integration'
    )
