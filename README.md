# Metas bonos



## Install Python


```
export VERSION="3.7.0"
xcode-select --install
brew update
brew upgrade
brew install zlib
brew reinstall zlib
export LDFLAGS="-L/usr/local/opt/zlib/lib"
export CPPFLAGS="-I/usr/local/opt/zlib/include"
export PYTHON_CONFIGURE_OPTS="--enable-unicode=ucs4"
pyenv install $VERSION
pyenv virtualenv $VERSION metas_bonos
pyenv activate metas_bonos
python --version 
```


## Execute code

```
git clone git@github.com:eduardolujan/metas_bonos.git
cd metas_bonos 
python src/main.py
```
