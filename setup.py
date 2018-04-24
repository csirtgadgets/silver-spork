import os
from setuptools import setup, find_packages
import versioneer
import sys

# vagrant doesn't appreciate hard-linking
if os.environ.get('USER') == 'vagrant' or os.path.isdir('/vagrant'):
    del os.link

# https://www.pydanny.com/python-dot-py-tricks.html
if sys.argv[-1] == 'test':
    test_requirements = [
        'pytest',
        'coverage',
        'pytest_cov',
    ]
    try:
        modules = map(__import__, test_requirements)
    except ImportError as e:
        err_msg = e.message.replace("No module named ", "")
        msg = "%s is not installed. Install your test requirments." % err_msg
        raise ImportError(msg)
    r = os.system('py.test test -v --cov=csirtg_predict_api --cov-fail-under=50')
    if r == 0:
        sys.exit()
    else:
        raise RuntimeError('tests failed')


data_files = [
    'data/whitelist.txt',
]

package_data = {}

setup(
    name="csirtg_predict_api",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="CSIRTG Predict REST API Framework",
    long_description="The FASTEST way to deploy a REST Prediction API",
    url="https://github.com/csirtgadgets/csirtg_predict_api",
    license='MPL2',
    data_files=[('csirtg_predict_api/data', data_files)],
    package_data=package_data,
    keywords=['network', 'security'],
    author="Wes Young",
    author_email="wes@csirtgadgets.com",
    packages=find_packages(),
    install_requires=[
        'csirtg_indicator',
        'csirtg_mail',
        'csirtg_urlsml',
        'csirtg_domainsml',
        'csirtg_ipsml',
        'Flask',
        'flask-restplus',
    ],
    entry_points={
       'console_scripts': [
           'csirtg-predictd=csirtg_predict_api:main'
       ]
    },
)
