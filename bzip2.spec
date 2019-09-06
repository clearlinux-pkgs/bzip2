Name:           bzip2
Version:        1.0.8
Release:        37
License:        BSD-3-Clause
Summary:        Data compressor
Url:            https://sourceware.org/bzip2/
Group:          utils
Source0:        https://sourceware.org/pub/bzip2/bzip2-1.0.8.tar.gz
Source1:        configure.ac
Source2:        Makefile.am
Source3:        bzip2.pc.in
BuildRequires:	autoconf automake-dev m4 gettext libtool-dev libtool
BuildRequires: gcc-dev32
BuildRequires: gcc-libgcc32
BuildRequires: gcc-libstdc++32
BuildRequires: glibc-dev32
BuildRequires: glibc-libc32

Patch1: 0001-Improve-file-access.patch
Patch2: 0002-provide-soname-compat-with-ubuntu.patch


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
Requires:       bzip2 = %{version}-%{release}

%description dev
Data compressor.

%package dev32
Summary:        Data compressor
Group:          devel
Requires:       bzip2 = %{version}-%{release}
Requires:       bzip2-lib32 = %{version}-%{release}
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
install %{SOURCE3} .
export AR=gcc-ar
export RANLIB=gcc-ranlib
export CFLAGS="$CFLAGS -fno-semantic-interposition -ffunction-sections -O3  -fPIC "
export CFLAGS2="$CFLAGS -fno-semantic-interposition -ffunction-sections -O3  -fPIC  "
export CXXFLAGS="$CXXFLAGS -fno-semantic-interposition -ffunction-sections -O3  -fPIC "
export SOURCE_DATE_EPOCH=1563382605

autoreconf -vfi
CFLAGS="$CFLAGS -fprofile-generate -fprofile-dir=pgo/ " %configure

make V=1 %{?_smp_mflags}

cp /usr/bin/x86_64-generic-linux-gcc .
LD_LIBRARY_PATH=. ./bzip2 -9 manual.ps
LD_LIBRARY_PATH=. ./bzip2 -9 configure
LD_LIBRARY_PATH=. ./bzip2 x86_64-generic-linux-gcc
LD_LIBRARY_PATH=. ./bzip2 -d manual.ps.bz2
LD_LIBRARY_PATH=. ./bzip2 -d configure.bz2
LD_LIBRARY_PATH=. ./bzip2 -d x86_64-generic-linux-gcc.bz2

rm -f bzip2 *.o
make clean

CFLAGS="$CFLAGS2 -fprofile-use -fprofile-dir=pgo/" %configure

make V=1 %{?_smp_mflags}
make -f Makefile-libbz2_so all

pushd ../build32
install %{SOURCE1} .
install %{SOURCE2} .
install %{SOURCE3} .
export CFLAGS="$CFLAGS2 -m32"
export CXXFLAGS="$CXXFLAGS2 -m32"
export LDFLAGS="$LDFLAGS2 -m32"
autoreconf -vfi
%configure --libdir=/usr/lib32  --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu

make V=1 %{?_smp_mflags}
make -f Makefile-libbz2_so all
popd



%install
pushd ../build32
%make_install32
rm -rf %{buildroot}/usr/bin
cp -a libbz2.so.1*  %{buildroot}/usr/lib32/
install -d %{buildroot}/usr/lib32/pkgconfig
sed s,@libdir@,/usr/lib32, bzip2.pc.in > %{buildroot}/usr/lib32/pkgconfig/bzip2.pc
ln -s bzip2.pc %{buildroot}/usr/lib32/pkgconfig/32bzip2.pc
popd

%make_install
cp -a libbz2.so.1*  %{buildroot}/usr/lib64/
install -d %{buildroot}/usr/lib64/pkgconfig
sed s,@libdir@,/usr/lib64, bzip2.pc.in > %{buildroot}/usr/lib64/pkgconfig/bzip2.pc

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
/usr/lib64/pkgconfig/bzip2.pc

%files dev32
/usr/include/bzlib.h
/usr/lib32/libbz2.so
/usr/lib32/pkgconfig/32bzip2.pc
/usr/lib32/pkgconfig/bzip2.pc

%files doc
/usr/share/man/man1/bzegrep.1
/usr/share/man/man1/bzdiff.1
/usr/share/man/man1/bzcmp.1
/usr/share/man/man1/bzfgrep.1
/usr/share/man/man1/bzmore.1
/usr/share/man/man1/bzip2.1
/usr/share/man/man1/bzgrep.1
/usr/share/man/man1/bzless.1
