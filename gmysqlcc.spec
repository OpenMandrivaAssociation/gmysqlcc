%define name	gmysqlcc
%define version 0.3.0
%define release 10

Name: 	 	%{name}
Summary: 	Graphically controls MySQL databases
Version: 	%{version}
Release: 	%{release}

Source:		http://ftp.thepozer.org/gmysqlcc/%{name}-%{version}.tar.gz
URL:		https://gmysqlcc.thepozer.net/
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
%makeinstall_std
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


%changelog
* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-9mdv2011.0
+ Revision: 645800
- relink against libmysqlclient.so.18

* Sat Jan 01 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-8mdv2011.0
+ Revision: 627242
- rebuilt against mysql-5.5.8 libs, again

* Thu Dec 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-7mdv2011.0
+ Revision: 626523
- rebuilt against mysql-5.5.8 libs

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-5mdv2011.0
+ Revision: 610913
- rebuild

* Thu Feb 18 2010 Funda Wang <fwang@mandriva.org> 0.3.0-4mdv2010.1
+ Revision: 507412
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sat Dec 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-3mdv2009.1
+ Revision: 311331
- rebuilt against mysql-5.1.30 libs

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.3.0-2mdv2009.0
+ Revision: 266891
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat May 17 2008 Funda Wang <fwang@mandriva.org> 0.3.0-1mdv2009.0
+ Revision: 208298
- New version 0.3.0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Adam Williamson <awilliamson@mandriva.org> 0.2.6-2mdv2008.0
+ Revision: 90112
- buildrequires desktop-file-utils
- fix icon installation
- fd.o icons
- fix up the included .desktop
- don't create a .desktop file in the spec when the tarball includes one
- drop old menu
- spec clean
- new license policy

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Tue Feb 20 2007 J√©r√¥me Soyer <saispo@mandriva.org> 0.2.6-1mdv2007.0
+ Revision: 123049
- Add BR
- Add BR
- New release 0.2.6
- Import gmysqlcc

* Mon Sep 04 2006 Emmanuel Andry <eandry@mandriva.org> 0.2.5-3mdv2007.0
- xdg menu

* Sat Apr 01 2006 Austin Acton <austin@mandriva.org> 0.2.5-2mdk
- Rebuild

* Fri Oct 07 2005 Austin Acton <austin@mandriva.org> 0.2.5-1mdk
- New release 0.2.5

* Thu Sep 29 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.2.4-2mdk
- Fix BuildRequires

* Thu Aug 25 2005 Austin Acton <austin@mandriva.org> 0.2.4-1mdk
- 0.2.4
- source URL

* Thu May 26 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.2.2a-2mdk
- Rebuild

* Wed Dec 01 2004 Austin Acton <austin@mandrake.org> 0.2.2a-1mdk
- initial package

