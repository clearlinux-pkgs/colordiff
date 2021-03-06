#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x45E1E473378BB197 (davee@sungate.co.uk)
#
Name     : colordiff
Version  : 1.0.19
Release  : 2
URL      : https://www.colordiff.org/colordiff-1.0.19.tar.gz
Source0  : https://www.colordiff.org/colordiff-1.0.19.tar.gz
Source1  : https://www.colordiff.org/colordiff-1.0.19.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: colordiff-license = %{version}-%{release}
BuildRequires : docbook-xml
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : lynx
BuildRequires : xmlto

%description
Name
colordiff — a tool to colorize diff output
Synopsis
colordiff [diff options] [colordiff options] {file1} {file2}

%package license
Summary: license components for the colordiff package.
Group: Default

%description license
license components for the colordiff package.


%prep
%setup -q -n colordiff-1.0.19
cd %{_builddir}/colordiff-1.0.19

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587399901
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1587399901
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/colordiff
cp %{_builddir}/colordiff-1.0.19/COPYING %{buildroot}/usr/share/package-licenses/colordiff/4cc77b90af91e615a64ae04893fdffa7939db84c
%make_install

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/colordiff/4cc77b90af91e615a64ae04893fdffa7939db84c
