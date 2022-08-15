from setuptools import setup, find_packages
import re



version = '0.0.7.9-a'



setup(name='discord-ext-owoify',
      author='Green',
      url='https://github.com/GreenDiscord/async-owoify/',
      version=version,
      packages=['owoify'],
      license='MIT',
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      download_url = 'https://github.com/GreenDiscord/async-owoify/archive/v0.0.7.9-a.tar.gz',
      description='An extension module to owoify text',
      python_requires='>=3.5.3'
)
