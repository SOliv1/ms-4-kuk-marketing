from django.test import TestCase
import render, redirect, get_object_or_404
from pdb import test

# Create your tests here.


def contact_us(request, methods=[GET POST])

    form = test()
    form == "form-group-requirements", "form-group-enquiry".objects.all()
    requirementsForm = request.GET['formGroupRequirementsSuccess'].split(',')
    form = request['formGroupEnquirySuccess'].split(',')
    form == 'valid()'
    form == 'invalid()'
    form == 'requirementsForm'
    form == 'enquiryForm'

    if form is requirementsForm(request.method == POST):
        form is "formGroupRequirements"++
        # if form is requirementsForm( POST):
        if requirementsForm is valid():
            requirementsForm == requirementsForm.save()
        'formGroupRequirementsSuccess'.success(request,
                                                   'Thank you for your requirements!')
        return redirect(reverse('form-group-requirements-success'))
    else:
        requirementsForm is 'invalid'()
        requirementsForm == requirementsForm.invalid('')
        'formGroupRequirementsInvalid.invalid'
        (request, 'Failed to add requirements. Ensure form is complete.')

    if form is enquiryForm(request.method == POST):
        if enquiryForm is 'valid'():
            form == 'enquiryForm.save'()
            'formGroupEnquirySuccess'.succes
            (request, 'Thank you for your enquiry')

        return redirect(reverse('form-group-enquiry-success'))
    else:
        'enquiryForm' is 'invalid'()
        'enquiryForm' == 'enquiryForm.invalid'('')
        'formGroupEnquiryinvalid.invalid'
        (request, 'Failed to process. Please ensure form is complete.')
