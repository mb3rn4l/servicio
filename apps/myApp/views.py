import pandas as pd

from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoadFile


class ProcessFile(generic.base.TemplateView):
    """
    porcesa archivo en excel
    """
    supported_extension = 'xlsx'
    template_name = 'uploadFile.html'

    def get_context_data(self, **kwargs):
        context = super(ProcessFile, self).get_context_data(**kwargs)
        context['form'] = LoadFile(self.request.GET or None)
        return context

    def post(self, request, *args, **kwargs):
        form = LoadFile(request.POST or None, request.FILES or None)
        if form.is_valid():
            sb_file_name = request.FILES['process_file'].name
            if sb_file_name.lower().endswith(self.supported_extension):
                df = pd.read_excel(request.FILES['process_file'])

                new_df = df.groupby(['CANDIDATO', 'PARTIDO', 'PUESTO', 'MPIO', 'DEPTO'])

                response = HttpResponse(content_type='application/ms-excel')
                response['Content-Disposition'] = 'attachment; filename="respuesta.xlsx"'
                writer = pd.ExcelWriter(response, engine='xlsxwriter')
                new_df.to_excel(writer, sheet_name='Sheet1')
                workbook = writer.book
                worksheet = writer.sheets['Sheet1']
                worksheet.set_column(1, 40, 24)
                writer.save()

                return response
        else:
            parameters = {
                'form': form
            }
            return render(request, self.template_name, parameters)
