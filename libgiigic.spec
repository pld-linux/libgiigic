Summary:	LibGIIGIC - a flexible library for action/event binding
Summary(pl):	LibGIIGIC - elastyczna biblioteka do przypisywania akcji/zdarzeñ
Name:		libgiigic
Version:	1.0.1
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://www.ggi-project.org/ftp/ggi/v2.1/%{name}-%{version}.src.tar.bz2
# Source0-md5:	ab294c824a58bc6b2a73428f19540a53
URL:		http://www.ggi-project.org/packages/libgiigic.html
BuildRequires:	XFree86-devel
# for snazzymgr, which is not installed anyway
#BuildRequires:	libggi-devel >= 2.1.2
BuildRequires:	libgii-devel >= 0.9.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GIC stands for General Input Configuration. LibGIIGIC is a convenience
library running on top of libgii, which implements easy
Descent/Forsaken style input configuration. It basically handles
binding of keystrokes, mice and valuators to program actions.

%description -l pl
GIC to skrót od General Input Configuration, czyli ogólnej
konfiguracji wej¶cia. LibGIIGIC to wygodna biblioteka dzia³aj±ca
powy¿ej libgii, implementuj±ca ³atw± konfiguracjê wej¶cia w stylu
Descenta/Forsaken. Zasadniczo obs³uguje przypisywanie naci¶niêæ
klawiszy, myszy itp. do akcji programu.

%package devel
Summary:	Header files for libgiigic library
Summary(pl):	Pliki nag³ówkowe biblioteki libgiigic
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgii-devel >= 0.9.2

%description devel
Header files for libgiigic library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libgiigic.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/ggi/gic/recognizer/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libgicaction.so.*.*.*
%attr(755,root,root) %{_libdir}/libgiigic.so.*.*.*
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
