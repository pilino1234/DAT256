from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class GrpcioRecipe(CompiledComponentsPythonRecipe):
    version = '1.20.1'
    url = 'https://pypi.python.org/packages/source/g/grpcio/grpcio-{version}.tar.gz'
    depends = ['setuptools']


recipe = GrpcioRecipe()
