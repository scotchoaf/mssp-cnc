
from pan_cnc.views import CNCBaseAuth, CNCBaseFormView, ProvisionSnippetView


class gsbProvisionView(ProvisionSnippetView):
    def generate_dynamic_form(self):

        simple_service = self.get_value_from_workflow('simple_service', '')
        print('simple service is ' + simple_service)
        if simple_service == 'True':
            print('only showing device name field')
            self.fields_to_render += ['FW_NAME']

        # save local workflow data to jinja context for template render
        self.save_workflow_to_session()

        return super().generate_dynamic_form()


class gsbWorkflow02(ProvisionSnippetView):


    def generate_dynamic_form(self):

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
        Called when the simple demo form is submitted
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