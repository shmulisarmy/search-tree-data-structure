from setuptools import setup, find_packages

# Read the README file for long description (optional but recommended)
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="your-package-name",  # Replace with your package name
    version="0.1.0",  # Replace with your package version
    author="Your Name",  # Replace with your name
    author_email="shmulikeller@gmail.com",  # Replace with your email
    description="A short description of your package",  # Short package description
    long_description=long_description,  # Use the content of README.md for the long description
    long_description_content_type="text/markdown",  # The format of the long description
    url="https://github.com/shmulisarmy/search-tree-data-structure",  # Replace with your GitHub repo URL
    packages=find_packages(),  # Automatically find and include your packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # You can change this to your license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
    install_requires=[
        # List your package's dependencies here
        "numpy>=1.21.0",
        "requests>=2.25.0",
    ],
    entry_points={
        'console_scripts': [
            # Define command-line scripts here (if applicable)
            # 'your-command = your_package.module:main_function',
        ],
    },
)
