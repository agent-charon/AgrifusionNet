from setuptools import setup, find_packages

setup(
    name='agri_fusion_net',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='Implementation of AgriFusionNet for precision agriculture.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='<your_repo_url>', # Replace with your repository URL
    packages=find_packages(exclude=["tests*", "data*", "docs*"]),
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', # Or your chosen license
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.8',
)