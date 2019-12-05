#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : imageio
Version  : 2.6.1
Release  : 7
URL      : https://files.pythonhosted.org/packages/0d/07/4d4c7768f3b88d90a999d81ca6852b9c2d38e87d47aab6d64de432293973/imageio-2.6.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/0d/07/4d4c7768f3b88d90a999d81ca6852b9c2d38e87d47aab6d64de432293973/imageio-2.6.1.tar.gz
Summary  : Library for reading and writing a wide range of image, video, scientific, and volumetric data formats.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: imageio-bin = %{version}-%{release}
Requires: imageio-license = %{version}-%{release}
Requires: imageio-python = %{version}-%{release}
Requires: imageio-python3 = %{version}-%{release}
Requires: Pillow
Requires: numpy
BuildRequires : Pillow
BuildRequires : buildreq-distutils3
BuildRequires : numpy

%description
# IMAGEIO
[![PyPI Version](https://img.shields.io/pypi/v/imageio.svg)](https://pypi.python.org/pypi/imageio/)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/imageio.svg)](https://pypi.python.org/pypi/imageio/)
[![Build Status](https://travis-ci.org/imageio/imageio.svg?branch=master)](https://travis-ci.org/imageio/imageio)
[![Coverage Status](https://coveralls.io/repos/imageio/imageio/badge.png?branch=master)](https://coveralls.io/r/imageio/imageio?branch=master)
[![Documentation Status](https://readthedocs.org/projects/imageio/badge/?version=latest)](https://imageio.readthedocs.io)
[![PyPi Download stats](http://pepy.tech/badge/imageio)](http://pepy.tech/project/imageio)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1488561.svg)](https://doi.org/10.5281/zenodo.1488561)

%package bin
Summary: bin components for the imageio package.
Group: Binaries
Requires: imageio-license = %{version}-%{release}

%description bin
bin components for the imageio package.


%package license
Summary: license components for the imageio package.
Group: Default

%description license
license components for the imageio package.


%package python
Summary: python components for the imageio package.
Group: Default
Requires: imageio-python3 = %{version}-%{release}

%description python
python components for the imageio package.


%package python3
Summary: python3 components for the imageio package.
Group: Default
Requires: python3-core

%description python3
python3 components for the imageio package.


%prep
%setup -q -n imageio-2.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570907194
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/imageio
cp LICENSE %{buildroot}/usr/share/package-licenses/imageio/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/imageio_download_bin
/usr/bin/imageio_remove_bin

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/imageio/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
