Summary:	C++ wrappers for libgnome
Summary(pl.UTF-8):	Interfejsy C++ dla libgnome
Name:		libgnomemm
Version:	2.18.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgnomemm/2.18/%{name}-%{version}.tar.bz2
# Source0-md5:	da6d481fc4a7fb0084d0e48f5c182112
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtkmm-devel >= 2.10.8
BuildRequires:	libgnome-devel >= 2.17.92
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	pkgconfig
Requires:	libgnome >= 2.17.92
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
Requires:	gtkmm-devel >= 2.10.8
Requires:	libgnome-devel >= 2.17.92

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
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgnomemm*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomemm*.so
%{_libdir}/libgnomemm*.la
%{_libdir}/%{name}-2.6
%{_includedir}/%{name}-2.6
%{_pkgconfigdir}/%{name}-2.6.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomemm*.a
