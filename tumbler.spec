Summary:	D-Bus service for applications to request thumbnails
Summary(pl.UTF-8):	Serwis D-Bus do udostępniania miniaturek
Name:		tumbler
Version:	0.1.30
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://archive.xfce.org/src/xfce/tumbler/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	2524e39439c13238565160da0b6fed2d
URL:		http://www.xfce.org/
BuildRequires:	curl-devel >= 7.25
BuildRequires:	dbus-devel >= 1.0.0
BuildRequires:	dbus-glib-devel >= 0.72
BuildRequires:	ffmpegthumbnailer-devel >= 2.0.0
BuildRequires:	freetype-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libgsf-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libopenraw-gnome-devel
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.12.0
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus >= 1.0.0
Provides:	dbus(org.xfce.Tumbler.Cache1.service)
Provides:	dbus(org.xfce.Tumbler.Manager1.service)
Provides:	dbus(org.xfce.Tumbler.Thumbnailer1.service)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D-Bus service for applications to request thumbnails.

%description -l pl.UTF-8
Serwis D-Bus do udostępniania miniaturek.

%package libs
Summary:	Tumbler shared library
Summary(pl.UTF-8):	Biblioteka tumbler
Group:		Libraries

%description libs
Tumbler shared library.

%description libs -l pl.UTF-8
Biblioteka tumbler.

%package devel
Summary:	Header files for tumbler library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki tumbler
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for tumbler library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki tumbler.

%package apidocs
Summary:	tumbler API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki timpler
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
tumpler API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki tumbler.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir} \
	--enable-debug=minimum

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/tumbler-1/plugins/{cache,}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%dir /etc/xdg/tumbler
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/tumbler/tumbler.rc
%dir %{_libdir}/tumbler-1
%dir %{_libdir}/tumbler-1/plugins
%dir %{_libdir}/tumbler-1/plugins/cache
%attr(755,root,root) %{_libdir}/tumbler-1/tumblerd
%attr(755,root,root) %{_libdir}/tumbler-1/plugins/cache/tumbler-cache-plugin.so
%attr(755,root,root) %{_libdir}/tumbler-1/plugins/cache/tumbler-xdg-cache.so
%attr(755,root,root) %{_libdir}/tumbler-1/plugins/tumbler-cover-thumbnailer.so
%attr(755,root,root) %{_libdir}/tumbler-1/plugins/tumbler-ffmpeg-thumbnailer.so
%attr(755,root,root) %{_libdir}/tumbler-1/plugins/tumbler-font-thumbnailer.so
%attr(755,root,root) %{_libdir}/tumbler-1/plugins/tumbler-gst-thumbnailer.so
%attr(755,root,root) %{_libdir}/tumbler-1/plugins/tumbler-jpeg-thumbnailer.so
%attr(755,root,root) %{_libdir}/tumbler-1/plugins/tumbler-odf-thumbnailer.so
%attr(755,root,root) %{_libdir}/tumbler-1/plugins/tumbler-pixbuf-thumbnailer.so
%attr(755,root,root) %{_libdir}/tumbler-1/plugins/tumbler-poppler-thumbnailer.so
%attr(755,root,root) %{_libdir}/tumbler-1/plugins/tumbler-raw-thumbnailer.so
%{_datadir}/dbus-1/services/org.xfce.Tumbler.*.service

%files libs -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtumbler-1.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libtumbler-1.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtumbler-1.so
%{_includedir}/tumbler-1
%{_pkgconfigdir}/tumbler-1.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/tumbler
