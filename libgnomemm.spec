Summary:	C++ wrappers for libgnome
Summary(pl):	Interfejsy C++ dla libgnome
Name:		libgnomemm
Version:	2.0.0
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.0/%{name}-%{version}.tar.bz2
# Source0-md5:	503b49486269046d486658ef33f092fe
Patch0:		%{name}-pkgconfig.patch
URL:		http://www.gnome.org/
BuildRequires:	gtkmm-devel >= 2.0.0
BuildRequires:	libgnome-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libgnome.

%description -l pl
Interfejsy C++ dla libgnome.

%package devel
Summary:	Devel files for libgnomemm
Summary(pl):	Pliki nag³ówkowe dla libgnomemm
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtkmm-devel >= 2.0.0
Requires:	libgnome-devel >= 2.0.0

%description devel
Devel files for libgnomemm.

%description devel -l pl
Pliki nag³ówkowe dla libgnomemm.

%package static
Summary:	libgnomecanvasmm static library
Summary(pl):	Biblioteka statyczna libgnomemm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
libgnomemm static library.

%description static -l pl
Biblioteka statyczna libgnomemm.

%prep
%setup -q
%patch0 -p1

%build
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
%{_libdir}/%{name}-2.0
%{_includedir}/%{name}-2.0
%{_pkgconfigdir}/%{name}-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomemm*.a
