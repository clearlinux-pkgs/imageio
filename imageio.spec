#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : imageio
Version  : 2.12.0
Release  : 33
URL      : https://files.pythonhosted.org/packages/1b/e5/db19af2818becf3fc825f78a9859234566844d324c22d35eed0a9ff29462/imageio-2.12.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/1b/e5/db19af2818becf3fc825f78a9859234566844d324c22d35eed0a9ff29462/imageio-2.12.0.tar.gz
Summary  : Library for reading and writing a wide range of image, video, scientific, and volumetric data formats.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: imageio-bin = %{version}-%{release}
Requires: imageio-license = %{version}-%{release}
Requires: imageio-python = %{version}-%{release}
Requires: imageio-python3 = %{version}-%{release}
BuildRequires : Pillow
BuildRequires : buildreq-distutils3
BuildRequires : pypi(numpy)
BuildRequires : pypi(pillow)

%description
# IMAGEIO
[![CI](https://github.com/imageio/imageio/workflows/CI/badge.svg)](https://github.com/imageio/imageio/actions/workflows/ci.yml)
[![CD](https://github.com/imageio/imageio/workflows/CD/badge.svg)](https://github.com/imageio/imageio/actions/workflows/cd.yml)
[![codecov](https://codecov.io/gh/imageio/imageio/branch/master/graph/badge.svg?token=81Zhu9MDec)](https://codecov.io/gh/imageio/imageio)
[![Docs](https://readthedocs.org/projects/imageio/badge/?version=latest)](https://imageio.readthedocs.io)

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
%setup -q -n imageio-2.12.0
cd %{_builddir}/imageio-2.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637766563
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/imageio
cp %{_builddir}/imageio-2.12.0/LICENSE %{buildroot}/usr/share/package-licenses/imageio/c3f3ee58b67ca6a8d73f562dd42eda4e897eb1c0
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
