#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	C++ wrappers for libgnome
Summary(pl.UTF-8):	Interfejsy C++ dla libgnome
Name:		libgnomemm
Version:	2.30.0
Release:	12
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgnomemm/2.30/%{name}-%{version}.tar.bz2
# Source0-md5:	860f5e835cd4674393ffdd692b0c9147
URL:		https://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtkmm-devel >= 2.12.0
BuildRequires:	libgnome-devel >= 2.20.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	m4
BuildRequires:	pkgconfig
Requires:	libgnome >= 2.20.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libgnome.

%description -l pl.UTF-8
Interfejsy C++ dla libgnome.

%package devel
Summary:	Devel files for libgnomemm
Summary(pl.UTF-8):	Pliki nagłówkowe dla libgnomemm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtkmm-devel >= 2.12.0
Requires:	libgnome-devel >= 2.20.1

%description devel
Devel files for libgnomemm.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla libgnomemm.

%package static
Summary:	libgnomemm static library
Summary(pl.UTF-8):	Biblioteka statyczna libgnomemm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libgnomemm static library.

%description static -l pl.UTF-8
Biblioteka statyczna libgnomemm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgnomemm-2.6.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgnomemm-2.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnomemm-2.6.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomemm-2.6.so
%{_libdir}/libgnomemm-2.6
%{_includedir}/libgnomemm-2.6
%{_pkgconfigdir}/libgnomemm-2.6.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomemm-2.6.a
%endif
