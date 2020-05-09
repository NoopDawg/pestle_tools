import pestle.sigtools.{{cookiecutter.SigToolname}} as {{cookiecutter.SigToolname}}

def {{cookiecutter.toolname}}(**kwargs):
    obj = {{cookiecutter.SigToolname}}(**kwargs)
    obj.run(**kwargs)
