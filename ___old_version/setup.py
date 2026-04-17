from distutils.core import setup

setup(
    name='cetico-dev',
    version='2.8.9',
    packages=['data.libs.exifread', 'data.libs.exifread.tags', 'data.libs.exifread.tags.makernote',
              'data.libs.reportlab', 'data.libs.reportlab.lib', 'data.libs.reportlab.pdfgen',
              'data.libs.reportlab.pdfbase', 'data.libs.reportlab.graphics', 'data.libs.reportlab.graphics.charts',
              'data.libs.reportlab.graphics.barcode', 'data.libs.reportlab.graphics.samples',
              'data.libs.reportlab.graphics.widgets', 'data.libs.reportlab.platypus'],
    url='https://github.com/FBSLikan/Cetico-TCC',
    license='',
    author='Fausto Biazzi de Sousa',
    author_email='fausto@biazzitech.com.br',
    description=''
)
