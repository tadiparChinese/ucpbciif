from rest_framework.routers import DefaultRouter
from .api import *

router = DefaultRouter()
router.register(r'paymenttypes',PaymentTypeViewSet) 
router.register(r'payments',PaymentViewSet) 
# router.register(r'loans',LoanViewSet) 
# router.register(r'terms',TermViewSet)
# router.register(r'paymentperiods',PaymentPeriodViewSet)
# router.register(r'loanprograms',LoanProgramViewSet) 
urlpatterns = router.urls