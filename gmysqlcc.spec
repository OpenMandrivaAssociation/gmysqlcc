%define name	gmysqlcc
%define version 0.3.0
%define release %mkrel 3

Name: 	 	%{name}
Summary: 	Graphically controls MySQL databases
Version: 	%{version}
Release: 	%{release}

Source:		http://ftp.thepozer.org/gmysqlcc/%{name}-%{version}.tar.gz
URL:		http://gmysqlcc.thepozer.net/
License:	GPL+
Group:		Databases
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig 
BuildRequires:	imagemagick 
BuildRequires:	gtk2-devel 
BuildRequires:	bison
BuildRequires:  mysql-common 
BuildRequires:  mysql-client 
BuildRequires:  mysql-devel
BuildRequires:	desktop-file-utils

%description
With gmysqlcc, you can :
    * manage your server list
    * execute all SQL queries you want
    * dump queries, tables, databases and servers

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -fr $RPM_BUILD_ROOT/usr/doc/%name

# icons

install -m 644 -D data/%{name}-16.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m 644 -D data/%{name}-32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m 644 -D data/%{name}-48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install -m 644 -D data/%{name}-64.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png

# menu

perl -pi -e 's,gmysqlcc-32.png,%{name},g' %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install --vendor="" \
  --remove-key="Encoding" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*


%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}-*.png
%{_iconsdir}/hicolor/*/apps/%{name}.png
