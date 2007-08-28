%define name	gmysqlcc
%define version 0.2.6
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Graphically controls MySQL databases
Version: 	%{version}
Release: 	%{release}

Source:		http://ftp.thepozer.org/gmysqlcc/%{name}-%{version}.tar.bz2
URL:		http://gmysqlcc.thepozer.net/
License:	GPL
Group:		Databases
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig ImageMagick gtk2-devel bison
BuildRequires:  automake1.4 mysql-common mysql-client mysql-devel

%description
With gmysqlcc, you can :
    * manage your server list
    * execute all SQL queries you want
    * dump queries, tables, databases and servers

%prep
%setup -q
cp /usr/share/automake-1.4/mkinstalldirs .

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -fr $RPM_BUILD_ROOT/usr/doc/%name

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="databases_section.png" needs="x11" title="GMySQLCC" longtitle="Database Control Centre" section="More Applications/Databases" xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=GMySQLCC
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=databases_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Databases;Database;
EOF

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS NEWS README TODO
%{_bindir}/%name
%{_menudir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/applications/gmysqlcc.desktop
%{_datadir}/pixmaps/%{name}-*.png


