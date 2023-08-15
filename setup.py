import setuptools

if __name__ == "__main__":
    setuptools.setup(
        setup_requires=["setuptools_scm"], 
        install_requires=[
            "transformers==4.28.0",
            "accelerate"
        ],
        include_package_data=True
    )
