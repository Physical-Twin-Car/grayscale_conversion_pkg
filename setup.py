from setuptools import setup

package_name = 'grayscale_conversion_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email',
    description='Package to convert images to grayscale',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'grayscale_node = grayscale_conversion_pkg.grayscale_node:main',
        ],
    },
)
