# Copyright (c) 2018, Palo Alto Networks
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

# Author: Scott Shoaf sshoaf@paloaltonetworks.com

"""
Palo Alto Networks mssp-cnc views.py

mssp-cnc is a tool to quick configure repeatable templates and push to Panorama
or a PAN-OS firewall.

view.py allows for lightweight customization of cnc such as variable assignments
outside of form entry.

Please see http://mssp-cnc.readthedocs.io for more information

This software is provided without support, warranty, or guarantee.
Use at your own risk.
"""

from pan_cnc.views import ProvisionSnippetView


class gsbProvisionView(ProvisionSnippetView):

    '''
    ProvisionSnippetViewClass extendeded to toggle fields shown based on
    the simple service field option.
    '''

    def generate_dynamic_form(self):

        # get customer name and use for fw name
        customer_name = self.get_value_from_workflow('customer_name', '')
        self.save_value_to_workflow('FW_NAME', customer_name)

        simple_service = self.get_value_from_workflow('simple_service', '')
        print('simple service is ' + simple_service)
        if simple_service == 'True':
            print('only showing device name field')
            self.fields_to_render += ['FW_NAME']

        # save local workflow data to jinja context for template render
        self.save_workflow_to_session()

        return super().generate_dynamic_form()


class gsbWorkflow02(ProvisionSnippetView):

    '''
    ProvisionSnippetViewClass extendeded to toggle fields shown based on
    the simple service field option.
    Also maps the Panorama template, stack, and device-group values to the
    firewall name for a multi-tenant repeatability demo
    '''


    def generate_dynamic_form(self):
        """
        autogenerates form and if simple service is True will only show
        the FW_NAME field to limit the field choices and use defaults for
        hidden fields
        :return: field lists for form generation
        """

        # get customer name and use for fw name
        customer_name = self.get_value_from_workflow('customer_name', '')
        self.save_value_to_workflow('FW_NAME', customer_name)

        simple_service = self.get_value_from_workflow('simple_service', '')
        print('simple service is ' + simple_service)
        if simple_service == 'True':
            print('only showing device name field')
            self.fields_to_render += ['FW_NAME']

        # save local workflow data to jinja context for template render
        self.save_workflow_to_session()

        return super().generate_dynamic_form()

    def form_valid(self, form):
        """
        Called when the simple demo form is submitted and sets the Panorama
        device-group and template/stack values to match the fw hostname creating
        a multi-tenant model of dg/stack per customer
        :param form: SimpleDemoForm
        :return: rendered html response
        """

        # get FW_NAME value from form submit
        fw_name = self.get_value_from_workflow('FW_NAME', '')

        # set stack and device-group names to fw_name
        self.save_value_to_workflow('TEMPLATE', fw_name)
        self.save_value_to_workflow('STACK', fw_name)
        self.save_value_to_workflow('DEVICE_GROUP', fw_name)

        print('set device-group and template to firewall name')

        return super().form_valid(form)