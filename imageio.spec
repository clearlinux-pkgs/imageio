#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : imageio
Version  : 2.9.0
Release  : 21
URL      : https://files.pythonhosted.org/packages/c3/73/f37f428748c4f10a7991ac5bff00f113a34bcc0d0a78957d6e1cdc29a94e/imageio-2.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c3/73/f37f428748c4f10a7991ac5bff00f113a34bcc0d0a78957d6e1cdc29a94e/imageio-2.9.0.tar.gz
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
[![Coverage Status](https://coveralls.io/repos/github/imageio/imageio/badge.svg?branch=master)](https://coveralls.io/github/imageio/imageio?branch=master)
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
Provides: pypi(imageio)
Requires: pypi(numpy)
Requires: pypi(pillow)

%description python3
python3 components for the imageio package.


%prep
%setup -q -n imageio-2.9.0
cd %{_builddir}/imageio-2.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594047048
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/imageio
cp %{_builddir}/imageio-2.9.0/LICENSE %{buildroot}/usr/share/package-licenses/imageio/c3f3ee58b67ca6a8d73f562dd42eda4e897eb1c0
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
/usr/share/package-licenses/imageio/c3f3ee58b67ca6a8d73f562dd42eda4e897eb1c0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
