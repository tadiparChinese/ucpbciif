from rest_framework.routers import DefaultRouter
from .api import *
from django.urls import path

router = DefaultRouter()
router.register(r'amortizationitems',AmortizationItemViewSet) 
router.register(r'amortizations',AmortizationViewSet) 
router.register(r'creditlines',CreditLineViewSet) 
router.register(r'loans',LoanViewSet) 
router.register(r'terms',TermViewSet)
router.register(r'paymentperiods',PaymentPeriodViewSet)
router.register(r'loanprograms',LoanProgramViewSet) 
router.register(r'interestrates',InterestRateViewSet) 
router.register(r'status',StatusViewSet) 




urlpatterns =  [ path('updatecreditline/', UpdateCreditLineView.as_view()),
        ]


urlpatterns += router.urls