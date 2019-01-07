
from pan_cnc.views import CNCBaseAuth, CNCBaseFormView, ProvisionSnippetView


class gsbProvisionView(ProvisionSnippetView):
    def generate_dynamic_form(self):

        simple_service = self.get_value_from_workflow('simple_service', '')

        if simple_service == 'True':
            print('only showing device name field')
            self.fields_to_render += ['FW_NAME']

        # save local workflow data to jinja context for template render
        self.save_workflow_to_session()

        return super().generate_dynamic_form()