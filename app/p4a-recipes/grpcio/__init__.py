import logging
logging.getLogger('p4a').setLevel(logging.DEBUG)

from pythonforandroid.recipe import PythonRecipe


class GrpcioRecipe(PythonRecipe):
    version = '1.20.1'
    url = 'https://pypi.python.org/packages/source/g/grpcio/grpcio-{version}.tar.gz'
    call_hostpython_via_targetpython = False
    depends = ['setuptools']

    def get_recipe_env(self, arch):
        logging.getLogger('p4a').setLevel(logging.DEBUG)
        env = super(GrpcioRecipe, self).get_recipe_env(arch)
        env['TARGET_OS'] = 'OS_ANDROID_CROSSCOMPILE'
        env['CFLAGS'] += (
            ' -I' + self.ctx.ndk_dir + '/platforms/android-' + str(
                self.ctx.android_api) + '/arch-' + arch.arch.replace(
                    'eabi', '') + '/usr/include' + ' -I' + self.ctx.ndk_dir +
            '/sources/cxx-stl/gnu-libstdc++/' + self.ctx.toolchain_version +
            '/include' + ' -I' + self.ctx.ndk_dir +
            '/sources/cxx-stl/gnu-libstdc++/' + self.ctx.toolchain_version +
            '/libs/' + arch.arch + '/include')
        env['CFLAGS'] += ' -std=gnu++11'
        env['CXXFLAGS'] = env['CFLAGS']
        env['CXXFLAGS'] += ' -frtti'
        env['CXXFLAGS'] += ' -fexceptions'
        env['LDFLAGS'] += (
            ' -L' + self.ctx.ndk_dir + '/sources/cxx-stl/gnu-libstdc++/' +
            self.ctx.toolchain_version + '/libs/' + arch.arch)
        env['LDFLAGS'] += (
            ' -L' + self.ctx.ndk_dir + '/android-27/arch-arm/usr/lib')
        env['LIBS'] = env.get('LIBS', '') + ' -lgnustl_shared -landroid -llog'

        print("NEONSKY_DEBUG")
        print(env)
        print("NEONSKY_DEBUG")
        logging.getLogger('p4a').setLevel(logging.DEBUG)
        return env


recipe = GrpcioRecipe()
