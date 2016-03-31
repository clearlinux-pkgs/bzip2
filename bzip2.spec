Name:           bzip2
Version:        1.0.6
Release:        17
License:        bzip2-1.0.6
Summary:        Data compressor
Url:            http://www.bzip.org/
Group:          utils
Source0:        http://www.bzip.org/1.0.6/bzip2-1.0.6.tar.gz
Source1:        configure.ac
Source2:        Makefile.am
BuildRequires:	autoconf automake-dev m4 gettext libtool-dev libtool

Patch1: fasterfile.patch

%description
Data compressor.

%package lib
Summary:        Data compressor
Group:          lib

%description lib
Data compressor.

%package dev
Summary:        Data compressor
Group:          devel
Requires:       %{name} = %{version}-%{release}

%description dev
Data compressor.


%package doc
Summary:        Data compressor
Group:          doc

%description doc
Data compressor.


%prep
%setup -q

%patch1 -p1

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



%install
%make_install

%files
%{_bindir}/bzless
%{_bindir}/bzcat
%{_bindir}/bzcmp
%{_bindir}/bzip2recover
%{_bindir}/bzgrep
%{_bindir}/bzdiff
%{_bindir}/bzegrep
%{_bindir}/bunzip2
%{_bindir}/bzmore
%{_bindir}/bzip2
%{_bindir}/bzfgrep

%files lib
%{_libdir}/libbz2.so.*

%files dev
%{_includedir}/bzlib.h
%{_libdir}/libbz2.so

%files doc
%{_mandir}/man1/bzegrep.1
%{_mandir}/man1/bzdiff.1
%{_mandir}/man1/bzcmp.1
%{_mandir}/man1/bzfgrep.1
%{_mandir}/man1/bzmore.1
%{_mandir}/man1/bzip2.1
%{_mandir}/man1/bzgrep.1
%{_mandir}/man1/bzless.1
