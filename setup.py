from setuptools import setup, find_packages
import re



version = 'v0.4.0a'



setup(name='async-owoify',
      author='Green',
      url='https://github.com/GreenDiscord/async-owoify/',
      version=version,
      packages=['owoify'],
      license='MIT',
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      download_url = 'https://github.com/GreenDiscord/async-owoify/releases/download/v0.4.0-alpha/async-owoify-0.4.0a0.tar.gz',
      description='An extension module to owoify text',
      python_requires='>=3.5.3'
)
