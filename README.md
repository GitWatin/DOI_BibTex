<h1 align="center">
  🚀 CLI BibTex Generator using DOI API 🖥️</br>
</h1>

<p align="center">
  <a href="#">
    <img src="https://img.shields.io/github/license/GitWatin/DOI_BibTex" alt="Licence">
  </a>


  <a href="https://www.paypal.me/valentindenis  " target="blank">
    <img src="https://img.shields.io/badge/Donate-PayPal-green.svg" alt="Donate">
  </a>
  </br>
  </br>
  <a href="mailto:github@valdenis.be">
    <img src="https://img.shields.io/badge/Contact%20me-github%40valdenis.be-informational" alt="ContactMe">
  </a>
<p>

---

## Disclaimer ⚠️

The doi.org API is quite unstable and can take up to 10 seconds to return a result.

At times it may appear inaccessible, just wait a few moment.



## Requirements

✔️ Compiler : Python 3.9

#### Pip install

```bash
pip install requests calendar pyperclip
```

## Utilisation

This script directly retrieves the metadata of an article using the API of www.doi.org

Just start the script and paste the url when asked
Once the script is finished, the text is copied directly into the clipboard

### Output : 

```bash
D:\>python -u main.py
Enter DOI Number Only URL
https://doi.org/10.1145/1376616.1376723
[INFO - 17/04/2021 19:00:22] : Wait for DOI Lookup
[INFO - 17/04/2021 19:00:23] : HTTP Status Code :200
[INFO - 17/04/2021 19:00:23] : BibTex copy to your clipboard

```

```latex

@misc{10.1145_6_2008,
author={Lee, Sang-Won and Moon, Bongki and Park, Chanik and Kim, Jae-Myung and Kim, Sang-Woo},
title={A case for flash memory ssd in enterprise database applications},
howpublished={\url{http://dx.doi.org/10.1145/1376616.1376723} },
month={juin},
year={2008},
note={ [En Ligne] - consulté le 17 avril 2021 }}
```
