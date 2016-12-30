Name:           bzip2
Version:        1.0.6
Release:        22
License:        bzip2-1.0.6
Summary:        Data compressor
Url:            http://www.bzip.org/
Group:          utils
Source0:        http://www.bzip.org/1.0.6/bzip2-1.0.6.tar.gz
Source1:        configure.ac
Source2:        Makefile.am
BuildRequires:	autoconf automake-dev m4 gettext libtool-dev libtool
BuildRequires: gcc-dev32
BuildRequires: gcc-libgcc32
BuildRequires: gcc-libstdc++32
BuildRequires: glibc-dev32
BuildRequires: glibc-libc32

Patch1: fasterfile.patch
Patch2: cve-2016-3189.patch

%description
Data compressor.

%package lib
Summary:        Data compressor
Group:          lib

%description lib
Data compressor.

%package lib32
Summary:        Data compressor
Group:          lib

%description lib32
Data compressor.

%package dev
Summary:        Data compressor
Group:          devel
Requires:       %{name} = %{version}-%{release}

%description dev
Data compressor.

%package dev32
Summary:        Data compressor
Group:          devel
Requires:       %{name} = %{version}-%{release}
Requires: bzip2-dev

%description dev32
Data compressor.


%package doc
Summary:        Data compressor
Group:          doc

%description doc
Data compressor.


%prep
%setup -q

%patch1 -p1
%patch2 -p1

pushd ..
cp -a bzip2-%{version} build32
popd

%build
install %{SOURCE1} .
install %{SOURCE2} .
export AR=gcc-ar
export RANLIB=gcc-ranlib
export CFLAGS="$CFLAGS -fno-semantic-interposition -ffunction-sections -O3 -flto "
export CFLAGS2="$CFLAGS -fno-semantic-interposition -ffunction-sections -O3 -flto "
export CXXFLAGS="$CXXFLAGS -fno-semantic-interposition -ffunction-sections -O3 -flto "

autoreconf -vfi
CFLAGS="$CFLAGS -fprofile-generate -fprofile-dir=pgo/ " %configure

make V=1 %{?_smp_mflags}
./bzip2 -9 manual.ps
./bzip2 -d manual.ps.bz2

rm -f bzip2 *.o
make clean

CFLAGS="$CFLAGS2 -fprofile-use -fprofile-dir=pgo/" %configure

make V=1 %{?_smp_mflags}

pushd ../build32
install %{SOURCE1} .
install %{SOURCE2} .
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
autoreconf -vfi
%configure --libdir=/usr/lib32  --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu

make V=1 %{?_smp_mflags}
popd



%install
pushd ../build32
%make_install32
rm -rf %{buildroot}/usr/bin
popd

%make_install

%files
/usr/bin/bzless
/usr/bin/bzcat
/usr/bin/bzcmp
/usr/bin/bzip2recover
/usr/bin/bzgrep
/usr/bin/bzdiff
/usr/bin/bzegrep
/usr/bin/bunzip2
/usr/bin/bzmore
/usr/bin/bzip2
/usr/bin/bzfgrep

%files lib
/usr/lib64/libbz2.so.*

%files lib32
/usr/lib32/libbz2.so.*

%files dev
/usr/include/bzlib.h
/usr/lib64/libbz2.so

%files dev32
/usr/include/bzlib.h
/usr/lib32/libbz2.so

%files doc
%{_mandir}/man1/bzegrep.1
%{_mandir}/man1/bzdiff.1
%{_mandir}/man1/bzcmp.1
%{_mandir}/man1/bzfgrep.1
%{_mandir}/man1/bzmore.1
%{_mandir}/man1/bzip2.1
%{_mandir}/man1/bzgrep.1
%{_mandir}/man1/bzless.1
