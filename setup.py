import setuptools

if __name__ == "__main__":
    setuptools.setup(
        setup_requires=["setuptools_scm"], 
        install_requires=[
            "transformers==4.28.0",
            "accelerate>=0.20.3",
            "datasets>=2.6.1",
            "numpy>=1.21.6",  # "numpy >= 1.23.4",
            "pandas>=1.3.5",  # "pandas >= 1.5.1",
            "scikit_learn>=1.0.2",  # "scikit_learn >= 1.1.3",
            "torch>=1.13.0",
            "tqdm>=4.64.1",
            "shapely>=1.8.5.post1",
        ],
        include_package_data=True
    )
