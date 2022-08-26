#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kdialog
Version  : 22.08.0
Release  : 44
URL      : https://download.kde.org/stable/release-service/22.08.0/src/kdialog-22.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.08.0/src/kdialog-22.08.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0
Requires: kdialog-bin = %{version}-%{release}
Requires: kdialog-data = %{version}-%{release}
Requires: kdialog-license = %{version}-%{release}
Requires: kdialog-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev

%description
kdialog allows you to display dialog boxes from shell scripts.
The syntax is very much inspired from the "dialog" command
(which shows text mode dialogs).

%package bin
Summary: bin components for the kdialog package.
Group: Binaries
Requires: kdialog-data = %{version}-%{release}
Requires: kdialog-license = %{version}-%{release}

%description bin
bin components for the kdialog package.


%package data
Summary: data components for the kdialog package.
Group: Data

%description data
data components for the kdialog package.


%package license
Summary: license components for the kdialog package.
Group: Default

%description license
license components for the kdialog package.


%package locales
Summary: locales components for the kdialog package.
Group: Default

%description locales
locales components for the kdialog package.


%prep
%setup -q -n kdialog-22.08.0
cd %{_builddir}/kdialog-22.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661551984
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1661551984
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdialog
cp %{_builddir}/kdialog-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/kdialog/e1d31e42d2a477d6def889000aa8ffc251f2354c || :
cp %{_builddir}/kdialog-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdialog/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
pushd clr-build
%make_install
popd
%find_lang kdialog

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kdialog
/usr/bin/kdialog_progress_helper

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/org.kde.kdialog.ProgressDialog.xml
/usr/share/metainfo/org.kde.kdialog.metainfo.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdialog/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kdialog/e1d31e42d2a477d6def889000aa8ffc251f2354c

%files locales -f kdialog.lang
%defattr(-,root,root,-)

