CryptoRL is developed on Python, user need Python and NumPy as prerequisites.

Run ```git clone https://github.com/ZiyiXia/CryptoRL.git``` to clone CryptoRL to your local directory.

Dependencies include: 
    "black>=22",
    "bump2version>=1.0.0",
    "check-manifest",
    "flake8>=3.7.8",
    "flake8-black>=0.2.1",
    "flake8-pyproject",
    "mypy",
    "pytest>=4.3.0",
    "pytest-cov>=2.6.1",
    "twine",
    "wheel",
    "numpy",
    "pandas",
    "gym",
    "Historic-Crypto"

Make sure you run ```make lint```, ```make format``` before opening a PR.

If you add new features, please add corresponding tests in ./cryptorl/tests