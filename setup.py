from setuptools import setup, find_packages

# Leia a versão de __init__.py ou defina aqui
version = '1.0.0'

setup(
    name='snapfix',
    version=version,
    description='Organize Snap .desktop entries automatically',
    author='Seu Nome',
    author_email='seu.email@example.com',
    url='https://github.com/SEU-USUARIO/snapfix',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        # deep-translator é opcional; você pode usar extras_require
    ],
    extras_require={
        'translate': ['deep-translator'],
    },
    entry_points={
        'console_scripts': [
            'snapfix=snapfix.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
    ],
    include_package_data=True,
    zip_safe=False,
)
