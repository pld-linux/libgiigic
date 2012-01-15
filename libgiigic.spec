Summary:	LibGIIGIC - a flexible library for action/event binding
Summary(pl.UTF-8):	LibGIIGIC - elastyczna biblioteka do przypisywania akcji/zdarzeń
Name:		libgiigic
Version:	1.1.2
Release:	1
License:	BSD-like
Group:		Libraries
# HTTP 403
#Source0:	http://www.ggi-project.org/ftp/ggi/v2.2/%{name}-%{version}.src.tar.bz2
Source0:	http://downloads.sourceforge.net/ggi/%{name}-%{version}.src.tar.bz2
# Source0-md5:	bac6241c96f706f7b97246d84c95220a
URL:		http://www.ggi-project.org/packages/libgiigic.html
# for ggidemo, confmgrdemo, snazzymgr - which are not installed anyway
#BuildRequires:	libggi-devel >= 2.2.2
BuildRequires:	libgii-devel >= 1.0.2
Requires:	libgii >= 1.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GIC stands for General Input Configuration. LibGIIGIC is a convenience
library running on top of libgii, which implements easy
Descent/Forsaken style input configuration. It basically handles
binding of keystrokes, mice and valuators to program actions.

%description -l pl.UTF-8
GIC to skrót od General Input Configuration, czyli ogólnej
konfiguracji wejścia. LibGIIGIC to wygodna biblioteka działająca
powyżej libgii, implementująca łatwą konfigurację wejścia w stylu
Descenta/Forsaken. Zasadniczo obsługuje przypisywanie naciśnięć
klawiszy, myszy itp. do akcji programu.

%package devel
Summary:	Header files for libgiigic libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek libgiigic
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgii-devel >= 1.0.2

%description devel
Header files for libgiigic libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek libgiigic.

%package static
Summary:	Static libgiigic libraries
Summary(pl.UTF-8):	Biblioteki statyczne libgiigic
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgiigic libraries.

%description static -l pl.UTF-8
Biblioteki statyczne libgiigic.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/ggi/gic/recognizer/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libgicaction.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgicaction.so.0
%attr(755,root,root) %{_libdir}/libgiigic.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgiigic.so.1
%dir %{_libdir}/ggi/gic
%dir %{_libdir}/ggi/gic/recognizer
%attr(755,root,root) %{_libdir}/ggi/gic/recognizer/*.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ggi/libgiigic.conf
%{_mandir}/man7/libgiigic.7*

%files devel
%defattr(644,root,root,755)
%doc doc/*.txt
%attr(755,root,root) %{_bindir}/gic2c
%attr(755,root,root) %{_libdir}/libgicaction.so
%attr(755,root,root) %{_libdir}/libgiigic.so
%{_libdir}/libgicaction.la
%{_libdir}/libgiigic.la
%{_includedir}/ggi/gic*.h
%{_mandir}/man3/gic*.3*
%{_mandir}/man7/libgiigic-usage.7*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgicaction.a
%{_libdir}/libgiigic.a
