from cookiecutter.main import cookiecutter
import os
import datetime
from utils.pestlepath import pestlepath

class SigToolify():
    def __init__(self):
        SigToolPackage = 'pestle.sigtools'

    def new(self):
        pestle_path = pestlepath()
        print(pestle_path)
        template_path = os.path.join(pestle_path, 'pestle/base/SigToolify/templates/SigToolTemplate/')
        print(template_path)
        today = datetime.datetime.today()
        date = today.date().isoformat()
        year = today.year

        extra_context = {
                'release_date': date
                }
        cookiecutter(template_path,
                     output_dir=os.path.join(pestle_path, 'pestle', 'sigtools'),
                     extra_context=extra_context)


