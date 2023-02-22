Name: libsafe-iop
Version: 1.0
Release: r0
Summary: Safe integer operation library for C.

License: ISC

URL: https://www.codelinaro.org/
#Source0: libsafe-iop-1.0.tar.gz
Source0: %{name}-%{version}.tar.gz

BuildRequires: autoconf automake libtool gcc-g++

%description
This library supplies a set of standard functions for performing
and checking safe integer operations.

%package dev
Summary: Safe integer operation library for C - Development files
License: ISC
Requires: %{name} = %{version}-%{release}

%description dev
This library supplies a set of standard functions for performing
and checking safe integer operations  This package contains
symbolic links, header files, and related items necessary
for software development.

%prep
%setup -n safe-iop

%build
autoreconf -if
%configure
%make_build

%install
%make_install

%files
%{_libdir}/libsafe_iop.a
%{_libdir}/libsafe_iop.la
%{_libdir}/libsafe_iop.so.0
%{_libdir}/libsafe_iop.so.0.0.0

%files dev
%{_includedir}/safe_iop.h
%{_libdir}/libsafe_iop.so
