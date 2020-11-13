#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xFC57E3CCACD99A78 (mjw@gnu.org)
#
Name     : bzip2
Version  : 1.0.8
Release  : 57
URL      : https://sourceware.org/pub/bzip2/bzip2-1.0.8.tar.gz
Source0  : https://sourceware.org/pub/bzip2/bzip2-1.0.8.tar.gz
Source1  : https://sourceware.org/pub/bzip2/bzip2-1.0.8.tar.gz.sig
Summary  : Data compressor
Group    : Development/Tools
License  : bzip2-1.0.6
Requires: bzip2-bin = %{version}-%{release}
Requires: bzip2-lib = %{version}-%{release}
Requires: bzip2-license = %{version}-%{release}
Requires: bzip2-man = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : patchelf
Patch1: 0001-Autotoolize-bzip2.patch
Patch2: 0002-Improve-file-access.patch
Patch3: 0003-libbz2-add-0.0-compat-library.patch

%description
This version is fully compatible with the previous public releases.
------------------------------------------------------------------
This file is part of bzip2/libbzip2, a program and library for
lossless, block-sorting data compression.

%package bin
Summary: bin components for the bzip2 package.
Group: Binaries
Requires: bzip2-license = %{version}-%{release}

%description bin
bin components for the bzip2 package.


%package dev
Summary: dev components for the bzip2 package.
Group: Development
Requires: bzip2-lib = %{version}-%{release}
Requires: bzip2-bin = %{version}-%{release}
Provides: bzip2-devel = %{version}-%{release}
Requires: bzip2 = %{version}-%{release}

%description dev
dev components for the bzip2 package.


%package dev32
Summary: dev32 components for the bzip2 package.
Group: Default
Requires: bzip2-lib32 = %{version}-%{release}
Requires: bzip2-bin = %{version}-%{release}
Requires: bzip2-dev = %{version}-%{release}

%description dev32
dev32 components for the bzip2 package.


%package lib
Summary: lib components for the bzip2 package.
Group: Libraries
Requires: bzip2-license = %{version}-%{release}

%description lib
lib components for the bzip2 package.


%package lib32
Summary: lib32 components for the bzip2 package.
Group: Default
Requires: bzip2-license = %{version}-%{release}

%description lib32
lib32 components for the bzip2 package.


%package license
Summary: license components for the bzip2 package.
Group: Default

%description license
license components for the bzip2 package.


%package man
Summary: man components for the bzip2 package.
Group: Default

%description man
man components for the bzip2 package.


%prep
%setup -q -n bzip2-1.0.8
cd %{_builddir}/bzip2-1.0.8
%patch1 -p1
%patch2 -p1
%patch3 -p1
pushd ..
cp -a bzip2-1.0.8 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605311581
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export CFLAGS_GENERATE="$CFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$FCFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$FFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CXXFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export LDFLAGS_GENERATE="$LDFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CFLAGS_USE="$CFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FCFLAGS_USE="$FCFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FFLAGS_USE="$FFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export CXXFLAGS_USE="$CXXFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export LDFLAGS_USE="$LDFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
CFLAGS="${CFLAGS_GENERATE}" CXXFLAGS="${CXXFLAGS_GENERATE}" FFLAGS="${FFLAGS_GENERATE}" FCFLAGS="${FCFLAGS_GENERATE}" LDFLAGS="${LDFLAGS_GENERATE}" %reconfigure --disable-static
make  %{?_smp_mflags}

cp /usr/bin/x86_64-generic-linux-gcc .
LD_LIBRARY_PATH=. ./bzip2 -9 manual.ps
LD_LIBRARY_PATH=. ./bzip2 -9 configure
LD_LIBRARY_PATH=. ./bzip2 x86_64-generic-linux-gcc
LD_LIBRARY_PATH=. ./bzip2 -d manual.ps.bz2
LD_LIBRARY_PATH=. ./bzip2 -d configure.bz2
LD_LIBRARY_PATH=. ./bzip2 -d x86_64-generic-linux-gcc.bz2
make clean
CFLAGS="${CFLAGS_USE}" CXXFLAGS="${CXXFLAGS_USE}" FFLAGS="${FFLAGS_USE}" FCFLAGS="${FCFLAGS_USE}" LDFLAGS="${LDFLAGS_USE}" %reconfigure --disable-static
make  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%reconfigure --disable-static   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1605311581
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bzip2
cp %{_builddir}/bzip2-1.0.8/LICENSE %{buildroot}/usr/share/package-licenses/bzip2/ddf157bc55ed6dec9541e4af796294d666cd0926
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
## install_append content
# fix SONAME so all dependent libraries are happy with this
for curr in 32 64; do
rm -f %{buildroot}/usr/lib${curr}/libbz2-compat.so
rm -f %{buildroot}/usr/lib${curr}/libbz2-compat.so.0
rm -f %{buildroot}/usr/lib${curr}/libbz2.so.1
mv %{buildroot}/usr/lib${curr}/libbz2-compat.so.0.0.0 %{buildroot}/usr/lib${curr}/libbz2.so.0.0.0
ln -sf libbz2.so.0.0.0 %{buildroot}/usr/lib${curr}/libbz2.so.0
ln -sf libbz2.so.1.0.0 %{buildroot}/usr/lib${curr}/libbz2.so.1
ln -sf libbz2.so.1.0.0 %{buildroot}/usr/lib${curr}/libbz2.so.1.0
ln -sf libbz2.so.1.0.0 %{buildroot}/usr/lib${curr}/libbz2.so.%{version}
rm -f %{buildroot}/usr/lib${curr}/libbz2-compat.so*
done
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bunzip2
/usr/bin/bzcat
/usr/bin/bzcmp
/usr/bin/bzdiff
/usr/bin/bzegrep
/usr/bin/bzfgrep
/usr/bin/bzgrep
/usr/bin/bzip2
/usr/bin/bzip2recover
/usr/bin/bzless
/usr/bin/bzmore

%files dev
%defattr(-,root,root,-)
/usr/include/bzlib.h
/usr/lib64/libbz2.so
/usr/lib64/pkgconfig/bzip2.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libbz2.so
/usr/lib32/pkgconfig/32bzip2.pc
/usr/lib32/pkgconfig/bzip2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbz2.so.0
/usr/lib64/libbz2.so.0.0.0
/usr/lib64/libbz2.so.1
/usr/lib64/libbz2.so.1.0
/usr/lib64/libbz2.so.1.0.0
/usr/lib64/libbz2.so.1.0.8

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libbz2.so.0
/usr/lib32/libbz2.so.0.0.0
/usr/lib32/libbz2.so.1
/usr/lib32/libbz2.so.1.0
/usr/lib32/libbz2.so.1.0.0
/usr/lib32/libbz2.so.1.0.8

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bzip2/ddf157bc55ed6dec9541e4af796294d666cd0926

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/bzcmp.1
/usr/share/man/man1/bzdiff.1
/usr/share/man/man1/bzegrep.1
/usr/share/man/man1/bzfgrep.1
/usr/share/man/man1/bzgrep.1
/usr/share/man/man1/bzip2.1
/usr/share/man/man1/bzless.1
/usr/share/man/man1/bzmore.1
