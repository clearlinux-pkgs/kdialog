#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kdialog
Version  : 19.08.2
Release  : 14
URL      : https://download.kde.org/stable/applications/19.08.2/src/kdialog-19.08.2.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.2/src/kdialog-19.08.2.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.2/src/kdialog-19.08.2.tar.xz.sig
Summary  : A utility for displaying dialog boxes from shell scripts
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0
Requires: kdialog-bin = %{version}-%{release}
Requires: kdialog-data = %{version}-%{release}
Requires: kdialog-license = %{version}-%{release}
Requires: kdialog-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev

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
%setup -q -n kdialog-19.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570742233
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1570742233
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdialog
cp COPYING %{buildroot}/usr/share/package-licenses/kdialog/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/kdialog/COPYING.DOC
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
/usr/share/package-licenses/kdialog/COPYING
/usr/share/package-licenses/kdialog/COPYING.DOC

%files locales -f kdialog.lang
%defattr(-,root,root,-)

