Summary:	D-Bus service for applications to request thumbnails
Summary(pl.UTF-8):	Serwis D-Bus do udostępniania miniaturek
Name:		tumbler
Version:	4.20.2
Release:	2
License:	GPL v2
Group:		Applications/Graphics
Source0:	https://archive.xfce.org/src/xfce/tumbler/4.20/%{name}-%{version}.tar.bz2
# Source0-md5:	544cd05cf6ec8d16c8c812529d09b34b
URL:		https://www.xfce.org/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11
BuildRequires:	curl-devel >= 7.32.0
BuildRequires:	dbus-devel >= 1.0.0
BuildRequires:	dbus-glib-devel >= 0.72
BuildRequires:	ffmpegthumbnailer-devel >= 2.0.0
BuildRequires:	freetype-devel >= 2
BuildRequires:	gdk-pixbuf2-devel >= 2.42.8
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.72.0
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.35.0
# or 0.7.0
BuildRequires:	libgepub-devel >= 0.6.0
BuildRequires:	libgsf-devel >= 1.14.9
BuildRequires:	libjpeg-devel
BuildRequires:	libopenraw-gnome-devel >= 0.1.0
BuildRequires:	libpng-devel >= 1.2.0
BuildRequires:	libtool >= 2:2.4
BuildRequires:	libxfce4util-devel >= 4.20.0
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.12.0
BuildRequires:	rpmbuild(macros) >= 1.682
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	curl-libs%{?_isa} >= 7.32.0
Requires:	dbus >= 1.0.0
Requires:	ffmpegthumbnailer%{?_isa} >= 2.0.0
Requires:	gdk-pixbuf2%{?_isa} >= 2.42.8
Requires:	libgsf%{?_isa} >= 1.14.9
Requires:	libopenraw-gnome%{?_isa} >= 0.1.0
Requires:	poppler-glib%{?_isa} >= 0.12.0
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
Requires:	glib2%{?_isa} >= 1:2.72.0
Requires:	libxfce4util%{?_isa} >= 4.20.0

%description libs
Tumbler shared library.

%description libs -l pl.UTF-8
Biblioteka tumbler.

%package devel
Summary:	Header files for tumbler library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki tumbler
Group:		Development/Libraries
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	glib2-devel%{?_isa} >= 1:2.72.0

%description devel
Header files for tumbler library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki tumbler.

%package apidocs
Summary:	tumbler API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki timpler
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
tumpler API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki tumbler.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-debug=minimum \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/tumbler-1/plugins/{cache,}/*.la

# unify
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}
# not supported (as of glibc 2.32)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/hye

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md
%dir /etc/xdg/tumbler
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/tumbler/tumbler.rc
%dir %{_libdir}/tumbler-1
%attr(755,root,root) %{_libdir}/tumbler-1/tumblerd
%dir %{_libdir}/tumbler-1/plugins
%{_libdir}/tumbler-1/plugins/tumbler-cover-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-desktop-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-ffmpeg-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-font-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-gepub-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-gst-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-jpeg-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-odf-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-pixbuf-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-poppler-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-raw-thumbnailer.so
%dir %{_libdir}/tumbler-1/plugins/cache
%{_libdir}/tumbler-1/plugins/cache/tumbler-cache-plugin.so
%{_libdir}/tumbler-1/plugins/cache/tumbler-xdg-cache.so
%{_datadir}/dbus-1/services/org.xfce.Tumbler.*.service
%{systemduserunitdir}/tumblerd.service
%{_iconsdir}/hicolor/*x*/apps/org.xfce.tumbler.png

%files libs -f %{name}.lang
%defattr(644,root,root,755)
%{_libdir}/libtumbler-1.so.0.0.0
%ghost %{_libdir}/libtumbler-1.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libtumbler-1.so
%{_includedir}/tumbler-1
%{_pkgconfigdir}/tumbler-1.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/tumbler
