from setuptools import setup

setup(
    name='texttospeech-server',
    packages=['ttsapi'],
    include_package_data=True,
    install_requires=[
        'falcon',
        'google-cloud-texttospeech',
        'python-slugify',
    ]
)