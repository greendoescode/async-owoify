[![License](https://img.shields.io/github/license/GreenDiscord/async-owoify)](https://mit-license.org/) ![version](https://img.shields.io/pypi/v/async-owoify)

### async-owoify
Simple ext package for owoifing text.

### Install
Simple paste this into your terminal

- ```shell script
  pip install async-owoify
  ```

If you need to **update** please use the following:

- ```shell script
  pip install --upgrade async-owoify
  ```

### Simple Use
Firstly, import the package using

- ```python
  import owoify
  ```

Now, lets use the ```owoify.owoify()``` attribute to **owoify** your text!

- ```python
  import owoify

  print(owoify.owoify("TEXT"))

  ```

Wanna decode this now? Use the ```owoify.decode()``` attribute for this module.
- ```python
  import owoify
  
  print(owoify.decode("TEXT"))
  ```
  
  Note: The decode attribute is still in dev, as i need to find all words that would get owoified :) 
  
  
### Devlepoment version

To install this, you need to install from the github

- ```shell script
  pip install -U git+https://github.com/GreenDiscord/async-owoify
  ```
Thanks! Please give feedback in issues :)
