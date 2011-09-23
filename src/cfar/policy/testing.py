from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

from zope.configuration import xmlconfig

class cfarPolicy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import cfar.policy
        xmlconfig.file('configure.zcml', cfar.policy, context=configurationContext)
        
        # Install products that use an old-style initialize() function
        z2.installProduct(app, 'Products.PloneFormGen')
    
    def tearDownZope(self, app):
        # Uninstall products installed above
        z2.uninstallProduct(app, 'Products.PloneFormGen')
        
    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cfar.policy:default')

CFAR_POLICY_FIXTURE = cfarPolicy()
CFAR_POLICY_INTEGRATION_TESTING = IntegrationTesting(bases=(CFAR_POLICY_FIXTURE,), name="leadtheway:Integration")
